# CMSC-23
Programming Paradigms

## `Lab_2.hs`
Easy functions
```
cube :: Int -> Int - Consumes an integer and produces the cube of that integer
double :: Int -> Int - Consumes an integer and produces the 2 times that integer
```
Recursive Functions
```
modulus :: Int -> Int -> Int - Consumes two integers x and m and produces xmodm
factorial :: Int -> Int - Consumes an integer and produces the factorial of the integer
summation :: Int -> Int - Consumes a natural number and produces the summation of numbers from 1 to n.
```
Higher order function
```
compose :: (Int -> Int) -> (Int -> Int) -> (Int -> Int) - Consumes two functions f:Z→Z, and g:Z→Z and produces the function f∘g.
subtractMaker :: Int -> (Int -> Int) - Consumes an integer x and produces a function that consumes an integer y and produces x−y
applyNTimes :: (Int -> Int) -> Int -> Int -> Int - Consumes a function f:Z→Z and and two integers n and x. applyNTimes produces an integer which is the result of the function applied to x, n-times. If n is less than or equal to 0 it must produce zero applications of f therefore it produces x.
```
-------------------
