def doubledInt(x):
    return 2 * x

def largest(x, y):
    if x < y:
        return y
    else:
        return x

def isVertical(a ,b):
    if a[0] == b[0]:
        return True
    else:
        return False

def primes(n):
    ans = []
    count = 0
    num = 2

    if n <= 0:
        return ans
    else:
        while count != n:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                ans.append(num)
                count += 1
            num += 1
    return ans

def fibonacciSequence(n):
    first_term = 0
    second_term = 1
    seq = []

    if n <= 0:
        return seq
    elif n == 1:
        return first_term
    else:
        seq.append(first_term)
        seq.append(second_term)
        for i in range(n - 2):
            ans  = first_term + second_term
            first_term = second_term
            second_term = ans
            seq.append(ans)
        return seq

def sortedIntegers(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if(l[i] > l[j]):
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l

def sublists(l):
    res = [[]]

    for i in range(len(l) + 1):
        for j in range(i + 1, len(l) + 1):
            res.append(l[i:j])
    return res
    
#Testing
#print(doubledInt(250))
#print(largest(-10.4,-5.9))
#print(largest(69.69,70.45))
#print(isVertical((5.0,4.9), (5.0, -9.6)))
#print(isVertical((8.01,6.0), (5.00, 10.5)))
#print(primes(10))
#print(fibonacciSequence(20))
#print(sortedIntegers([5,6,1,2,5]))
#print(sublists([1,2,3,4,5]))