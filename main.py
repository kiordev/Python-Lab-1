# Лабораторная работа №2
# Киор Александр
# 2022
import math

task_number_marker = int(input("Enter number of task: "))

if task_number_marker == 1:
    print("TASK-1 IS ACTIVE")
    num_result = 0;
    num_s = int(input("Enter num S: "))
    num_n = int(input("Enter num N: "))
    if num_s == 0 or num_n == 0: # Проверка на равность нулю вводимых переменных
        print("Num equal ZERO")
    else:
        print("Settings: S - ", num_s, " N: ", num_n)
        print("CALCULATION STARTED")
        if (math.fabs(num_n) / num_n) < num_s and num_s <= math.fabs(num_n):
            num_result = math.sqrt(math.fabs(num_s * math.exp(2) - num_n * math.exp(-2)))
            if math.fabs(num_s * math.exp(2) - num_n * math.exp(-2)) == 0:
                print("MathError: SQRT equal 0")
            else:
                print("Result is: ", num_result)
        elif num_s > math.fabs(num_n):
            num_result = math.sqrt(math.fabs(num_s - num_n)) * math.pow((math.sin(num_s + num_n)), 3)
            print("Result is: ", num_result)
        else:
            print("Exception: wrong condition")

# elif task_number_marker == 2:
# else:
#     print("Wrong Task Number")