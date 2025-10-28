print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    user_input = input("Enter Number: ")
    string_list = user_input.split(",")
    float_list = [float(num) for num in string_list]
    return float_list
def calc_average():
    print("calc_average")
def find_min_max():
    print("find_min_max")
def sort_temperature():
    print("sort_temperature")
def calc_median_temperature():
    print("calc_median_temperature")