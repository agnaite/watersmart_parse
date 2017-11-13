# Solutions

## Problem 1

See `parse_data.py`.

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

## Problem 3

From the report, I can interpret that for March, April, and May the number of accounts reported were about the same, that each account was reporting for the same number of days, and that the gallons of water used per day was drastically higher in May of 2017, but similar to April and March in May of last year.

I would improve this chart by not using negative percentages to make it easier to read. The color coding for the previous period/year is also confusing, as the color green implies the increase in water used is positive, and the decrease in red is bad. 

## Problem 4

Selects all customers that have ordered pepperoni pizza in the past 30 days:

```sql
SELECT *
FROM customer INNER JOIN customer_order
ON customer.customer_id = order.customer_id
WHERE order.pizza_id = (SELECT pizza_id FROM pizza WHERE name = 'pepperoni')
AND order.order_date >= current_date - interval '30' day;
```

Selects customer that has spent the most on pizza in the past 30 days.

```sql
SELECT customer.customer_id, customer.customer_name,
customer_order.quantity * pizza.price AS total
FROM customer_order
JOIN pizza
ON customer_order.pizza_id = pizza.pizza_id
JOIN customer
ON customer_order.customer_id = customer.customer_id
WHERE customer_order.order_date >= current_date - interval '30' day
ORDER BY total DESC
LIMIT 1;
```

## Problem 5

- What format do the postal code and date parameters need to be passed in?
  (datetime, string?)
- Need unit tests to make sure the function is returning data as expected
- If data is returned as expected, need to check if results are accurate