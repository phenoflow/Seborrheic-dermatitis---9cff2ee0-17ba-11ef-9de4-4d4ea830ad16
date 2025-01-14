# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"62750.0","system":"readv2"},{"code":"3069.0","system":"readv2"},{"code":"7425.0","system":"readv2"},{"code":"38493.0","system":"readv2"},{"code":"45407.0","system":"readv2"},{"code":"48473.0","system":"readv2"},{"code":"35810.0","system":"readv2"},{"code":"3453.0","system":"readv2"},{"code":"57525.0","system":"readv2"},{"code":"21266.0","system":"readv2"},{"code":"6295.0","system":"readv2"},{"code":"359.0","system":"readv2"},{"code":"18970.0","system":"readv2"},{"code":"2556.0","system":"readv2"},{"code":"65283.0","system":"readv2"},{"code":"48641.0","system":"readv2"},{"code":"20150.0","system":"readv2"},{"code":"653.0","system":"readv2"},{"code":"3580.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('seborrheic-dermatitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["seborrhoeic-seborrheic-dermatitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["seborrhoeic-seborrheic-dermatitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["seborrhoeic-seborrheic-dermatitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
