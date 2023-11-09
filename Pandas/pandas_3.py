import pandas as pd
##Reading the files :
df = pd.read_csv('data\survey_results_public.csv')
# print(df)
##Reading another csv file:
schema_df = pd.read_csv('data\survey_results_schema.csv')

# pd.set_option('Display.max_columns', 85)
# pd.set_option('Display.max_rows', 85)

print(df.head(10))
