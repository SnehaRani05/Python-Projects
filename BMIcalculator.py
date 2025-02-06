def calculate_bmi(weight, height, system):
    if system == "Imperial":
        bmi = (weight / (height ** 2)) * 703
    else:  # Metric
        bmi = weight / (height ** 2)
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        return f"{bmi:.2f} - Underweight"
    elif bmi > 25:
        return f"{bmi:.2f} - Overweight"
    else:
        return f"{bmi:.2f} - Healthy"
def BMI():   
    while True:
        choice = input("Which system do you prefer (Imperial/Metric):").capitalize()
        if choice=="Imperial":
            weight = float(input("Enter your weight in lbs: "))
            height_ft = float(input("Enter your height in feet: "))
            height_inch = int(input("Inches:"))
            height = (height_ft*12) + height_inch   #converting height into inches
            bmi = calculate_bmi (weight,height,"Imperial")
            print(classify_bmi(bmi))
            break
                
                    
        elif choice=="Metric":  
            weight = float(input("Enter your weight in kgs: "))
            height = float(input("Enter your height in m: "))
            bmi = calculate_bmi (weight,height,"Metric")
            print(classify_bmi(bmi))
            break
                    
        else:
            print("Invalid response!")
            retry = input("Want to try again? (yes/no): ").lower()
            if retry != "yes":
                print("Goodbye!")
                break
            
BMI()
