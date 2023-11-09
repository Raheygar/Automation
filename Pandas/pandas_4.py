import pandas as pd

##Let us declare a dictionary
people = {
             'first':['John','Jane','Rachel'],
             'last': ['Davis','Doe','Dawson'],
             'email': ['john_davis@example.com','jane_doe@example.com','r_dawson@example.com']
}


##We want to create a dataframe for the dictionary above. Below id the step
df = pd.DataFrame(people)
print(df)

##Output
#     first    last                   email
# 0    John   Davis  john_davis@example.com
# 1    Jane     Doe    jane_doe@example.com
# 2  Rachel  Dawson    r_dawson@example.com

##getting a whole column :
print(df['email'])
##output
# 0    john_davis@example.com
# 1      jane_doe@example.com
# 2      r_dawson@example.com
# Name: email, dtype: object

##If w=you want to access multiple columns :
print(df[['last','email']])

##Output
#      last                   email
# 0   Davis  john_davis@example.com
# 1     Doe    jane_doe@example.com
# 2  Dawson    r_dawson@example.com

##If we want to know all the column indexes:
print(df.columns)
##OUTPUT
# Index(['first', 'last', 'email'], dtype='object')

##To access rows of a data frame we use the integer loc (iloc) method and pass an integer as an argument which 
#represents the line of the row and it prints out all th evalues of that row.
print(df.iloc[0])
##Output
# first                      John
# last                      Davis
# email    john_davis@example.com
# Name: 0, dtype: object

##To access multiple rows using iloc
print(df.iloc[[0,1]])
##Output
#   first   last                   email
# 0  John  Davis  john_davis@example.com
# 1  Jane    Doe    jane_doe@example.com

##To access a specific column for given rows. Lets say we wanted column details for the first two rows.
print(df.iloc[[0,1],2])
##Output
# 0    john_davis@example.com
# 1      jane_doe@example.com
# Name: email, dtype: object