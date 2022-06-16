+++
title = "8_R"
date = 2021-10-28T20:03:36+02:00
description = "Some statistical researches"


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

## 8_R assignament

### Request
Do a research about the following topics:

- The law of large numbers LLN, the various definitions of convergence

- The convergence of the Binomial to the normal and Poisson distributions

- The central limit theorem [in anticipation of a topic we will study later]





### The Low of large numbers
In probability theory, the law of large numbers (LLN) is a theorem that describes the result of performing the same experiment a large number of times. According to the law, the average of the results obtained from a large number of trials should be close to the expected value and will tend to become closer to the expected value as more trials are performed.
There is two main forms of this law a weak and a strong one:
#### Weak
The weak law of large numbers (also called Khinchin's law) states that the sample average converges in probability towards the expected value [1].

We have largly tested this with our work on the bernulli trials when we have see drowing the histograms 
that the frequencies tend to the probability the much more n is larger.
Interpreting this result, the weak law states that for any nonzero margin specified (ε), no matter how small, with a sufficiently large sample there will be a very high probability that the average of the observations will be close to the expected value; that is, within the margin.


#### Uniform law of large numbers
Suppose f(x,θ) is some function defined for θ ∈ Θ, and continuous in θ. Then for any fixed θ, the sequence {f(X1,θ), f(X2,θ), ...} will be a sequence of independent and identically distributed random variables, such that the sample mean of this sequence converges in probability to E[f(X,θ)]. This is the pointwise (in θ) convergence.[1]


#### Borel's low of large number
Named after Emile Borel states that if an experiment is repated a large number of times,independently under identical conditions, then the proportion of times that any specified event occurs approximately equals the probability of the event's occurrence on any particular trial; the larger the number of repetitions, the better the approximation tends to be. More precisely, if E denotes the event in question, p its probability of occurrence, and Nn(E) the number of times E occurs in the first n trials, then with probability one:

Nn(E)/N --> p as n→∞


#### Strong 
The strong law of large numbers (also called Kolmogorov's law) states that the sample average converges almost surely to the expected value,(with almost sureley we mean with probability 1)

### The convergence of the Binomial to the normal and Poisson dsistributions

If n→∞ and p→0 while np approaches some positive number λ, then the binomial distribution approaches a Poisson distribution with expected value λ.

If n→∞ as p stays fixed, and X∼Binomial(n,p) then the distribution of (X−np)/√np(1-p) approaches the standard normal distribution, i.e. the normal distribution with expected value 0 and standard deviation 1.





### The central limit theorem 
The central limit theorem state that when indipendent random variable are summed up their normalized sum tend to a normal distributions(beell curve) even when the original variable are not distribuited normaly(Lyapunov CLT[2]).

In other words we could say that given a poupulation and calculated the mean and the standard deviation,if we take a sufficiently large random samples from the population with replacement, then the distribution of the sample means will be approximately normally distributed and that this will hold  true regardless of whether the source population is normal or skewed, provided the sample size is sufficiently large. 
In this week app this is particularly spottable in the realtive case,in fact when n increases,the convergence become centralIn this weak app this is particularly spottable eein the realtive case,in fact when n increases,the convergence become central.



[1]"url","https://en.wikipedia.org/wiki/Law_of_large_numbers#Weak_law"
[2]"url","https://en.wikipedia.org/wiki/Central_limit_theorem#Lyapunov_CLT"
