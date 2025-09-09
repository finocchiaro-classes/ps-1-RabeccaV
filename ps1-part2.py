
def number_fun(a,b):
    print("You entered",a, "and", b)
    print(a,"+", b,"=", int(a)+int(b))    #sum
    print(a, "*", b,"=", int(a)*int(b))    #product
    print(a,"**", b,"=", int(a)**int(b))  #exponent
    print(a,"%", b,"=", int(a)%int(b))    #remainder

firstnum=input("Enter an integer between 10 and 100: ")
secondnum= input("Enter an integer less than 4: ")
number_fun(firstnum,secondnum)
