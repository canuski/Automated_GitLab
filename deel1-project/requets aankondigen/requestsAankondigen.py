import csv

csvFile = "testFile.csv"  # pad naar csv file
with open(csvFile, newline='') as csvfile:  # csv file openen
    reader = csv.reader(csvfile)  # csv reader doen
    found_vakken = {}
    found_groepen = {}  # dicts voor storage
    next(reader, None)  # over de header rij gaan
    for row in reader:
        vak, groep, studentEmail = row
        if vak not in found_vakken:
            found_vakken[vak] = True
        else:  # vak al gevonden blijf door gaan
            continue
        if groep not in found_groepen:
            found_groepen[groep] = True
        else:  # groep al gevonden blijf door gaan
            continue
        print(
            f"Nu moet een groep gemaakt worden voor {studentEmail}. Dit is een subgroep van klasgroep {groep} voor het vak {vak}")
