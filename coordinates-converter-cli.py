import sys, csv
from pyproj import Transformer

def main():
    program_intro()
    input_output_settings()

def program_intro():
    print("CBA's COORDINATES CONVERTER - PYTHON3")
    print("CONVERTS PRS92 COORDINATES TO WGS84 (AND VICE VERSA) - PLEASE SEE THE README FOR USER INSTRUCTIONS.\n")

def input_output_settings():
    input_system = input_coord_system()
    input_format = input_coord_format(input_system)

def input_coord_system():
    while True:
        input_coord_system_prompt = input("Converting from PRS92 or WGS84? (PRS92/WGS84): ").casefold()
        if input_coord_system_prompt in ["prs92", "wgs84"]:
            return input_coord_system_prompt
        else:
            print("Invalid input. Please try again...")

def input_coord_format(input_system):
    while True:
        if input_system == "prs92":
            input_coord_format_prompt = input("Converting from PRS92 DEGREES, ZONE 1, ZONE 2, ZONE 3, ZONE 4, or ZONE 5? (DEG/Z1/Z2/Z3/Z4/Z5): ").casefold()
            if input_coord_format_prompt in ["deg", "z1", "z2", "z3", "z4", "z5"]:
                return input_coord_format_prompt
            else:
                print("Invalid input. Please try again...")
        elif input_system == "wgs84":
            input_coord_format_prompt = input("Converting from WGS84 DEGREES or UTM ZONE 50N/51N? (DEG/50N/51N): ").casefold()
            if input_coord_format_prompt in ["deg", "50n", "51n"]:
                return input_coord_format_prompt
            else:
                print("Invalid input. Please try again...")        

if __name__ == "__main__":
    main()