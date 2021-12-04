##
#  Read a file and save it to a new file with line numbers.
#

# Read the file names from the user.
input_name = 'input.txt'
output_name = 'output.txt'

# Open the input and output file names.
inf = open(input_name, "r", encoding='utf-8')
outf = open(output_name, "w", encoding='utf-8')

# Read lines from the file and save them to a new file with line numbers.
number = 1
for line in inf:
    # outf.write("/*" + str(number) + "*/ " + line)
    outf.write(f'/*{number}*/ {line}')
    number = number + 1

# Close the files.
inf.close()
outf.close()

