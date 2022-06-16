+++
title = "4_RA"
date = 2021-10-18T20:03:36+02:00
description = "Real world window to viewport transformation"

draft = false
toc = false
categories = ["statistic"]
tags = ["after", "statistic"]
images = [
  "https://source.unsplash.com/collection/983219/1600x900"
] # overrides site-wide open graph image

[[resources]]
  src = "images/1.jpg"
  name = "header thumbnail"

+++

![header](images/1.jpg)

## 4_RA assignament

### Request

Do a personal research about the real world window to viewport transformation, and note separately the formulas and code which can be useful for your present and future applications.

### real world to viewport

When we want to drow a chart in .net we need to address the problem of rappresenting points inside a pictureBox(often inside a rectangle), for do this we need to operate some trasformation, we can do this one by one, or create a trasformation matrix and use this on every point.
The matrix  is for sure more rapid,and functional,so let's look in depth how it works:

#### Traformation Matrix

{{< highlight cs >}}
//Frist we need to create a matrix
Matrix m = new Matrix();
//-----
// then we need to prepare the needed trasformation
m.Translate(-(int)minX_Window,-(int)minY_Window,MatrixOrder.Append);
m.Scale( (int)(viewPort.Width / (maxX_Window - minX_Window)),(int)(-viewPort.Height / (maxY_Window - minY_Window)), MatrixOrder.Append);
m.Translate(viewPort.Left, viewPort.Top + viewPort.Height, MatrixOrder.Append);

// we apply the trasformation to the array of points that we need in the graphics
m.TransformPoints(myPoints );

// in the end we can write the point to the graphics (THIS IS AN EXAMPLE FROM MY IMPLEMENTATION) 
 foreach(PointF punto in myPoints)
            {
                if (myPointsreal[i].X <= maxX_Window && myPointsreal[i].Y <= maxY_Window)
                {
                    g.FillEllipse(Brushes.Black, new Rectangle(new Point((int)(punto.X - 2), (int)(punto.Y - 2)), new Size(4, 4)));
                   
                    g.DrawString(myPointsreal[i].ToString(), new Font("Arial", 10), Brushes.Black,(int)(punto.X), (int)(punto.Y));
                    g.FillEllipse(Brushes.Red, new Rectangle(new Point((int)(punto.X - 2), (int)(viewPort.Y + viewPort.Height - 2)), new Size(4, 4)));
                    g.FillEllipse(Brushes.Red, new Rectangle(new Point((int)(viewPort.X), (int)(int)(punto.Y - 2)), new Size(4, 4)));
                   

                }
            }
{{< /highlight >}}
