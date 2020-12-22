def power(x,y):

               dval=1
               if(x==0):
                          return 0
               elif(y==0):
                          return 1
               else :
                          while(y!=0):
                                      dval*=dval
                                      y=y-1
                          return dval
    
def order(n):
               r=0
               while(n!=0):
                           r=r+1
                           n=n//10
                            
               return r            
    
num=int(input("\n Enter the number: "))

n=num

while(n!=0):
            d=0
            r=order(n)
            dig=n%10
            d=d+power(dig,r)
            n=n//10

if(d==num):        
           print("\n Entered number is an Armstrong Number")

else:
           print("\n Entered number is not an Armstrong Number")
