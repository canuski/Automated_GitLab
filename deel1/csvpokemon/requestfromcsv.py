import sys
import csv
pad = sys.argv[1]
with open(f'{pad}', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=' ')
    for row in reader:
        name = row["Name"]
        gen = row["Generation"]
        if gen == '2':
            print(f'{name}, {gen}')
