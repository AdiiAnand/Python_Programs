student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_heights = 0
for height in student_heights:
  total_heights += height
print(f"Total Height:", total_heights)

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"Total number of students:",number_of_students)

average_of_students = total_heights/number_of_students
print(f"Average of the heights:", round(average_of_students))