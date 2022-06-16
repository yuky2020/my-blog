+++
title = "7_A"
date = 2021-10-23T20:03:36+02:00
description = "Given 2 variables from a csv compute and represent the statistical regression lines (X to Y and viceversa) and the scatterplot."

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

## 7_A assignament

### Request
Given 2 variables from a csv compute and represent the statistical regression lines (X to Y and viceversa) and the scatterplot.
Optionally, represent also the histograms on the "sides" of the chart (one could be draw vertically and the other one horizontally, in the position that you prefer).
[Remember that all our charts must alway be done within "dynamic viewports" (movable/resizable rectangles). No third party libraries, to ensure ownership of creative process. May choose the language you prefer.].



### My Solution

{{< youtube 9TfFEY9eGrs >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment7)


#### Class Main Form  in C#

{{< highlight cs >}}
public partial class Bivarianteform : Form
    {
        public Bivarianteform()
        {
            InitializeComponent();
            contb = new Bitmap(755, 681);
            g2 = Graphics.FromImage(contb);
           
        }


        Dictionary<int, ElementoDisribuzione> csvContent = new Dictionary<int, ElementoDisribuzione>();
        Distribuzione distr = new Distribuzione();
        MediaCalOnline medie = new MediaCalOnline();
        String[,] bivariantMatrix;
        List<String> attributename = new List<string>();
        List<String> bivariante = new List<string>();//per ora poi diventera n variante;
        Bitmap contb;
        Graphics g2;
       
        List<PointF> points = new List<PointF>();
        List<PointF> regressiony = new List<PointF>();
        List<PointF> regressionx = new List<PointF>();

        Matrix m = new Matrix();
        Matrix m2 = new Matrix();
        Matrix m3 = new Matrix();
        int nr, nc;

        //Distributions 
        SortedDictionary<Tuple<double, double>, int> firstdistr;
        SortedDictionary<Tuple<double, double>, int> seconddistr;
        bool movable = false;
        bool resiable = false;
        // movable view port
        int contgleft = 0;
        int contgtop = 50;
        int contgwid = 400;
        int contgheight = 400;
        int mouseDeltax=0;
        int mouseDeltay=0;
        // window
        double minX_Window = 0;
        double maxX_Window = 400;
        double minY_Window = 0;
        double maxY_Window = 400;


        Rectangle viewPortcontig=new Rectangle(0,50, 400, 400);






        private void button1_Click(object sender, EventArgs e)


        {

            var filePath = string.Empty;
            openFileDialog1.InitialDirectory = "c:\\";
            openFileDialog1.Filter = "csv files (*.csv)|*.csv|All files (*.*)|*.*";
            openFileDialog1.FilterIndex = 2;
            openFileDialog1.RestoreDirectory = true;

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //Get the path of specified file
                filePath = openFileDialog1.FileName;

                //Read the contents of the file into a stream
                using (TextFieldParser csvParser = new TextFieldParser(filePath))
                {
                    csvParser.CommentTokens = new string[] { "#" };
                    csvParser.SetDelimiters(new string[] { "," });
                    csvParser.HasFieldsEnclosedInQuotes = true;

                    // Save the row with the column names
                    string[] fieldsNames = csvParser.ReadFields();
                    attributename.AddRange(fieldsNames);
                    int i = 0;
                    while (!csvParser.EndOfData)
                    {
                        // Read current line fields, pointer moves to the next line.

                        string[] fields = csvParser.ReadFields();
                        ElementoDisribuzione elem = new ElementoDisribuzione(fields[0]);
                        int j = 0;
                        foreach (String field in fields)
                        {
                            if (!String.IsNullOrEmpty(field))
                            {
                                double tmp;
                                if (Double.TryParse(field, out tmp)) { elem.setVariable(fieldsNames[j], new Tuple<Object, Type>(tmp, tmp.GetType())); medie.addAttribute(fieldsNames[j], tmp); }
                                else elem.setVariable(fieldsNames[j], new Tuple<Object, Type>(field, field.GetType()));
                            }
                            j++;
                        }
                        csvContent.Add(i, elem);
                        distr.addElementoDef(elem);
                        i++;
                    }
                }
                button2.Visible = true;
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            ;

            foreach (var elem in attributename)
                contextMenuStrip1.Items.Add(elem);
            contextMenuStrip1.Visible = true;

        }

        private void contextMenuStrip1_Opening(object sender, CancelEventArgs e)
        {

        }

        private void contextMenuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

            bivariante.Add(e.ClickedItem.Text);
          
            button2.Visible = false;
            foreach (var elem in attributename)
                contextMenuStrip2.Items.Add(elem);
            contextMenuStrip2.Visible = true;
        }

        private void contextMenuStrip2_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

            bivariante.Add(e.ClickedItem.Text);

            double mediax = 0;
            double mediay = 0;
            double sigmax2=0;
            double sigmay2=0;
            double sigmaxy=0;

            bool isDouble = false;

            List<Double> valuesx = new List<double>(0);
            List<Double> valuesy = new List<double>(0);
            medie.getMedia(bivariante.ElementAt(0), out mediax);
            //se la media è diversa da zero sono sicuro che è double
            medie.getMedia(bivariante.ElementAt(1), out mediay);

            if (mediax != 0)
            {
                if (mediay != 0) {


                    isDouble = true;
                    Tuple<Object, Type> tmp;
                    foreach (var elm in csvContent.Values)
                    {
                        elm.getVariable(bivariante.ElementAt(0), out tmp);
                        valuesx.Add((double)tmp.Item1);

                        elm.getVariable(bivariante.ElementAt(1), out tmp);
                        valuesy.Add((double)tmp.Item1);

                    }
                    medie.getdDeviation2(bivariante.ElementAt(0), valuesx, out sigmax2);
                    distr.getdistribuzioneN(bivariante.ElementAt(0), out firstdistr);
                    medie.getdDeviation2(bivariante.ElementAt(1), valuesy, out sigmay2);    
                    distr.getdistribuzioneN(bivariante.ElementAt(1), out seconddistr);
                    medie.getbivariantDeviation(bivariante.ElementAt(0), bivariante.ElementAt(1), valuesx,valuesy, out sigmaxy);

                    for (int i = 0; i <= maxX_Window; i++)
                    {
                        regressionx.Add(new PointF(i, (float) (((sigmaxy / sigmax2) * (i - mediax)) + mediay)));
                            
                     }

                    for (int i = 0; i <= maxY_Window; i++)
                    {
                        regressiony.Add(new PointF((float)(((sigmaxy / sigmay2) * (i - mediay)) + mediax), i));

                    }



                } }

            bivariantMatrix = distr.getbivariantmatrix(bivariante, csvContent.Values, out nr, out nc);            
            this.button3.Visible = true;


        }


        
        private void button3_Click(object sender, EventArgs e)
        {
            creaGrafici();
        }

        private void creaGrafici()
        {
          
            foreach (var elem in csvContent)
            {
                Tuple<Object, Type> a, b;

                float x, y;
                elem.Value.getVariable(bivariante.ElementAt(0), out a);
                elem.Value.getVariable(bivariante.ElementAt(1), out b);
                x = (float)(double)a.Item1;
                y = (float)(double)b.Item1;


                points.Add(new PointF(x, y));

            }

          
                
            
            //contingency
            createconting(g2, 0, 50,400,400);

        }

        private void createconting(Graphics g2, int dinamicleft, int dinamictop,int contgw,int contgh)
        {

            viewPortcontig.X = dinamicleft;
            viewPortcontig.Y = dinamictop;
            viewPortcontig.Width = contgw;
            viewPortcontig.Height = contgh;
            //viewPortcontig.Location= new Point(viewPortcontig.Location.X+dinamicleft,viewPortcontig.Location.Y+dinamictop);
            g2.Clear(BackColor);
            g2.FillRectangle(Brushes.White, viewPortcontig);
            // window drow 
            g2.DrawLine(new Pen(Color.Black, 2), viewPortcontig.X, viewPortcontig.Y, viewPortcontig.X, (viewPortcontig.Y + viewPortcontig.Height));
            g2.DrawLine(new Pen(Color.Black, 2), viewPortcontig.X, (viewPortcontig.Y + viewPortcontig.Height), (viewPortcontig.X + viewPortcontig.Width), (viewPortcontig.Y + viewPortcontig.Height));

            m.Reset();
            m.Translate(-(int)minX_Window, -(int)minY_Window, MatrixOrder.Append);
            m.Scale((int)(viewPortcontig.Width / (maxX_Window - minX_Window)), (int)(-viewPortcontig.Height / (maxY_Window - minY_Window)), MatrixOrder.Append);
            m.Translate(viewPortcontig.Left, viewPortcontig.Top + viewPortcontig.Height, MatrixOrder.Append);
            
         
            PointF[] myPoints = points.ToArray();
            PointF[] myPointsreal = points.ToArray();
            PointF[] pRegressionx = regressionx.ToArray();
            PointF[] pRegressiony = regressiony.ToArray();


            int i = 0;
            m.TransformPoints(myPoints);
            m.TransformPoints(pRegressionx);
            m.TransformPoints(pRegressiony);

            foreach (PointF punto in myPoints)
            {
                if (myPointsreal[i].X <= maxX_Window && myPointsreal[i].Y <= maxY_Window)
                {
                    g2.FillEllipse(Brushes.Black, new Rectangle(new Point((int)(punto.X - 2), (int)(punto.Y - 2)), new Size(4, 4)));

                    g2.DrawString(myPointsreal[i].ToString(), new Font("Arial", 10), Brushes.Black, (int)(punto.X), (int)(punto.Y));
                    g2.FillEllipse(Brushes.Red, new Rectangle(new Point((int)(punto.X - 2), (int)(viewPortcontig.Y + viewPortcontig.Height - 2)), new Size(4, 4)));
                    g2.FillEllipse(Brushes.Red, new Rectangle(new Point((int)(viewPortcontig.X), (int)(punto.Y - 2)), new Size(4, 4)));


                }
                i++; ;

            }
            foreach (PointF punto in pRegressionx)
            {
                g2.FillEllipse(Brushes.Red, new Rectangle(new Point((int)(punto.X - 2), (int)(punto.Y - 2)), new Size(4, 4)));
            }
            foreach (PointF punto in pRegressiony)
            {
                g2.FillEllipse(Brushes.Green, new Rectangle(new Point((int)(punto.X - 2), (int)(punto.Y - 2)), new Size(4, 4)));
            }




            pictureBox2.Image = contb ;
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            if (   (e.Location.Y>=viewPortcontig.Top &&e.Location.Y <= (viewPortcontig.Top+viewPortcontig.Height))&&(e.Location.X >= viewPortcontig.Left && e.Location.X <= (viewPortcontig.Left + viewPortcontig.Width)))
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
                createconting(g2, contgleft, contgtop, contgwid, contgheight);
            }
            if (resiable == true)
            {
                mouseDeltax = -mouseDeltax + e.Location.X ;
                mouseDeltay = -mouseDeltay + e.Location.Y;
                contgwid += mouseDeltax/40;
                contgheight += mouseDeltay/40;
                createconting(g2, contgleft, contgtop, contgwid, contgheight);
            }

               
                

            

        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            resiable = false;
            movable = false;
        }

      
    }
    }


{{< /highlight >}}
