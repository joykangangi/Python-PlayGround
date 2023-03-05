#The questions can be found online(hackerrank) by searching the functions definitions
# challenges practiced Day1:
def timeConversion(s):
    lastChar = s[-2]
    if(lastChar == 'P'):
        if s[:2] == "12":
            time = s[:-2]  
        else:      
            hours = (12 + int(s[:2]))
            time = str(hours) + s[2:-2]
    else:
        if s[:2] == "12":
            hours = "00"
            time = hours + s[2:-2]
        else:
            time = s[:-2]    
    return time  
  
 def lonelyinteger(a):
    seta =set(a)
    for x in seta:
        least = a.count(x)
        if least == 1:
            return x
          
          
def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2  # integer division to get the middle index
    if n % 2 == 0:
        # if there are an even number of elements, return the average of the middle two
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # if there are an odd number of elements, return the middle element
        return sorted_numbers[mid]        
    
    
def diagonalDifference(arr):
     leftSum = 0
     rightSum = 0
     for i in range(len(arr)):
         leftSum = leftSum + arr[i][i]
         i = i+1 
 
     j=0
     for i in reversed(range(len(arr))):
         rightSum = rightSum + arr[i][j]
         j = j+1
         i = i-1 
     return abs(leftSum - rightSum)       

# Day2:
# this one is very easy but understanding it was difficult.
# Mainly, I was not understanding how P2 wins when the tower height = 1. 
# But from online searches, P1 wont have any valid move to make
# so it's like P2 will win cause P1 is stuck.
def towerBreakers(n, m):
    specialOne = m == 1
    p2win = n % 2 == 0
    return 2 if specialOne or p2win else 1
