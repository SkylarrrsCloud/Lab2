def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = (weight/(height*height))
    
    print("Your BMI is " + str(bmi))
    if bmi < 18.5:
        print("You are Under weight")
    elif bmi <= 25:
        print("You are Normal weight")
    else:
        print("You are Over weight")

calculate_bmi(weight=57, height=1.73)