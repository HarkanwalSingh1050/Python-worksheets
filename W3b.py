import math
#Q12
# class student:
#     def __init__(self,student_name,student_id,student_class):
#         self.student_name = student_name
#         self.student_id = student_id
#         self.student_class = student_class

#     def show(self):
#         print(f"Name : {self.student_name}, ID : {self.student_id}, Class : {self.student_class}")

# std = student("Karman",1024230067,"2W13")
# std.show()

#Q13
# class student:
#     def __init__(self,name,age,r_no):
#         self.name = name
#         self.age = age
#         self.r_no = r_no

# student1 = student("Karman",19,30067)
# student2 = student("Jashan",19,30000)
# print(student1.name,student1.age,student1.r_no)
# print(student2.name,student2.age,student2.r_no)

#Q14
# class circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         arr = math.pi*self.radius**2
#         print(f"Area is : {arr}")

#     def peri(self):
#         per = 2*math.pi*self.radius
#         print(f"Perimeter is : {per}")

# r = int(input("Enter radius : "))
# hp = circle(r)
# hp.area()
# hp.peri()

#Q15
# class str:
#     def get_string(self):
#         self.s = input("Enter a string : ")

#     def print_string(self):
#         print(self.s.upper())

# hp = str()
# hp.get_string()
# hp.print_string()

#Q16
# class robot:
#     def __init__(self,name,task,battery_level):
#         self.name = name
#         self.task = task
#         self.battery_level = battery_level

#     def perform_task(self):
#         self.battery_level = self.battery_level-10
#         print(f"Performing : {self.task}, Battery remaining : {self.battery_level}")

#     def recharge(self):
#         self.battery_level = 100
#         print(f"Battery level : {self.battery_level}")

#     def status(self):
#         print(f"Name : {self.name}, Task : {self.task}, Battery level : {self.battery_level}")

# rbt = robot("Jarvis","Cleaning",50)
# rbt.status()
# rbt.perform_task()
# rbt.recharge()
