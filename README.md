import pandas as pd
import matplotlib.pyplot as plt
import os

# Get user input for month and year
month = input("Enter the month (MM): ")
year = input("Enter the year (YY): ")

# Validate month and year format
if len(month) != 2 or not month.isdigit() or len(year) != 2 or not year.isdigit():
    print("Invalid input. Please enter the month and year in MM and YY format.")
    exit()

# Define input file name in MM-YY format and output file names
input_file = f'{month}_{year}.csv'
temp_output_file = f'{month}_{year}_temporary.csv'
final_output_file = f'expenses_report_{month}_{year}.xlsx'

print('This is a Bank-app processing the csv from your bank')
print('...processing csv...')

# Processing csv
def process_csv(input_file, temp_output_file):
    # Read the input CSV file
    with open(input_file, 'r', encoding='utf-8') as read_file:
        # Read the first line (header)
        header = read_file.readline().strip()
        # Replace semicolons with commas
        header = header.replace(';', ',')
        # Split the header into columns
        columns = header.split(',')
        # Remove columns at positions 2 and 4
        columns = [col for i, col in enumerate(columns) if i not in [1, 3]]
        # Join the columns back into a line
        new_header = ','.join(columns)

        # Process each line in the file
        with open(temp_output_file, 'w', encoding='utf-8') as write_file:
            write_file.write(new_header + '\n')  # Write the corrected header to the new file

            for line in read_file:
                # Remove quotation marks
                line = line.replace('"', '')
                # Split the line into columns
                columns = line.strip().split(';')
                # Replace commas with full stops in numeric values
                for i, col in enumerate(columns):
                    if i != 1 and i != 3:
                        try:
                            columns[i] = str(float(col.replace(',', '.')))
                        except ValueError:
                            pass
                # Remove 'EUR' and dates (columns 1 and 3)
                columns = [col.strip() if i not in [1, 3] else '' for i, col in enumerate(columns)]
                # Remove empty values
                columns = [col for col in columns if col]
                # Join the columns back into a line
                new_line = ','.join(columns)
                # Write the modified line to the new file
                if any(new_line):
                    write_file.write(new_line + '\n')

# Function to remove quotes
def remove_quotes(input_file):
    with open(input_file, 'r', encoding='utf-8') as file_in:
        content = file_in.read()
        content_without_quotes = content.replace('"', '')
    
    with open(input_file, 'w', encoding='utf-8') as file_out:
        file_out.write(content_without_quotes)

# Process the CSV file
process_csv(input_file, temp_output_file)

# Remove quotes from the processed CSV file
remove_quotes(temp_output_file)

print(f'The temporary file called {temp_output_file} was created')

# Read the CSV file
df = pd.read_csv(temp_output_file)

# Initialize variables to store sums
positive_sum_euros = 0
negative_sum_euros = 0

# Iterate through the volumes to calculate sums
for volume in df['Objem']:
    # Check if the volume is a string and contains a decimal point
    if isinstance(volume, str) and '.' in volume:
        euro, _ = volume.split('.')
        euro = int(euro.replace(',', ''))  # Extract euros and convert to integer
        if euro > 0:
            positive_sum_euros += euro
        elif euro < 0:
            negative_sum_euros += euro
    else:
        if volume > 0:
            positive_sum_euros += volume
        elif volume < 0:
            negative_sum_euros += volume

# Calculate total sum
total_sum_euros = round(positive_sum_euros + negative_sum_euros, 2)

# Create a table
table_data = {
    'Category': ['Profits', 'Expenses', 'Total'],
    'Sum (in Euros)': [positive_sum_euros, negative_sum_euros, total_sum_euros]
}
table_df = pd.DataFrame(table_data)

# Save the processed data and table as Excel
with pd.ExcelWriter(final_output_file) as writer:
    df.to_excel(writer, sheet_name='Data', index=False)
    table_df.to_excel(writer, sheet_name='Summary', index=False)

print(f"Processed data saved as {final_output_file}")

# Delete the temporary CSV file
os.remove(temp_output_file)
print(f"Temporary file {temp_output_file} has been deleted")

# Print the table
print("Table:")
print(table_df)

# Create a bar graph for profits and total
bars = plt.barh(['Profits', 'Expenses', 'Total'], [positive_sum_euros, negative_sum_euros, total_sum_euros], color=['green', 'red', 'lightblue'])
plt.title(f'Expenses and Profits for {month}/{year}', fontsize=16, fontweight='bold')
plt.xlabel('Sum (in Euros)')

# Annotate the bars with their values
for bar, value in zip(bars, [positive_sum_euros, negative_sum_euros, total_sum_euros]):
    if value != 0:  # Only annotate bars with non-zero values
        text_x = bar.get_width() - (0.05 * bar.get_width()) if value > 0 else bar.get_width() + (0.05 * bar.get_width())
        if value > 0:
            text_x = bar.get_width() - 10  # 10 units inside the bar for positive values
        else:
            text_x = bar.get_width() + 10  # 10 units inside the bar for negative values
        plt.text(text_x, bar.get_y() + bar.get_height() / 2, str(round(value, 2)),
                 ha='right' if value > 0 else 'left', va='center', color='black', fontsize=12, weight='bold')

plt.gca().invert_yaxis()  # Invert the y-axis to display profits on top
plt.show()
