#Loops.py
#We are using these loops to print a list of integers, which will be from one set amount to another set amount
#Created by Kaihehau "Kai" Goo (again for the second time) on May 4th 2025
#may the fourth be with you 

var1=0
while var1<22:
    print(var1)
    print(var1)
    var1=var1+1
#This comment is for the (above) while loop, which will print the variable var1 until it reaches 5

least_number=5
ultra_least_favorite_number=13

#For the (above) for loop, which will print text and the variable var1 from least_favorite_number=5 until it reaches 20

while var1<20:
    if var1 == least_number:
        var1=var1+1
        print(var1)
        continue
    if var1==ultra_least_favorite_number:
        var1= var1 + 1
        print(var1)
        continue
    #  This continue sends the code reader back to before the indent


#Will print the variable var1 from var1=5 until it reaches 20               
print("Now we are printing variable 2 and 3. Variable 3 will print every integer 0,1,2,3,4. After Variable 3 prints, "
      "Var2 will print every integer 0-49, besides 13. "
      "Then the code will prompt a user input to change the range."
      "If the range is expanded by the user, the code will run in the same way, but var2 will break at 420")
for var2 in range(50):
    if var2==ultra_least_favorite_number:
        var2=var2+1
        continue
    for var3 in range(5):
            print(var3)
    print(var2)
    print('')

var420=int(input("Enter a number between 1 and 500: "))


for var2 in range(var420):
    if var2 == 420:
        break
    if var2 == ultra_least_favorite_number:
        var2 = var2 + 1
        continue
    for var3 in range(5):
        print(var3)
    print(var2)
    print('')
     #break ends the code and stops the rest of the program from running for the (above) number
print(''
      '')

print("done")

print("you've reached the end of the program and the end of the line")
#Prints "done" and a cowboy movie line when the program is finished
