+++
title = "3_A"
date = 2021-10-05T20:03:36+02:00
description = "an object providing a rectangular area which can be moved and resized using the mouse"

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

## 3_A assignament

### Request
Create an object providing a rectangular area which can be moved and resized using the mouse. This area will hold our future charts and graphics.


### My Solution
{{< youtube ePe5KlR914c>}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment3/Resiziable%20model)


#### Main Form:

{{< highlight cs >}}
  public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        bool allowResize = false;
        bool allowMove = false;
        private void resizaileBox_MouseUp(object sender, MouseEventArgs e)
        {
            allowResize = false;
            allowMove = false;
        }

        private void resizaileBox_MouseMove(object sender, MouseEventArgs e)
        {
            if (allowResize)
            {
                this.panel1.Height = resizaileBox.Top + e.Y;
                this.panel1.Width = resizaileBox.Left + e.X;
            }
            if (allowMove)
            {
                this.panel1.Location = new Point(this.panel1.Location.X + e.X, this.panel1.Location.Y + e.Y);
                

                
            }
        }

        private void resizaileBox_Click(object sender, EventArgs e)
        {

        }

        private void resizaileBox_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right) allowResize = true;
            else allowMove = true;
        }

       

    }
  {{< /highlight >}}

