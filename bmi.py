def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight/(height*height)

    print(BMI)
    if (BMI < 18.5):
        print("Under weight")
    elif (18.5 <= BMI <= 25):
        print("Normal weight")
    else:
        print("Over weight")

calculate_bmi(weight=57,height=1.73)

