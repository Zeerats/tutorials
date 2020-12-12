import pandas as pd


all_data = pd.read_csv('../output/all_company_data.csv')
tech_data = all_data[all_data['finnhubIndustry'] == 'Technology'].reset_index()
tech_data.to_csv('../output/tech_company_data.csv')
