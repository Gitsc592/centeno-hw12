###########################################
## Filename : sumLines.py
## Author : Sed Centeno
## Date : 11/21/2024
##
## Description :
## Takes in a txt file named "dataInput.txt" and all of it's elements.
## It sums the elements, gets the number of elements, and gets the average
## and prints them out.
##
## Arguments :
## FilePath (./dataInput.txt)
##
## Example Invocation :
## python3 ./sumLines.py ./dataInput.txt
#############################################
import sys
f = open(sys.argv[1])
flines = f.readlines()
sum = 0
num = 0
avg = 0


for x in flines:
    line = x.split()
    num = num + len(line)
    for y in line:
        sum = sum + eval(y)


avg = sum / num

print("The average is:", avg)
print("The sum is:", sum)
print("The number of elements is:", num)