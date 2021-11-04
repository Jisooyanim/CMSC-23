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
## `Lab_Ex5.py`
double
```
def doubledInt(x:int) -> int:
    #accepts an int and return the double of that int
```
largest
```
def largest(x:float,y:float) -> float:
    #accepts two floats and returns the larger value
```
vertical line
```
def isVertical(a:(float,float),b:(float,float)) -> bool:
    #accepts two (float,float) tuples which represent two points in a cartesian plane and returns true if the points describe a vertical line and false otherwise
```
primes
```
def primes(n:int) -> [int]:
    #accepts an integer n and returns the first n primes
```
fibonacci
```
def fibonacciSequence(n:int) -> [int]:
    #accepts an integer n and returns a list containing the first n elements of fibonacci sequence (starting with 0 and 1)
```
sorting
```
def sortedIntegers(l:[int]) -> [int]:
    #accepts a list of integers and returns a list with the same integers sorted from smallest to highest
```
sublists
```
def sublists(l:[int]) -> [[int]]:
    #accepts a list of integers and returns all the sublists of the list. Sublists are contiguous chunks of a list (including an empty list and the list itself). [1,2], [2], [], [2,3,4], and [1,2,3,4,5] are sublists of [1,2,3,4,5] but [3,5] and [1,2,3,4,6] are not.
```
------------------------------------
