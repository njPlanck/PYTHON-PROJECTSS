#the program fouses on calculating the score of lovers using their names
#where surname_m, firstname_f are defined parameters for male and female
surname_m = input(print('Enter your Surname of the boy here\n'))
firstname_m = input(print('Enter your Firstname of the boy here\n'))
surname_f = input(print('Enter your Surname of the girl here\n'))
firstname_f = input(print('Enter your Firstname girl here\n'))
name = surname_m + firstname_m + surname_f + firstname_f
lowercase_name = name.lower()  #name.lower() ensures all names are in lower cases
t = lowercase_name.count('t')  #for people who would begin their name in capital letters
r = lowercase_name.count('r')
u = lowercase_name.count('u')
e = lowercase_name.count('e')
true = t + r + u + e
l = lowercase_name.count('l')
o = lowercase_name.count('o')
v = lowercase_name.count('v')
e = lowercase_name.count('e')
love = l + o + v + e
love_score = str(true) + str(love)
love_score = int(love_score)
print(love_score)

if love_score < 10 or love_score > 90:
    print(f'your love is is {love_score}, you go together coke and mentoes')
elif love_score >= 40 and love_score <= 50:
    print(f'your love is  {love_score}, you are alright together')
else:
    print(f'your love is {love_score}')
    