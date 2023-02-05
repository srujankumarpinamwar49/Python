student_heights = input("Input a list of student heights ").split()
student_heights_len  = len(student_heights)

for n in range(0, student_heights_len):
    student_heights[n] = int(student_heights[n])

total_sum = 0
for average_height in student_heights:
    total_sum += average_height

total_len = 0
for height in student_heights:
    total_len +=1


print(round(total_sum/total_len))


