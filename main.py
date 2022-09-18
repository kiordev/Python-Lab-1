# Лабораторная работа №2
# Киор Александр
# 2022
import math

task_number_marker = int(input("Enter number of task: "))

if task_number_marker == 1:
    print("TASK-1 IS ACTIVE")
    num_result = 0;
    num_s = float(input("Enter num S: "))
    num_n = float(input("Enter num N: "))
    if num_s == 0 or num_n == 0: # Проверка на равность нулю вводимых переменных
        print("Num equal ZERO")
    else:
        print("Settings: S - ", num_s, " N: ", num_n)
        print("CALCULATION STARTED")
        if (math.fabs(num_n) / num_n) < num_s and num_s <= math.fabs(num_n):
            num_result = math.sqrt(math.fabs(num_s * math.exp(2) - num_n * math.exp(-2)))
            print("Result is: ", num_result)
            try: (math.fabs(num_s * math.exp(2) - num_n * math.exp(-2)))/1
            except ZeroDivisionError:
                print("SqrtError result = zero")

        elif num_s > math.fabs(num_n):
            num_result = math.sqrt(math.fabs(num_s - num_n)) * math.pow((math.sin(num_s + num_n)), 3)
            print("Result is: ", num_result)
        else:
            print("Exception: wrong condition")

elif task_number_marker == 2:
    a = 2.5
    num_t = float(input("Enter num t: "))
    f_result = 1;
    if num_t >= 1 and num_t <= 5:
        if num_t>a:
            f_result = math.pow(num_t,3)*math.pow(num_t-a, (1/3))
            print("Result is: ", f_result)
        elif num_t == a:
            f_result = num_t*math.sin(a)*num_t
            print("Result is: ", f_result)
        elif num_t < a:
            f_result = math.exp(-a*num_t)*math.cos(a)*num_t
            print("Result is: ", f_result)
    else:
        print("T num is out of border")
else:
    print("Error: Wrong Task Number")

