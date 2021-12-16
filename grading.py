# Grade rounding function
import sys

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