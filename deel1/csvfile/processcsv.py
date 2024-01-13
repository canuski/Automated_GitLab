import sys
import csv
pad = sys.argv[1]
with open(f'{pad}', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(', '.join(row))
