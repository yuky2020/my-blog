+++
title = "4_A"
date = 2021-10-05T20:03:36+02:00
description = "read data from a CSV file, and store it into a suitable collection of suitably designed objects, for further processing. Compute mean and standard deviation and frequency distribution"

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

## 4_A assignament

### Request
Create a program - in both languages C# and VB.NET (and optionally in js) - to read data from a CSV file, and store it into a suitable collection of suitably designed objects, for further processing. Compute mean and standard deviation and frequency distribution for at least one of the variable, and for one pair of variables.

### My Solution
{{< youtube pwyU0rRJ9xQ >}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment4)

[Code in VB.net](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment4/VB.NET/Biavariante)


#### Class Elemento Distribuzione in C#

{{< highlight cs >}}
  class ElementoDisribuzione
    {
        private String name;
        private Dictionary<String, Tuple<Object,Type>> variabili;
        public ElementoDisribuzione(String nome)
        {
            this.name = nome;
            this.variabili = new Dictionary<string, Tuple<Object, Type>>();

        }

        public void setVariable(String name, Tuple<Object, Type>s)
        {
            this.variabili.Add(name,s);
        }

        public bool getVariable(String name, out Tuple<Object, Type> ret)
        {
            if (this.variabili.TryGetValue(name, out ret)) return true;
            else return false;
        }
        public Dictionary<String, Tuple<Object, Type>> getVariabili()
        {
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
                if (item.Value.Item2 == typeof(Double)) 
                addAttribute(item.Key,(double) item.Value.Item1);

        }

        public bool getStandardDeviation(String name, List<Double> list, out double i)
        {
            double media;
            i = 0;
            if (!medieAritmetica.TryGetValue(name, out media)) return false;
            foreach (double elemnt in list)
            {
                i = i + ((elemnt - media) * (elemnt - media));

            }
            i = i / list.Count;
            i = Math.Sqrt(i);
            return true;
        }

            
        }
{{< /highlight >}}

#### Class Distribuzione in C#

{{< highlight cs >}}
  class Distribuzione

    {
        private Dictionary<String, SortedDictionary<Tuple<double, double>, int>> distrN;
        private Dictionary<string, SortedDictionary<String, int>> distrS;
        double intervall = 10;

        public Distribuzione()
        {
            distrN = new Dictionary<String, SortedDictionary<Tuple<double, double>, int>>();
            distrS = new Dictionary<String, SortedDictionary<String, int>>();

        }
        //intervall standard 10
        public void addAttributNDef(String s, double i)
        {
            addAttributeN(s, i, intervall);
        }
        public void addAttributeN(String s, double value, double inte)
        {
            SortedDictionary<Tuple<double, double>, int> actualdistr;
            double min, max;
            int i = 1;
            min = value - (value % inte);
            max = value + (inte - (value % inte));
            Tuple<double, double> tmp = new Tuple<double, double>(min, max);

            if (!distrN.TryGetValue(s, out actualdistr))
            {
                actualdistr = new SortedDictionary<Tuple<double, double>, int>();
                actualdistr.Add(tmp, 1);
                distrN.Add(s, actualdistr);

            }
            else
            {
                if (!actualdistr.TryGetValue(tmp, out i)) actualdistr.Add(tmp, 1); 
                else { i++; actualdistr.Remove(tmp); actualdistr.Add(tmp, i); }
                distrN.Remove(s); 
                distrN.Add(s, actualdistr);
            }
        }


        private void addAttributeS(string key, String value)
        {
            SortedDictionary<String, int> actualdistrS;
            int i=1;
            if (!distrS.TryGetValue(key, out actualdistrS))
            {
               
                actualdistrS = new SortedDictionary<String, int>();
                actualdistrS.Add(value, 1);
                distrS.Add(key, actualdistrS);

            }
            else
            {
                if (!actualdistrS.TryGetValue(value, out i)) actualdistrS.Add(value, 1);
                else { i++; actualdistrS.Remove(value); actualdistrS.Add(value, i); }
                distrS.Remove(key);
                distrS.Add(key, actualdistrS);
            }

        }

        public void addElemento(ElementoDisribuzione e, double inter)
        {
            foreach (var item in e.getVariabili()) {
                if (item.Value.Item2 == typeof(string))
                this.addAttributeS(item.Key, (String)item.Value.Item1);
                else
                this.addAttributeN(item.Key, (double)item.Value.Item1, inter);
            }


        }

      

        public void addElementoDef(ElementoDisribuzione e)
        {
            addElemento(e, intervall);
        }



        public bool getdistribuzioneN(string s, out SortedDictionary<Tuple<double, double>, int> req)
        {
     
            if (distrN.TryGetValue(s, out req)) return true;
            else return false;

        }
        public bool getdistribuzioneS(string s, out SortedDictionary<String, int> req)
        {

            if (distrS.TryGetValue(s, out req)) return true;
            else return false;

        }



        public string[,] getbivariantmatrix(List<string> bivariante, Dictionary<int, ElementoDisribuzione>.ValueCollection values, out int numeroRighe, out int numeroColonnne)
        { string[] variabili = bivariante.ToArray();
            SortedDictionary<Tuple<double, double>, int> columns;
            SortedDictionary<Tuple<Double, double>, int> rows;
            int i, j = 0;

            distrN.TryGetValue(variabili[0], out columns);
            distrN.TryGetValue(variabili[1], out rows);
            //mi ricavo gli intervalli
            double intervalloRow = 0;
            while (intervalloRow == 0) { intervalloRow = rows.ElementAt(j).Key.Item2 - rows.ElementAt(j).Key.Item1; j++; }

            j = 0;
            double intervalloCol = 0;
            while (intervalloCol == 0) {intervalloCol = columns.ElementAt(j).Key.Item2 - columns.ElementAt(j).Key.Item1; j++; }

             numeroColonnne = columns.Count();
             numeroRighe = rows.Count();

            String[,] outputM = new String[numeroRighe+1,numeroColonnne+1];
            int[,] outputMV = new int[numeroRighe, numeroColonnne];
            //inizilizo la matrice outputMatriceValori
            for (i = 0; i < numeroRighe; i++)
                for (j = 0; j < numeroColonnne; j++) outputMV[i,j] = 0;

            i = 1;
            j = 1;
            outputM[0, 0] = " ";

            // riempo gli estremi della tabella
            foreach(var column in columns.Keys)
            {
                outputM[0, i] = column.ToString();
                i++;


            }
            foreach (var row in rows.Keys)
                {
                 outputM[j, 0] = row.ToString();
                 j++;


                }

            //cerco l'intervallo giusto per entrambi e li carico
            foreach (var elm in values)
            {
                bool trov0 = false; 
                bool trov1 = false;
                Tuple<Object, Type> tmpv0;
                Tuple<Object, Type> tmpv1;
                elm.getVariable(variabili[0], out tmpv0);
                elm.getVariable(variabili[1], out tmpv1);
                 i = 0;
                 j = 0 ;
                while (!trov0&& i<numeroColonnne)
                {
                    if (((double)tmpv0.Item1 - columns.Keys.ElementAt(i).Item1) <= intervalloCol) trov0 = true;
                    else i++;
                }

                while (!trov1&&j<numeroRighe)
                {
                    if ((double)tmpv1.Item1 - rows.Keys.ElementAt(j).Item1 <= intervalloCol) trov1 = true;
                    else j++;
                }

                if(trov0 && trov1)outputMV[j, i] += 1;
               
                

            }
            for (i = 1; i <= numeroColonnne; i++)
                for (j = 1; j <= numeroRighe; j++) outputM[j, i] = outputMV[j - 1, i - 1].ToString();
            return outputM;

        }
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


        Dictionary<int, ElementoDisribuzione> csvContent = new Dictionary<int, ElementoDisribuzione>();
        Distribuzione distr = new Distribuzione();
        MediaCalOnline medie = new MediaCalOnline();
        List<String> attributename = new List<string>();
        List<String> bivariante = new List<string>();//per ora poi diventera n variante;
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
            richTextBox1.Text += "-------------------------------------------------------------" + Environment.NewLine;
            richTextBox1.Text += e.ClickedItem.Text + Environment.NewLine;

            double media = 0;
            double stdVariation;
            List<Double> values=new List<double>(0);
            SortedDictionary<Tuple<double, double>, int> firstdistr;
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
                foreach (var el in firstdistr)
                {
                    richTextBox1.Text += el.Key.ToString() + " : " + el.Value + Environment.NewLine;
                }
            }
            else stdVariation = 0;


            richTextBox1.Text += e.ClickedItem + " with average: " + media + " and standard variation: " + stdVariation+ Environment.NewLine;
            bivariante.Add(e.ClickedItem.Text);
          
            button2.Visible = false;
            foreach (var elem in attributename)
                contextMenuStrip2.Items.Add(elem);
            contextMenuStrip2.Visible = true;
        }

        private void contextMenuStrip2_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {
            richTextBox1.Text += "-------------------------------------------------------------" + Environment.NewLine;
            richTextBox1.Text += e.ClickedItem.Text + Environment.NewLine;
            double media2 = 0;
            double stdVariation;
            List<Double> values = new List<double>(0);
            SortedDictionary<Tuple<double,double>,int> seconddistr;
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
                foreach (var el in seconddistr)
                {
                    richTextBox1.Text += el.Key.ToString() +" : " + el.Value +Environment.NewLine;
                }
            }
            else stdVariation = 0;
            richTextBox1.Text += e.ClickedItem + " with average: " + media2 + " and standard variation: " + stdVariation +  Environment.NewLine;
            bivariante.Add(e.ClickedItem.Text);
           
            richTextBox1.Text += Environment.NewLine;
            int nr, nc;
            String[,] bivariantMatrix = distr.getbivariantmatrix(bivariante, csvContent.Values, out nr, out nc);

            for (int i = 0; i <= nr; i++)
            {
                richTextBox1.Text += Environment.NewLine;
                for (int j = 0; j <= nc; j++)
                {
                    richTextBox1.Text += bivariantMatrix[i, j].PadLeft(6);
                    
                }
            }

        }



    }
{{< /highlight >}}