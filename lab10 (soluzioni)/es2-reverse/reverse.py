##
#  Copy the lines from one file into another so that they are in reverse
#  order.
#
import sys

# Read the input file name from the command line and open the input file.
input_file = 'input.txt'
inf = open(input_file, "r", encoding='utf-8')

# Read all the lines from the input file.
lines = inf.readlines()

# Close the input file.
inf.close()

# Read the output file name from the command line and open the output file.
output_file = 'output.txt'
outf = open(output_file, "w", encoding='utf-8')

# Write the lines in reverse order.
for i in range(len(lines) - 1, -1, -1):
    outf.write(lines[i])

# Close the output file.
outf.close()
