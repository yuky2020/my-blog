+++
title = "1_RA"
date = 2021-10-05T20:03:36+02:00
description = "Floating point problems"

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

## 1_RA assignament

### Request
Understand how the floating point representation works and describe systematically (possibly using categories) all the possible problems that can happen. Try to classify the various issues and limitations (representation, comparison, rounding, propagation, approximation, loss of significance, cancellation, etc.) and provide simple examples for each of the categories you have identified

### Floating point notation
It's a fantastic thing, we could express a vast range of value in a very efficent way: 32 bit  notation:
The frist bit is for sign, then 8 bit of exponent (frist bit is sign of the exponent ) so  from 2^-127 to 2^127 and then 23 bit of mantissa.

#### Limitation
A floating-point format has limited range and precision. These limitations can be understood by considering using scientific notation with a limited range of exponents and a limited number of digits in the mantissa.

   1. Range limitation: A fixed number of "Exp" bits is comparable to limiting the size of the exponent in scientific notation.

   2. Precision limitation: A fixed number of "Fraction" bits is comparable to limiting the number of digits in the mantissa in scientific notation. [1]


## Errors: Approximation

this notation anyway present some problem,for example on how to rappreset 0.1, 0.2 ,0.3 without getting an error on the 17th decimal place that even if low is an approximation,and even if solution such as use decimal notation exist we should know this behaveiour.[2]

## Errors: Rounding 

Because floating-point numbers have a limited number of digits, they cannot represent all real numbers accurately: when there are more digits than the format allows, the leftover ones are omitted - the number is rounded. There are three reasons why this can be necessary: [2]

1. Too many significant digits
   - The great advantage of   floating point is that leading and trailing zeroes (within the range provided by the exponent) don’t need to be stored. But if, without those, there are still more digits than the significand can store, rounding becomes necessary. In other words, if your number simply requires more precision than the format can provide, you’ll have to sacrifice some of it, which is no big surprise. For example, with a floating point format that has 3 digits in the significand, 1000 does not require rounding, and neither does 10000 or 1110 - but 1001 will have to be rounded. With the large number of significand digits available in typical floating-point formats, this may seem to be a rarely encountered problem, but if you perform a sequence of calculations, especially multiplication and division, you can very quickly reach this point.
2. Periodical digits
   - Any (irreducible) fraction where the denominator has a prime factor that does not occur in the base requires an infinite number of digits that repeat periodically after a certain point, and this can already happen for very simple fractions. For example, in decimal 1/4, 3/5 and 8/20 are finite, because 2 and 5 are the prime factors of 10. But 1/3 is not finite, nor is 2/3 or 1/7 or 5/6, because 3 and 7 are not factors of 10. Fractions with a prime factor of 5 in the denominator can be finite in base 10, but not in base 2 - the biggest source of confusion for most novice users of floating-point numbers.


 3. Non-rational numbers 
     - Non-rational numbers cannot be represented as a regular fraction at all, and in positional notation (no matter what base) they require an infinite number of non-recurring digits.


## Comparison

Due to rounding errors, most floating-point numbers end up being slightly imprecise. As long as this imprecision stays small, it can usually be ignored. However, it also means that numbers expected to be equal (e.g. when calculating the same result through different correct methods) often differ slightly, and a simple equality test fails. For example:[2]

	float a = 0.15 + 0.15
	float b = 0.1 + 0.2
	if(a == b) // can be false!
	if(a >= b) // can also be false!

## Propagation

While the errors in single floating-point numbers are usualy very small, even simple calculations on them can contain pitfalls that increase the error in the result way beyond just having the individual errors “add up”.[2]
this usualy come-up  with addition or subtraction

- of number of differet magnitude es: 
  if you add 1 to 100000000000 the value will not change even if you do this 10000000000000 times
- When numbers are very close to each other and are subtracted:
 the result’s less significant digits consist mostly of rounding errors 

the more calculatuion are done the more the error propagate




# BONUS: THE GENIUS MOVE IN QUAKE III  
{{< youtube p8u_k2LIZyo >}}



[1]Title:"Floating-Point-Limtation" url:"https://www.d.umn.edu/~gshute/asm/floating-point.xhtml"

[2]Title:"0.00112" url:"https://floating-point-gui.de/basic/"

