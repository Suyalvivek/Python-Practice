import csv
from csv import DictReader

with open('sample_contacts.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    # next(csv_reader)
    # for line in csv_reader:
    #     print(line[2])
    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)

with open('new_names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file,delimiter='\t')
    for line in csv_reader:
        print(line['email'])
    with open('new_names.csv','r') as new_file:
        fieldnames = ['firstname','lastname','email']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='--')
        for line in csv_reader:
            csv_writer.writerow(line)

