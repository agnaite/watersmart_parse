# Solutions

## Problem 2

Rewriting the function so that we sum up all the distances between each data
point and the mean first, and then divide by the number of data points and
take the square root, fixes the problem. In other words, we do not want to
divide and take the square root of the sum in each iteration.

```py
import math

def standard_deviation(number_list):
    average = sum(number_list) / float(len(number_list))

    stdev = 0

    for value in number_list:
        stdev += (average - value)**2

    return math.sqrt(stdev/float(len(number_list)))
```
