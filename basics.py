#SUM#
spent = 3
donated = 4
total_amount = spent + donated
print(total_amount)

#Multiple#
item = 4
price = 10
total_price = item * price
print(total_price)

#Intergers & String & Floats#
x = 10 #interger#
y = "10" #string#
z= 10.10 #Floats#

sum1 = x + z
sum2 = x + x
sum3 = y + y

print(type(x), type(y), type(z))
print(sum1, sum2, sum3)

#Compound Data Types
#List
Student_Grades = [9, "Hello", 7.5, [1, 2, 4.4]]
print(Student_Grades)

#Math operations with List
#Multiplication repeates the List, increases same list with the multiplication value
#Plus operation don't work as List is not able to perform anything (List + Integer)
#(List + List) it repeates, works as multiplication

Test = Student_Grades * 3
print(Test)

#List_Range(Range Object)
Student_Grades = list(range(0, 11)) #Start from first no. till the prior no of last no. mentioned in the range
print(Student_Grades)

Student_Grades = list(range(0, 11, 2)) #Range(First no., +1 last no., Argument for Plus)
print(Student_Grades)

#dir() gives details about a command, attributes can be performed
#dir(list)
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append',
#  'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#help(str.upper) details about the attribute/function what it does

#dir(__builtins__) all the built in functions

#Mean Value of List
Student_Grades = [9.1, 7.5, 8.8]
Sum_of_grades = sum(Student_Grades)
Length = len(Student_Grades)
Mean = Sum_of_grades / Length
print(Mean)

#Dictonary
Student_Grades = {"A": 9.1, "B": 7.5, "C": 8.8} #Dictionary {"Key": Value} Structure
print(Student_Grades.values())
print(Student_Grades.keys())
#Mean Value of a Dict
Sum_of_grades = sum(Student_Grades.values())
Length = len(Student_Grades)
Mean = Sum_of_grades / Length
print(Mean)

#Tuple
Monday_Temp = (20, 22, 25) #Diff between list and tuple, List are mutable/increased,decreased, Tuple is non mutable/fixed

