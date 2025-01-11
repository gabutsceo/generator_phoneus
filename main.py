import os
import random
import json

def generate_us_numbers(quantity, state_code):
    """
    Generate US numbers with a specific state code, including the +1 country code.
    
    Args:
        quantity (int): Number of US numbers to generate.
        state_code (str): The area code for the state.

    Returns:
        list: List of generated US numbers with +1 country code.
    """
    numbers = []
    for _ in range(quantity):
        # Ensure the generated number is 10 digits including the area code
        number = f"+1{state_code}{random.randint(1000000, 9999999):07d}"
        numbers.append(number)
    return numbers

def save_to_file(numbers, folder="results", filename="result.txt"):
    """
    Save the generated numbers to a file.
    
    Args:
        numbers (list): List of generated numbers.
        folder (str): The folder where the file will be saved.
        filename (str): The name of the file to save.
    """
    # Ensure the folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Create the file and write the numbers
    filepath = os.path.join(folder, filename)
    try:
        with open(filepath, "w") as file:
            file.write("\n".join(numbers))
        print(f"Numbers saved to {filepath}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_area_codes(file_path):
    """
    Load area codes and city data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing area codes and cities.

    Returns:
        dict: Dictionary of area codes and their corresponding cities.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")

    try:
        with open(file_path, "r") as file:
            area_codes = json.load(file)
        return area_codes
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file {file_path}: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while loading the file: {e}")

def handle_user_input():
    """
    Handle user input for generating US phone numbers.
    """
    # Ask the user to provide the path to the JSON file
    area_codes_file = input("Please enter the JSON file path for area codes (e.g., california_area_codes.json): ")

    try:
        california_area_codes = load_area_codes(area_codes_file)
    except (FileNotFoundError, ValueError, Exception) as e:
        print(f"Error: {e}")
        exit(1)

    print("Welcome to the US Number Generator for California!")
    try:
        quantity = int(input("How many numbers would you like to generate? "))
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
    except ValueError as e:
        print(f"Invalid input for quantity: {e}")
        exit(1)

    print("Choose an area code:")
    for i, (code, cities) in enumerate(california_area_codes.items(), 1):
        print(f"{i}. {code} (Cities: {', '.join(cities)})")

    try:
        code_index = int(input("Enter the number corresponding to your choice: "))
        if not (1 <= code_index <= len(california_area_codes)):
            raise ValueError("Invalid area code selection.")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    selected_code = list(california_area_codes.keys())[code_index - 1]
    generated_numbers = generate_us_numbers(quantity, selected_code)
    save_to_file(generated_numbers)

if __name__ == "__main__":
    handle_user_input()
