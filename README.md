def bmi_calculator():
    print("=== BMI CALCULATOR ===")
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than 0")
            return
        
        bmi = weight / (height ** 2)
        
        print(f"\nYour BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
            advice = "Eat more protein, carbs + healthy fats. See a doctor if too low."
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
            advice = "Great job! Keep eating balanced + exercise."
        elif 25 <= bmi < 30:
            category = "Overweight" 
            advice = "Add more veggies, walk daily, reduce sugary drinks."
        else:
            category = "Obese"
            advice = "Talk to a doctor/nutritionist for a safe plan."
        
        print(f"Category: {category}")
        print(f"Advice: {advice}")
        
    except ValueError:
        print("Please enter numbers only")

bmi_calculator()
