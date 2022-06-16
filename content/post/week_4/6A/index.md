+++
title = "6_A"
date = 2021-10-18T20:03:36+02:00
description = "Create some chart and a dinamic contingency table "

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

## 6_A assignament

### Request
Prepare separately the following charts: 1) Scatterplot, 2) Histogram/Column chart [in the histogram, within each class interval, draw also a vertical colored line where lies the true mean of the observations falling in that class] and 3) Contingency table, using the graphics object and its methods (Drawstring(), MeasureString(), DrawLine(), etc).
Use them to represent 2 numerical variables that you select from a CSV file. In particular, in the same picture box, you will make at least 2 separate charts: 1 dynamic rectangle will contain the contingency table, and 1 rectangle (chart) will contain the scatterplot, with the histograms/column charts and rug plots drawn respectively near the two axis (and oriented accordingly)

### My Solution

{{< youtube DsTEWsdZju8 >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment6/C%23/BivarianteGraphics)


#### Class Main Form  in C#

{{< highlight cs >}}
 public partial class Bivarianteform : Form
    {
        public Bivarianteform()
        {
            InitializeComponent();
            b = new Bitmap(755,681);
            g = Graphics.FromImage(b);
            contb = new Bitmap(739,668);
            g2 = Graphics.FromImage(contb); 
        }


        Dictionary<int, ElementoDisribuzione> csvContent = new Dictionary<int, ElementoDisribuzione>();
        Distribuzione distr = new Distribuzione();
        MediaCalOnline medie = new MediaCalOnline();
        String[,] bivariantMatrix;
        List<String> attributename = new List<string>();
        List<String> bivariante = new List<string>();//per ora poi diventera n variante;
        Bitmap b;
        Bitmap contb;
        Graphics g2;
        Graphics g;
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
        int contgwid = 300;
        int contgheight = 400;
        int mouseDeltax=0;
        int mouseDeltay=0;


        Rectangle viewPortcontig=new Rectangle(0,50, 300, 400);






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
           
            double media = 0;
            double stdVariation;
            List<Double> values=new List<double>(0);
            medie.getMedia(e.ClickedItem.Text, out media);
            //se la media è diversa da zero sono sicuro che è double
            if (media != 0)
            {
                Tuple<Object, Type> tmp;
                foreach (var elm in csvContent.Values)
                {
                    elm.getVariable(e.ClickedItem.Text, out tmp);

                    values.Add((double)tmp.Item1);

                }
                medie.getStandardDeviation(e.ClickedItem.Text, values,out stdVariation);
                distr.getdistribuzioneN(e.ClickedItem.Text, out firstdistr);
               
            }
            else stdVariation = 0;


            bivariante.Add(e.ClickedItem.Text);
          
            button2.Visible = false;
            foreach (var elem in attributename)
                contextMenuStrip2.Items.Add(elem);
            contextMenuStrip2.Visible = true;
        }

        private void contextMenuStrip2_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {
            double media2 = 0;
            double stdVariation;
            List<Double> values = new List<double>(0);
           
            bool isDouble = false;
            medie.getMedia(e.ClickedItem.Text, out media2);
            if (media2 != 0)
            {
                isDouble = true;
                Tuple<Object, Type> tmp;
                foreach (var elm in csvContent.Values)
                {
                    elm.getVariable(e.ClickedItem.Text, out tmp);

                    values.Add((double)tmp.Item1);

                }
                medie.getStandardDeviation(e.ClickedItem.Text, values, out stdVariation);
                distr.getdistribuzioneN(e.ClickedItem.Text, out seconddistr);
            }
            else stdVariation = 0;
            bivariante.Add(e.ClickedItem.Text);
           
            
            bivariantMatrix = distr.getbivariantmatrix(bivariante, csvContent.Values, out nr, out nc);
            
            this.button3.Visible = true;


        }


        
        private void button3_Click(object sender, EventArgs e)
        {
            creaGrafici(g);
        }

        private void creaGrafici(Graphics g)
        { 
            //viewport scatterport
            Rectangle viewPort = new Rectangle(300, 50, 400,400);
            int i = 0;
            

            // window
            double minX_Window = 0;
            double maxX_Window =  400;
            double minY_Window = 0;
            double maxY_Window = 400;

            g.Clear(Color.DarkGray);
            g.FillRectangle(Brushes.White , viewPort);
         

            g.DrawLine(new Pen(Color.Black,2), viewPort.X,viewPort.Y ,viewPort.X, (viewPort.Y +viewPort.Height));
            g.DrawLine(new Pen(Color.Black,2), viewPort.X,(viewPort.Y + viewPort.Height),(viewPort.X+viewPort.Width), (viewPort.Y + viewPort.Height));

          
            m.Translate(-(int)minX_Window,-(int)minY_Window,MatrixOrder.Append);
            m.Scale( (int)(viewPort.Width / (maxX_Window - minX_Window)),(int)(-viewPort.Height / (maxY_Window - minY_Window)), MatrixOrder.Append);
            m.Translate(viewPort.Left, viewPort.Top + viewPort.Height, MatrixOrder.Append);

            List<PointF> points = new List<PointF>();
            foreach(var elem in csvContent)
            {
                Tuple<Object,Type >a, b;
   
                float x,y;
                elem.Value.getVariable(bivariante.ElementAt(0), out a);
                elem.Value.getVariable(bivariante.ElementAt(1), out b);
                x = (float)(double)a.Item1;
                y = (float)(double)b.Item1;


                points.Add(new PointF(x, y));

            }
            PointF[] myPoints = points.ToArray();
            PointF[] myPointsreal = points.ToArray();
            i = 0;
            m.TransformPoints(myPoints );

            foreach(PointF punto in myPoints)
            {
                if (myPointsreal[i].X <= maxX_Window && myPointsreal[i].Y <= maxY_Window)
                {
                    g.FillEllipse(Brushes.Black, new Rectangle(new Point((int)(punto.X - 2), (int)(punto.Y - 2)), new Size(4, 4)));
                   
                    g.DrawString(myPointsreal[i].ToString(), new Font("Arial", 10), Brushes.Black,(int)(punto.X), (int)(punto.Y));
                    g.FillEllipse(Brushes.Red, new Rectangle(new Point((int)(punto.X - 2), (int)(viewPort.Y + viewPort.Height - 2)), new Size(4, 4)));
                    g.FillEllipse(Brushes.Red, new Rectangle(new Point((int)(viewPort.X), (int)(int)(punto.Y - 2)), new Size(4, 4)));
                   

                }
                i++;  ;

            }

            //Column x chart viewport
            Rectangle viewPort2 = new Rectangle(300, 450, 400, 100);
            g.FillRectangle(Brushes.White, viewPort2);
            g.DrawLine(new Pen(Color.Black, 2), viewPort2.X, viewPort2.Y, viewPort2.X, (viewPort2.Y + viewPort2.Height));
            g.DrawLine(new Pen(Color.Black, 2), viewPort2.X, (viewPort2.Y + viewPort2.Height), (viewPort2.X + viewPort2.Width), (viewPort2.Y + viewPort2.Height));

            m2.Translate(-(int)minX_Window, -(int)minY_Window, MatrixOrder.Append);
            m2.Scale((int)(viewPort2.Width / (maxX_Window - minX_Window)), (int)(-viewPort2.Height / (maxY_Window - minY_Window)), MatrixOrder.Append);
            m2.Translate(viewPort2.Left, viewPort2.Top + viewPort2.Height, MatrixOrder.Append);

            List<PointF> distrF = new List<PointF>();
            foreach(var point in firstdistr)
            {
                distrF.Add(new PointF((float)((point.Key.Item2 - point.Key.Item1)/2 +point.Key.Item1), point.Value));

            }
            PointF[] myPoints2 = distrF.ToArray();
            PointF[] myPoints2real = distrF.ToArray();
            i = 0;

            m2.TransformPoints(myPoints2);

            foreach (PointF punto in myPoints2)
            {
                if (myPoints2real[i].X <= maxX_Window && myPoints2real[i].Y <= maxY_Window)
                    g.FillRectangle(Brushes.DarkCyan, new Rectangle((int)punto.X,viewPort2.Top,viewPort2.Width/30, (int)myPoints2real[i].Y/10));
                i++;
            }

            //contingeny
           Rectangle viewPort3 = new Rectangle(200, 50, 100, 400);
            g.FillRectangle(Brushes.White, viewPort3);
            g.DrawLine(new Pen(Color.Black, 2), viewPort3.X, viewPort3.Y, viewPort3.X, (viewPort3.Y + viewPort3.Height));
            g.DrawLine(new Pen(Color.Black, 2), viewPort3.X, (viewPort3.Y + viewPort3.Height), (viewPort3.X + viewPort3.Width), (viewPort3.Y + viewPort3.Height));

            m3.Translate(-(int)minX_Window, -(int)minY_Window, MatrixOrder.Append);
            m3.Scale((int)(viewPort3.Width / (maxX_Window - minX_Window)), (int)(-viewPort3.Height / (maxY_Window - minY_Window)), MatrixOrder.Append);
            m3.Translate(viewPort3.Left, viewPort3.Top + viewPort3.Height, MatrixOrder.Append);

            List<PointF> distrS = new List<PointF>();
            foreach (var point in seconddistr)
            {
                distrS.Add(new PointF(point.Value, (float)((point.Key.Item2 - point.Key.Item1) / 2 + point.Key.Item1)));

            }
            PointF[] myPoints3 = distrS.ToArray();
            PointF[] myPoints3real = distrS.ToArray();
            i = 0;
            

            m3.TransformPoints(myPoints3);

            foreach (PointF punto in myPoints3)
            {
               if (myPoints3real[i].X <= maxX_Window && myPoints3real[i].Y <= maxY_Window)
                   g.FillRectangle(Brushes.DarkCyan, new Rectangle(viewPort3.Left, (int)punto.Y, (int)punto.X/10, viewPort3.Height/30));
                i++;

            }


            //contingency
            createconting(g2, 0, 50,300,400);
            

            pictureBox1.Image = b;


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
            int j = 0;
            for (int i = 0; i <= nr; i++)
            {
                for (j = 0; j <= nc; j++)
                {
                    Rectangle tmp = new Rectangle(viewPortcontig.Left + (j * (viewPortcontig.Width / (nc + 1))), viewPortcontig.Top + (i * (viewPortcontig.Height / (nr + 1))), viewPortcontig.Width / (nc + 1), viewPortcontig.Height / (nr + 1));
                    g2.DrawRectangle(new Pen(Color.Black, 2), tmp);
                    g2.DrawString(bivariantMatrix[i, j], new Font("Arial", 6), Brushes.Black, tmp);


                }
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
            }
            if (resiable == true)
            {
                mouseDeltax = -mouseDeltax + e.Location.X ;
                mouseDeltay = -mouseDeltay + e.Location.Y;
                contgwid += mouseDeltax/40;
                contgheight += mouseDeltay/40;
            }

                 createconting(g2, contgleft, contgtop,contgwid,contgheight);
                

            

        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            resiable = false;
            movable = false;
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
    }
    }

{{< /highlight >}}
