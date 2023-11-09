import pandas as pd

##Defining a dictionary
people = {
    'first':['John','Jane','Stephen'],
    'last':['Doe','Doe','Lazarus'],
    'email':['jh_d@example.com','jd_@example.com','sl_@example.com']
}

##Reading the above dictionary as a dataframe
df = pd.DataFrame(people)
print(df)

##Output
#      first     last             email
# 0     John      Doe  jh_d@example.com
# 1     Jane      Doe   jd_@example.com
# 2  Stephen  Lazarus   sl_@example.com

##lets say we wanted everyone with last name 'Doe' from the above dataframe
print(df['last'] == 'Doe')

##Output
# 0     True
# 1     True
# 2    False
# Name: last, dtype: bool