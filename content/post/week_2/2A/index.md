+++
title = "2_A"
date = 2021-10-05T20:03:36+02:00
description = "arithmetic mean and my own algo to compute the distribution for a discrete variable and for a continuous variable"

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

## 2_A assignament

### Request
Create - in both languages C# and VB.NET - a demonstrative program which computes the online arithmetic mean (if it's a numeric variable) and your own algo to compute the distribution for a discrete variable and for a continuous variable (can use values simulated with RANDOM object).

### My Solution
{{< youtube e3GvPX-zsH8 >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment2/C%23/OnlineArithmeticMean)

[Code in VB.net](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment2/VB.NET/AritMeanDistr)

[Code in zip(mirror)](https://drive.google.com/file/d/1Qv5ttEjqGmwPA4nUcWTi5KP9sYKkm8QJ/view?usp=sharing)

#### Class Elemento Distribuzione in C#

{{< highlight cs >}}
  class ElementoDisribuzione
    {
       private String name;
       private  Dictionary<String,Double> variabili;
    public ElementoDisribuzione(String nome)
        {
            this.name = nome;
            this.variabili = new Dictionary<string, double>();

        }

    public void setVariable(String name,double value) {
            this.variabili.Add(name, value);
        }

    public bool getVariable(String name,out double ret)
        { 
            if (this.variabili.TryGetValue(name, out ret)) return true;
            else return false;
        }
    public Dictionary<String, Double> getVariabili() {
            return this.variabili;
        }

    }

{{< /highlight >}}

#### Class MediaCalOnline in C#

{{< highlight cs >}}
  class MediaCalOnline
    {

        Dictionary<String, double> medieAritmetica;
        Dictionary<String, int> numeroElementi;


        public MediaCalOnline()
        {
            medieAritmetica = new Dictionary<string, double>();
            numeroElementi = new Dictionary<String, int>();

        }
        public void addAttribute(String nome, double value)
        {
            double tmp;
            int i;
            if (medieAritmetica.ContainsKey(nome))
            {
                medieAritmetica.TryGetValue(nome, out tmp);
                numeroElementi.TryGetValue(nome, out i);
                i++;
                tmp = tmp + (value - tmp) / i;
                numeroElementi.Remove(nome);
                medieAritmetica.Remove(nome);
                medieAritmetica.Add(nome, tmp);
                numeroElementi.Add(nome, i);



            }
            else
            {
                medieAritmetica.Add(nome, value);
                numeroElementi.Add(nome, 1);
            }
        }
            public bool getMedia(String name,out double i)
            {
            if (medieAritmetica.TryGetValue(name, out i)) return true;
            else return false;
            }
        public void addElemento(ElementoDisribuzione e)
        {
            foreach (var item in e.getVariabili())
                addAttribute(item.Key, item.Value);

        }
        


    }

{{< /highlight >}}

#### Class Distribuzione in C#

{{< highlight cs >}}
  class Distribuzione

    {
        private Dictionary<String, SortedDictionary<Tuple<double, double>, int>> distr;
        double intervall = 10;

        public Distribuzione()
        {
            distr = new Dictionary<String, SortedDictionary<Tuple<double, double>, int>>();

        }
        //intervall standard 10
        public void addAttributDef(String s, double i)
        {
            addAttribute(s, i, intervall);
        }
        public void addAttribute(String s, double value, double inte)
        {
            SortedDictionary<Tuple<double, double>, int> actualdistr;
            double min, max;
            int i = 1;
            min = value - (value % inte);
            max = value + (inte - (value % inte));
            Tuple<double, double> tmp = new Tuple<double, double>(min, max);

            if (!distr.TryGetValue(s, out actualdistr))
            {
                actualdistr = new SortedDictionary<Tuple<double, double>, int>();
                actualdistr.Add(tmp, 1);
                distr.Add(s, actualdistr);

            }
            else
            {
                if (!actualdistr.TryGetValue(tmp, out i)) actualdistr.Add(tmp, 1); 
                else { i++; actualdistr.Remove(tmp); actualdistr.Add(tmp, i); }
                distr.Remove(s); 
                distr.Add(s, actualdistr);
            }
        }

        public void addElemento(ElementoDisribuzione e, double inter)
        {
            foreach (var item in e.getVariabili()) {
                this.addAttribute(item.Key, item.Value, inter);
            }


        }
        public void addElementoDef(ElementoDisribuzione e)
        {
            addElemento(e, intervall);
        }



        public bool getdistribuzione(string s, out SortedDictionary<Tuple<double, double>, int> req)
        {
     
            if (distr.TryGetValue(s, out req)) return true;
            else return false;

        }
    }  

{{< /highlight >}}

#### Main Form in C#

{{< highlight cs >}}
     public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        Random r = new Random();
        MediaCalOnline mc=new MediaCalOnline();
        Distribuzione dc = new Distribuzione();
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Interval = 2;
            timer1.Start();
            button3.Visible = true;
            button2.Visible = true;
            button1.Visible = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer2.Interval = 10;
            timer2.Start();
            button2.Visible = false;
            
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            double height;
            ElementoDisribuzione studente = new ElementoDisribuzione("Student");
            height =r.NextDouble()+r.Next(140,200);
            studente.setVariable("height", height);
            mc.addElemento(studente);
            dc.addElementoDef(studente);

            richTextBox1.Text += "nuovo Studente altezza: " + height + Environment.NewLine;




        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            double i;
            SortedDictionary<Tuple<double, double>, int> distTest =new  SortedDictionary<Tuple<double, double>, int>();
            mc.getMedia("height", out i);
            if (dc.getdistribuzione("height", out distTest))
            {
                richTextBox3.Text = "";
                foreach (var item in distTest)
                {
                    richTextBox3.Text += item.Key.Item1 + "-" + item.Key.Item2 + " presenta " + item.Value + " entita "+Environment.NewLine;

                }
            }

            richTextBox2.Text = "the A M of the height is" + i + Environment.NewLine;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            timer1.Stop();
            timer2.Stop();
            button1.Visible = true;
            button2.Visible = true;
        }

      
    }

{{< /highlight >}}