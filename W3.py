#Q1
# def fun(n):
#     if n<=17:
#         return 17-n
#     else:
#         return 2*(n-17)
# print(fun(18))

#Q2
# def fun(n):
#     if n in range(100,1001):
#         print("100-1000")
#     elif n in range(1001,2001):
#         print("1001-2000")
#     else:
#         print("NOT IN ANY RANGE!!")
# fun(970)

#Q3
# def fun(n):
#     print(n[::-1])
# a = "i am karman"
# fun(a)

#Q4
# def fun():
#     a= 0
#     b= 0
#     n = input("Enter a string : ")
#     for i in n:
#         if i.isupper():
#             a+=1
#         elif i.islower():
#             b+=1
#     print(f"LOWER : {b}, UPPER : {a}")
# fun()

#Q5
# def fun():
#     l = []
#     for i in range(1,6):
#         a = int(input("Enter number : "))
#         l.append(a)
#     print(list(set(l)))
# fun()

#Q6
# def fun(l):
#     for i in l:
#         if i%2==0:
#             print(i, end=" ")
# sl = [1,2,3,4,5,6,7,8,9]
# fun(sl)

#Q7
# def summ(l):
#     return sum(l)
# def mean(l):
#     s = len(l)
#     return summ(l)/s
# li = [1,2,3,4,5,6]
# print(mean(li))

