print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

t1_count = name1_lower.count('t')
# print(t1_count)
r1_count = name1_lower.count('r')
# print(r1_count)
u1_count = name1_lower.count('u')
# print(u1_count)
e1_count = name1_lower.count('e')
# print(e1_count)

total_true_count1 = t1_count + r1_count + u1_count + e1_count
# print(f"total true count for name1: {total_true_count1}")

l1_count = name1_lower.count('l')
# print(l1_count)
o1_count = name1_lower.count('o')
# print(o1_count)
v1_count = name1_lower.count('v')
# print(v1_count)
e2_count = name1_lower.count('e')
# print(e2_count)

total_love_count1 = l1_count + o1_count + v1_count + e2_count
# print(f"total love count for name1: {total_love_count1}")

t2_count = name2_lower.count('t')
# print(t2_count)
r2_count = name2_lower.count('r')
# print(r2_count)
u2_count = name2_lower.count('u')
# print(u2_count)
e3_count = name2_lower.count('e')
# print(e3_count)

total_true_count2 = t2_count + r2_count + u2_count + e3_count
# print(f"total true count for name2: {total_true_count2}")

l2_count = name2_lower.count('l')
# print(l2_count)
o2_count = name2_lower.count('o')
# print(o2_count)
v2_count = name2_lower.count('v')
# print(v2_count)
e4_count = name2_lower.count('e')
# print(e4_count)

total_love_count2 = l2_count + o2_count + v2_count + e4_count
# print(f"total love count for name2: {total_love_count2}")

total_true_count = total_true_count1 + total_true_count2
total_love_count = total_love_count1 + total_love_count2

love_score = total_true_count*10 + total_love_count
# print(type(love_score))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 or love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
