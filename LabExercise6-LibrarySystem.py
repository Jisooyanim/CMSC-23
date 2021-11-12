from abc import ABC, abstractmethod
from datetime import date

class Date:
    def __init__(self, month:int, day:int, year:int):
        self.__month = month
        self.__day = day
        self.__year = year

    def mdyFormat(self) -> str:
        return str(self.__month) + "/" + str(self.__day) + "/" + str(self.__year)

    def year(self):
        return self.__year

    def month(self):
        return self.__month

    def day(self):
        return self.__day

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

    def __repr__(self):
        return "Book"

class Periodical(BorrowableItem):
    def __init__(self, periodicalID:int, title:str, issue:Date, pages: [Page]):
        self.__periodicalID = periodicalID
        self.__title = title
        self.__issue = issue
        self.__pages = pages

    def uniqueItemId(self) -> int:
        return self.__periodicalID

    def commonName(self) -> str:
        return "Borrowed Item:" + self.__title + " issue: " + self.__issue.mdyFormat()

    def __repr__(self):
        return "Periodical"

class PC(BorrowableItem):
    def __init__(self, pcID:int):
        self.__pcID = pcID

    def uniqueItemId(self) -> int:
        return self.__pcID

    def commonName(self) -> str:
        return("Borrowed Item:PC" + str(self.__pcID))

    def __repr__(self):
        return "PC"

class LibraryCard:
    def __init__(self, idNumber: int, name: str, borrowedItems: {BorrowableItem:Date}):
        self.__idNumber = idNumber
        self.__name = name
        self.__borrowedItems = borrowedItems

    def borrowItem(self, BorrowedItems:BorrowableItem, date:Date):
        self.__borrowedItems[BorrowedItems] = date

    def borrowerReport(self) -> str:
        r:str = self.__name + "\n"
        for borrowedItem in self.__borrowedItems:
            r = r + borrowedItem.commonName() + ", borrow date:" + self.__borrowedItems[borrowedItem].mdyFormat() + "\n"
        return r

    def returnItem(self, b:BorrowableItem):
        for borrowedItem in self.__borrowedItems:
            if b == borrowedItem:
                self.__borrowedItems.pop(b)
                break
    #Calculates the gap between the borrowed date and date returned
    def gapDays(self, borrowedItem, today:date):
        date_borrow = date(self.__borrowedItems[borrowedItem].year(), self.__borrowedItems[borrowedItem].month(), self.__borrowedItems[borrowedItem].day())
        date_today = date(today.year(), today.month(), today.day())
        return date_today - date_borrow

    def penalty(self, b:BorrowableItem, today:Date) -> float:
        exist = False

        for borrowedItem in self.__borrowedItems:
            if b == borrowedItem:
                exist = True

        if exist == True:
            due = 0
            days = self.gapDays(borrowedItem, today)

            if repr(b) == "Book":
                if days.days > 7:
                    due = days.days - 7
            elif repr(b) == "Periodical":
                if days.days > 1:
                    due = days.days - 1
            elif repr(b) == "PC":
                if days.days > 0:
                    due = days.days

            return float(due * 3.5)

    def itemsDue(self, today:Date) -> list[BorrowableItem]:
        arr = []

        for borrowedItem in self.__borrowedItems:
            days = self.gapDays(borrowedItem, today)

            if repr(borrowedItem) == "Book":
                if days.days >= 7:
                    arr.append(borrowedItem)
            elif repr(borrowedItem) == "Periodical":
                if days.days >= 1:
                    arr.append(borrowedItem)
            elif repr(borrowedItem) == "PC":
                if days.days >= 0:
                    arr.append(borrowedItem)
        return arr

    def totalPenalty(self, today:Date) -> float:
        total = 0.0
        due = 0

        for borrowedItem in self.__borrowedItems:
            days = self.gapDays(borrowedItem, today)

            if repr(borrowedItem) == "Book":
                if days.days > 7:
                    due = days.days - 7
            elif repr(borrowedItem) == "Periodical":
                if days.days > 1:
                    due = days.days - 1
            elif repr(borrowedItem) == "PC":
                if days.days > 0:
                    due = days.days
            total += due * 3.5
        return total

##Test##
borrow_1 : BorrowableItem = Book(5, "Fault in Our Stars", "John Green", Date(1, 10, 2012), 313)
borrow_2 : BorrowableItem = Periodical(10001, "SunStar", Date(11,13,2021), 500)
borrow_3 : BorrowableItem = PC(69)
Card : LibraryCard = LibraryCard(1561, "Harry Potter", {})
Card.borrowItem(borrow_1, Date(11,13,2021))
Card.borrowItem(borrow_2, Date(11,13,2021))
Card.borrowItem(borrow_3, Date(11,13,2021))
#print(Card.borrowerReport())
#Card.returnItem(borrow_3)
#print(Card.borrowerReport())
print(Card.penalty(borrow_2, Date(12,25,2021)))
print(Card.itemsDue(Date(12,25,2021)))
print(Card.totalPenalty(Date(12,25,2021)))