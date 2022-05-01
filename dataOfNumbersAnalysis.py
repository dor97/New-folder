
'''
The program prints the average, variation, max and min values and the 40 percentage
from a file of numbers
'''

toMean = open("DataFile.txt","r")
cou = sum = sqSum = smallCou = bigCou = 0
firstRead = True
isNotPre = False
min = max = 0

for fillLine in toMean:
    line = fillLine.split()
    cou += len(line)
    for num in line:
        num = float(num)
        if firstRead or max < num:
            max = num
            firstRead = False
        if firstRead or min > num:
            min = num
            firstRead = False
        sum += num
        sqSum += num** 2

start = min
end = max

#find the 40 percentage with binary search on the values of the numbers in the file
while not isNotPre:
    toMean.seek(0)
    smallCou = bigCou = 0
    mid = (start + end) / 2
    for fillLine in toMean:
        line = fillLine.split()
        for num in line:
            num = float(num)
            if num <= mid:
                smallCou += 1
            if num >= mid:
                bigCou += 1
    isNotPre = True
    if smallCou < 0.4 * cou:
        start = mid
        isNotPre = False
    if bigCou < 0.6 * cou:
        end = mid
        isNotPre = False    
        
        

avr = sum / cou
var = (sqSum - cou*(avr**2)) / cou

print("The average is:",avr)

print("The variation is:",var)

print("The max value is:",max)

print("The min value is:",min)

print("The 40 percentage:",mid)
    
toMean.close()

