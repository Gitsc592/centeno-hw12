#################################################
## Filename : reconstructSentence.py
## Author : Sed Centeno
## Date : 11/26/2024
##
## Description :
## Takes two text files that each contains fragments of a sentence
## in reverse order and correctly arranges them and writes it to
## "output.txt" in the current directory.
##
## Arguments :
## Filename_1 Filename_2
##
## Example Invocation :
## python3 ./reconstructSentence.py ./input1.txt ./input2.txt
###################################################


import sys

file_input1 = open(sys.argv[1])
file_input2 = open(sys.argv[2])

flines_1 = file_input1.readlines()
flines_2 = file_input2.readlines()

line_1 = flines_1[0].split()
line_2 = flines_2[0].split()
out = []

for i in range(len(line_1)):
    out.append(line_1[-i-1])

for i in range(len(line_2)):
    out.insert((i*2)+1, line_2[-i-1])

outfile = open("output.txt", "w")
for i in range(len(out) - 1):
    outfile.write(out[i] + " ")

outfile.write(out[-1])