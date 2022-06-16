+++
title = "8_A"
date = 2021-10-28T20:03:36+02:00
description = "Generate and represent m sample paths of n point each (m, n are program parameters), where each point represents a pair of:time index t, and relative frequency of success f(t)"
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

## 8_A assignament

### Request
Generate and represent m "sample paths" of n point each (m, n are program parameters), where each point represents a pair of:
time index t, and relative frequency of success f(t),

where f(t) is the sum of t Bernoulli random variables with distribution B(x, p) = p^x(1-p)^(1-x) observed at the various times up to t: j=1, ..., t..


At time n (last time) and one other chosen inner time 1<j<n (where j is a user parameter) represent with a histogram the distribution of f(t).
See also what happens if you replace the relative frequency f(t) with the absolute frequency n(t) or by standard relative frequency: (f(t)-p) / sqrt(p(1-p)/t) [ or simply the "normalized" sum of bernoulli r.v.'s: n(t) / Math.sqrt(t) ].

Comment briefly on the convergence results you see.

### My Solution

{{< youtube Y3NToOvrCuM >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment8/C%23/BernulliGraphics/BernulliGraphics)


#### Class Main Form  in C#

{{< highlight cs >}}
public partial class BernulliGraphics : Form
    {
        public BernulliGraphics()
        {
            InitializeComponent();
            contb = new Bitmap(755, 681);
            g2 = Graphics.FromImage(contb);
            comboBox1.SelectedIndex = 0;
        }



        Bitmap contb;
        Graphics g2;

        bool movable = false;
        bool resiable = false;
        // movable view port
        int contgleft = 0;
        int contgtop = 50;
        int contgwid = 400;
        int contgheight = 400;
        int mouseDeltax = 0;
        int mouseDeltay = 0;
        // window
        double minX_Window = 0;
        double maxX_Window = 400;
        double minY_Window = 0;
        double maxY_Window = 400;


        Rectangle viewPortc = new Rectangle(0, 50, 600, 600);






        private void button1_Click(object sender, EventArgs e)


        {
            creaGrafici();


        }








        private void creaGrafici()
        {
            bool is_abs = false;
            if (comboBox1.SelectedIndex == 1) is_abs = true;
            int m = (int)this.numericUpDown1.Value;
            int n = (int)this.numericUpDown2.Value;
            double p = (double)this.numericUpDown3.Value / 100;
            int j = 40;
            double epsilon = (double)this.numericUpDown4.Value;


            DisegnaGrafici gr = new DisegnaGrafici(m, n, j, g2, p, epsilon, viewPortc, contgleft, contgtop, contgwid, contgheight, textBox1, textBox2,is_abs);
            gr.getGrapichs();
            pictureBox2.Image = contb;


        }



        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            if ((e.Location.Y >= viewPortc.Top && e.Location.Y <= (viewPortc.Top + viewPortc.Height)) && (e.Location.X >= viewPortc.Left && e.Location.X <= (viewPortc.Left + viewPortc.Width)))
            {
                if (e.Button == MouseButtons.Left)
                    movable = true;
                if (e.Button == MouseButtons.Right)
                    resiable = true;
                mouseDeltax = e.Location.X;
                mouseDeltay = e.Location.Y;

            }


        }

        private void pictureBox2_MouseLeave(object sender, EventArgs e)
        {
            resiable = false;
            movable = false;
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (movable == true)
            {

                contgleft = e.Location.X;
                contgtop = e.Location.Y;
                if (contgleft <= 0) contgleft = 0;
                if (contgtop <= 20) contgtop = 20;
                creaGrafici();
            }
            if (resiable == true)
            {
                mouseDeltax = -mouseDeltax + e.Location.X;
                mouseDeltay = -mouseDeltay + e.Location.Y;
                contgwid += mouseDeltax / 40;
                contgheight += mouseDeltay / 40;
                creaGrafici();
            }






        }



        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            resiable = false;
            movable = false;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            creaGrafici();

        }
    }
    
    
{{< /highlight >}}

### DisegnaGrafici class 

{{< highlight cs >}}
 public class DisegnaGrafici
    {
        public Bitmap bitmap;
        public Graphics g2;
        public PictureBox pictureBox;

        private int SCALE = 10;

        private Random R = new Random();

        public List<Strade> viewPortPaths;
        public List<Strade> viewPortAbsolute;

        private Rectangle viewPort;
        Matrix m1;
        BernulliPathfinder bernulli;

        public DisegnaGrafici(int m, int n, int j, Graphics graphics, double p, double epsilon, Rectangle vPort, int dinamicleft, int dinamictop, int contgw, int contgh, TextBox boxassfreq, TextBox boxrelfreq, bool is_abs)
        {
            this.g2 = graphics;
            this.viewPort = vPort;
            this.viewPort.X = dinamicleft;
            this.viewPort.Y = dinamictop;
            this.viewPort.Width = contgw;
            this.viewPort.Height = contgh;
            this.m1 = new Matrix();
            g2.Clear(Color.Transparent);
            g2.FillRectangle(Brushes.Transparent, this.viewPort);
            g2.DrawRectangle(new Pen(Color.Black), this.viewPort);
            //genero la marice per le trasformazioni
            m1.Reset();
            m1.Translate(-0, -(int)0, MatrixOrder.Append);
            m1.Scale((int)(viewPort.Width / (n - 0)), (int)(-viewPort.Height / (1 - 0)), MatrixOrder.Append);
            m1.Translate(viewPort.Left, viewPort.Top + viewPort.Height, MatrixOrder.Append);

            //genero le "strade"
            bernulli = new BernulliPathfinder(n, m, p);

            //disegno i vari path convertendoli per il viewport
            if (is_abs)
                disegnaABSPaths(fromPathstoAbsViewport(bernulli.paths, viewPort,n));
            else
            {
                disegnaPaths(fromPathstoViewport(bernulli.paths, viewPort));

                disegnaHistogramma(viewPort, getDistribution(bernulli.paths, m / SCALE, j), n, j);
                disegnaHistogramma(viewPort, getDistribution(bernulli.paths, m / SCALE, n), n, n);
            }

            getAbsoluteFrequencies(bernulli.paths, n, m, p, epsilon, boxassfreq, boxrelfreq);


        }

        private void disegnaABSPaths(List<List<PointF>> viewPortABSPaths)
        {
            for (int i = 0; i < viewPortABSPaths.Count; i++)
            {
                Pen pen = new Pen(Color.FromArgb(R.Next(0, 255), R.Next(0, 255), R.Next(0, 255)));


                for (int j = 0; j < viewPortABSPaths[i].Count - 1; j++)
                {
                    g2.DrawLine(pen, (float)viewPortABSPaths[i][j].X, (float)viewPortABSPaths[i][j].Y,
                        (float)viewPortABSPaths[i][j + 1].X, (float)viewPortABSPaths[i][j + 1].Y);
                }
            }
        }

        public List<List<PointF>> fromPathstoAbsViewport(List<Strade> paths, Rectangle viewPort,int n)
        {
            List<List<PointF>> viewPortAbsPaths = new List<List<PointF>>();
           
            float tmpy = 0;
            float tmpx = 0;

            foreach (Strade path in paths)
            {
                tmpy = 0;
                tmpx = 0;
                List<PointF> abtmp = new List<PointF>();
                foreach (int p in path.values)
                {
                    if (p == 1) tmpy++;
                    tmpx++;
                    //only for graphic it rapidly
                    abtmp.Add(new PointF(tmpx, (tmpy / n)));

                }
                    PointF[] viewPortArrayPath = abtmp.ToArray();

                    this.m1.TransformPoints(viewPortArrayPath);

                    viewPortAbsPaths.Add(viewPortArrayPath.ToList());
                }
            

            return viewPortAbsPaths;
        }

        public void getAbsoluteFrequencies(List<Strade> paths, int n, int m, double p, double epsilon, TextBox boxassfreq, TextBox boxrelfreq)
        {
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
                x = (int)(this.viewPort.Left + this.viewPort.Width * (j) / n);
                y = (int)(viewPort.Top + viewPort.Height * ((100 - intervals[i].UpperBound * 100) / 100));


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

            for (int i = 0; i < noIntervals; i++)
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


### BernoulliPathfinder (Class with bernulli random variable creation methods)
{{< highlight cs >}}
 public class BernulliPathfinder
    {
       

        int m;      //number of paths
        int n;      //number of points 
        double p;   //probability
        public List<Strade> paths = new List<Strade>();
        private Random R;

        public BernulliPathfinder(int n, int m, double p)
        {
            this.m = n;
            this.n = m;
            this.p = p;

            this.R = new Random();

            for (int i=0; i < m; i++)
            {
                paths.Add(new Strade(createBernulliList()));
            }
            
        

        }

        private int bernoulli_Result(double p)
        {
           double random_outcome = R.NextDouble();

            if (random_outcome <= p) return 1;
            else return 0;
        }

        private List<int> createBernulliList()
        {
            List<int> bernoulli = new List<int>();

            for (int i = 0; i < n; i++)
            {
                bernoulli.Add(bernoulli_Result(p));
            }

            return bernoulli;
        }
        

    }

{{< /highlight >}}


### Strade.cs (path struct creation and useful methods)
{{< highlight cs >}}

 public class Strade
    {
        public List<PointF> path = new List<PointF>();
        public List<int> values = new List<int>();

        //Dalla lista di valori passo ai punti ;
        public Strade(List<int> values)
        {
            this.values = values;
            double mean = 0;

            for (int i=0; i < values.Count; i++)
            {
                if (i == 0)
                {
                    mean = values[0];
                }
                else
                {
                    mean += (values[i] - mean) / (double)(i + 1);
                }

                path.Add(new PointF(i + 1, (float) mean));
            }
        }

        public Strade(List<PointF> points) 
        {
            path = points;
        }

        public List<double> getXs()
        {
            List<double> x_coordinates = new List<double>();

            foreach (PointF p in this.getPath())
            {
                x_coordinates.Add(p.X);
            }

            return x_coordinates;
        }

        public List<double> getYs()
        {
            List<double> y_coordinates = new List<double>();

            foreach (PointF p in this.getPath())
            {
                y_coordinates.Add(p.Y);
            }

            return y_coordinates;
        }

        public List<PointF> getPath()
        {
            return this.path;
        }

        public void setPath(List<PointF> path)
        {
            this.path = path;
        }
    }


{{< /highlight >}}
