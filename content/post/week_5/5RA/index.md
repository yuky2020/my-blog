+++
title = "5_RA"
date = 2021-10-23T20:03:36+02:00
description = "The various methods to generate, from a Uniform([0,1)), all the most important random variables (discrete and continuous)."

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

## 5_RA assignament

### Request

Do a web research about the various methods to generate, from a Uniform([0,1)), all the most important random variables (discrete and continuous). Collect all source code you think might be useful code of such algorithms (keep credits and attributions wherever applicable), as they will be useful for our next simulations.  

### Generate a bernulli distribution
Various freamework include this distribution (for example Accord), and also some standard  libraries like MathNet:
```csharp
 public void GenerateChange(Point reference)
 {
     Bernoulli rBernoulli = new Bernoulli(0.5);
     double percentage = (rBernoulli.Sample() > 0.5 ? -1 : 1) * Simulation.Default.Data_Change_Maximum_Percentage * random.NextDouble();
     GenerateChange(reference, percentage);
 }

```

Or in pure c:

```c
#include <iostream>
   2:  #include <iomanip>
   3:  #include <chrono>
   4:  #include "ZZ.h"
   5:  using namespace std;
   6:   
   7:  typedef std::pair<ZZ_t*, ZZ_t*> QQ_t;
   8:   
   9:  // Computes the first n even absolute Bernoulli numbers
  10:  // B[0], B[2], B[4], ..., B[2*n - 2] for n >= 1.
  11:  QQ_t bernoulliT(int n)
  12:  {
  13:      /* assert(n > 0); */
  14:   
  15:      ZZ_t g, num, den = ZZ_t(1), p = ZZ_t(1);
  16:      long k, j;
  17:   
  18:      ZZ_t* T = new ZZ_t[n];
  19:      ZZ_t* N = new ZZ_t[n];
  20:      ZZ_t* D = new ZZ_t[n];
  21:   
  22:      N[0] = ZZ_t(1);
  23:      D[0] = ZZ_t(1);
  24:   
  25:      if (n == 1) return QQ_t(N, D);
  26:   
  27:      T[1] = ZZ_t(1);
  28:   
  29:      for (k = 2; k < n; k++)
  30:      {
  31:          T[k] = T[k - 1] * (k - 1);
  32:      }
  33:   
  34:      for (k = 2; k < n; k++)
  35:      {
  36:          for (j = k; j < n; j++)
  37:          {
  38:              T[j] = T[j - 1] * (j - k) + T[j] * (j - k + 2);
  39:          }
  40:      }
  41:   
  42:      for (k = 1; k < n; k++)
  43:      {
  44:          p *= 4;
  45:          den = p * (p - 1);
  46:          num = T[k] * (k + k);
  47:          g = gcd(num, den);
  48:          N[k] = num / g;
  49:          D[k] = den / g;
  50:      }
  51:   
  52:      delete[] T;
  53:      return QQ_t(N, D);
  54:  }
  55:   
  56:  // Computes the first n even absolute Bernoulli numbers
  57:  // B[0], B[2], B[4], ..., B[2*n - 2] for n >= 1.
  58:  QQ_t bernoulliS(int n)
  59:  {
  60:      /* assert(n > 0); */
  61:   
  62:      ZZ_t g, den = ZZ_t(1), p = ZZ_t(1);
  63:      long h = 0, k, i, j = 1, tog = 1;
  64:   
  65:      ZZ_t* T = new ZZ_t[n];
  66:      ZZ_t* N = new ZZ_t[n];
  67:      ZZ_t* D = new ZZ_t[n];
  68:   
  69:      N[0] = ZZ_t(1);
  70:      D[0] = ZZ_t(1);
  71:   
  72:      if (n == 1) return QQ_t(N, D);
  73:   
  74:      T[1] = ZZ_t(1);
  75:   
  76:      for (i = 3; i <= 2 * n; i++)
  77:      {
  78:          if (tog)
  79:          {
  80:              p *= 4;
  81:              den = (p - 1) * 2;
  82:   
  83:              for (k = h++; k > 0; k--)
  84:                  T[k] += T[k + 1];
  85:          }
  86:          else
  87:          {
  88:              for (k = 1; k <= h; k++)
  89:                  T[k] += T[k - 1];
  90:   
  91:              g = gcd(T[h], den);
  92:              N[j] = T[h] / g;
  93:              D[j++] = den / g;
  94:          }
  95:          tog = 1 - tog;
  96:      }
  97:   
  98:      delete [] T;
  99:      return QQ_t(N, D);
 100:  }
 101:   
 102:  int main()
 103:  {
 104:      int n = 500, i, rep;
 105:      pair<ZZ_t*, ZZ_t*> B;
 106:   
 107:      chrono::time_point<chrono::system_clock> start, end;
 108:      start = chrono::system_clock::now();
 109:   
 110:      for (rep = 0; rep < 10; rep++)
 111:      {
 112:           B = bernoulliT(n);
 113:      }
 114:   
 115:      end = chrono::system_clock::now();
 116:      chrono::duration<double> elapsed_seconds = end - start;
 117:   
 118:      cout << "elapsed time: " << elapsed_seconds.count() / rep
 119:           << " seconds." << endl;
 120:   
 121:      ZZ_t* numer = B.first;
 122:      ZZ_t* denom = B.second;
 123:   
 124:      if (n < 100)
 125:      {
 126:          for (i = 0; i < n; i++)
 127:          {
 128:              cout << "B[" << i << "] = "
 129:                   << numer[i]  << "/"
 130:                   << denom[i]  << endl;
 131:          }
 132:      }
 133:   
 134:      delete [] numer;
 135:      delete [] denom;
 136:   
 137:      cout << endl << "Done!" << endl;
 138:      cin.get();
 139:   
 140:      return 0;
 141:  }
C#

   1:  using ZZ_t = System.Numerics.BigInteger;
   2:  using QQ_t = System.Tuple<System.Numerics.BigInteger, System.Numerics.BigInteger>;
   3:   
   4:  namespace WilliamHartChallenge
   5:  {
   6:      class Bernoulli
   7:      {
   8:          // Computes the first n even _absolute_ Bernoulli numbers.
   9:          // B[0], B[2], B[4], ..., B[2*n - 2] for n >= 1.
  10:          static QQ_t[] bernoulliT(int n)
  11:          {
  12:              // System.Diagnostics.Debug.Assert(n > 0); 
  13:   
  14:              ZZ_t p = 1, g, den, num;
  15:              int k, j;
  16:   
  17:              var B = new QQ_t[n];
  18:              var T = new ZZ_t[n];
  19:   
  20:              B[0] = new QQ_t(1, 1);
  21:              if (n == 1) return B;
  22:   
  23:              T[1] = 1;
  24:   
  25:              for (k = 2; k < n; k++)
  26:              {
  27:                  T[k] = (k - 1) * T[k - 1];
  28:              }
  29:   
  30:              for (k = 2; k < n; k++)
  31:              {
  32:                  for (j = k; j < n; j++)
  33:                  {
  34:                      T[j] = (j - k) * T[j - 1] + (j - k + 2) * T[j];
  35:                  }
  36:              }
  37:   
  38:              for (k = 1; k < n; k++)
  39:              {
  40:                  p *= 4;
  41:                  den = p * (p - 1);
  42:                  num = (k + k) * T[k];
  43:                  g = gcd(num, den);
  44:                  B[k] = new QQ_t(num / g, den / g);
  45:              }
  46:   
  47:              return B;
  48:          }
  49:   
  50:          // Computes the first n even _absolute_ Bernoulli numbers.
  51:          // B[0], B[2], B[4], ..., B[2*n - 2] for n >= 1.
  52:          static QQ_t[] bernoulliS(int n)
  53:          {
  54:              // System.Diagnostics.Debug.Assert(n > 0); 
  55:   
  56:              ZZ_t p = 1, den = 0, g;
  57:              int h = 0, j = 1, k, i;
  58:              bool tog = true;
  59:   
  60:              var B = new QQ_t[n];
  61:              var T = new ZZ_t[n];
  62:   
  63:              B[0] = new QQ_t(1, 1);
  64:              if (n == 1) return B;
  65:   
  66:              T[1] = 1;
  67:   
  68:              for (i = 3; i <= 2 * n; i++)
  69:              {
  70:                  if (tog)
  71:                  {
  72:                      p <<= 2;
  73:                      den = (p - 1) << 1;
  74:   
  75:                      for (k = h++; k > 0; k--) 
  76:                          T[k] += T[k + 1];
  77:                  }
  78:                  else
  79:                  {
  80:                      for (k = 1; k <= h; k++) 
  81:                          T[k] += T[k - 1];
  82:   
  83:                      g = gcd(T[h], den);
  84:                      B[j++] = new QQ_t(T[h] / g, den / g);
  85:                  }
  86:                  tog = !tog;
  87:              }
  88:   
  89:              return B;
  90:          }
  91:   
  92:          static ZZ_t gcd(ZZ_t a, ZZ_t b)
  93:          {
  94:              ZZ_t x, y;
  95:   
  96:              if (a >= b) { x = a; y = b; }
  97:              else { x = b; y = a; }
  98:   
  99:              while (y != 0)
 100:              {
 101:                  ZZ_t t = x % y; x = y; y = t;
 102:              }
 103:   
 104:              return x;
 105:          }
 106:   
 107:          static void Main()
 108:          {
 109:              int n = 100;
 110:              var B = bernoulliS(n);
 111:   
 112:              for (int i = 0; i < n; i++)
 113:              {
 114:                  System.Console.WriteLine(i + " : " + B[i]);
 115:              }
 116:   
 117:              System.Console.WriteLine("Done");
 118:              System.Console.ReadLine();
 119:          }
 120:      }
 121:  }

```


### Generate a binomial ditribution[7]
```c++
#include "nmath.h"
#include "dpq.h"
#include <stdlib.h>
#include <limits.h>

#define repeat for(;;)

double rbinom(double nin, double pp)
{
    /* FIXME: These should become THREAD_specific globals : */

    static double c, fm, npq, p1, p2, p3, p4, qn;
    static double xl, xll, xlr, xm, xr;

    static double psave = -1.0;
    static int nsave = -1;
    static int m;

    double f, f1, f2, u, v, w, w2, x, x1, x2, z, z2;
    double p, q, np, g, r, al, alv, amaxp, ffm, ynorm;
    int i, ix, k, n;

    if (!R_FINITE(nin)) ML_WARN_return_NAN;
    r = R_forceint(nin);
    if (r != nin) ML_WARN_return_NAN;
    if (!R_FINITE(pp) ||
	/* n=0, p=0, p=1 are not errors <TSL>*/
	r < 0 || pp < 0. || pp > 1.)	ML_WARN_return_NAN;

    if (r == 0 || pp == 0.) return 0;
    if (pp == 1.) return r;

    if (r >= INT_MAX)/* evade integer overflow,
			and r == INT_MAX gave only even values */
	return qbinom(unif_rand(), r, pp, /*lower_tail*/ 0, /*log_p*/ 0);
    /* else */
    n = (int) r;

    p = fmin2(pp, 1. - pp);
    q = 1. - p;
    np = n * p;
    r = p / q;
    g = r * (n + 1);

    /* Setup, perform only when parameters change [using static (globals): */

    /* FIXING: Want this thread safe
       -- use as little (thread globals) as possible
    */
    if (pp != psave || n != nsave) {
	psave = pp;
	nsave = n;
	if (np < 30.0) {
	    /* inverse cdf logic for mean less than 30 */
	    qn = R_pow_di(q, n);
	    goto L_np_small;
	} else {
	    ffm = np + p;
	    m = (int) ffm;
	    fm = m;
	    npq = np * q;
	    p1 = (int)(2.195 * sqrt(npq) - 4.6 * q) + 0.5;
	    xm = fm + 0.5;
	    xl = xm - p1;
	    xr = xm + p1;
	    c = 0.134 + 20.5 / (15.3 + fm);
	    al = (ffm - xl) / (ffm - xl * p);
	    xll = al * (1.0 + 0.5 * al);
	    al = (xr - ffm) / (xr * q);
	    xlr = al * (1.0 + 0.5 * al);
	    p2 = p1 * (1.0 + c + c);
	    p3 = p2 + c / xll;
	    p4 = p3 + c / xlr;
	}
    } else if (n == nsave) {
	if (np < 30.0)
	    goto L_np_small;
    }

    /*-------------------------- np = n*p >= 30 : ------------------- */
    repeat {
      u = unif_rand() * p4;
      v = unif_rand();
      /* triangular region */
      if (u <= p1) {
	  ix = (int)(xm - p1 * v + u);
	  goto finis;
      }
      /* parallelogram region */
      if (u <= p2) {
	  x = xl + (u - p1) / c;
	  v = v * c + 1.0 - fabs(xm - x) / p1;
	  if (v > 1.0 || v <= 0.)
	      continue;
	  ix = (int) x;
      } else {
	  if (u > p3) {	/* right tail */
	      ix = (int)(xr - log(v) / xlr);
	      if (ix > n)
		  continue;
	      v = v * (u - p3) * xlr;
	  } else {/* left tail */
	      ix = (int)(xl + log(v) / xll);
	      if (ix < 0)
		  continue;
	      v = v * (u - p2) * xll;
	  }
      }
      /* determine appropriate way to perform accept/reject test */
      k = abs(ix - m);
      if (k <= 20 || k >= npq / 2 - 1) {
	  /* explicit evaluation */
	  f = 1.0;
	  if (m < ix) {
	      for (i = m + 1; i <= ix; i++)
		  f *= (g / i - r);
	  } else if (m != ix) {
	      for (i = ix + 1; i <= m; i++)
		  f /= (g / i - r);
	  }
	  if (v <= f)
	      goto finis;
      } else {
	  /* squeezing using upper and lower bounds on log(f(x)) */
	  amaxp = (k / npq) * ((k * (k / 3. + 0.625) + 0.1666666666666) / npq + 0.5);
	  ynorm = -k * k / (2.0 * npq);
	  alv = log(v);
	  if (alv < ynorm - amaxp)
	      goto finis;
	  if (alv <= ynorm + amaxp) {
	      /* stirling's formula to machine accuracy */
	      /* for the final acceptance/rejection test */
	      x1 = ix + 1;
	      f1 = fm + 1.0;
	      z = n + 1 - fm;
	      w = n - ix + 1.0;
	      z2 = z * z;
	      x2 = x1 * x1;
	      f2 = f1 * f1;
	      w2 = w * w;
	      if (alv <= xm * log(f1 / x1) + (n - m + 0.5) * log(z / w) + (ix - m) * log(w * p / (x1 * q)) + (13860.0 - (462.0 - (132.0 - (99.0 - 140.0 / f2) / f2) / f2) / f2) / f1 / 166320.0 + (13860.0 - (462.0 - (132.0 - (99.0 - 140.0 / z2) / z2) / z2) / z2) / z / 166320.0 + (13860.0 - (462.0 - (132.0 - (99.0 - 140.0 / x2) / x2) / x2) / x2) / x1 / 166320.0 + (13860.0 - (462.0 - (132.0 - (99.0 - 140.0 / w2) / w2) / w2) / w2) / w / 166320.)
		  goto finis;
	  }
      }
  }

 L_np_small:
    /*---------------------- np = n*p < 30 : ------------------------- */

  repeat {
     ix = 0;
     f = qn;
     u = unif_rand();
     repeat {
	 if (u < f)
	     goto finis;
	 if (ix > 110)
	     break;
	 u -= f;
	 ix++;
	 f *= (g / ix - r);
     }
  }
 finis:
    if (psave > 0.5)
	 ix = n - ix;
  return (double)ix;
}
```
### Poisson Ditribution

more easy to compute than other:
```c++

# Include <stdio. h>
# Include <math. h>
# Include <time. h>
 
Double U_Random ();
Int possion ();
 
 
Void main ()
{
Double u = U_Random ();
Int p = possion ();
Printf ("% fn", u );
Printf ("% dn", p );
 
}
 
Int possion ()/* generates a random number with a Poisson distribution. Lamda is the average number */
{
Int Lambda = 20, k = 0;
Long double p = 1.0;
Long double l = exp (-Lambda);/* it is defined as long double for precision, and exp (-Lambda) is a decimal near 0 */
Printf ("%. 15Lfn", l );
While (p> = l)
        {
Double u = U_Random ();
P * = u;
K ++;
        }
Return K-1;
}
 
Double U_Random ()/* generates a 0 ~ Random number between 1 */
{
Double f;
Srand (unsigned) time (NULL ));
F = (float) (rand () % 100 );
/* Printf ("% fn", f );*/
Return f/100;
}

```


[1]"url","https://en.wikipedia.org/wiki/List_of_probability_distributions"
[2]"url","https://www.cs.wm.edu/~va/software/park/park.html"
[3]https://www.johndcook.com/blog/2010/05/03/c-random-number-generation-code/
[4]https://homeweb.csulb.edu/~tebert/teaching/lectures/552/variate/variate.pdf
[5]https://www.jstor.org/stable/1402590
[6]https://www.icosaedro.it/phplint/generating-statistical-distributions/index.html  
[7]"url","https://svn.r-project.org/R/trunk/src/nmath/rbinom.c"

