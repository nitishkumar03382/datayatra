# Sales City

Table: `sales`

Column Name  | DataType
-------------|---------
orderid|int
customerid|int
city|varchar
zipcode|varchar


Write sql query to find all the city, city names should not repeat in the output result.

The result fromat is in the following example.

**Example 1:**

**Input**
```Sales Table:```

orderid | customerid |zipcode | city
--------|------------|--------|------
1000|12|804453|Patna
1000|12|804453|Patna
1001|15|123242|Dehradun

**Output:** 

| city      |
|-----------|
| Patna     |
| Dehradun  |


**Note:** Order doesn`t matter






