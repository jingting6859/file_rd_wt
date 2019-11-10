import csv
fileobj='csv_wt.csv'
# 写csv
with open (fileobj,'w')as f:
    csv_writer = csv.writer(f)
    for i in range(10):
        item = [i]*10
        csv_writer.writerow(item)

# 读csv
with open(fileobj,'r')as rd:
    csv_reader = csv.reader(rd)
    for line in csv_reader:
        print(line)

