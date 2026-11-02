print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height,weight):
    print("value of height is: ", height)
    print("value of wight is: ", weight)
    
    bmi = weight / (height*height)
    print("value of bmi is: ", bmi)
    if bmi <18.5:
        print("BMI is underweight")
        value = -1
    
    elif bmi >= 18.5 and bmi <25:
        print("BMI is acceptable")
        value=0
    else:   
        print("BMI is overweight")
        value=1
    print("BMI output is: ", bmi)
    return bmi, value

    
bmi_oaASSASASutput = calculate_bmi(1.72,65)



   

    