import sys, csv
from pyproj import Transformer

def main():
    program_intro()
    settings = input_output_settings()
    output_coords = converter(settings)

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
                print("\n", end="")
                return output_coord_format_prompt
            else:
                print("Invalid input. Please try again...")
        elif output_system == "wgs84":
            output_coord_format_prompt = input("Converting to WGS84 DEGREES or UTM ZONE 50N/51N? (DEG/50N/51N): ").casefold()
            if output_coord_format_prompt in ["deg", "50n", "51n"]:
                print("\n", end="")
                return output_coord_format_prompt
            else:
                print("Invalid input. Please try again...")

def converter(settings):
    EPSG_codes = {
        "prs92,deg":"EPSG:4683",
        "prs92,z1":"EPSG:3121",
        "prs92,z2":"EPSG:3122",
        "prs92,z3":"EPSG:3123",
        "prs92,z4":"EPSG:3124",
        "prs92,z5":"EPSG:3125",
        "wgs84,deg":"EPSG:4326",
        "wgs84,50n":"EPSG:32650",
        "wgs84,51n":"EPSG:32651"
    }
    input_settings = ",".join(settings[0])
    output_settings = ",".join(settings[1])
    transformer = Transformer.from_crs(EPSG_codes.get(input_settings), EPSG_codes.get(output_settings), always_xy=True)
    input_coords = csv_file_checker()
    input_x = []
    input_y = []
    for i, xy in enumerate(input_coords):
        input_x.append(input_coords[i][0])
        input_y.append(input_coords[i][1])
    output_coords = []
    for n in range(len(input_coords)):
        output_coord = transformer.transform(input_x[n], input_y[n])
        output_coords.append(output_coord)
    return output_coords

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
                        sys.exit("Exiting program...")
                        input()
                else:
                    print("Invalid input. Please try again...")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()