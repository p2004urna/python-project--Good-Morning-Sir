import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
hourstamp = time.strftime("%H")
print(int(hourstamp))
if (int(hourstamp)>=0 and int(hourstamp)<12):
    print("Good Morning Sir")
elif(int(hourstamp)>12 and int(hourstamp)<13):
    print("Good Noon Sir")
if(int(hourstamp)>=13 and int(hourstamp)<18):
    print("Good Afternoon Sir")
else:
    print("good Night Sir")