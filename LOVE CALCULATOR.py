
print ("Welcome To the Love Calculator!")
# asking for the user name
name1 = input ("What is your name?\n")
name2 = input ("What is their name?\n")

# combining the two name from the input
combinedName = name1 + name2

# converting the combination of two input  to Lowercase
lowerCaseName = combinedName.lower()

#counting letters occurrence in the in the combined word
t = lowerCaseName.count("t")
r = lowerCaseName.count("r")
u = lowerCaseName.count("u")
e = lowerCaseName.count("e")

l = lowerCaseName.count("l")
o = lowerCaseName.count("o")
v = lowerCaseName.count("v")
e = lowerCaseName.count("e")
 
 #bringing together the piece of counted value as one
true = t + r + u + e

love = l + o + v + e

#combining these number to make a 2 digit number e.g. 6 + 7 = 67
score = int(str(true) + str(love))

#condition for the above code to print
if (score < 10) or (score > 90): # check either less than 10 or greater than 90, if one of them is true
    print(f"Your Score is {score}, you go together like coke and mentos")

elif (score > 40) and (score < 50): # check if both of them are true
    print(f"Your Score is {score}, you are alright together.")

else: #it is executed when others are false
    print (f"Your Score is {score}.")
