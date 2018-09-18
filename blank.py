import csv
with open('Dauerzeitschrieb_20171218_053831.csv', 'r') as inp, open('Without_space_data.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    it=0
    for row in csv.reader(inp):
        it=it+1
        if it % 2 != 0:
            writer.writerow(row)
