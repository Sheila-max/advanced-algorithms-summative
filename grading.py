# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# Examples

#  grade = 84 round to 85 (85 - 84 is less than 3)
#  grade = 29 do not round (result is less than 40)
#  grade = 57 do not round (60 - 57 is 3 or higher)

# Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.


import sys
# from array import * 
# import math 

#Function for grading students with the grades parameter
def gradingStudents(grades):
    result = []   #Array of grades

    # Loop through the given grades if it's less than 38, no rounding
    for grade in grades:
        # if the grade is greater than 38 and the next grade is a multiple of 5 is less than 3
        if grade >= 38:
            mod5 = grade % 5

            if mod5 >= 3:    #the next grade is of multiple of 5 is less than 3,
                grade += (5-mod5)  #round grade to the next multiple of 3
        result.append(grade)   #update the grades of the student in the array

    return result

# Output the final grades
print("The original grades are:[73, 67, 38,33] and" , "\n" + "The final grades are ", gradingStudents([73, 67, 38,33]))