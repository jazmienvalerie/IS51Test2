"""
Laymen's terms (structure english)

The program will use Final.txt to determine and display the following.
It will display the number of grades. It will also display the average grade.
Lastly, it will display the percentage of grades that are higher than the average grade.

We will use the numbers in Final.txt to calculate the percentage of grades that 
are above the average grade. 

Num_of_grades will be 24.
Average_grade will be 83.25

Percentage_of_grades_above_average will be 54.17%

Add all 24 grades to find the sum.
Divide the sum by 24 (number of grades).
The given output will display the overall average. 

Add all grades that are higher than the average. 
Divide the sum by 100.
The given output will display the percentage of grades that are 
above the average grade.

"""

"""
# function1 
main() to start up the application
return sum / 24 


#function2
calculate_percent_above_average()
sum of higher grades above average divided by average grade (83.25)
multiply by 100 to output percent

"""

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t 
    avg = sum_num / len(num)
    return avg
print ("The average is", cal_average([78,67,56,99,80,83,82,91,94,95,77,88,85,92,91,79,88,82,81,86,94,93,92,45]))

num= 78,67,56,99,80,83,82,91,94,95,77,88,85,92,91,79,88,82,81,86,94,93,92,45
print (len(num))


def cal_average(num2):
    sum_num2 = 0
    for t in num2:
        sum_num2 = sum_num2 + t
    avg= sum_num2 / len(num2)
    return avg
print ("The average is", cal_average ([99,91,94,95,88,85,92,91,88,86,94,93,92]))

num2= 99,91,94,95,88,85,92,91,88,86,94,93,92


avg2=(1998 / 1188)
print("The percentage of grades that are above the average grade is", (avg2*100))






