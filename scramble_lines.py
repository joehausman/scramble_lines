import sys
import random

start = 0
end = 0

syslen = len(sys.argv)

if syslen != 3 and syslen != 5:
    print('error: wrong number of arguments (3 or 5 expected)\n' +
    'usage: md_table_flip <infile> <outfile> [startline endline]', file = sys.stderr)
    exit(0)

file_list = []

with open(sys.argv[1], 'r') as infile:
    file_list = infile.readlines()

if syslen == 3:         # will scramble the whole file
    start = 0
    end = len(file_list)
else:                   # syslen must be 5
    start = int(sys.argv[3])
    end = int(sys.argv[4])

with open(sys.argv[2], 'w') as outfile:
    outfile.write(''.join(file_list))

# print('start: ' + str(start))
# print('end: ' + str(end))
