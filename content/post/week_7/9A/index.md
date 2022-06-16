+++
title = "9_A"
date = 2021-10-28T20:03:36+02:00
description = "Create a simulation with graphics to convince yourself of the pointwise convergence of the empirical CDF(9A1) and  Generate sample paths of jump processes(9A2)"
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

## 9_A1 assignament

### Request
 Create a simulation with graphics to convince yourself of the pointwise convergence of the empirical CDF to the theoretical distribution (Glivenko-Cantelli theorem). Use a simple random variable of your chooice for such a demonstration.



### My Solution

{{< youtube btWiAAvVsho >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment9/C%23)


#### Methods for calculate empirical CDS  in C#

{{< highlight cs >}}
    
     public List<PointF> CDFtoViewport(Rectangle viewPort,int n)
        {
            List<PointF> cdfs=new List<PointF>();
            List<int> values=new List<int>();
            for (int i=0; i < n; i++)
            {
              values.Add(R.Next(149, 220));
            }
                       
            float tmpy = 0;
            float tmpx = -1;

            for (int i = 150; i <= 220; i = i + 5)
            {
                tmpy = 0;
                tmpx = tmpx + 1 ;

                foreach (int p in values)
                {
                    if (p < i) tmpy++;

                    //empirical CDF


                }
                cdfs.Add(new PointF(tmpx, tmpy/n));
               

            }
            PointF[] viewPortArraycdf = cdfs.ToArray();
            this.m2.TransformPoints(viewPortArraycdf);
            return(viewPortArraycdf.ToList());
           
        }
{{< /highlight >}}

### Method to draw both empirical and theorical rapresentation
{{< highlight cs >}}
    
    private void disegnaCDFPaths(List<PointF> viewPortCDF)
        {

            Pen pen = new Pen(Color.Red);
            Pen pen2 = new Pen(Color.Green);

            //empirical cdf
            for (int j = 1; j < viewPortCDF.Count; j++)
            {
                g2.DrawLine(pen, (float)viewPortCDF[j-1].X, (float)viewPortCDF[j-1].Y,
                    (float)viewPortCDF[j].X, (float)viewPortCDF[j].Y);

                g2.DrawEllipse(pen, new Rectangle((int)viewPortCDF[j].X, (int)viewPortCDF[j].Y, 4,4));
            }

            //theorical cdf
           
                g2.DrawLine(pen2,(viewPort.Left+viewPort.Width), viewPort.Top,
                      viewPort.Left, viewPort.Top+viewPort.Height);
            

        }
{{< /highlight >}}

## 9_A2 assignament

### Request
Generate sample paths of jump processes which at each time considered t = 1, ..., n perform jumps computed as:

-   σ sqrt(1/n) R(t)
where R(t)  is a [-1,1] Rademacher random variable (https://en.wikipedia.org/wiki/Rademacher_distribution).

-  σ sqrt(1/n) * Z(t), where  Z(t) is a N(0,1) random variable (https://en.wikipedia.org/wiki/Normal_distribution)

and see what happens as n (simulation parameter) becomes larger.

[As before, at time n (last time) and one other chosen inner time 1<j<n (j is a program parameter) create and represent with histogram the distribution of the process ]

### My Solution

{{< youtube sv5G70K74xQ >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment9/C%23)

#### Interface  Pathfinder  in C#

{{< highlight cs >}}
  interface Pathfinder
    {
        abstract public List<Strade> Get_paths();

    }
    
{{< /highlight >}}



#### Class Rademacher Pathfinder  in C#

{{< highlight cs >}}
    
     public class RademacherPathfinder : Pathfinder
    {
       

        int m;      //number of paths
        int n;      //number of points 
        double p;   //probability
        public List<Strade> paths = new List<Strade>();
        private Random R;

        public RademacherPathfinder(int n, int m)
        {
            this.m = n;
            this.n = m;
            this.p = 0.5;

            this.R = new Random();

            for (int i=0; i < m; i++)
            {
                paths.Add(new Strade(createRademacherList()));
            }
            
        

        }

        private int rademacher_Result(double p)
        {
           double random_outcome = R.NextDouble();

            if (random_outcome < p) return 1;

            else if (random_outcome == p) return 0;
                return -1;
        }

        private List<double> createRademacherList()
        {
            List<double> rademacher = new List<double>();

            for (int i = 0; i < n; i++)
            {
                rademacher.Add(rademacher_Result(p));
            }

            return rademacher;
        }
        
         public List<Strade> Get_paths()
        {
            return this.paths;
        }

    }
{{< /highlight >}}


### Class Normal Pathfinder in C#
{{< highlight cs >}}
        public class NormalPathfinder: Pathfinder
    {
       

        int m;      //number of paths
        int n;      //number of points 
        double p;   //probability
        public List<Strade> paths = new List<Strade>();
        private Random R;

        public NormalPathfinder(int n, int m)
        {
            this.m = n;
            this.n = m;
            this.p = 0.5;

            this.R = new Random();

            for (int i=0; i < m; i++)
            {
                paths.Add(new Strade(createNormalList()));
            }
            
        

        }

        private double normal_Result(double p)
        {
           double random_outcome = R.NextDouble();
            double normal_distrbAtOut;
            double v = R.NextDouble();
            //create a value between 1 and -1
            random_outcome = random_outcome * 2 - 1;
            //get the standard normal for that point 
            normal_distrbAtOut= Math.Pow(Math.E, (Math.Pow(-random_outcome, 2) / 2))/Math.Sqrt(2*Math.PI) ;
            //then use the other generated random
            if (v < normal_distrbAtOut) return random_outcome;
            else return 0;

        }

        private List<double> createNormalList()
        {
            List<double> normal = new List<double>();

            for (int i = 0; i < n; i++)
            {
               normal.Add(normal_Result(p));
            }

            return normal;
        }


       public List<Strade> Get_paths()
        {
            return this.paths;
        }


    }
    
{{< /highlight >}}

### Disegna grafici class
{{< highlight cs >}}
       public class DisegnaGrafici
    {
        public Bitmap bitmap;
        public Graphics g2;
        public PictureBox pictureBox;

        private int SCALE = 4;

        private Random R = new Random();

        public List<Strade> viewPortPaths;
        public List<Strade> viewPortAbsolute;

        private Rectangle viewPort;
        int n;
        Matrix m1;
        Matrix m2;
        Pathfinder distrubution;

        public DisegnaGrafici(int m, int n, int j, Graphics graphics, double epsilon, Rectangle vPort, int dinamicleft, int dinamictop, int contgw, int contgh, TextBox boxassfreq, TextBox boxrelfreq, bool is_abs,bool is_norml)
        {
            this.g2 = graphics;
            this.viewPort = vPort;
            this.viewPort.X = dinamicleft;
            this.viewPort.Y = dinamictop;
            this.viewPort.Width = contgw;
            this.viewPort.Height = contgh;
            this.n = n;
            this.m1 = new Matrix();
            this.m2 = new Matrix();
            g2.Clear(Color.Transparent);
            g2.FillRectangle(Brushes.Transparent, this.viewPort);
            g2.DrawRectangle(new Pen(Color.Black), this.viewPort);
            //genero la marice per le trasformazioni
            m1.Reset();
            m1.Translate((float)-0, -(float)0, MatrixOrder.Append);
            m1.Scale((float)(viewPort.Width /m ), (float)(-viewPort.Height /1), MatrixOrder.Append);
            m1.Translate(viewPort.Left, viewPort.Top + viewPort.Height, MatrixOrder.Append);

            //Matrix for the cdf
            m2.Reset();
            m2.Translate((float)-0, -(float)0, MatrixOrder.Append);
            m2.Scale((float)(viewPort.Width /14), (float)(-viewPort.Height / 1), MatrixOrder.Append);
            m2.Translate(viewPort.Left, viewPort.Top + viewPort.Height, MatrixOrder.Append);

            //genero le "strade"
            if (is_norml == false)
                distrubution = new RademacherPathfinder(n, m);
            else distrubution = new NormalPathfinder(n, m);
            //disegno i vari path convertendoli per il viewport
            if (is_abs)
                disegnaCDFPaths(CDFtoViewport(viewPort,n));
            else
            {
                disegnaPaths(fromPathstoViewport(distrubution.Get_paths(), viewPort));

                disegnaHistogramma(viewPort, getDistribution(distrubution.Get_paths(), m / SCALE, j), n, j);
                disegnaHistogramma(viewPort, getDistribution(distrubution.Get_paths(), m / SCALE, n), n, n);
            }

            getAbsoluteFrequencies(distrubution.Get_paths(), n, m, epsilon, boxassfreq, boxrelfreq);


        }

        private void disegnaCDFPaths(List<PointF> viewPortCDF)
        {

            Pen pen = new Pen(Color.Red);
            Pen pen2 = new Pen(Color.Green);

            //empirical cdf
            for (int j = 1; j < viewPortCDF.Count; j++)
            {
                g2.DrawLine(pen, (float)viewPortCDF[j-1].X, (float)viewPortCDF[j-1].Y,
                    (float)viewPortCDF[j].X, (float)viewPortCDF[j].Y);

                g2.DrawEllipse(pen, new Rectangle((int)viewPortCDF[j].X, (int)viewPortCDF[j].Y, 4,4));
            }

            //theorical cdf
           
                g2.DrawLine(pen2,(viewPort.Left+viewPort.Width), viewPort.Top,
                      viewPort.Left, viewPort.Top+viewPort.Height);
            

        }
                
        public List<PointF> CDFtoViewport(Rectangle viewPort,int n)
        {
            List<PointF> cdfs=new List<PointF>();
            List<int> values=new List<int>();
            for (int i=0; i < n; i++)
            {
              values.Add(R.Next(149, 220));
            }
                       
            float tmpy = 0;
            float tmpx = -1;

            for (int i = 150; i <= 220; i = i + 5)
            {
                tmpy = 0;
                tmpx = tmpx + 1 ;

                foreach (int p in values)
                {
                    if (p < i) tmpy++;

                    //empirical CDF


                }
                cdfs.Add(new PointF(tmpx, tmpy/n));
               

            }
            PointF[] viewPortArraycdf = cdfs.ToArray();
            this.m2.TransformPoints(viewPortArraycdf);
            return(viewPortArraycdf.ToList());
           
        }

        public void getAbsoluteFrequencies(List<Strade> paths, int n, int m, double epsilon, TextBox boxassfreq, TextBox boxrelfreq)
        {
            double p=0.5 ;
            Intervalli p_neighbourhood = new Intervalli(p - epsilon, p + epsilon);

            int absolute_frequency = 0;
            double relative_frequency = 0;

            foreach (Strade path in paths)
            {
                for (int i = 0; i < path.getPath().Count; i++)
                {
                    if (
                        (path.getPath()[i].X == n)
                        &&
                        (path.getPath()[i].Y >= p_neighbourhood.LowerBound)
                        &&
                        (path.getPath()[i].Y < p_neighbourhood.UpperBound)
                        )
                    {
                        absolute_frequency++;
                    }
                }
            }

            relative_frequency = (double)absolute_frequency / (double)m;

            boxassfreq.Text = absolute_frequency.ToString();
            boxrelfreq.Text = relative_frequency * 100 + "%";



        }


        public void disegnaPaths(List<Strade> viewPortPaths)
        {
            for (int i = 0; i < viewPortPaths.Count; i++)
            {
                Pen pen = new Pen(Color.FromArgb(R.Next(0, 255), R.Next(0, 255), R.Next(0, 255)));


                for (int j = 0; j < viewPortPaths[i].getPath().Count - 1; j++)
                {
                    g2.DrawLine(pen, (float)viewPortPaths[i].getPath()[j].X, (float)viewPortPaths[i].getPath()[j].Y,
                        (float)viewPortPaths[i].getPath()[j + 1].X, (float)viewPortPaths[i].getPath()[j + 1].Y);
                }
            }
        }

        public void disegnaHistogramma(Rectangle viewPort, List<Intervalli> intervals, int n, int j)
        {

            for (int i = 0; i < intervals.Count; i++)
            {
                int x, y;
                int width, height;
                // in this case on the fly trasformation is way faster
                x = (int)(this.viewPort.Left + this.viewPort.Width * (j) /n);
                y = (int)(viewPort.Top + viewPort.Height/2 * ((100 - (intervals[i].UpperBound) * 100) / 100));


                width = intervals[i].Counter;
                height = viewPort.Height / intervals.Count;

                Rectangle rectangle = new Rectangle(x, y, width, height);

                g2.DrawRectangle(Pens.Black, rectangle);
                SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(128, 150, 0, 0));
                g2.FillRectangle(semiTransBrush, rectangle);

                g2.FillRectangle(Brushes.Violet, rectangle);
            }
        }

        public List<Intervalli> getDistribution(List<Strade> paths, int noIntervals, int j)
        {


            List<double> frequencies = new List<double>();

            for (int i = 0; i < paths.Count; i++)
            {
                for (int k = 0; k < paths[i].getPath().Count; k++)
                {
                    if (paths[i].getPath()[k].X == j)
                    {
                        frequencies.Add(paths[i].getPath()[k].Y);
                    }
                }
            }

            List<Intervalli> intervals = new List<Intervalli>();

            double intervalLength = 1.0 / (double)noIntervals;

            for (int i= -noIntervals; i < noIntervals; i++)
            {
                intervals.Add(new Intervalli(i * intervalLength, (i + 1) * intervalLength));
            }

            for (int i = 0; i < intervals.Count; i++)
            {
                for (int k = 0; k < frequencies.Count; k++)
                {
                    if ((frequencies[k] >= intervals[i].LowerBound) && (frequencies[k] < intervals[i].UpperBound))
                    {
                        intervals[i].Counter++;
                    }
                }
            }

            return intervals;
        }

        public List<Strade> fromPathstoViewport(List<Strade> paths, Rectangle viewPort)
        {
            List<Strade> viewPortPaths = new List<Strade>();

            foreach (Strade path in paths)
            {

                PointF[] viewPortArrayPath = path.getPath().ToArray();
                for (int i = 0;i < viewPortArrayPath.Length; i++)
                {

                  viewPortArrayPath[i].Y= (viewPortArrayPath[i].Y + 1) / 2;
                    
                }

                this.m1.TransformPoints(viewPortArrayPath);
                viewPortPaths.Add(new Strade(viewPortArrayPath.ToList()));
            }

            return viewPortPaths;
        }




        public Graphics getGrapichs()
        {
            return this.g2;
        }
    } 
    
{{< /highlight >}}
