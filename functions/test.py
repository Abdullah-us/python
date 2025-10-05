
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
# a=153
# b=2853
# c=398
# print(greatest(a,b,c))



# def c_to(f):
#     return 5*(f-32)/9
# f=int(input("enter tum: "))
# c= c_to(f)
# print(f"{round(c,2)}° C")


# print("a")
# print("b")
# print("c", end="")
# print("d", end="")


# def sum(n):
#         if(n==1):
#                 return 1
#         return sum(n-1)+n
# print(sum(4))


# def star(n):
#     if(n==0):
#         return
#     print("*" * n)
#     star(n-1)


# star(2)


# def to_cm(inch):
#     return inch * 2.54
# n=int(input("Enter the number: "))
# print(to_cm(n) )



n=int(input("Enter a number: "))
for i in range(1,11):
     print(f"{n}*{i}={n*i}")

