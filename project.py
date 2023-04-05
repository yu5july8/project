###
#Airline reservation system
#video demo: <URL: >
#Description:
#input PAX info and create a list of passengers like airline reservation system. keep record of name and a
#utomatically assign seats basically reservation system of airline
###

#import
import sys
import csv
from tabulate import tabulate
import validators


#month dictionary goes here for date input
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


#main function and create list of csv file
def main():
    myReservation = get_info()
    list_creator(myReservation)
    print("You Successfuilly reserved your flight")


def get_info():
    name = input("What is your name?: ").strip().capitalize()
    date = input("when is the date of yoru travel?: ").strip()
    destination = input("where is your destination?: ").strip().capitalize()
    email = (input("What is your email?: ")).strip()
    return name, date, destination, email




def list_creator(myReservation):
    reserv =  ['name', 'date', 'destination', 'email']
    with open('reservation.csv', 'w') as csvfiles:
            writer = csv.DictWriter(csvfiles, fieldnames = reserv)
            writer.writeheader()
            print(myReservation)
            name = myReservation[0]
            date = myReservation[1]
            destination = myReservation[2]
            email = myReservation[3]
            myDict = {'name': name, 'date': date, 'destination': destination, 'email': email}
            writer.writerow(myDict)
            print(myDict)
            table = tabulate(myDict, headers=reserv, tablefmt = "grid")
            print(table)

def name():
    if len(sys.argv) > 4:
        sys.exit("Invalid name")
    elif len(sys.argv) < 3:
        sys.exit("Invalid name")

def date():
    if "/" in date:
        try:
            month,day ,year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if (day > 32 or day < 0):
                return True
            if(month > 13 or month < 0):
                return True
            if year <= 1000:
                return True
            return f"{year}-{month:02}-{day:02}"
        except:
                return()
    else:
        try:
            month, day, year = date.split(" ")
            if ("," in day):
                day = day.replace(","," ")
                year = int(year)
                day = int(day)
                if day >= 31 or day <= 1:
                    return True
                if year < 999:
                    return True
                if month.title() in months:
                    dictionary = months.index(month.title()) + 1
                    if (dictionary == month.title()):
                        dictionary = int(month +1)
                    return f"{year}-{dictionary:02}-{day:02}"
                else:
                    pass

        except:
            return()

def destination():
    if len(sys.argv) > 1:
        sys.exit("Please input something")
    elif len(sys.argv) < 3:
        sys.exit("Invalid destination")


def email(s):
    if validators.email(s)== True:
        return f"Valid"
    else:
        return f"Invalid"

if __name__ == "__main__":
    main()
