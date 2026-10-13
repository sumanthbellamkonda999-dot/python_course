#functions

# def greets(name):
#     print("this is sumanth",name)
#     print("i like cricket")

# name="virat kohli"

# greets(name)

# def greets(name):
#     print("hello",name)
# name="sumanth"
# greets(name)

# def greet():
#     print("sumanth")

# greet()

# def greet(name):
#     print("hello",name)
# greet("sumanth")



# def sub(a,b):
#     return a-b

# result = sub(10,4)
# print(result)

# def mul(a,b):
#     return 6*8
# result = mul(6,8)
# print(result)

# def add(a,b):
#     return a+b
# result = add(6,4)
# print(result)


# def add(a,b):
#     return a+b
# result = add(9,5)

# final = result*3
# print(final)

# def square(a):
#     return a*a
# result = square(6)
# print(result)

# def even_is(a):
#     return a % 4 ==0
# print(even_is(8))

# def calculate_average(a,b,c):
#     return (a+b+c)/3
# result = calculate_average(10,7,6)
# print(result)

# def bro(name):
#     print("virat kohli",name)

# bro("anushka")

def calculate_total(marks):
    return sum(marks)

def calculate_average(total,number_of_subjects):
    return total/number_of_subjects

def calculate_grade(average):
    if average >=90:
        return "A"
    elif average >=80:
        return "B"
    elif average >=70:
        return "C"
    elif average >=60:
        return "D"
    else:
        return"F"

def check_result(average):
    if average >=40:
            return "PASS"
    else:
            return "FAIL"


#student details

name = input("Enter your name:")

maths = int(input("Enter maths marks:"))
hindi = int(input("Enter hindi marks:"))
english = int(input("Enter english marks:"))
science = int(input("Enter science marks:"))
telugu = int(input("Enter telugu marks:"))

#marks


# Store marks

marks = [maths,hindi,english,science,telugu]


total = calculate_total(marks)
average = calculate_average(total,len(marks))
grade = calculate_grade(average)
result = check_result(average)

print()
print("======STUDENT PROFILE======")

print("Name", name)
print("Total", total)
print("average", average)
print("Grade", garde)
print("Result", result)

