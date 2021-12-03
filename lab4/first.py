#1
import csv
import random
import codecs
f1 = codecs.open('words1.txt', "r", "utf_8_sig")
f2 = codecs.open('words2.txt', "r", "utf_8_sig")
f3 = codecs.open('words3.txt', "r", "utf_8_sig")
rw1 = csv.reader(f1)
wo1 = [row for row in rw1]
rw2 = csv.reader(f2)
wo2 = [row for row in rw2]
rw3 = csv.reader(f3)
wo3 = [row for row in rw3]
print(random.choice(wo1)+random.choice(wo2)+random.choice(wo3))
