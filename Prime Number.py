#number should greater tha 1
# it had only 2 factor:0 and itself

num=int(input("Enter a number:"))
count=0
if num > 1:
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
            print("its prime number")
    else:
        print("It is not prime number")
else:
    print("It is not a prime number")