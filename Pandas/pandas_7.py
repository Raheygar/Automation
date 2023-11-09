import pandas as pd
##Reading the first csv file into a dataframe 
df = pd.read_csv('data\survey_results_public.csv',index_col='Respondent')
##Reading the second csv file into another dataframe
df_schema = pd.read_csv('data\survey_results_schema.csv',index_col='Column')
df.head(5)
print(df)
print(df_schema)

##Output
#        Respondent                                         MainBranch  ...           SurveyLength                  SurveyEase
# 0               1             I am a student who is learning to code  ...  Appropriate in length  Neither easy nor difficult
# 1               2             I am a student who is learning to code  ...  Appropriate in length  Neither easy nor difficult
# 2               3  I am not primarily a developer, but I write co...  ...  Appropriate in length  Neither easy nor difficult
# 3               4                     I am a developer by profession  ...  Appropriate in length                        Easy
# 4               5                     I am a developer by profession  ...  Appropriate in length                        Easy
# ...           ...                                                ...  ...                    ...                         ...
# 88878       88377                                                NaN  ...  Appropriate in length                        Easy
# 88879       88601                                                NaN  ...                    NaN                         NaN
# 88880       88802                                                NaN  ...                    NaN                         NaN
# 88881       88816                                                NaN  ...                    NaN                         NaN
# 88882       88863                                                NaN  ...  Appropriate in length                        Easy

# [88883 rows x 85 columns]

##From the above output we want to clear the df a little bit and have Index set to Respondent column
##We can acheive it by inserting an argument when reading the dataframe in line 3 pass the 'index_col'
## and specify the column name in it.

print(df)

##Output
#                                                    MainBranch Hobbyist  ...           SurveyLength                  SurveyEase
# Respondent                                                              ...
# 1                      I am a student who is learning to code      Yes  ...  Appropriate in length  Neither easy nor difficult
# 2                      I am a student who is learning to code       No  ...  Appropriate in length  Neither easy nor difficult
# 3           I am not primarily a developer, but I write co...      Yes  ...  Appropriate in length  Neither easy nor difficult
# 4                              I am a developer by profession       No  ...  Appropriate in length                        Easy
# 5                              I am a developer by profession      Yes  ...  Appropriate in length                        Easy
# ...                                                       ...      ...  ...                    ...                         ...
# 88377                                                     NaN      Yes  ...  Appropriate in length                        Easy
# 88601                                                     NaN       No  ...                    NaN                         NaN
# 88802                                                     NaN       No  ...                    NaN                         NaN
# 88816                                                     NaN       No  ...                    NaN                         NaN
# 88863                                                     NaN      Yes  ...  Appropriate in length                        Easy

# [88883 rows x 84 columns]

##Sorting the indexes of each csv sheet
print(df.sort_index())          ##It is temporary but to make it permanent use "inplace=True"
print(df_schema.sort_index())

##Output
#                                                    MainBranch  ...                  SurveyEase
# Respondent                                                     ...
# 1                      I am a student who is learning to code  ...  Neither easy nor difficult       
# 2                      I am a student who is learning to code  ...  Neither easy nor difficult       
# 3           I am not primarily a developer, but I write co...  ...  Neither easy nor difficult       
# 4                              I am a developer by profession  ...                        Easy       
# 5                              I am a developer by profession  ...                        Easy       
# ...                                                       ...  ...                         ...       
# 88879                          I am a developer by profession  ...                        Easy       
# 88880       I am not primarily a developer, but I write co...  ...                         NaN       
# 88881                          I am a developer by profession  ...                        Easy       
# 88882                          I am a developer by profession  ...                        Easy       
# 88883                          I am a developer by profession  ...                        Easy       

# [88883 rows x 84 columns]
#                                                     QuestionText
# Column
# Age            What is your age (in years)? If you prefer not...
# Age1stCode     At what age did you write your first line of c...
# BetterLife     Do you think people born today will have a bet...
# BlockchainIs   Blockchain / cryptocurrency technology is prim...
# BlockchainOrg  How is your organization thinking about or imp...
# ...                                                          ...
# WorkPlan                 How structured or planned is your work?
# WorkRemote                       How often do you work remotely?
# WorkWeekHrs     On average, how many hours per week do you work?
# YearsCode      Including any education, how many years have y...
# YearsCodePro   How many years have you coded professionally (...

# [85 rows x 1 columns]