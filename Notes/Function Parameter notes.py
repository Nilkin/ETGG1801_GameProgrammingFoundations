#Review
    #Functions:
    #create your own function:
def addem(n1,n2):
    result=n1+n2
    return result

#Positional Parameters Notes:
    #Position of passed data determines the name of the data within the function.
print addem(1,2) #inside the function we have n1=1, n2=2 when the function gets called. n1 is the first position, and n2 is the second position. the computer expects the code to go in order of position.
x=addem(104,201)#n1=104,n2=201

#Named Parameters:
    #we can also use the parameter names:
    x=addem(n1=104,n2=201)
    or
    x=addem(n2=201,n1=104)
    #When using names, the position doesn't matter.
#Optional Parameters/Default Parameter values:
    def addem (n1=0,n2=0):#when adding the = in defining the function, it makes the specified number the default value.
        result=n1+n2
        return result
    #if a parameter is not used in a function call, then the defined default value is used.

    #Function to Average Two numbers:
    def avgTwo(num1,num2):
        avg=(num1+num2)/2
        return avg
#To call
    print(avgTwo(20,40))#this would equal 30

#Function to average the numbers in a list:
    def avgList(List1):
        #add up all items in list
        sum=0
        for num in List1:
            sum+=num
        #divide by the number of items
        avg= sum/len(List1)
        #return the average
        return avg

#built in function in python
    #Function to return the Max number in a list:
    def maximum(List1):
        maxSoFar=List[0]
        for x in List1[:]:
            if x>maxSoFar:
                maxSoFar=x
            return maxSoFar
#could also do if len(List1)==1:return maxSoFar
        
