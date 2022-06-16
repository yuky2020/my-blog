+++
title = "6_R"
date = 2021-10-23T20:03:36+02:00
description = "Think and explain in your own words what is the role that probability plays in Statistics and the relation between the observed distribution and frequencies their theoretical counterparts."


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

## 6_R assignament

### Request

Think and explain in your own words what is the role that probability plays in Statistics and the relation between the observed distribution and frequencies their "theoretical" counterparts. Do some practical examples where you explain how the concepts of an abstract probability space relate to more "concrete" and "real-world" objects when doing statistics.


### The role of probability in statistic 
In statistcs when we  talk about inference we move the  contest from frequencies  to a more interesting probability area, in this area we say for example that
if a dice hit six with a frequencies of 1/6 (concrete) in the real world , we would have a probability of 1/6, note that probability is not about what happened, for if so then we do not need probability theory. Probability is about what may happen. [1]



### Relation between empircal case (distribution and frequencies) and theoretical
starting from  the same distribution let'try to analyze the two view:

 | Theoretical | distribution |   | Empirical | distribution |
 |-------------|--------------|---|-----------|--------------|
 | Units       | Frequencies  |   | Units     | Probability  |
 | X1          | f1           |   | X1        | P1           |
 | Xn          | fn           |   | Xn        | Pm           |

We could say so that frequency is an incarnation of probability, a realization in the real world of the abstract concept of probability and in this sense it's easy to assume that the two fenomenus are goverend by the same law and that frequencies are just the actualization of the probability.
 
 In inference statistics the objective is to determine which theta (we call it also states of nature) is the most probable so the one  that can generate  sample of empirical distribution (evidence) equivalent to the real one.
 
#### The methods of Bayesian inference 
You can never be certain about a hypothesis, but as the availability and dimension of  data increases, the quality of the inference becomes better and better; with sufficient empirical evidence, it will become very high (for example, tending to 1) or very low (tending to 0). this represent a sort of implementation of the scientific method  which normally involves the collection of data (empirical evidence), and hypothesis, here the hypothesis are the probability distributions that more rappresent the real fact.  
In practice we have:


- P(θ|E)
 
Where θ is the state of nature that can could be an array of values or a single value and E the evidence.
So, referring to the frequencies, we have that for frequencies in an empirical contest we have that:
 - Freq(X|Y)=Freq(X∧Y)/Freq(Y)
 
Where X and Y are just labels and this is an identity. With
 - P(X|Y)=P(X∧Y)/P(Y)
 
we are in the realm of probability, so a branch of mathematics, and this is the definition for conditional probability.



















[1]"url","https://math.stackexchange.com/questions/1443015/why-do-we-say-almost-surely-in-probability-theory"
[2]"url""https://en.wikipedia.org/wiki/Probability_axioms"
