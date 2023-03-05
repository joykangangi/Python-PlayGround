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

# Exercise 2
# This is very easy to understand, but it took me almost 3 hours to figure it out.
# STEPS:
# 1. Create an alphabet in lowercase and uppercase
# 2. Create an empty map for storing the normal alphabet letters to the new moved letter
# 3. Create an empty list; this will be changed to a string.
# 4. Start looping in each character in the passed string.
# 5. If char is in lowercase; 
#          -> loop in the lowercase list
#          -> get the old letter by index in lowercase list
#          -> calculate the moving index;
#          -> use % to factor in getting at the end of alphabet;case k=2; (26+2)%26 = 2 == 'b',(22+2)%26 = 24 == 'x'
#          -> new letter will be at the new index
#          -> in the map;add the old letter as a key and new letter as value
# 6. If char is in uppercase:
#          -> do as step 5
# 7. if char isnt in there; its key and value will be same
# 8. append to the sentence the value of the key in the map 
# 9. make the list of chars to str
def caesarCipher(s, k):
    s_alphabets = [chr(i) for i in  range(ord('a'),ord('z')+1)]
    c_alphabets = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    newalp_map = {}
    new_sent = []

    for c in s:
        if c in s_alphabets:
            for j in range(len(s_alphabets)):
                letter = s_alphabets[j]
                print("ol1",letter)
                moving_index = (j + k) % len(s_alphabets) 
                new_letter = s_alphabets[moving_index]
                newalp_map[letter] = new_letter
                print("nl1",new_letter)
        
        elif c in c_alphabets:    
            for l in range(len(c_alphabets)):
                letter = c_alphabets[l]
                print("ol2",letter)
                moving_index = (l + k) % len(c_alphabets)
                new_letter = c_alphabets[moving_index]
                newalp_map[letter] = new_letter
                print("nl2",new_letter)
        else:
            newalp_map[c] = c       

        new_sent.append(newalp_map[c])                
    imp_new_sent = ''.join(new_sent)

    return imp_new_sent 
