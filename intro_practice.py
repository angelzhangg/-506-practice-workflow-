import pandas as pd
import numpy as np

num_variable = 10
string_variable = "hello world"
my_dict = {
    'age' : '22',
    'firstName' : 'Angela',
    'lastName' : 'Zhang',
    'list' : [1, 2, 3], 
    'nested_dictionary' : {
        'sex' : 'female',
        'race' : 'asian',

    }
}

print("number variables:", num_variable)
print("string variables:", string_variable)
print("dictionaries:", my_dict)


def analyze_bmi(height,weight):

#How to calculate bmi

    bmi = weight / (height**2)
    if bmi < 18.5:
        return f"underweight"
    elif 18.5 <= bmi < 24.9:
        return f"normal"
    else:
        return f"overweight"
    
height_input = 1.78  # height in meters
weight_input = 73    # weight in kilograms
    
bmi_category = analyze_bmi(height_input, weight_input)
print("BMI Category:", bmi_category)

