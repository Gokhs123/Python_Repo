# Programe to calculate the Average Height of Students from the list of given heights

student_heights = input("Enter the list of student's heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print("\n") 

# With built-in functions 

total_height = sum(student_heights)
print(f"Total Height is {total_height}")
number_of_students = len(student_heights)
print(f"Number of Students are {number_of_students} ")
average = round(total_height/number_of_students)
print(f"The Average (Using Built-in Function) is {average}")
print("^*^"*15)

# Using Loops

print("^*^"*15)

Total_Height = 0
for height in student_heights:
    Total_Height += height
print(f"Total_Height is {Total_Height}")

Number_Of_Students = 0
for students in student_heights:
    Number_Of_Students += 1            # Please Note that the operator is "+=" and not =+
print(f"Number_Of_Students are {Number_Of_Students}")

Average = round(Total_Height/Number_Of_Students)
print(f"The Average (Using Loops) is {Average}")