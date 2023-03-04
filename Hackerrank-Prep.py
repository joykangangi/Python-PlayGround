# challenges practiced today:
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
