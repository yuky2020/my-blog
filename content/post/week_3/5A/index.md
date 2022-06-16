+++
title = "5_A"
date = 2021-10-05T20:03:36+02:00
description = " Compute a frequency distribution of the meaningful words from any text file and create a personal graphical representation"

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

## 5_A assignament

### Request
Compute - in both languages C# and VB.NET (and optionally in js) - a frequency distribution of the meaningful words from any text file and create a personal graphical representation of the corresponding "word cloud" (in case, can use animation if you wish), keeping into account the frequencies of the words.




### My Solution
{{< youtube IzJsKn8E-Lo >}}


[Code in C  and VB.NET#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment5)


#### Main Form:

{{< highlight cs >}}
  public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

       SortedDictionary<String, int> wDstr = new SortedDictionary<string, int>();
      
        
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            var filePath = string.Empty;
            openFileDialog1.InitialDirectory = "c:\\";
            openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            openFileDialog1.FilterIndex = 2;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.Title = "Select Text File";

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //Get the path of specified file
                filePath = openFileDialog1.FileName;

                //Read the contents of the file into a stream
                using (StreamReader sr = new StreamReader(filePath))
                {
                    while (sr.Peek() >= 0)
                    {
                        string line = sr.ReadLine();
                        char[] delimiters = new char[] { ' ', '\r', '\n' };
                        string[] words = line.Split(delimiters, StringSplitOptions.RemoveEmptyEntries);
                        int i = 0;
                        foreach (string word in words)
                        {
                            if (!wDstr.TryGetValue(word, out i)) wDstr.Add(word, 1);
                            else { wDstr.Remove(word); i++; wDstr.Add(word, i); }
                            
                        }
                    }
                }
                int j = 0;
                foreach(var w in wDstr)
                {
                    chart1.Series["Words"].Points.AddXY(w.Key, w.Value);

                }


            }

        }
       

    }
  {{< /highlight >}}