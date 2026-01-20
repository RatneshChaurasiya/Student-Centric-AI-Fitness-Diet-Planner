def calculate_bmi(weight_kg, height_cm):
    """Calculates BMI given weight in kg and height in cm."""
    if height_cm <= 0:
        return 0
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)

def get_bmi_category(bmi):
    """Returns the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
