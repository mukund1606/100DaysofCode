# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

student_num = 0
total = 0
for student_height in student_heights:
  student_num += 1
  total += student_height

avg_height = total / student_num
avg_height = round(avg_height)

print(avg_height)