def add(num1,num2 ,ope):
    # if ope=="+":
    #     return num1+num2
    # elif ope=="-":
    #     return num1-num2
    # # elif ope=="*":
    # #     return num1*num2
    # elif ope=="**":
    #     return num1**num2
    # elif ope=="//": 
    #     return num1//num2
    # else:
    #     return num1/num2
    i=0
    sume=0

    read=[]
    while i<len(num1):
        sume=num1[i]*num2[i]
        read.append(sume)
        i+=1
    return read

        
# user1=int(input("enter a number"))
# user2=int(input("enter a number"))
# addtion=add(user1,user2,"+")
# print("addtion","=",addtion)
# sub=add(user1,user2,"-")
# print("substration =",sub)
# doc=addtion+sub
# print("total",doc)


multiply=add([5, 10, 50, 20], [2, 20, 3, 5],"*") 
print(multiply)
