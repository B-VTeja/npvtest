num=int(input("\n Enter number : "))
n=num//2

flag=0
if(num>1):
           for i in range(2,n+1):
                            
                               if((num%i)==0):
                                              break
                                           

                               else:
                                           flag=1
                                         

           if(flag==0):
                       print("\n Not a prime number")

           else:
                       print("\n Entered number is prime number")

else:
    print("\n Not a prime number")

"""i=2
while (i<=n):
    if(num%i==0):
        print("not prime")
        break
        #exit
    i=i+1
if(i>n):
    print("prime")"""
