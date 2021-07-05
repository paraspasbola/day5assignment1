#day5 #assignment1
#build a function for finding number is prime or not.

#Prime numbers:
#A prime number is a natural number greater than 1 and having no 
#positive divisor other than 1 and itself.

#For example: 3, 7, 11 etc are prime numbers.

num=int(input("Enter a number : "))

def prime(num):                       #function
    if num>1:
        
        for i in range(2,int(num/2)+1):
            if num%i==0:
                return(str(num)+" is not a prime number")
                break
        return(str(num)+"  is a Prime Number")
    else:
        print(str(num)+" is a Prime Number")
 
 
print(prime(num))