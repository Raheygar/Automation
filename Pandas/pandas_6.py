import pandas as pd
##Declaring a dictionary called 'people'
people = {
        'first':['John','Joe','Jeremey'],
        'last':['Davis','Shmoe','Lockhart'],
        'email':['john@example.com','joe@example.com','lock@example.com']
        }
##Converting the above dictionary into a data frame.
df = pd.DataFrame(people)
print(df)
##Output
#      first      last             email
# 0     John     Davis  john@example.com
# 1      Joe     Shmoe   joe@example.com
# 2  Jeremey  Lockhart  lock@example.com

##Setting an index without changing the original dataframe
print(df.set_index('email'))
##Output
# email
# john@example.com     John     Davis
# joe@example.com       Joe     Shmoe
# lock@example.com  Jeremey  Lockhart

##In the above example we set the index without modifying the original dataframe.

##Now we want to change the original dataframe and set the index using 'inplace' argument.
df.set_index('email',inplace=True)
print(df)

##Output
# email
# john@example.com     John     Davis
# joe@example.com       Joe     Shmoe
# lock@example.com  Jeremey  Lockhart

##If we want to get back to our original dataframe which had integers then we can use the reset_index 
#function

df.reset_index(inplace=True)
print(df)

##OUTPUT
#              email    first      last
# 0  john@example.com     John     Davis
# 1   joe@example.com      Joe     Shmoe
# 2  lock@example.com  Jeremey  Lockhart