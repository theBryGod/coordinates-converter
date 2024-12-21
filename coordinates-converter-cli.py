import sys, csv
from pyproj import Transformer

def main():
    program_intro()
    input_output_settings()
    csv_file_checker()

def program_intro():
    print("CBA's COORDINATES CONVERTER - PYTHON3")
    print("CONVERTS PRS92 COORDINATES TO WGS84 (AND VICE VERSA) - PLEASE SEE THE README FOR USER INSTRUCTIONS.\n")

def input_output_settings():
    input_system = input_coord_system()
    input_format = input_coord_format(input_system)
    output_system = output_coord_system()
    output_format = output_coord_format(output_system)
    return [(input_system, input_format), (output_system, output_format)]

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
                print("\n", end="")
                return input_coord_format_prompt
            else:
                print("Invalid input. Please try again...")
        elif input_system == "wgs84":
            input_coord_format_prompt = input("Converting from WGS84 DEGREES or UTM ZONE 50N/51N? (DEG/50N/51N): ").casefold()
            if input_coord_format_prompt in ["deg", "50n", "51n"]:
                print("\n", end="")
                return input_coord_format_prompt
            else:
                print("Invalid input. Please try again...")

def output_coord_system():
    while True:
        output_coord_system_prompt = input("Converting to PRS92 or WGS84? (PRS92/WGS84): ").casefold()
        if output_coord_system_prompt in ["prs92", "wgs84"]:
            return output_coord_system_prompt
        else:
            print("Invalid input. Please try again...")

def output_coord_format(output_system):
    while True:
        if output_system == "prs92":
            output_coord_format_prompt = input("Converting to PRS92 DEGREES, ZONE 1, ZONE 2, ZONE 3, ZONE 4, or ZONE 5? (DEG/Z1/Z2/Z3/Z4/Z5): ").casefold()
            if output_coord_format_prompt in ["deg", "z1", "z2", "z3", "z4", "z5"]:
                return output_coord_format_prompt
            else:
                print("Invalid input. Please try again...")
        elif output_system == "wgs84":
            output_coord_format_prompt = input("Converting to WGS84 DEGREES or UTM ZONE 50N/51N? (DEG/50N/51N): ").casefold()
            if output_coord_format_prompt in ["deg", "50n", "51n"]:
                return output_coord_format_prompt
            else:
                print("Invalid input. Please try again...")

def csv_file_checker():
    while True:
        try:
            filename = input("Please input the filename of the CSV containing the coordinates: ")
            if not filename.endswith(".csv"):
                raise ValueError("Invalid input. Please try again...")
            input_coordinates = []
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    input_coordinates.append(row)
            return input_coordinates
        except FileNotFoundError:
            while True:
                fnf_prompt = input("File not found. Please make sure that the CSV file is in the same folder as the program. Try again? (Y/N): ").casefold()
                if fnf_prompt in ["y", "n"]:
                    if fnf_prompt == "y":
                        return csv_file_checker()
                    else:
                        sys.exit("Exiting program. Press Enter to exit...")
                else:
                    print("Invalid input. Please try again...")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()