+++
title = "7_R"
date = 2021-10-23T20:03:36+02:00
description = "Explain the Bayes Theorem and its key role in statistical induction"


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

## 7_R assignament

### Request

Explain the Bayes Theorem and its key role in statistical induction. Describe the different paradigs that can be found within statistical inference (such as"bayesian", "frequentist" [Fisher, Neyman]).


### The Bayes Theorem 
Bayes' theorem is used to calculate the probability of a cause that triggered the occurred event, and the importance of this theorem for statistics is such that different interpretation and usage divided  the statisticians into  two schools  Bayesian  and Frequentist

P(A|B)=(P(B|A)P(A))/P(B)


### Frequentist and Bayesian statistics

we called this therm prior probability.

#### Frequentist
According to the frequentist definition of probability, only repeatable random events (like a dice rool) have probabilities. These probabilities are equal to the long-term frequency of occurrence of the events in question. Frequentists don’t attach probabilities to hypotheses or to any fixed but unknown values in general. [1]
Basically, a frequentist method makes predictions on the underlying truths of the experiment using only data from the current experiment.

#### Bayesian
Bayesians view probabilities as a more general concept a Bayesian can use probabilities to represent the uncertainty in any event or hypothesis. [1]

### Statistical infernce paradigm

So, the biggest distinction is that Bayesian probability specifies that there is some prior probability.
The division between the two schools of thought occurs because of the term P(B) (P(θ) in the classroom)
| The Frequentist                                                 | The Bayesian                                                                     |
|:----------------------------------------------------------------|:---------------------------------------------------------------------------------|
| chose to ignore the term and assign it a uniform distribution | choose to use a certain already calculated shape distribution(like bernulli etc..) |





[1]"url","https://en.wikipedia.org/wiki/Bayes%27_theor"
