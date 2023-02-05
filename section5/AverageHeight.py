student_heights = input("Input a list of student heights ").split()
# print (student_heights)

student_heights_len  = len(student_heights)
# print(student_heights_len)

for n in range(0, student_heights_len):
    student_heights[n] = int(student_heights[n])
# print (student_heights)

sum = 0

for average_height in student_heights:
    sum += average_height

print(round(sum/student_heights_len))
