+++
title = "11_R"
date = 2021-11-05T20:03:36+02:00
description = "Do a research about the general correlation coefficient for ranks and the most common indices that can be derived by it"
katex=true
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

## 11_R assignament

### Request
Do a research about the general correlation coefficient for ranks and the most common indices that can be derived by it. Do one example of computation of these correlation coefficients for ranks.
 
### General correlation coefficient for ranks

In statistics, a rank correlation is any of several statistics that measure an ordinal association—the relationship between rankings of different ordinal variables or different rankings of the same variable, where a “ranking” is the assignment of the ordering labels “first”, “second”, “third”, etc. to different observations of a particular variable.

A rank correlation coefficient measures the degree of similarity between two rankings, and can be used to assess the significance of the relation between them.

Some of the more popular rank correlation statistics include

- Spearman’s ρ
- Kendall’s τ
- Goodman and Kruskal’s γ
- Somers’ D

An increasing rank correlation coefficient implies increasing agreement between rankings. The coefficient is inside the interval [−1, 1] and assumes the value:

- 1 if the agreement between the two rankings is perfect; the two rankings are the same.
- 0 if the rankings are completely independent.
- −1 if the disagreement between the two rankings is perfect; one   ranking is the reverse of the other.

Following Diaconis (1988), a ranking can be seen as a permutation of a set of objects. Thus we can look at observed rankings as data obtained when the sample space is (identified with) a symmetric group. We can then introduce a metric, making the symmetric group into a metric space. Different metrics will correspond to different rank correlations.

To illustrate the computation, suppose a coach trains long-distance runners for one month using two methods. Group A has 5 runners, and Group B has 4 runners. The stated hypothesis is that method A produces faster runners. The race to assess the results finds that the runners from Group A do indeed run faster, with the following ranks: 1, 2, 3, 4, and 6. The slower runners from Group B thus have ranks of 5, 7, 8, and 9.

The analysis is conducted on pairs, defined as a member of one group compared to a member of the other group. For example, the fastest runner in the study is a member of four pairs: (1,5), (1,7), (1,8), and (1,9). All four of these pairs support the hypothesis, because in each pair the runner from Group A is faster than the runner from Group B. There are a total of 20 pairs, and 19 pairs support the hypothesis. The only pair that does not support the hypothesis are the two runners with ranks 5 and 6, because in this pair, the runner from Group B had the faster time. By the Kerby simple difference formula, 95% of the data support the hypothesis (19 of 20 pairs), and 5% do not support (1 of 20 pairs), so the rank correlation is r = .95 – .05 = .90.


The maximum value for the correlation is r = 1, which means that 100% of the pairs favor the hypothesis. A correlation of r = 0 indicates that half the pairs favor the hypothesis and half do not; in other words, the sample groups do not differ in ranks, so there is no evidence that they come from two different populations. An effect size of r = 0 can be said to describe no relationship between group membership and the members’ ranks.



[1]"url","https://en.wikipedia.org/wiki/Rank_correlation"
