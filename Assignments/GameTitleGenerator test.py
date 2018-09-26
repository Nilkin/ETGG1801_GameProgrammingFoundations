#Game Title Generator v1.0
import random
t1=["super","Xtreme","Elite","Delux","Virtual","Fighting","TomClancy's","Sid Meyer's"]
t2=["Black-Ops","Undecover","Mutant","Covert","Iron","Happy"]
t3=["Ninja","War","Shotgun","Mummy","Tank","Warrior","Mario","Horse","Wrestler","ETTG1801.02","Porn-Star"]
t4=["Puzzle","Bobble","Nipples","Universe","Slam","Balls","Blaster","Fighter"]
#name generator
word1=t1[random.randint(0,len(t1)-1)]
word2=t2[random.randint(0,len(t2)-1)]
word3=t3[random.randint(0,len(t3)-1)]
word4=t4[random.randint(0,len(t4)-1)]
title=word1+" "+word2+" "+word3+" "+word4
print(title)
#Functions:
#   -Mini-Programm that can be defined and used later.
#   -Named sequence of commands or instructions that can be called upon to perform a task.
#   -We can define them and then call upon these functions from within our programs.
#Why you should use functions:
#   -Reduce redundancy in the code.
#   -Can make code shorter, faster to program
#   -Makes code more readable, writeable, and maintainable.
#   -Organize code into libraries of useful functions.
#   -Divide larger programs into smaller, more manageable pieces.
#   -Allows for abstraction of functionality.
#Functions are like seperate mini-programs:
#def function():
#   "function Body"
#   indented code is the sequence of Statements.
def rolldie():#defining the function rolldie
    import random
    print(random.randint(1,6))
rolldie()#calls the function
rolldie()#calls the function again
print(random.randint(1,6))#error! random was only imported within the function.
#Functions to show in a game:
#   -ShowGold
def ShowGold():
    print("you have",PlayerGold,"gold pieces.")
#this is a Global Variable
PlayerGold = 100
#   -LoseGold
def LoseGold():
    #this is a Local Variable
    global PlayerGold = 0
    print("you lost your gold!")
#Functions are like cars with tinted windows:
#   -functions can see out to access global variables
#   -functions can't see other function variables.
#   -functions can't change other function's Local variables.
#   -functions are free to create & change their own local variables.
#   -functions cant change global variables(by default).
#   -to change a global variable we can use the "global"statement to "roll down the window" per say.
def addem(n1,n2):#data that the function expects to recieve. Called Peramaters.
    result=n1+n2
    return result #answer value that the function reports. Called the Return Value
print(addem(2,14))#makes 16
#Parameters:
#   -A function can be defined to accept 0 or more parameters.
#   -The position of the parameters is important because the order passed is matched to the defined parameter names.
#   -We can also pass the parameters by name
        #print(addem(n2=14,n1=2))
#Return Value:
#   -A function can only return one single item.
#   -The single itme can be a list, sequence, or object.
#   -If no return value is specified, a special value of none is returned.
#make the name gen into function
def generateTitle():
    import random
    t1=["super","Xtreme","Elite","Delux","Virtual","Fighting","TomClancy's","Sid Meyer's"]
    t2=["Black-Ops","Undecover","Mutant","Covert","Iron","Happy"]
    t3=["Ninja","War","Shotgun","Mummy","Tank","Warrior","Mario","Horse","Wrestler","ETTG1801.02","Porn-Star"]
    t4=["Puzzle","Bobble","Nipples","Universe","Slam","Balls","Blaster","Fighter"]
    #name generator
    word1=t1[random.randint(0,len(t1)-1)]
    word2=t2[random.randint(0,len(t2)-1)]
    word3=t3[random.randint(0,len(t3)-1)]
    word4=t4[random.randint(0,len(t4)-1)]
    title=word1+" "+word2+" "+word3+" "+word4
    print(title)
    
