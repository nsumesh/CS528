import pandas as pd
import re
import json

def extract_tensor_values(tensor_str):
    match = re.search(r'tensor\(([\d\.]+)\)', tensor_str)
    if match:
        return float(match.group(1))
    return None

# Load the CSV file
df = pd.read_csv(r'detections.csv')

df['X1'] = df['X1'].apply(extract_tensor_values)
df['Y1'] = df['Y1'].apply(extract_tensor_values)
df['X2'] = df['X2'].apply(extract_tensor_values)
df['Y2'] = df['Y2'].apply(extract_tensor_values)
df['Confidence'] = df['Confidence'].apply(extract_tensor_values)

columns_to_save = ['X1', 'Y1', 'X2', 'Y2', 'Confidence']
for column in columns_to_save:
    json_str = json.dumps(list(df[column].dropna()))
    with open(f'{column}.json', 'w') as file:
        file.write(json_str)
