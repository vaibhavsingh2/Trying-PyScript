import arrr
from pyscript import document

import random
import string
'''
# List to store dictionaries with unique alphanumeric codes and question data
saved_code_list = []

# Function to generate a random 5-character alphanumeric code
def generate_random_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
'''
# Function to add the current form data to saved_code_list and display the code
def createrandomcode():
    print("Hi")
'''
    # Generate a unique alphanumeric code
    random_code = generate_random_code()

    # Access values from the form inputs
    question_data = {
        "Q1": [document.getElementById("O1").value,
               document.getElementById("O2").value,
               document.getElementById("O3").value,
               document.getElementById("O4").value],
        "Q2": [document.getElementById("P1").value,
               document.getElementById("P2").value,
               document.getElementById("P3").value,
               document.getElementById("P4").value],
        "Q3": [document.getElementById("R1").value,
               document.getElementById("R2").value,
               document.getElementById("R3").value,
               document.getElementById("R4").value]
    }

    # Create the dictionary with the generated code as the key
    form_data = {random_code: question_data}

    # Add the dictionary to saved_code_list
    saved_code_list.append(form_data)

    # Display the generated code in the HTML
    document.getElementById("generatedCode").innerHTML = f"Form submitted! Your code is: <b>{random_code}</b>"

    # Optional: return the code if you want to use it further
    return random_code'''
