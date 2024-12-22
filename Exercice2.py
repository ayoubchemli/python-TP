print ("Please type in the temperature:")
temp = int(input())
if temp < 0:
    print("It is freezing!")
elif temp >= 0 and temp < 10:
    print("It is cold!")
elif temp >= 10 and temp < 20:
    print("It is cool!")
    
print("stay safe!")