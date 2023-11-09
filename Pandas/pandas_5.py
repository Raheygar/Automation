import pandas as pd
##Reading first csv
df = pd.read_csv('data\survey_results_public.csv')
##Reading the second csv 
df_schema = pd.read_csv('data\survey_results_schema.csv')
# df.head(10)
# print(df.columns)
##If we wanted to know all the values of an entire column. Example let's figure out what are the values in
##'Hobbyist' column
print(df['Hobbyist'])

##Output
# 0        Yes
# 1         No
# 2        Yes
# 3         No
# 4        Yes
#         ... 
# 88878    Yes
# 88879     No
# 88880     No
# 88881     No
# 88882    Yes
# Name: Hobbyist, Length: 88883, dtype: object

##If we wanted to know number of 'yes' and 'no' in the column 'Hobbyist' using 'value_counts()' method.
print(df['Hobbyist'].value_counts())

##output
# Yes    71257
# No     17626
# Name: Hobbyist, dtype: int64

print(df)

##Looking for a specific rows and columns
print(df.loc[[88878,88879,88880],['BlockchainOrg','LanguageWorkedWith','LanguageDesireNextYear']])
##OUTPUT
#       BlockchainOrg             LanguageWorkedWith                             LanguageDesireNextYear
# 88878           NaN  HTML/CSS;JavaScript;Other(s):  C++;HTML/CSS;JavaScript;SQL;WebAssembly;Other(s):
# 88879           NaN                            NaN                                                NaN
# 88880           NaN                            NaN                                                NaN

##If we wanted to get continous specific rows and columns(consecutively)
print(df.loc[0:10,'Respondent':'OpenSourcer'])
##OUTPUT
#     Respondent                                         MainBranch Hobbyist                 OpenSourcer
# 0            1             I am a student who is learning to code      Yes                       Never
# 1            2             I am a student who is learning to code       No     Less than once per year
# 2            3  I am not primarily a developer, but I write co...      Yes                       Never
# 3            4                     I am a developer by profession       No                       Never
# 4            5                     I am a developer by profession      Yes  Once a month or more often
# 5            6  I am not primarily a developer, but I write co...      Yes                       Never
# 6            7                     I am a developer by profession       No                       Never
# 7            8                        I code primarily as a hobby      Yes     Less than once per year
# 8            9                     I am a developer by profession      Yes  Once a month or more often
# 9           10                     I am a developer by profession      Yes  Once a month or more often
# 10          11                        I code primarily as a hobby      Yes  Once a month or more often

