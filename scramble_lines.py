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
    start = int(sys.argv[3]) - 1
    end = int(sys.argv[4])

if start < 0 or start > len(file_list):
    print('error: invalid start value')
    exit(1)
if end < 0 or end > len(file_list):
    print('error: invalid end value')
    exit(1)
if start > end:
    print('error: start cannot be greater than end')
    exit(0)

sub_file_list = file_list[start:end]

random.shuffle(sub_file_list)       # this function makes things so easy
file_list[start:end] = sub_file_list

with open(sys.argv[2], 'w') as outfile:
    outfile.write(''.join(file_list))
