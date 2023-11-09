import pandas as pd
##Lets open the csv file and read it
df = pd.read_csv('data\survey_results_public.csv')
##Print after reading the data
print(df)
#Output is displayed in a concise manner:
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



##Let's print the number of rows and column just like the numpy library
print(df.shape)
##Output
# (88883, 85)

##Gathering information of the file using the info() method
print(df.info())
##Output
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 88883 entries, 0 to 88882
# Data columns (total 85 columns):
#  #   Column                  Non-Null Count  Dtype
# ---  ------                  --------------  -----
#  0   Respondent              88883 non-null  int64
#  1   MainBranch              88331 non-null  object
#  2   Hobbyist                88883 non-null  object
#  3   OpenSourcer             88883 non-null  object
#  4   OpenSource              86842 non-null  object
#  5   Employment              87181 non-null  object
#  6   Country                 88751 non-null  object
#  7   Student                 87014 non-null  object
#  8   EdLevel                 86390 non-null  object
#  9   UndergradMajor          75614 non-null  object
#  10  EduOther                84260 non-null  object
#  11  OrgSize                 71791 non-null  object
#  12  DevType                 81335 non-null  object
#  13  YearsCode               87938 non-null  object
#  14  Age1stCode              87634 non-null  object
#  15  YearsCodePro            74331 non-null  object
#  16  CareerSat               72847 non-null  object
#  17  JobSat                  70988 non-null  object
#  18  MgrIdiot                61159 non-null  object
#  19  MgrMoney                61157 non-null  object
#  20  MgrWant                 61232 non-null  object
#  21  JobSeek                 80555 non-null  object
#  22  LastHireDate            79854 non-null  object
#  23  LastInt                 67155 non-null  object
#  24  FizzBuzz                71344 non-null  object
#  25  JobFactors              79371 non-null  object
#  26  ResumeUpdate            77877 non-null  object
#  27  CurrencySymbol          71392 non-null  object
#  28  CurrencyDesc            71392 non-null  object
#  29  CompTotal               55945 non-null  float64
#  30  CompFreq                63268 non-null  object
#  31  ConvertedComp           55823 non-null  float64
#  32  WorkWeekHrs             64503 non-null  float64
#  33  WorkPlan                68914 non-null  object
#  34  WorkChallenge           68141 non-null  object
#  35  WorkRemote              70284 non-null  object
#  36  WorkLoc                 70055 non-null  object
#  37  ImpSyn                  71779 non-null  object
#  38  CodeRev                 70390 non-null  object
#  39  CodeRevHrs              49790 non-null  float64
#  40  UnitTests               62668 non-null  object
#  41  PurchaseHow             61108 non-null  object
#  42  PurchaseWhat            62029 non-null  object
#  43  LanguageWorkedWith      87569 non-null  object
#  44  LanguageDesireNextYear  84088 non-null  object
#  45  DatabaseWorkedWith      76026 non-null  object
#  46  DatabaseDesireNextYear  69147 non-null  object
#  47  PlatformWorkedWith      80714 non-null  object
#  48  PlatformDesireNextYear  77443 non-null  object
#  49  WebFrameWorkedWith      65022 non-null  object
#  50  WebFrameDesireNextYear  62944 non-null  object
#  51  MiscTechWorkedWith      59586 non-null  object
#  52  MiscTechDesireNextYear  64511 non-null  object
#  53  DevEnviron              87317 non-null  object
#  54  OpSys                   87851 non-null  object
#  55  Containers              85366 non-null  object
#  56  BlockchainOrg           48175 non-null  object
#  57  BlockchainIs            60165 non-null  object
#  58  BetterLife              86269 non-null  object
#  59  ITperson                87141 non-null  object
#  60  OffOn                   86663 non-null  object
#  61  SocialMedia             84437 non-null  object
#  62  Extraversion            87305 non-null  object
#  63  ScreenName              80486 non-null  object
#  64  SOVisit1st              83877 non-null  object
#  65  SOVisitFreq             88263 non-null  object
#  66  SOVisitTo               88086 non-null  object
#  67  SOFindAnswer            87816 non-null  object
#  68  SOTimeSaved             86344 non-null  object
#  69  SOHowMuchTime           68378 non-null  object
#  70  SOAccount               87828 non-null  object
#  71  SOPartFreq              74692 non-null  object
#  72  SOJobs                  88066 non-null  object
#  73  EntTeams                87841 non-null  object
#  74  SOComm                  88131 non-null  object
#  75  WelcomeChange           85855 non-null  object
#  76  SONewContent            69560 non-null  object
#  77  Age                     79210 non-null  float64
#  78  Gender                  85406 non-null  object
#  79  Trans                   83607 non-null  object
#  80  Sexuality               76147 non-null  object
#  81  Ethnicity               76668 non-null  object
#  82  Dependents              83059 non-null  object
#  83  SurveyLength            86984 non-null  object
#  84  SurveyEase              87081 non-null  object
# dtypes: float64(5), int64(1), object(79)
# memory usage: 57.6+ MB
# None