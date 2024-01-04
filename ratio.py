import pandas as pd

# Read the Excel file
file_path = 'C:/Users/nalin/OneDrive/Documente/Analysis/final_excell.xlsx'
df = pd.read_excel(file_path)

# Create ratios
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
df['females_ratio'] = df['females']/(df['females']+df['males'])
# Print data after gender ratio calculation
print("Data after gender ratio calculation:")
print(df['females_ratio'])

# Save the DataFrame to a new Excel file
ratio_excel_path = 'C:/Users/nalin/OneDrive/Documente/Analysis/ratio_file.xlsx'
df.to_excel(ratio_excel_path, index=False)
print(f"Excel file saved to: {ratio_excel_path}")