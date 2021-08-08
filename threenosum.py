def sum(num1,num2,num3):
    add=num1+num2+num3
    
    def sum():
        add=(num1+num2+num3)/3
        return(add)

    average=sum()
    print(average)
    return(add)
    
user1=int(input("enter a number"))
user2=int(input("enter a number"))
user3=int(input("enter a number"))
average=sum(user1,user2,user3)
print(average)