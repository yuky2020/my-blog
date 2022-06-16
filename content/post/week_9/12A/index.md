+++
title = "12_A"
date = 2021-10-28T20:03:36+02:00
description =" Discover one of the most important stochastic process by yourself "
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

## 12_A assignament

### Request
Discover one of the most important stochastic process by yourself !

Consider the general scheme we have used so far to simulate stochastic processes (such as the relative frequency of success in a sequence of trials, the sample mean, the random walk, the Poisson point process, etc.) and now add this new process to our simulator.

Starting from value 0 at time 0, for each of m paths, at each new time compute P(t) = P(t-1) + Random step(t), for t = 1, ..., n,
where the Random step(t) is now:

σ * sqrt(1/n) * Z(t),

where  Z(t) is a N(0,1) random variable (the "diffusion" σ is a user parameter, to scale the process dispersion).

At time n (last time) and one (or more) other chosen inner time 1<j<n (j is a program parameter) create and represent with histogram the distribution of P(t). Observe the behavior of the process for large n.

### My Solution

{{< youtube 6zfdwGTiVC0 >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment11/C%23/BernulliGraphics)


### In Disiegnagrafici 
We  graphicate   the paths and the histograms as before but for sure now we use as a random step the new formula  so i made a class
WN graphicate  ormalpaths and the histograms as before but for sure now we use as a random step the new formula  so i made a class "NormalPathfinder" in witch i generate the list of value:

{{< highlight cs >}}
   public NormalPathfinder(int n, int m)
        {
            this.m = n;
            this.n = m;
            this.p = 0.5;

            this.R = new Random();

            for (int i=0; i < m; i++)
            {
                List<Double> list = createNormalList();
                paths.Add(new Strade(list));
                values.Add(list);
            }
            
        

        }

        private bool normal_Result(double p,out double ou)
        {
           double random_outcome =( R.NextDouble()+R.NextDouble());
            double normal_distrbAtOut;
            double v = R.NextDouble();
            //create a value between 1 and -1
            random_outcome = random_outcome  - 1;
            //get the standard normal for that point 
            normal_distrbAtOut= Math.Pow(Math.E, (Math.Pow(-random_outcome, 2) / 2))/Math.Sqrt(2*Math.PI) ;
            //then use the other generated random
            if (v <= normal_distrbAtOut*Math.Sqrt(2*Math.PI))
            {
                ou = random_outcome;
                return true;
            }

            else { ou = 0; return false; }

        }

        private List<double> createNormalList()
        {
            List<double> normal = new List<double>();

            for (int i = 0; i < n; i++)
            {
                double j;
                if (normal_Result(p, out j))
                    normal.Add(j);
                else i--;
            }

            return normal;
        }
{{< /highlight >}}

Here we use create also the path with a Strade object : 


{{< highlight cs >}}
     //Dalla lista di valori passo ai punti ;
        public Strade(List<double> values)
        {
            this.values = values;
            double sqrt1n = (double)1 / values.Count;
                Math.Sqrt(sqrt1n);
            double jump=0;

            for (int i=0; i < values.Count; i++)
            {
                
                    jump += (sqrt1n)*values[i];
               
                path.Add(new PointF(i + 1, (float) jump));
            }
        }
{{< /highlight >}}

