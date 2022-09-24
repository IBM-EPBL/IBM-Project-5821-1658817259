import random
def temperature():
    value=random.randint(15,100)
    print(value)
    return value
t=temperature()
t=int(input("Enter the temperature value: "))
def humidity():
    range=random.randint(20,100)
    print(range)
    return range
h=humidity()
h=int(input("Enter the humidity value: "))
#for temperature
if(t>30):
    print("High temperature is detected")
    print("Buzzer on,alarm sound is high")
elif(t==30):
    print("Temperature reached maximum")
else:
    print("Temperature is good")
#for humidity
if(h>65):
    print("High Humidity is detected")
    print("Buzzer on,alarm sound is high")
elif(h==65):
    print("Humidity reached maximum")
else:
    print("Humidity is good")

