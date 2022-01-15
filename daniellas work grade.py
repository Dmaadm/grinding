def testWeekend(date):
    # Successfully tests for "S" in "Sat" and "Sun"
    return date[0].upper() == 'S'

def pesterStudent():
    # Accepts incorrect format as testWeekend doesn't depend on format.
    if testWeekend(input("What is the date? (In 3 letter format)")):
        print("Hooray - it's the weekend!")
    else:
        print("Haha - get back to work.")

# Input: "Sat"


# Input: "Wed"
pesterStudent()


"""
this is a very profecional script 
i can see your enthusiasime to coding 
very impresve to have analised the days of the week and reaise the days of the weekend start with an S
very smart to have done a sneeky test in the inithial function
i can see something in you young wamen
NOW


NEXT ASSIGNEMENT:
    make a pi calculator 
        it must demonstrate how to calculate pi using turtle
        
        
due date: 27th of january 2022
"""


_aGrades = [(80, 'A'),(70, 'B'),(60, 'C'),(50, 'D'),(0, 'U')]
_mGrades = [(80, 'Excellent result', 'Not bad.'),(70, 'Very good', 'You tried'),(60, 'Good effort', 'Disappointed in you'),(50, 'You achieved a Pass', 'Hope you like the salary of a McDonalds worker :)'),(0, 'Would you like to book a retake?', 'Signed you up for a psych evalutation.')]

# No longer uses ranges nor if abuse.
def alphaGrade(num):
    return [alph for min, alph in _aGrades if num >= min][0]

# We've gone over this, your pessissimistic AI proposition was denied.
def msgGrade(num, pessimism):
    return [(pess if pessimism else msg) for min, msg, pess in _mGrades if num >= min][0]

grade = eval(input("What was your grade?"));

# Please stop changing pessimism to True.
print(str(grade) + " | Grade: " + alphaGrade(grade) + " | Teacher's 'Comments': " + msgGrade(grade, True))

print(str(grade) + " | Grade: " + alphaGrade(grade) + " | Teacher's Comments: " + msgGrade(grade, False))

"""
this is an exelent and lovely code to demonstrate my proudness of you.
i am very proud of you daniella you have demonstrated how good of a programer you are countless times 
and i will definitly steal your code 
don't be a naughty girl.
REMENMBER I KNOW WHEN YOU'RE NAUGHTY
I AM ALWAYS WATCHING
also my favourit lines were the 50 those made me laught
nice work!

in conclution you're over all grade is a 19/20 since i know you can do better since YOU ARE LITURALY PROGRAMING A NUKE YOU HAVE PROGRAMED GAMES AND WHY NOT PROGRAME WAMEN?
also i might work with robots on my next NSI project!

LOVE, MIRIAM THE PYTHON PROFETIONAL
"""