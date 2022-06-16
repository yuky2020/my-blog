+++
title = "9_RA"
date = 2021-11-05T20:03:36+02:00
description = "Try to find on the web what are the names of the random variables that you just simulated in the applications"

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

## 9_RA assignament

### Request
Try to find on the web what are the names of the random variables that you just simulated in the applications, and see if the means and variances that you obtain in the simulation are compatible with the "theory". If not fix the possible bugs.

### Brawnian motion 
In our application we can observe the behavior of the brownian motion properties.
1. Is verified observing from the image that the starting point is x=0 y=0 
2. Is verified by observing that the graphic is continuous in every path.
3. Is verified by the fact that  increments are independent and random, in fact all the values generated have the the same probability of being chosen. No increment will therefore influence the next one.

4. The histograms represent the distribution of the brownian motion which is a realization of a normal distribution, we found infact  that  more sample we take the more the histograms take the beel form(the form of a normal distribution). 

### Normal distributions realization
In the last homework  we take an important  distributions the Normal(0,1) and make some trasformation:

- Exp(N(0,1)) this is very intresting in fact we found it when we talk about Log-normal distribution[1].
- Squared N(0,1) this is called chi-squared distribution with one degree of freedom  {A chi-squared distribution constructed by squaring a single standard normal distribution is said to have 1 degree of freedom.Just as extreme values of the normal distribution have low probability (and give small p-values), extreme values of the chi-squared distribution have low probability.[2]}

The generalazied sum of different(k) squared normal distribution make the grade of freedoom higher(k degree of freedoom);
an important result  is that since this distribution is the sum of k independent random variables with finite mean and variance, it converges to a normal distribution for large k.This is for sure insured by The CTL.
For many practical purposes, for k>50 the distribution is sufficiently close to a normal distribution for the difference to be ignored.






[1]"url":"https://en.wikipedia.org/wiki/Log-normal_distribution"
[2]"url":"https://en.wikipedia.org/wiki/Chi-squared_distribution#:~:text=A%20chi%2Dsquared%20distribution%20constructed,have%201%20degree%20of%20freedom.&text=Just%20as%20extreme%20values%20of,squared%20distribution%20have%20low%20probability."

