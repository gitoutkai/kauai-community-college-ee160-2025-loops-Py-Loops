#Loops.py
#We are using these loops to print a list of integers, which will be from one set amount to another set amount
#Created by Kaihehau "Kai" Goo (again for the second time) on May 4th 2025
#may the fourth be with you
#I am writing another sentence here so this goes to the top of the most recently editted.

print("Var1 will print two times. It will print every integer from 0-10")
var1=1
while var1<11:
    print(var1)
    var1=var1+1
    if var1==11:
        continue
#this should accomplish the first task of integers from 0-10

for var1 in range(1,11):
  print(var1)
  var1=var1+1
print(' ')
#For the (above) for loop, which will print text and the variable var1 from 0 until it reaches 10, then it will happen again

for var1 in range(1,51):
    if (var1%3==0):
        print(var1)
        var1=var1+1

    #  This continue sends the code reader back to before the indent
    #Will print the variable var1 from var1=5 until it reaches 50

var12: int=12
var3=var12/1
count=0
for var1 in range(0,20):
    if var3>0.0001:
        print(var3)
        var3 = (var3 / 2)
        count=count+1
        continue
#This is setting the range and denominator for the equation   in this case we are dividing my 2
#until the divident is less then 0.0001, that would be the if var3> part

if var3 < 0.0001:
    print(count,"rounds of dividin 12 by 2")
    print("done")
#the if var3 < 0.0001 statement ensure that the number of interations is stopped at the right time

var69 = var12-var3
print("the change in the value is 12 minus ", var3, " which equals", var69,".")
#gthis is the change in the value of 12, before and after it was divided by 2, on 17 occasions

# THIS LITERALLY TOOK 3 HOURS BECAUSE THE VAR1 RANGE WAS BUGGIN  PLEASE LMK IF THERES AN EASIER WAY

#Prints "done" and a cowboy movie line when the program is finished
