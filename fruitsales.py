import pandas as pd
fruit.csv = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

fruit_sales = pd.read_csv("fruit.csv")
