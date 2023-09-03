# program to find the average height of the students.

students_height = [180, 124, 165, 173, 189, 169, 146]

sum = 0
count = 0

for i in students_height:
    sum += i
    count += 1

average = round(sum/count)

print(average)
# program to illustrate the highest score in the class.

student_scores = [78, 65, 89, 80, 70, 90]

# using a for loop we will iterate through the list and will save the max number.

max_num = 0

for i in student_scores:
    if i > max_num:
        max_num = i


print(max_num)
