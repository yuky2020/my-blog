+++
title = "11_A"
date = 2021-10-28T20:03:36+02:00
description = "Discover a new important stochastic process by yourself! "
draft = false
toc = false
categories = ["statistic"]
tags = ["after", "statistic"]
images = [
  "https://source.unsplash.com/collection/983219/1600x900"
] # overrides site-wide open graph image

[[resources]]
  src = "images/2.png"
  name = "header thumbnail"

+++

![header](images/2.png)

## 11_A assignament

### Request
Discover a new important stochastic process by yourself! Consider the general scheme we have used so far to simulate some stochastic processes (such as the relative frequency of success in a sequence of trials, the sample mean and the random walk) and now add this new process to our simulator.
Same scheme as previous program (random walk), except changing the way to compute the values of the paths at each time. Starting from value 0 at time 0, for each of m paths, at each new time compute N(i) = N(i-1) + Random step(i), for i = 1, ..., n, where Random step(i) is now a Bernoulli random variable with success probability equal to λ * (1/n)  (where λ is a user parameter, eg. 50, 100, ...).
At time n (last time) and one (or more) other chosen inner time 1<j<n (j is a program parameter) create and represent with histogram the distribution of N(i). 
Represent also the distributions of the following quantities (and any other quantity that you think of interest):
- Distance (time elapsed) of individual jumps from the origin
- Distance (time elapsed) between consecutive jumps ("holding times")

### My Solution

{{< youtube UaO_tyuwBZE>}}


[Code in C#]https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment10/C%23/BernulliGraphics)


#### The part in disegna Grafici in witch i call the various usefull function

{{< highlight cs >}}
      {
                distrubution = new BernulliPathfinder(n, m, lambda);

                disegnaPaths(fromPathstoViewport(distrubution.Get_paths(), viewPort));

                disegnaHistogramma(viewPort, getDistribution(distrubution.Get_paths(), m / SCALE, j), n, j);
                disegnaHistogramma(viewPort, getDistribution(distrubution.Get_paths(), m / SCALE, n), n, n);
                //disegno le distanze
                disegnaDistanze(viewPort, individualJumpFromOriginD(distrubution.Get_paths()), 0, "Single jump distace ");
                disegnaDistanze(viewPort, doublejumpD(distrubution.Get_paths()), 80, "Double jump distance");

            }
{{< /highlight >}}

the class for writing the histogram and for get the distribution are the same as the precedent hw
so i will skip it,but bernulli pathfinder now work with lamba insted of p 

#### Bernoulli pathfinder class
{{< highlight cs >}}
      public class BernulliPathfinder: Pathfinder
    {
       

        int m;      //number of paths
        int n;      //number of points 
        double p;   //probability
        public List<Strade> paths = new List<Strade>();
        private Random R;

        public BernulliPathfinder(int n, int m, double p)
        {
            this.m = m;
            this.n = n;
            this.p = p;

            this.R = new Random();

            for (int i=0; i < m; i++)
            {
                paths.Add(new Strade(createBernulliList()));
            }
            
        

        }

        private int bernoulli_Result(double p,int n)
        {
           double random_outcome = R.NextDouble();

            if (random_outcome <= p/n) return 1;
            else return 0;
        }

        private List<double> createBernulliList()
        {
            List<double> bernoulli = new List<double>();

            for (int i = 0; i < n; i++)
            {
                bernoulli.Add(bernoulli_Result(p, n));
            }

            return bernoulli;
        }
       public List<Strade> Get_paths()
        {
            return this.paths;
        }



    }
{{< /highlight >}}

#### Disegna Distanze method
{{< highlight cs >}}
     private void disegnaDistanze(Rectangle viewPort, Dictionary<int, int> intervals, int offset, String text)
        {
            int i = 0;
            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(128, 0, 0, 0));

            foreach (var v in intervals)
            {
                int x, y;
                int width, height;
                // in this case on the fly trasformation is way faster
                x = (int)(this.viewPort.Left + 20 * i);
                y = (int)(viewPort.Top + viewPort.Height + offset);


                width = v.Value;
                height = viewPort.Height / intervals.Count;

                Rectangle rectangle = new Rectangle(x, y, width, height);

                g2.DrawRectangle(Pens.Black, rectangle);
                g2.FillRectangle(semiTransBrush, rectangle);

                g2.FillRectangle(Brushes.Violet, rectangle);
                g2.DrawString(v.Key.ToString(), new Font("Calibri", 10.0f,
                                 FontStyle.Regular, GraphicsUnit.Pixel), semiTransBrush, new Point(x, y));
                i++;
            }
            g2.DrawString(text, new Font("Calibri", 13.0f,
                               FontStyle.Italic, GraphicsUnit.Pixel), semiTransBrush, new Point(this.viewPort.Left - 140, (viewPort.Top + viewPort.Height + offset)));

        }
{{< /highlight >}}
#### Individual jump
{{< highlight cs >}}
     private Dictionary<int, int> individualJumpFromOriginD(List<Strade> strades)
        {
            Dictionary<int, int> dbj = new Dictionary<int, int>();
            int i = 0;
            int tmp = 1;
            Boolean trov = false;
            foreach (Strade s in strades)
            {
                i = 0;
                tmp = 1;
                trov = false;
                while (!trov && (i < s.getPath().Count() - 2))
                {
                    if (s.getPath()[i].Y != s.getPath()[i + 1].Y) trov = true;
                    i++;
                }
                i++;
                if (dbj.TryGetValue(i, out tmp))
                {
                    dbj.Remove(i);
                    dbj.Add(i, tmp + 1);
                }
                else dbj.Add(i, tmp);
            }
            return dbj;
        }
{{< /highlight >}}
#### Double jump 
{{< highlight cs >}}
    private Dictionary<int, int> doublejumpD(List<Strade> strades)
        {
            Dictionary<int, int> dbj = new Dictionary<int, int>();
            int i = 0;
            int tmp = 1;
            Boolean trov = false;
            foreach (Strade s in strades)
            {
                i = 0;
                tmp = 1;
                trov = false;
                while (!trov && (i < s.getPath().Count() - 2))
                {
                    if (s.getPath()[i].Y != s.getPath()[i + 1].Y && s.getPath()[i + 1].Y != s.getPath()[i + 2].Y) trov = true;
                    i++;
                }
                i = i + 1;
                if (dbj.TryGetValue(i, out tmp))
                {
                    dbj.Remove(i);
                    dbj.Add(i, tmp + 1);
                }
                else dbj.Add(i, tmp);
            }
            return dbj;
        }
{{< /highlight >}}
