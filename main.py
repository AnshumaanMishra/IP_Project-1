from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta
import re
import time

flight_details = pd.read_csv("D:\Programming\IP_Project\ip_data.csv")
user_details = pd.DataFrame({'S_No':[],'Passenger_Name':[], 'Flight_No':[],'PNR_No':[],'Departure':[],'Arrival':[]})
 
user_data = pd.DataFrame({'name':[], 'dob': [], 'email':[], 'password': []})
i = int(input("Enter 1 to Login and enter 2 to Sign Up:")
if i == 1:  
        login()
elif i == 2:
        signup()

        


def main():
    choice = int(input("""
                   Please choose any option from the following using (1,2,3,4,5 and 6 as inputs):

                   1. Live flight status
                   2. Flight booking
                   3. Flight availability
                   4. Cancel flight
                   5. Current schedule of flights
                   6. Your flight info
                   """))
    return choice

def f_book():
    f_no = input("Enter the correct flight no:")
    if f_no in flight_details['Flight_No']:
            print("Seats Available are: ", flight_details['Seats_Available'])
            print("Flight starts from:", flight_details['From'])
            print("Flight's destination is:", flight_details['To'])
            print("It departs at time: ", flight_details['Departure'])
            print("The arrival time is:", flight_details['Arrival'])
            print("The flight will be live for:", flight_details['Duration'])
            print("The number of stops are:", flight_details['Stops'])
            print("Ticket per person:", flight_details['Price'])
        
    else:
        print("Invalid flight number entered. Please try again.")






def f_avail():





def f_cancel():







def f_sched():
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        print("Flight schedule for today is as follows:")
        time.sleep(2)
        print(flight_details[flight_details["Day"] == day and flight_details["Month"] == month and flight_details["Year"] == year])



def user_flight():


def login():
    username = input("Enter your email address:")
    if username in user_data['email']:
        pwd = input("Enter your password:")
        if pwd == user_data['password']:
            "Login successful."
        else: 
            print("Invalid password. Try again later.")
    else: 
        print("The email address entered is incorrect. ")

def signup():
        name = input("Enter your full name:")
        dob = input("Enter your DOB in the DD/MM/YYYY format:")
        email = input("Enter your email address:")
        password = input("Create a strong password for your account. It must contain at least 8 alphanumeric characters:")
        user_data.append({'name': name, 'dob': dob, 'email': email, 'password': password}, inplace = True)

def convert24(time):
    t = dt.strptime(time, '%I:%M %p')
    return t.strftime('%H:%M')

def f_status():
    flight_data = pd.read_csv('flight_data.csv')
    
    id = input("Enter Flight ID: ")
    
    extracted_data = flight_data[flight_data['Flight_No']==id]
    
    timeRegex = re.compile('..:.. .m')
    
    imdex = flight_data['Flight_No']==id
    index = 0
    for j in range(0, len(imdex)):    
        if imdex.iat[j]==True:
            index = j
            break
    
    extract = convert24(re.findall(timeRegex, extracted_data.Departure[index])[0].strip())
    depart = dt.strptime(extract, '%H:%M')
    
    extract = convert24(re.findall(timeRegex, extracted_data.Arrival[index])[0].strip())
    arrival = dt.strptime(extract, '%H:%M')
    
    now = dt.strptime(dt.now().strftime("%H:%M"),'%H:%M')
    
    
    status = ''
    statindex = 0
    
    
    if arrival<depart:
        arrival += timedelta(hours=24)
    
    
    if now < depart:
        status = 'Not Yet Started'
    
    elif now > arrival: 
        status = 'FLight Has Landed At Its Destination'
    
    else:
        statindex = (now-depart)/(arrival-depart)
        status = 'Flight In Progress'
    
    
    stops = extracted_data.Stops[index]
    sections = 1/(stops+1)
    
    
    i = 0 
    a1 = list()
    while i <= 1:
        a1.append(i)
        i += sections
    
    
    print(status)
    
    
    plt.plot(a1, [5]*len(a1), marker='o')
    
    
    plt.plot([statindex], [5], marker='X', markeredgecolor='k')
    plt.legend(['Path', 'Current Location'])
    plt.show()
