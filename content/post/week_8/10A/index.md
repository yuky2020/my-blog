+++
title = "10_A"
date = 2021-10-28T20:03:36+02:00
description = "Given a random variable, extract m samples of size n and plot the empirical distribution of its mean (histogram), the first and the last order statistics"
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

## 10_A assignament

### Request
 Given a random variable, extract m samples of size n and plot the empirical distribution of its mean (histogram), the first and the last order statistics. Comment on what you see.


### My Solution

{{< youtube _t6xILUnXLk >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment10/C%23/BernulliGraphics)


### Class for graphicate the histogram's
{{< highlight cs >}}
private void disegnaIstogrammi(Rectangle viewPort, Tuple<Dictionary<double, int>, Dictionary<decimal, int>, Dictionary<decimal, int>> tuple)
        {
            int i = 0;
            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(128, 0, 0, 0));

            foreach (var v in tuple.Item1)
            {
                int x, y;
                int width, height;
                // in this case on the fly trasformation is way faster
                x = (int)(this.viewPort.Left + 20 * i);
                y = (int)(viewPort.Top + viewPort.Height / 4 - v.Value / 10);


                width = 15;
                height = v.Value / 10;

                Rectangle rectangle = new Rectangle(x, y, width, height);

                g2.DrawRectangle(Pens.Black, rectangle);
                g2.FillRectangle(semiTransBrush, rectangle);

                g2.FillRectangle(Brushes.Cyan, rectangle);
                g2.DrawString(((decimal)v.Key).ToString(), new Font("Calibri", 10.0f,
                                 FontStyle.Regular, GraphicsUnit.Pixel), semiTransBrush, new Point(x, y+v.Value/10+1));
                i++;
            }
            g2.DrawString("Distribuzione originale ", new Font("Calibri", 13.0f,
                               FontStyle.Italic, GraphicsUnit.Pixel), semiTransBrush, new Point(this.viewPort.Left - 140, (viewPort.Top + viewPort.Height/4)));

            i = 0;

            foreach (var v in tuple.Item2)
            {
                int x, y;
                int width, height;
                // in this case on the fly trasformation is way faster
                x = (int)(this.viewPort.Left + 20 * i);
                y = (int)(viewPort.Top + viewPort.Height /2  - v.Value / 2);


                width = 15;
                height = v.Value / 2;

                Rectangle rectangle = new Rectangle(x, y, width, height);

                g2.DrawRectangle(Pens.Black, rectangle);
                g2.FillRectangle(semiTransBrush, rectangle);

                g2.FillRectangle(Brushes.Cyan, rectangle);
                g2.DrawString(v.Key.ToString(), new Font("Calibri", 10.0f,
                                 FontStyle.Regular, GraphicsUnit.Pixel), semiTransBrush, new Point(x, y+v.Value/2));
                i++;
            }
            g2.DrawString("Min ", new Font("Calibri", 13.0f,
                               FontStyle.Italic, GraphicsUnit.Pixel), semiTransBrush, new Point(this.viewPort.Left - 50, (viewPort.Top + viewPort.Height/2)));



            i = 0;

            foreach (var v in tuple.Item3)
            {
                int x, y;
                int width, height;
                // in this case on the fly trasformation is way faster
                x = (int)(this.viewPort.Left + 20 * i);
                y = (int)(viewPort.Top + viewPort.Height -30  - v.Value /2);


                width = 15;
                height = v.Value / 2;

                Rectangle rectangle = new Rectangle(x, y, width, height);

                g2.DrawRectangle(Pens.Black, rectangle);
                g2.FillRectangle(semiTransBrush, rectangle);

                g2.FillRectangle(Brushes.Cyan, rectangle);
                g2.DrawString(v.Key.ToString(), new Font("Calibri", 10.0f,
                                 FontStyle.Regular, GraphicsUnit.Pixel), semiTransBrush, new Point(x, y+v.Value/2));
                i++;
            }
            g2.DrawString("Max ", new Font("Calibri", 13.0f,
                               FontStyle.Italic, GraphicsUnit.Pixel), semiTransBrush, new Point(this.viewPort.Left - 50, (viewPort.Top + viewPort.Height-30 )));



        }

{{< /highlight >}}



### Class for the generation and distribution calculus
{{< highlight cs >}}
public Tuple<Dictionary<double, int>, Dictionary<decimal, int>, Dictionary<decimal, int>> valueToDictionarys(int m, int n)
        {
            Dictionary<double, List<double>> randomvalues = new Dictionary<double, List<double>>();
            int i = 0;
            int j = 0;
            decimal min;
            decimal max;

            //generation of random ditribution
            for (i = 0; i < m; i++)
            {
                List<Double> tmp = new List<double>();
                for (j = 0; j < n; j++)
                    tmp.Add(R.NextDouble());

                randomvalues.Add(i, tmp);
            }

            Dictionary<double, int> randomdistrib = new Dictionary<double, int>();
            Dictionary<decimal, int> minValues = new Dictionary<decimal,int>();
            Dictionary<decimal, int> maxValues = new Dictionary<decimal, int>();

            for (double k = 0.0; k <= 1.0000; k = k + 0.100)
            {
                foreach (var list in randomvalues)
                {
                    foreach (var elem in list.Value)
                    {
                        if (elem >= k && elem <= (k + 0.1))
                        {
                            int tmp = 1;
                            if (randomdistrib.TryGetValue(k, out tmp)) { randomdistrib.Remove(k); tmp++; }
                            randomdistrib.Add(k, tmp);
                        }
                    }
                }
            }


            foreach (var list in randomvalues)
            {
                min = 1;
                max = 0;
                foreach (var elem in list.Value)
                {
                    if ((decimal)elem < min) min =((decimal)( elem-(elem%0.01)));
                    if ((decimal)elem > max) max =  ((decimal)(elem - (elem % 0.01)));
                }
                int tmp2 = 1;
                if (minValues.TryGetValue(min, out tmp2)) { minValues.Remove(min); tmp2++; }
                minValues.Add(min, tmp2);
                tmp2 = 1;
                if (maxValues.TryGetValue(max, out tmp2)) { maxValues.Remove(max); tmp2++; }
                maxValues.Add(max, tmp2);

            }

            return new Tuple<Dictionary<double, int>, Dictionary<decimal, int>, Dictionary<decimal, int>>(randomdistrib, minValues, maxValues);
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
{{< /highlight >}}
