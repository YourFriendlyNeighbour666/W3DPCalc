import json
import os

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
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as file:
        return json.load(file)

def save_profiles(profiles, profile_type):
    filename = SETTINGS_FILES[profile_type]
    with open(filename, 'w') as file:
        json.dump(profiles, file, indent=4)

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
def create_printer_profile(global_settings):
    profile_name = input_non_empty_string("Enter a name for the new printer profile: ")
    price = input_float("Enter the purchase price of the printer in $: ")
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
    price_per_1000g = input_float("Enter the price of the material per 1000g in $: ")
    filament_diameter = input_float("Enter the filament diameter in mm: ")
    
    new_material = {
        'name': profile_name,
        'density': density,
        'price_per_1000g': price_per_1000g,
        'filament_diameter': filament_diameter
    }
    return profile_name, new_material

def create_part_profile(material_profiles):
    profile_name = input_non_empty_string("Enter a name for the new part profile: ")
    
    # Ask the user for the unit of volume measurement
    print("Enter the volume of the part:")
    volume_unit = input("Choose the unit (mm3, g, m): ").strip().lower()
    
    if volume_unit == 'mm3':
        volume_mm3 = input_float("Enter the volume of the part in cubic mm: ")
    elif volume_unit == 'g':
        # For volume in grams, we need the density of the material
        material_name = input_non_empty_string("Enter the material name to get its density: ")
        if material_name in material_profiles:
            density = material_profiles[material_name]['density']
            weight_g = input_float("Enter the weight of the part in grams: ")
            volume_mm3 = (weight_g / density) * 1000  # Convert g to cm³ and then to mm³
        else:
            print("Material not found. Please create a material profile first.")
            return None
    elif volume_unit == 'm':
        # For volume in meters, we need the filament diameter from the material profile
        material_name = input_non_empty_string("Enter the material name to get its filament diameter: ")
        if material_name in material_profiles:
            filament_diameter = material_profiles[material_name]['filament_diameter']
            length_m = input_float("Enter the length of the filament in meters: ")
            radius_mm = filament_diameter / 2
            volume_mm3 = length_m * 1000 * 3.14159 * (radius_mm ** 2)  # Convert m to mm and calculate volume
        else:
            print("Material not found. Please create a material profile first.")
            return None
    else:
        print("Invalid unit of volume.")
        return None

    print_time = input_float("Enter the print time in hours: ")
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
def create_profile(profile_type, profiles, global_settings=None):
    if profile_type == 'printers':
        profile_name, profile_data = create_printer_profile(global_settings)
    elif profile_type == 'materials':
        profile_name, profile_data = create_material_profile()
    elif profile_type == 'parts':
        material_profiles = load_profiles('materials')
        if not material_profiles:
            print("No material profiles found. Please create a material profile first.")
            return None
        profile_name, profile_data = create_part_profile(material_profiles)
        if profile_data is None:
            return None
    
    profiles[profile_name] = profile_data
    save_profiles(profiles, profile_type)
    print(f"New {profile_type} profile '{profile_name}' saved.")
    return profile_data

# Function to select or create a profile
def select_or_create_profile(profiles, profile_type, global_settings=None):
    if not profiles:
        print(f"No {profile_type} profiles found. Please create a new one.")
        return create_profile(profile_type, profiles, global_settings)
    
    print(f"Select a {profile_type} profile or create a new one:")
    profile_names = list(profiles.keys())
    for i, profile_name in enumerate(profile_names, 1):
        print(f"{i}: {profile_name}")
    print(f"{len(profiles) + 1}: Create new {profile_type} profile")
    
    choice = input_positive_int(f"Select a number (1-{len(profiles) + 1}): ")
    if 1 <= choice <= len(profiles):
        return profiles[profile_names[choice - 1]]
    elif choice == len(profiles) + 1:
        return create_profile(profile_type, profiles, global_settings)

# Cost calculation function
def calculate_costs(printer, material, part, global_settings):
    volume_cm3 = part['volume_mm3'] / 1000  # Convert mm^3 to cm^3
    weight_g = volume_cm3 * material['density']  # Convert cm^3 to g
    weight_kg = weight_g / 1000  # Convert g to kg
    
    material_cost_per_instance = weight_kg * material['price_per_1000g']
    total_material_cost = material_cost_per_instance * part['instances']
    
    total_print_time = part['print_time'] * part['instances']
    electricity_cost = (total_print_time * printer['power_consumption'] / 1000) * global_settings['electricity_cost_per_kWh']
    depreciation_cost = (printer['price'] / printer['depreciation_time']) * total_print_time
    
    labor_cost = (part['setup_time'] + part['post_processing_time'] * part['instances']) * global_settings['labor_cost_per_hour']
    
    total_cost = total_material_cost + electricity_cost + depreciation_cost + labor_cost
    
    return {
        'material_cost_per_instance': material_cost_per_instance,
        'total_material_cost': total_material_cost,
        'electricity_cost': electricity_cost,
        'depreciation_cost': depreciation_cost,
        'labor_cost': labor_cost,
        'total_cost': total_cost,
        'weight_g_per_instance': weight_g,
        'total_weight_g': weight_g * part['instances']
    }

# Main function
def main():
    global_settings = load_profiles('settings')
    if not global_settings:
        # Default settings
        global_settings = {
            'labor_cost_per_hour': 25.00,  # Default labor cost per hour in $
            'electricity_cost_per_kWh': 0.23  # Default electricity cost per kWh in $
        }
        save_profiles(global_settings, 'settings')
    
    printer_profiles = load_profiles('printers')
    material_profiles = load_profiles('materials')
    part_profiles = load_profiles('parts')
    
    printer_profile = select_or_create_profile(printer_profiles, 'printers', global_settings)
    material_profile = select_or_create_profile(material_profiles, 'materials', global_settings)
    part_profile = select_or_create_profile(part_profiles, 'parts', global_settings)
    
    cost_details = calculate_costs(printer_profile, material_profile, part_profile, global_settings)
    
    # Output the cost details
    print(f"Material Cost per Instance: {cost_details['material_cost_per_instance']} $")
    print(f"Total Material Cost: {cost_details['total_material_cost']} $")
    print(f"Electricity Cost: {cost_details['electricity_cost']} $")
    print(f"Depreciation Cost: {cost_details['depreciation_cost']} $")
    print(f"Weight per Instance: {cost_details['weight_g_per_instance']} g")
    print(f"Total Weight: {cost_details['total_weight_g']} g")
    print(f"Labor Cost: {cost_details['labor_cost']} $")
    print(f"Total Cost: {cost_details['total_cost']} $")

if __name__ == "__main__":
    main()

