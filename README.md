# US Phone Number Generator

This Python script allows you to generate random US phone numbers based on a selected area code from a provided JSON file. The script is intended for educational purposes, such as generating test data, learning about working with area codes, or creating mock datasets.

### Features:
- Generates random 10-digit US phone numbers (area code + 7-digit number).
- Allows the user to select an area code from a list of available area codes and cities (from a JSON file).
- Saves the generated phone numbers to a file in a specified folder.

---

## Requirements:

- Python 3.x
- A JSON file containing area codes and their corresponding cities.

### Example JSON File (`california_area_codes.json`):
```json
{
    "415": ["San Francisco", "Oakland", "Berkeley"],
    "818": ["Los Angeles", "Glendale", "Burbank"],
    "310": ["Los Angeles", "Santa Monica", "Beverly Hills"]
}


### How to Use:
1. Clone or Download the Repository:
Clone or download the repository to your local machine.

2. Prepare the Area Code JSON File:
You will need to provide a JSON file containing the area codes and corresponding cities. You can either create your own JSON file or use an existing one (e.g., california_area_codes.json).

The JSON file should be structured as follows:

json
Copy code
{
    "area_code": ["City1", "City2", "City3", ...]
}
3. Run the Script:
Open a terminal or command prompt.

Navigate to the folder where you saved the script.

Run the script with the following command:

bash
Copy code
python generator_phoneus.py
4. Input Prompts:
The script will prompt you to provide the following information:

Area Code JSON File: Enter the path to the JSON file containing area codes (e.g., california_area_codes.json).
Quantity: Specify how many phone numbers you want to generate.
Area Code Selection: Choose an area code from the list of available area codes and cities.
5. Generated Numbers:
The script will generate the specified number of phone numbers, each with a valid area code. The numbers will be saved to a file in the results folder (by default, result.txt).
