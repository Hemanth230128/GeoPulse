import pandas as pd

# Load the Excel file
excel_file = 'Book1.xlsx'  # Replace with your .xlsx file path
df = pd.read_excel(excel_file)

# Save as CSV
csv_file = 'mpinew.csv'   # Desired output .csv file path
df.to_csv(csv_file, index=False)

print(f"Converted {excel_file} to {csv_file}")
