+++
title = "5_R"
date = 2021-10-18T20:03:36+02:00
description = "Explain a possibly unified conceptual framework to obtain all most common measures of central tendency and of dispersion using the concept of distance"


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

## 5_R assignament

### Request

Explain a possibly unified conceptual framework to obtain all most common measures of central tendency and of dispersion using the concept of distance (or "premetric", or similarity in general). Discuss why it is useful to discuss these concepts introducing the notion of distance. Finally, point out the difference between the mathematical definition of "distance" and the properties of the "premetrics" useful in statistics, pointing out trhe most important distances, indexes and similarity measures used in statistics, data analysis and machine learning (such as for instance; Mahalanobis distance, Euclidean distance, Minkowski distance, Manhattan distance, Hamming distance, Cosine distance, Chebishev distance, Jaccard index, Haversine distance, Sørensen-Dice index, etc.).



## Central tendency 
In statistics, a central tendency (or measure of central tendency) is a typical or central  value for a probability distribution [2] also  called a center or location of the distribution. nevertheless measures of central tendency are often called averages.

common measures of central tendency are the arithmetic mean, the median, and the mode. A middle tendency can be calculated for either a finite set of values or for a theoretical distribution, such as the normal distribution. Occasionally authors use central tendency to denote “the tendency of quantitative data to cluster around some central value.”
The central tendency of a distribution is typically contrasted with its dispersion or variability; dispersion and central tendency are the often characterized properties of distributions. Analysis may judge whether data has a strong or a weak central tendency based on its dispersion.
In statistics, probability theory, and information theory, a statistical distance quantifies the distance between two statistical objects, which can be two random variables, or two probability distributions or samples, or the distance can be between an individual sample point and a population or a wider sample of points.[3]

### Arithmetic Mean:

In mathematics and statistics, the arithmetic mean or simply the mean or the average (when the context is clear), is the sum of a collection of numbers divided by the count of numbers in the collection. For sure we can also use is online implementation fon fast computation but the meaning remain the same,[2]

### Median:

the median of a population is any value such that at most half of the population is less than the proposed median and at most half is greater than the proposed median.Medians may not be unique. If each set contains less than half the population, then some of the population is exactly equal to the unique median[4].

The median is well-defined for any ordered (one-dimensional) data, and is independent of any distance metric. The median can thus be applied to classes which are ranked but not numerical (e.g. working out a median grade when students are graded from A to F), although the result might be halfway between classes if there is an even number of cases.

### Mode:

The mode of a sample is the element that occurs most often in the collection. For example, the mode of the sample 
[1,3, 3, 3, 3, 5, 7, 7, 20, 30, 50 is 3.
 Given the list of data [1, 1, 2, 4, 4] the mode is not unique – the dataset may be said to be bimodal, while a set with more than two modes may be described as multimodal.Usualy in the bimodal case we take as the mode the avreage of the two mode if is possible, infact unlike mean and median, the concept of mode also makes sense for “nominal data” (i.e., not consisting of numerical values in the case of mean, or even of ordered values in the case of median).

### Dispersion: percentiles and standard deviations

Several measures of dispersion include range,standard deviations and  quantiles, in general we  can say that dispersion is the size of distribution of values in a data set. 


### Based on the mean, the standard deviation 
It’s a measure of how far each observed value is from the mean in a data set usualy deviation will be represented by the lower case Greek letter sigma (σ).
Can be used when the distribution of data is rappresentable as a normal distribution, and is used to determine whether a particular data point is in standard or unusual range. 
The more devieted a data point is from the mean, the more “unusual” that data point is.
A low value for the standard deviation  means that most of the  data are  around the mean,while 
a high value  means that the data are spread  over a wider range of values.[7]

### Quantiles

Quantiles can be applied to any continuous data set, a quantile divides a data set in continuos distribution made of  equal proportions and represents the proportion of data at any point; the most used  quantiles are:
- Quartiles: dataset diveded in 4 quarters.
- Quintiles: dataset is divided in 5
- Percentiles: dataset is divided into 100 
we can for sure also extract the median from the quantiles for ex: the 50th percentile and the 3 quintiles  is the median.

### Distance

Distance is a numerical measurement of how far apart objects or points are. In mathematics, a distance function or metric is a generalization of the concept of physical distance; it is a way of describing what it means for elements of some space to be “close to”, or “far away from” each other.[6]

In the Euclidean space Rn, the distance between two points is usually given by the Euclidean distance (2-norm distance); but Euclidean distance could be extended also to n-space, and become usefull also in other field as ML and biometrics(Algorithm like HOG: [my implementation](https://github.com/yuky2020/Face-recognition-with-NOIR-camera-on-RaspberryPi));
the infinity version is called  also Chebyshev distance. Other distances, based on other norms, are sometimes usefull like the  Minkowski distance(of various order p (p-norm distance))



[1] "https://en.wikipedia.org/wiki/Arithmetic_mean "
[2]"https://en.wikipedia.org/wiki/Statistical_distance "
[3]"https://en.wikipedia.org/wiki/Central_tendency "
[4]"https://en.wikipedia.org/wiki/Median "
[5]"https://en.wikipedia.org/wiki/Mode_(statistics) "
[6]"https://it.wikipedia.org/wiki/Distanza_(matematica) "
