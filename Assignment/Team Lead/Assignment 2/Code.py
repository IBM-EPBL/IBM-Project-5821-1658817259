import random
def temperature():
    value=random.randint(25,100)
    return value


def humidity():
    range=random.randint(40,100)
    return range
    
t=temperature()
t=int(input("Enter the temperature value: "))

h=humidity()
h=int(input("Enter the humidity value: "))

#Temperatrue 
if(t>30):
    print("High temperature is detected")
    print("Buzzer on,alarm sound is high")
elif(t==30):
    print("Temperature reached maximum")
else:
    print("Temperature is good")

#Humidity
if(h>65):
    print("High Humidity is detected")
    print("Buzzer on,alarm sound is high")
elif(h==65):
    print("Humidity reached maximum")
else:
    print("Humidity is good")
