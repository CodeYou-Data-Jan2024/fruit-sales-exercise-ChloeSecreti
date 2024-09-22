import pandas as pd

data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

df = pd.DataFrame(data, index=['2017 Sales', '2018 Sales'])

output_file_path = 'fruit.csv'

# Write the DataFrame to a CSV file
df.to_csv(output_file_path)

