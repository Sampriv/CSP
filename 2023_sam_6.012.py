# returning inside the function help from paul

def course_numbers(courses, course):
    if course in courses:
        x = (course, courses[course])
        return x
    else:
        y = 'Does not exist'
        return y


zzz = {'CS2': 'T527',
       'Cybersecurity 2': 'T746',
       'IT2': 'T746',
       'McGlathery': 'M416',
       'AP Computer Science': 'M416',
       'AP Computer Science': 'M416'}

user_input = input("What course are you looking for? ")

print(course_numbers(zzz, user_input))
