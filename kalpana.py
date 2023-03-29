import csv
import time

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    
    for i in reader:
        print(i)
        time.sleep(1) # wait for 1 second before printing the next row
