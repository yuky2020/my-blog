+++
title = "13_A"
date = 2021-10-28T20:03:36+02:00
description = "Create a distribution representation( histogram or CDF) "
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

## 13_A assignament

### Request
Create  a distribution representation (histogram, or CDF ...) to represent the following:

- Realizations taken from a Normal(0,1)

- Realizations of the mean, obtained by averaging several times (say m times, m large) n of the above realizations
- Realizations of the variance, obtained by averaging several times (say m times, m large) n of the above realizations

- Realizations taken from exp(N(0,1)))

- Realizations taken from N(0,1) squared

- Realizations taken from a (squared N(0,1)) divided by another (squared N(0,1))


### My Solution

{{< youtube agkC-X-HTYY>}}


[Code in C#](https://github.com/yuky2020/Statistics-Pratical-LABS/tree/main/Assignment11/C%23/BernulliGraphics)


#### The part in disegna Grafici in witch i call the various usefull function

{{< highlight cs >}}
  disgnaIstogrammi(viewPort, valueToDictionarys(n, m, index13a));
   {{< /highlight >}}

### valueToDictionarys
disegnaIstogrami is the same method used before for graphicate 3 Dictionary.
 In valueToDictionry we use the before created Distribution (see 12A ) and  based also on the actual type of dstribution that we need  (1 normal N(0,1),exp(N(0,1),squared normal or 1 squared normal divided by another one ) to create the realization, the mean and variance distributions:
 
{{< highlight cs >}}
  disgnaIstogrammi(viewPort, valueToDictionarys(n, m, index13a)); public Tuple<Dictionary<double, int>, Dictionary<decimal, int>, Dictionary<decimal, int>> valueToDictionarys(int m, int n, int index13a)
        {
            Dictionary<double, List<double>> randomvalues = new Dictionary<double, List<double>>();
            int i = 0;
            int j = 0;


            //calcolation of the  random ditribution
            for (i = 0; i < n; i++)
            {
                List<Double> tmp = new List<double>();
                tmp = distrubution.values[i];
                randomvalues.Add(i, tmp);
            }
            //controllo se è da fare exp squred o squared/ squared 
            if (index13a != 0)
            {
                for (i = 0; i < n; i++)
                    for (j = 0; j < m; j++)

                    {
                        if (index13a == 1) randomvalues[i][j] = Math.Pow(Math.E, randomvalues[i][j]);
                        if (index13a == 2) randomvalues[i][j] = Math.Pow(randomvalues[i][j], 2);
                        if (index13a == 3) randomvalues[i][j] = Math.Pow(randomvalues[i][j], 2);

                    }
                if (index13a == 3)
                {
                    NormalPathfinder distribution2 = new NormalPathfinder(n, m);
                    Dictionary<double, List<double>> otherones = new Dictionary<double, List<double>>();
                    for (i = 0; i < n; i++)
                    {
                        List<Double> tmp = new List<double>();
                        tmp = distribution2.values[i];
                        otherones.Add(i, tmp);
                         for (j = 0; j < m; j++)
                        {
                            otherones[i][j]= Math.Pow(otherones[i][j], 2);
                            randomvalues[i][j] = randomvalues[i][j] / otherones[i][j]; 

                        }

                    }


                }
            }

            Dictionary<double, int> randomdistrib = new Dictionary<double, int>();
            Dictionary<decimal, int> meanValues = new Dictionary<decimal, int>();
            Dictionary<decimal, int> varValues = new Dictionary<decimal, int>();

            for (double k = -1.0; k <= 1.0000; k = k + 0.100)
            {
                foreach (var list in randomvalues)
                {
                    foreach (var elem in list.Value)
                    {
                        if (elem > k && elem <= (k + 0.1))
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
                double mean = 0;
                double variance = 0;
                foreach (var elem in list.Value)
                {
                    mean = mean + (elem - mean);

                }
                foreach (var elem in list.Value)
                {
                    variance = variance + ((elem - mean) * (elem - mean));
                }
                mean = mean - (mean % 0.1);
                variance = variance - (variance % 2);
                int tmp2 = 1;
                if (meanValues.TryGetValue((decimal)mean, out tmp2)) { meanValues.Remove((decimal)mean); tmp2++; }
                meanValues.Add((decimal)mean, tmp2);
                tmp2 = 1;
                if (varValues.TryGetValue((decimal)variance, out tmp2)) { varValues.Remove((decimal)variance); tmp2++; }
                varValues.Add((decimal)variance, tmp2);

            }

            return new Tuple<Dictionary<double, int>, Dictionary<decimal, int>, Dictionary<decimal, int>>(randomdistrib, meanValues, varValues);
        }
   {{< /highlight >}}
