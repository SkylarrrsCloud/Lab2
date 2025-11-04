def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = (weight/(height*height))
    
    print("Your BMI is " + str(bmi))
    if bmi < 18.5:
        print("You are Under weight")
        return -1
    elif bmi <= 25:
        print("You are Normal weight")
        return 0
    else:
        print("You are Over weight")
        return 1

calculate_bmi(weight=57, height=1.73)