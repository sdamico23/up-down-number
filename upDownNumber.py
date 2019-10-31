import math
//palindrone
def isPalin(n):
    div = 1
    while (n / div) >= 10:
        div *= 10
    while n != 0:
        lead = n // div
        trail = n % 10
        if (lead != trail):
            return False
        n = (n % div)//10
        div = div/100
    return True
//near prime
def checkNear(n):
    cnt = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n /= i
            cnt += 1
        if cnt >= 2:
            break
    if (n > 1):
        cnt += 1
    return cnt == 2 or cnt == 1

def nearPrime(n):
    if checkNear(n):
        return True
    else:
        return False
//up number (digits increasing)
def upnum(lst):
    for x in range(1, len(lst)):
        if ((lst[x] > lst[x-1])):
            return False
    return True
//down number
def downNum(lst):
    for x in range(1, len(lst)):
        if ((lst[x] < lst[x-1])):
            return False
    return True
def updown(lst):
    incr = True
    for x in range(1, len(lst)):
        if ((lst[x] < lst[x-1]) and incr):
            incr = False
        elif ((lst[x] > lst[x-1]) and not incr):
            return False
    return True
def isNice(n):
    lst = []
    while n > 0:
        lst.append(n%10)
        n //=10
    if (upnum(lst) == True or downNum(lst) == True or updown(lst) == True):
        return True
    else:
        return False
inp = input("Please enter the list: ")
lst1 = [int(x) for x in inp.split()]
def main():
    for x in range(0, len(lst1)):
        n = int(lst1[x])
        count = 0
        prev = 0
        nxt = 0
        if isPalin(n) and not nearPrime(n) and not isNice(n):
            count += (2*n)
        elif isPalin(n) and nearPrime(n) and not isNice(n):
            count += (4*n)
        elif isPalin(n) and nearPrime(n) and isNice(n):
            count += (12*n)
        elif not isPalin(n) and nearPrime(n) and not isNice(n):
            count += (2*n)
        elif not isPalin(n) and nearPrime(n) and isNice(n):
            count += (6*n)
        elif isPalin(n) and not nearPrime(n) and isNice(n):
            count += (6*n)
        elif not isPalin(n) and not nearPrime(n) and isNice(n):
            count += (n*3)
        elif not isPalin(n) and not nearPrime(n) and not isNice(n):
            count += n
        print(n, count)
main()
        
            
            
