print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    
def get_user_input():
    user_input = input("Enter Number: ")
    string_list = user_input.split(",")
    float_list = [float(num) for num in string_list]
    return float_list

def calc_average(num_list):
    print (sum(num_list) / len(num_list))

def find_min_max(num_list):
    print (min(num_list) , max(num_list))

def sort_temperature(num_list):
    print (sorted(num_list))

def calc_median_temperature(num_list):
    n = len(num_list)
    if n == 0:
        return 0.0
    
    sorted_list = sorted(num_list)
    middle = n // 2
    if n % 2 == 0:
        median = ((sorted_list[middle - 1] + sorted_list[middle]) / 2)
        print (median)
    else:
        median = sorted_list[middle]
        print (median)

def calc_average_temperature(num_list):
    total = sum(num_list)
    length = len(num_list)  
    ave = total / length
    print (ave)

def calc_min_max_temperature(num_list):
    min_temp = min(num_list)
    max_temp = max(num_list)
    print (min_temp, max_temp)
    
display_main_menu()
num_list = get_user_input()
calc_average(num_list)
find_min_max(num_list)
sort_temperature(num_list)
calc_median_temperature(num_list)
calc_average_temperature(num_list)
calc_min_max_temperature(num_list)