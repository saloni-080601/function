# def add_number_list(num1,num2):
#     print(num1+num2)
#     i=0
#     sum=0
#     let=[]
#     while len(num1)>i:
#         sum=num1[i]+num2[i]
#         let.append(sum)       
#         i+=1
#     print(let)

# add_number_list([50,60,10],[10,20,13])
# def check_numbers(num1,num2):
#     num1=4
#     num2=6
#     if num1%2==0 and num2%2==0:
#         print("both are even")
# num1=4
# num2=6
# check_numbers(num1,num2)
# 1
# def check_numbers(num1,num2):
#     i=0
#     while i<len(num1):
#         if num1[i]%2==0 and num2[i]%2==0:
#             print("both are even")
#         else:
#             print("both are not even")
#         i+=1
# check_numbers([2,4,6,6,30],[1,3,5,6,9])
# 55
# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum

# sum6 = add_numbers_more(100, 20) 
def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    else:
        return "Chole Bhature"

    print ("Kya main print ho payungi? :-(")

mon_menu = menu("monday")
print (mon_menu)
tues_menu = menu("tuesday")
print (tues_menu)
fri_menu = menu("friday")
print (fri_menu) 


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    