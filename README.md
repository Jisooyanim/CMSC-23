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

## `LabExercise6-LibrarySystem.py`
```
from abc import ABC, abstractmethod

class Date:
    def __init__(self, month:int, day:int, year:int):
        self.__month = month
        self.__day = day
        self.__year = year
    def mdyFormat(self) -> str:
        return str(self.__month) + "/" + str(self.__day) + "/" + str(self.__year)

class Page:
    def __init__(self, sectionHeader:str, body: str):
        self.__sectionHeader = sectionHeader
        self.__body = body

class BorrowableItem(ABC):
    @abstractmethod
    def uniqueItemId(self) -> int:  
        pass
    @abstractmethod
    def commonName(self) -> str:
        pass



class Book(BorrowableItem):
    def __init__(self, bookId:int, title:str, author:str, publishDate:Date, pages: [Page]):
        self.__bookId = bookId
        self.__title = title
        self.__publishDate = publishDate
        self.__author = author
        self.__pages = pages
    def coverInfo(self) -> str:
        return "Title: " + self.__title + "\nAuthor: " + self.__author
    def uniqueItemId(self) -> int:
        return self.__bookId
    def commonName(self) -> str:
        return "Borrowed Item:" + self.__title + " by " + self.__author


class LibraryCard:
    def __init__(self, idNumber: int, name: str, borrowedItems: {BorrowableItem:Date}):
        self.__idNumber = idNumber
        self.__name = name
        self.__borrowedItems = borrowedItems
    def borrowItem(self,book:BorrowableItem, date:Date):
        self.__borrowedItems[book] = date
    def borrowerReport(self) -> str:
        r:str = self.__name + "\n"
        for borrowedItem in self.__borrowedItems:
            r = r + borrowedItem.commonName() + ", borrow date:" + self.__borrowedItems[borrowedItem].mdyFormat() + "\n"
        return r
```

Creating an instance of a `BorrowableItem`(in this case an instance of the particular realization, Book) is done using the following code.
```
b:BorrowableItem = Book(10991,"Corpus Hermeticum", "Hermes Trismegistus", Date(9,1,1991), [])
print(b.commonName()) #commonName() returns the string representation of a borrowable item
```

Creating an instance of a `LibraryCard` is done using the following.
```
l:LibraryCard = LibraryCard(9982,"Rubelito Abella",{})
```
A library card borrows something using the borrowItem(BorrowableItem) method. And the borrowerReport() prints the library card owners name and the items he/she has borrowed.
```
l.borrowItem(b,Date(9,25,2019))
print(l.borrowerReport())
```
**What you should do:** <br/>
The class definitions above are still missing Periodical and PC.
a Periodical represents a periodical (newspaper, magazines, etc). It is a realization of a BorrowableItem. It contains the following methods and attributes:
```
__init__: initializes a periodical instance with the attributes __periodicalID:int, __title:str, __issue:Date, __pages:[Page]
__periodicalID:int: unique id for a periodical
__title:str: The title of the periodical ("National Geographic", "New York Times")
__issue:Date: The date when the issue was published
__pages:[Page]: A list of Pages that represent the contents
uniqueItemId(): Returns periodicalID
commonName():str: (Implementation of the abstract method from BorrowableItem). It returns the title and the issue date in month/date/year format as a string for example "National Geographic issue: 4/6/2001")
```
a PC represents a library PC. It is a realization of a BorrowableItem. It contains the following methods and attributes:
```
__init__: initializes a PC instance with the attribute __pcID:int.
__pcID:int : unique id for a PC
uniqueItemId():int: Returns __pcID
commonName():str: (Implementation of the abstract method from BorrowableItem). It returns "PC<__pcID>" (the string "PC" followed by the value attribute __pcID, for example "PC1342")
```
Add the following methods to LibraryCard and implement them
```
returnItem(b:BorrowableItem): : returns nothing, it removes the BorrowableItem, b from the __borrowedItems dictionary.
penalty(b:BorrowableItem,today:Date):float : returns a float which is the calculated penalty for BorrowableItem, b when returned today. Every day after the due date the penalty increases by 3.5. An item which is overdue for 4 days has a penalty of 14.
itemsDue(today:Date):[BorrowableItem] : returns a list of BorrowableItems which are on or past the due date. The due date for a Book is 7 days, a Periodical is 1 day, and a PC is 0 days.
totalPenalty(today:Date):float : returns a float which is the total penalty for all the overdue items when calculated today
```
The parameter `today:Date` represents the date today. For example `itemsDue(today:Date)` will return a list of BorrowableItems past the due date if if the date was today.
