import schedule
import time
##Declare functions for your work
def morning():
    print("Learn Terraform in the morning!!")
def afternoon():
    print("Learn Python libraries!!")
def evening():
    print("Implement it in a project!!")
def night():
    print("Update yourself with new technologies!!")
def midnight():
    print("All work and no play makes Abhishek a very pissed off guy!!")
def nextday():
    print("Start the grind all over again")

##Now lets schedule the tasks:
#Lets Schedule the first task every 5 minutes:
schedule.every(5).minutes.do(morning)

#Lets Schedule the second task every 1 hour:
schedule.every(1).hour.do(afternoon)

#Lets Schedule the third task every day:
schedule.every(1).day.do(evening)

#Lets Schedule the fourth task at a specific time in a day:
schedule.every().day.at('00:00').do(night)

#Lets Schedule the fifth task on a specific weekday at a specific time:
schedule.every().wednesday.at('18:00').do(midnight)

#Lets Schedule the sixth task in between specific time:
schedule.every(5).to(10).minutes.do(nextday)

#Loop these tasks so that this schedule keeps running all the time:
while True:
    #Check if any tasks are pending or not
    schedule.run_pending()
    time.sleep(2)
