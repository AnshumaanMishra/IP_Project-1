import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

flight_details = pd.read_csv("D:\Programming\IP_Project\ip_data.csv")
user_details = pd.DataFrame({'S_No':[],'Passenger_Name':[], 'Flight_No':[],'PNR_No':[],'Departure':[],'Arrival':[]})




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
            