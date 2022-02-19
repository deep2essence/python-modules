#!/usr/bin/python3

# Save list contents to TXT file line by line
def list2file(filepath,values):
    with open(filepath, 'w') as output:
        for row in values:
            output.write(str(row) + '\n')
