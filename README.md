# W3DPCalc
Wild 3D Print Offiline calculator. Basic calc that lets you estimate weight and costs.Create profiles for printers/filaments/parts etc
This 3D Printing Cost Calculator is a Python script designed to help makers, hobbyists, and small businesses estimate the cost of 3D printing projects. It takes into account various factors such as material, electricity, depreciation of the printer, and labor costs. This tool is open-source and free for everyone to use and contribute to.

Features

Profile Management: Create and manage profiles for printers, materials, and parts to quickly calculate costs for different configurations.
Cost Calculation: Calculate the cost of 3D printing based on material usage, electricity consumption, printer depreciation, and labor.
Material Flexibility: Add new materials with specific properties like density and price, or select from a list of predefined materials.
Printer Database: Maintain a database of printer profiles, including purchase price, power consumption, and expected lifetime for accurate depreciation calculation.
Part Specifications: Define parts with detailed specifications such as volume, print time, setup time, post-processing time, and the number of instances.
Batch Processing: Calculate costs for printing multiple instances of a part, with setup time added only once.
Labor Costing: Include labor costs in the calculation, with the ability to specify different labor rates for setup and post-processing.
Electricity Costing: Input the cost of electricity per kWh as a global setting to be used in all calculations.
Depreciation Calculation: Determine the depreciation cost of the printer over its useful life, factored into the total cost of printing.
Output Details: Get detailed breakdowns of costs per instance and for the entire batch, including material, electricity, depreciation, labor, and total costs.
Unit Conversion: Automatically convert between different units of measurement for volume and weight.
JSON Storage: Save and load profiles and settings in JSON format for easy editing and sharing.
User-Friendly Input: Interactive prompts guide the user through the process of creating profiles and calculating costs.
Future Updates

Parts Database: Implement a comprehensive database to store and retrieve previously calculated parts for ease of cost estimation in future projects.
Enhanced Reporting: Develop advanced reporting features to visualize cost breakdowns and historical data trends.
API Integration: Integrate with APIs to fetch real-time prices for materials and electricity to keep cost estimations up to date.
User Interface: Create a web-based interface to allow users to manage profiles and calculate costs without needing to run a Python script.
Multi-Language Support: Localize the application to support multiple languages, making it accessible to a global audience.
Customizable Templates: Provide templates for common part profiles and printer settings to streamline the setup process for new users.
Getting Started

To use the 3D Printing Cost Calculator, clone the repository and run the script in a Python 3 environment:

git clone https://github.com/YourFriendlyNeighbour666/W3DPCalc
cd W3DPCalc-main
python3 PrintCalcv0.1.py

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

- Ensure that you enter the numerical values correctly, without any currency symbols or commas. The script expects plain numbers (e.g., `60.00` not `60,00 zł`).
- If you make a syntax error in the JSON file, the script may not run correctly. If this happens, check the file for missing commas, quotation marks, or braces.

By following these steps, you can tailor the 3D Printing Cost Calculator to more accurately reflect your costs, ensuring that the estimates it provides are as close to your actual expenses as possible.


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request


Enjoy :))))
