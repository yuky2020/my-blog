---
title: 1_A
description: Very frist pratical homework of statistics, main scope is to better understanding VB.net and C# programming leanguage
slug: 1_A
date:  2019-04-26T20:03:36+02:00
image: images/2.png
categories:
    statistics
tags:
     ["after", "statistic"]
---

## 1_A assignament

### Request
Create - in both languages C# and VB.NET - a program which does the following simple tasks to get acquainted with the tool:

when a button is pressed some text appears in a richtexbox on the startup form
when another button is pressed animate one or more colored balls within a rectangle

### My Solution
{{< youtube airtd7gfgA4 >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment1/C%23)

[Code in VB.net](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment1/VB.NET/WindowsApp1)

[Code in zip(mirror)](https://drive.google.com/file/d/1d5qdIW5dQYCQ6KT-iTq8_dEiNh4ylUIS/view?usp=sharing)
#### Form code In C#

{{< highlight cs >}}
  public MyFristGUI()
        {
            InitializeComponent();

            t.Interval = 4;
            flag = new Bitmap(480, 160);
            g = Graphics.FromImage(flag);
            t.Tick += T_Tick;

        }
        Bitmap flag;
        Graphics g;
        int x = 20;
        int y = 20;
        Timer t = new Timer();
       

        private void button1_Click(object sender, EventArgs e)
        {
            this.richTextBox1.Text = "button pressed";
        }

     
        private void T_Tick(object sender, EventArgs e)
        {    
            var rand2 = new Random();
            g = Graphics.FromImage(flag);
            g.Clear(Color.White);
            g.DrawCircle(new Pen(Brushes.Red, 2), x, y, 20);
            g.FillCircle(Brushes.Red, x, y, 20);
           
            x = x+rand2.Next(-10, 10);
            y = y+ rand2.Next(-10,10);
            if (x > 460) x = x - 10;
            if (x < 20) x = x + 10;
            if (y > 140) y = y - 10;
            if (y < 20) y = y + 10;
            pictureBox2.Image = flag;

         
           
        }



        private void MyFristGUI_Load(object sender, EventArgs e)
        {


        }

        private void button2_MouseClick(object sender, MouseEventArgs e)
        {
            
            var rand = new Random();
            x = rand.Next(20, 460);
            y = rand.Next(20, 140);
            t.Start();
            this.button2.Visible = false;
            this.button3.Text = "STOP";
            this.button3.Visible = true;
        }

        private void button3_MouseClick(object sender, MouseEventArgs e)
        {
            t.Stop();
            g.Clear(BackColor);
            this.button3.Visible = false;
            this.button2.Visible = true;
            pictureBox2.Image = flag;
        }

       
    }
{{< /highlight >}}
