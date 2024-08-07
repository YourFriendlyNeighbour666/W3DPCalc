# Rusty3Dprint
Wild 3D Print Offline calculator. Terminal based, simplistic calc that lets you estimate filament used weight and costs.Create profiles for printers/filaments/parts etc
This 3D Printing Cost Calculator is a Python script designed to help makers, hobbyists, and small businesses estimate the cost of 3D printing projects. It takes into account various factors such as material, electricity, depreciation of the printer, and labor costs. This tool is open-source and free for everyone to use and contribute to.

# UPDATES
Updated to:
- Rusty3Dprint.py

Inside you will find neat, cleaner version of the code, with few features from "Future updates" included (parts_database is here!)
* including example generated output, you don't have to use those files. If you wish to have a clean instance of script, simply delete every .json file before running the script. 

# Tips for new terminal/python users
Coming soon

# Features

1. Profile Management:
 Create and manage profiles for:
        - printers
        - materials
        - parts 
To quickly calculate costs for different configurations.

2.  Cost Calculation:
Calculate the cost of 3D printing based on material usage, electricity consumption, printer depreciation, and labor.
3.  Material properties:
Add new materials with specific properties like density and price, or select from a list of predefined materials.
4.  Printer Database:
Maintain a database of printer profiles, including purchase price, power consumption, and expected lifetime for accurate depreciation calculation.
5.  Part Specifications:
Define parts with detailed specifications such as volume, print time, setup time, post-processing time, and the number of instances.
6. Batch Processing: 
Calculate costs for printing multiple instances of a part, with setup time added only once.
7. Labor costs:
Include labor costs in the calculation, with the ability to specify different labor rates for setup and post-processing.
8. Electricity costs:
Input the cost of electricity per kWh as a global setting to be used in all calculations.
9. Depreciation Calculation:
Determine the depreciation cost of the printer over its useful life, factored into the total cost of printing.
10. Output Details:
Get detailed breakdowns of costs per instance and for the entire batch, including material, electricity, depreciation, labor, and total costs.
11. Unit Conversion:
Automatically convert between different units of measurement for volume and weight.
12. JSON Storage:
Save and load profiles and settings in JSON format for easy editing and sharing.
13. User-Friendly Input:
Interactive prompts guide the user through the process of creating profiles and calculating costs.


# Future Updates
- Parts Database: Implement a comprehensive database to store and retrieve previously calculated parts for ease of cost estimation in future projects.
-  Enhanced Reporting: Develop advanced reporting features to visualize cost breakdowns and historical data trends.
- API Integration: Integrate with APIs to fetch real-time prices for materials and electricity to keep cost estimations up to date.
- User Interface: Create a web-based interface to allow users to manage profiles and calculate costs without needing to run a Python script.
- Multi-Language Support: Localize the application to support multiple languages, making it accessible to a global audience.
- Customizable Templates: Provide templates for common part profiles and printer settings to streamline the setup process for new users.

# Getting Started
To use the 3D Printing Cost Calculator, clone the repository and run the script in a Python 3 environment:

git clone https://github.com/YourFriendlyNeighbour666/W3DPCalc
cd W3DPCalc-master
python3 W3DPC 0.2.py

Follow the on-screen prompts to create profiles and calculate the cost of your 3D printing projects.
## Customizing Global Settings

The 3D Printing Cost Calculator comes with a set of default global settings that you can easily customize to match your local costs and preferences. These settings include the labor cost per hour and the cost of electricity per kWh, among others.

### Steps to Customize Global Settings:

1. **Locate the Settings File**: Find the `settings.json` file in the root directory of the project. If it doesn't exist, the script will generate one with default values the first time it's run.

2. **Edit the Settings File**: Open the `settings.json` file in a text editor of your choice. You will see a structure similar to this:

    ```json
    {
        "labor_cost_per_hour": 50.00,
        "electricity_cost_per_kWh": 0.23
    }
    ```

3. **Modify the Values**: Change the values to reflect your actual costs. For example, if your electricity cost is 0.23 $ per kWh and your labor cost is 50 $ per hour, you would edit the file to look like this:

    ```json
    {
        "labor_cost_per_hour": 50.00,
        "electricity_cost_per_kWh": 0.23
    }
    ```

4. **Save the File**: After making your changes, save the file and close the text editor.

5. **Run the Calculator**: The next time you run the calculator script, it will use the updated values from the `settings.json` file for all cost calculations.

### Note:

- Ensure that you enter the numerical values correctly, without any currency symbols or commas. The script expects plain numbers (e.g., `60.00` not `60,00 $`).
- If you make a syntax error in the JSON file, the script may not run correctly. If this happens, check the file for missing commas, quotation marks, or braces.

By following these steps, you can tailor the 3D Printing Cost Calculator to more accurately reflect your costs, ensuring that the estimates it provides are as close to your actual expenses as possible.


# Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.




Enjoy :))))
