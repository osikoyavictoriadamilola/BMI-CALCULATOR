def bmi_calculator():
    print("=== BMI CALCULATOR ===")

    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)
        print(f"\nYour BMI: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
            advice = "Eat more protein-rich foods and maintain a balanced diet."
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
            advice = "Great job! Keep eating balanced meals and exercising regularly."
        elif 25 <= bmi < 30:
            category = "Overweight"
            advice = "Add more vegetables and fruits to your diet, and increase physical activity."
        else:
            category = "Obese"
            advice = "Talk to a certified health professional for personalized guidance."

        print(f"Category: {category}")
        print(f"Advice: {advice}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the program
bmi_calculator()
