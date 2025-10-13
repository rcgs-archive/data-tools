import csv

with open("test.csv","w",encoding="utf_8") as f:
    writer = csv.writer(f,lineterminator="\n")
    writer.writerows(["0","目的"])
