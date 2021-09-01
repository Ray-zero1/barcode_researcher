import csv
import datetime

#s = [int(input()) for i in range(10)]      
#print(s)

s = []
print("Enter your number")
while True:
    try:
        a = int(input())
    except Exception:
        continue
    if a == 1920197008001:
        print("FINISH")
        break
    s.append(a)
    
print(s)    

now = datetime.datetime.now()
filename = now.strftime('%Y%m%d_%H%M') + '.csv'

with open(filename, 'a') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(s)
       



     
