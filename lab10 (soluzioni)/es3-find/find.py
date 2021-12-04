##
#  Find occurrences of a word in several files.
#
import sys

# Target files
filenames = input('Insert the list of files to search (separate with ,): ')

# Extract the target word from the command line.
target = input('Insert the word to search: ')

# For each filename on the command line.
for filename in filenames.split(','):
    # Save the filename and open the file.
    inf = open(filename.strip(), "r", encoding='utf-8')

    # Search each line in the file for the target.
    for line in inf:
        if target.lower() in line.lower():  # 'in' is used to serach for a substring
            print(f'{filename}: {line}', end='')  # end='' because 'line' already contains a \n

    # Close the file.
    inf.close()
