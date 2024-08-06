import json
import os
import math
import logging

# Initialize logging
logging.basicConfig(filename='profile_manager.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for the settings files
SETTINGS_FILES = {
    'printers': 'printer_profiles.json',
    'materials': 'material_profiles.json',
    'parts': 'part_profiles.json',
    'settings': 'global_settings.json',
    'database': 'parts_database.json'
}

# Utility functions
def load_profiles(profile_type):
    filename = SETTINGS_FILES[profile_type]
    try:
        if not os.path.exists(filename):
            return {}
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Failed to load {profile_type} profiles: {e}")
        return {}

def save_profiles(profiles, profile_type):
    filename = SETTINGS_FILES[profile_type]
    try:
        with open(filename, 'w') as file:
            json.dump(profiles, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to save {profile_type} profiles: {e}")

def input_float(prompt, min_value=0.0):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                raise ValueError(f"Value must be at least {min_value}.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def input_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Please enter a positive integer.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")

def input_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty.")

# Profile creation functions
def create_printer_profile():
    profile_name = input_non_empty_string("Enter a name for the new printer profile: ")
    price = input_float("Enter the purchase price of the printer in zł: ")
    depreciation_time = input_float("Enter the depreciation time of the printer in hours: ")
    power_consumption = input_float("Enter the power consumption of the printer in watts: ")
    
    new_printer = {
        'name': profile_name,
        'price': price,
        'depreciation_time': depreciation_time,
        'power_consumption': power_consumption
    }
    return profile_name, new_printer

def create_material_profile():
    profile_name = input_non_empty_string("Enter a name for the new material profile: ")
    density = input_float("Enter the density of the material in g/cm^3: ")
    price_per_1000g = input_float("Enter the price of the material per 1000g in zł: ")
    filament_diameter_mm = input_float("Enter the filament diameter in mm: ")
    
    new_material = {
        'name': profile_name,
        'density': density,
        'price_per_1000g': price_per_1000g,
        'filament_diameter_mm': filament_diameter_mm
    }
    return profile_name, new_material

def create_part_profile(material_profile):
    profile_name = input_non_empty_string("Enter a name for the new part profile: ")
    volume_unit = input("Enter the unit of volume (mm3, g, m): ").strip().lower()
    volume_mm3 = None

    if volume_unit == 'mm3':
        volume_mm3 = input_float("Enter the volume of the part in cubic mm: ")
    elif volume_unit == 'g':
        weight_g = input_float("Enter the weight of the part in grams: ")
        volume_mm3 = (weight_g / material_profile['density']) * 1000
    elif volume_unit == 'm':
        length_m = input_float("Enter the length of the filament in meters: ")
        filament_radius_mm = material_profile['filament_diameter_mm'] / 2
        volume_mm3 = math.pi * (filament_radius_mm ** 2) * (length_m * 1000)
    else:
        print("Invalid unit. Defaulting to cubic millimeters (mm3).")
        volume_mm3 = input_float("Enter the volume of the part in cubic mm: ")

    time_unit = input("Enter the unit for print time (hours/minutes): ").strip().lower()
    if time_unit not in ['hours', 'minutes']:
        print("Invalid unit for print time. Please enter 'hours' or 'minutes'.")
        return None

    print_time = input_float(f"Enter the print time in {time_unit}: ")
    if time_unit == 'minutes':
        print_time /= 60  # Convert minutes to hours

    setup_time = input_float("Enter the setup time in hours: ")
    post_processing_time = input_float("Enter the post-processing time in hours: ")
    instances = input_positive_int("Enter the number of instances: ")
    
    new_part = {
        'name': profile_name,
        'volume_mm3': volume_mm3,
        'print_time': print_time,
        'setup_time': setup_time,
        'post_processing_time': post_processing_time,
        'instances': instances
    }
    return profile_name, new_part

# Main profile creation function
def create_profile(profile_type, material_profile=None):
    if profile_type == 'printers':
        profile_name, profile_data = create_printer_profile()
    elif profile_type == 'materials':
        profile_name, profile_data = create_material_profile()
    elif profile_type == 'parts':
        profile_name, profile_data = create_part_profile(material_profile)
    
    profiles = load_profiles(profile_type)
    profiles[profile_name] = profile_data
    save_profiles(profiles, profile_type)
    print(f"New {profile_type} profile '{profile_name}' saved.")
    return profile_data

def select_or_create_profile(profiles, profile_type, material_profile=None):
    if not profiles:
        print(f"No {profile_type} profiles found. Please create a new one.")
        return create_profile(profile_type, material_profile)
    
    print(f"Select a {profile_type} profile or create a new one:")
    profile_names = list(profiles.keys())
    for i, profile_name in enumerate(profile_names, 1):
        print(f"{i}: {profile_name}")
    print(f"{len(profiles) + 1}: Create new {profile_type} profile")
    
    while True:
        try:
            choice = input_positive_int(f"Select a number (1-{len(profiles) + 1}): ")
            if 1 <= choice <= len(profiles):
                return profiles[profile_names[choice - 1]]
            elif choice == len(profiles) + 1:
                return create_profile(profile_type, material_profile)
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice, please try again.")

# Cost calculation function
def calculate_costs(printer, material, part, global_settings):
    volume_cm3 = part['volume_mm3'] / 1000
    weight_g = volume_cm3 * material['density']
    weight_kg = weight_g / 1000
    
    material_cost_per_instance = (weight_g / 1000) * material['price_per_1000g']
    total_material_cost = material_cost_per_instance * part['instances']
    
    total_print_time = part['print_time'] * part['instances']
    electricity_cost = (total_print_time * printer['power_consumption'] / 1000) * global_settings['electricity_cost_per_kWh']
    depreciation_cost = (printer['price'] / printer['depreciation_time']) * total_print_time
    
    labor_cost = (part['setup_time'] + part['post_processing_time'] * part['instances']) * global_settings['labor_cost_per_hour']
    
    total_cost = total_material_cost + electricity_cost + depreciation_cost + labor_cost
    
    return {
        'material_cost_per_instance': round(material_cost_per_instance, 2),
        'total_material_cost': round(total_material_cost, 2),
        'electricity_cost': round(electricity_cost, 2),
        'depreciation_cost': round(depreciation_cost, 2),
        'weight_g_per_instance': round(weight_g, 2),
        'total_weight_g': round(weight_g * part['instances'], 2),        
        'labor_cost': round(labor_cost, 2),
        'total_cost': round(total_cost, 2)

    }

# Function to save the cost calculation to the database
def save_to_database(part_name, cost_details):
    database = load_profiles('database') or {}
    database[part_name] = cost_details
    save_profiles(database, 'database')

# Main function
def main():
    try:
        global_settings = load_profiles('settings')
        if not global_settings:
            global_settings = {
                'labor_cost_per_hour': 50.00,
                'electricity_cost_per_kWh': 0.86
            }
            save_profiles(global_settings, 'settings')
        
        printer_profiles = load_profiles('printers')
        material_profiles = load_profiles('materials')
        
        printer_profile = select_or_create_profile(printer_profiles, 'printers')
        material_profile = select_or_create_profile(material_profiles, 'materials')
        part_profile = select_or_create_profile(load_profiles('parts'), 'parts', material_profile)
        
        cost_details = calculate_costs(printer_profile, material_profile, part_profile, global_settings)

        # Output the cost details
        print(f"Material Cost per Instance: {cost_details['material_cost_per_instance']} zł")
        print(f"Total Material Cost: {cost_details['total_material_cost']} zł")
        print(f"Electricity Cost: {cost_details['electricity_cost']} zł")
        print(f"Depreciation Cost: {cost_details['depreciation_cost']} zł")
        print(f"Weight per Instance: {cost_details['weight_g_per_instance']} g")
        print(f"Total Weight: {cost_details['total_weight_g']} g")
        print(f"Labor Cost: {cost_details['labor_cost']} zł")
        print(f"Total Cost: {cost_details['total_cost']} zł")

        # Ask user if they want to save the cost details to the database
        save_to_db = input("Do you want to save the cost details to the database? (yes/no): ").lower()
        if save_to_db == 'yes':
            save_to_database(part_profile['name'], cost_details)
            print("Cost details saved to the database.")

        logging.info("Script executed successfully.")
    except Exception as e:
        logging.exception("An error occurred")

if __name__ == "__main__":
    main()
