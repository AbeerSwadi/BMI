height = float(input("enter your height :"))
weight = float(input("enter your weight :"))


def bmi(height, weight):
    Bmi = weight / (height**2)
    return Bmi


def calculate_bmi(Bmi):
    if Bmi < 18.5:
        print("Underweight")
    elif Bmi > 18.5 and Bmi < 25:
        print("Normal weight")
    else:
        print("Over weight .")


cal = bmi(height, weight)
print(cal)
print(calculate_bmi(cal))
