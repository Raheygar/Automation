import pandas as pd
##Open the csv file and read it
df = pd.read_csv('data\survey_results_public.csv')
# print(df)

##If we want to see all the columns
columns = pd.set_option('display.max_columns',85)
# print(columns)

##If we want to see first 10 rows of the csv file we will use the "head()" method
print(df.head(10))

##Output
#    Respondent  ...                  SurveyEase
# 0           1  ...  Neither easy nor difficult
# 1           2  ...  Neither easy nor difficult
# 2           3  ...  Neither easy nor difficult
# 3           4  ...                        Easy
# 4           5  ...                        Easy
# 5           6  ...  Neither easy nor difficult
# 6           7  ...  Neither easy nor difficult
# 7           8  ...  Neither easy nor difficult
# 8           9  ...  Neither easy nor difficult
# 9          10  ...                   Difficult

# [10 rows x 85 columns]

##If we want to see last 10 rows of our csv file use "tail()" method
print(df.tail(10))

##Output
#                 SurveyLength                  SurveyEase
# 88873                    NaN                         NaN
# 88874                    NaN                         NaN
# 88875              Too short  Neither easy nor difficult
# 88876  Appropriate in length                        Easy
# 88877              Too short  Neither easy nor difficult
# 88878  Appropriate in length                        Easy
# 88879                    NaN                         NaN
# 88880                    NaN                         NaN
# 88881                    NaN                         NaN
# 88882  Appropriate in length                        Easy