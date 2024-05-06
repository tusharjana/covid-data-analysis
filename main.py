import matplotlib.pyplot as plt
import pandas as pd
import pyfiglet
from colorama import init, Fore

init(autoreset=True) # reset the terminal color 
covidData = pd.read_csv('clean-data.csv')

# menus
mainMenu = """
    [0] About the project 
    [1] Modify the dataframe
    [2] Analyze and interpret the dataframe
    [3] Exit 
"""
modifyMenu = """
    [0] View the dataframe
    [1] Add an entry
    [2] Delete an entry
    [3] Edit an entry
    [4] Exit to the main menu
"""
analyseMenu = """
    [0] Display line graph menu
    [1] Display bar graph menu
    [2] Exit to the main menu
"""
lineMenu = """
    [0] Display a line graph of positive cases
    [1] Display a line graph of negative cases
    [2] Display a line graph of deaths
    [3] Display a line graph of hospitalized cases
    [4] Display a line graph of recovered cases
    [5] Display a combined line graph
    [6] Exit to the main menu
"""
barMenu = """
    [0] Display a bar graph of positive cases
    [1] Display a bar graph of negative cases
    [2] Display a bar graph of deaths
    [3] Display a bar graph of hospitalized cases
    [4] Display a bar graph of recovered cases
    [5] Display a combined bar  graph
    [6] Exit to the main menu
"""

# functions
def newEntry():
    rowValues = input("Enter the row values separated by commas: ").split(",")
    covidData.loc[len(covidData.index)] = rowValues
    print(covidData)
    print(Fore.GREEN + "\nSuccess !\nEntry added\n")

def deleteEntry():
    entryState = input("Enter the state of the entry to delete: ")
    covidData.drop(covidData[covidData['state'] == entryState].index, inplace=True)
    print(covidData)
    print(Fore.GREEN + "\nSuccess !\nEntry deleted\n")

def updateEntry():
    states = covidData["state"]
    covidData.index = states
    covidData.drop("state", axis=1, inplace=True)
    entryUpdate = input("Enter state of entry to be updated: ")
    updatedValues = input(
        "Enter the updated row values separated by commas: ").split(",")
    covidData.loc[entryUpdate] = updatedValues
    covidData = covidData.reset_index()
    print(covidData)
    print(Fore.GREEN + "\nSuccess !\nEntry updated\n")

def lineGraphMenu():
    while True:
            print(Fore.MAGENTA + pyfiglet.figlet_format("LINE GRAPH MENU", justify="center", font="slant"))
            print("[1] Display a line graph of positive cases")
            print("[2] Display a line graph of negative cases")
            print("[3] Display a line graph of deaths")
            print("[4] Display a line graph of hospitalized")
            print("[5] Display a line graph of recovered")
            print("[6] Display a combined line graph")
            print("[7] Exit to the main menu\n")

            query = int(input("Enter option: "))

            if query == 1:
                states = covidData["state"]
                cases = covidData["positive"]
                plt.plot(states, cases)
                plt.title("Positive cases in each state of the US")
                plt.show()
            elif query == 2:
                states = covidData["state"]
                cases = covidData["negative"]
                plt.plot(states, cases)
                plt.title("Negative cases in each state of the US")
                plt.show()
            elif query == 3:
                states = covidData["state"]
                cases = covidData["deaths"]
                plt.plot(states, cases)
                plt.title("Deaths in each state of the US")
                plt.show()
            elif query == 4:
                states = covidData["state"]
                cases = covidData["hospitalized"]
                plt.plot(states, cases)
                plt.title("Hospitalized cases in each state of the US")
                plt.show()
            elif query == 5:
                states = covidData["state"]
                cases = covidData["recovered"]
                plt.plot(states, cases)
                plt.title("Recovered cases in each state of the US")
                plt.show()
            elif query == 6:
                states = covidData["state"]
                casesPositive = covidData["positive"]
                casesNegative = covidData["negative"]
                casesDeaths = covidData["deaths"]
                casesHospitalized = covidData["hospitalized"]
                casesRecovered = covidData["recovered"]
                plt.plot(states, casesPositive, label="Positive cases")
                plt.plot(states, casesNegative, label="Negative cases")
                plt.plot(states, casesDeaths, label="Deaths")
                plt.plot(states, casesHospitalized, label="Hospitalized cases")
                plt.plot(states, casesRecovered, label="Recovered cases")
                plt.title("COVID-19 in each state of the US")
                plt.legend()
                plt.show()
            elif query == 7:
                break
            else:
                print("Invalid option")

def barGraphMenu():
    while True:
            print(Fore.MAGENTA + pyfiglet.figlet_format("BAR GRAPH MENU", justify="center", font="slant"))
            print("[1] Display a bar graph of positive cases")
            print("[2] Display a bar graph of negative cases")
            print("[3] Display a bar graph of deaths")
            print("[4] Display a bar graph of hospitalized")
            print("[5] Display a bar graph of recovered")
            print("[6] Display a combined bar graph")
            print("[7] Exit to the main menu\n")

            query = int(input("Enter option: "))

            if query == 1:
                states = covidData["state"]
                cases = covidData["positive"]
                plt.bar(states, cases)
                plt.title("Positive cases in each state of the US")
                plt.show()
            elif query == 2:
                states = covidData["state"]
                cases = covidData["negative"]
                plt.bar(states, cases)
                plt.title("Negative cases in each state of the US")
                plt.show()
            elif query == 3:
                states = covidData["state"]
                cases = covidData["deaths"]
                plt.bar(states, cases)
                plt.title("Deaths in each state of the US")
                plt.show()
            elif query == 4:
                states = covidData["state"]
                cases = covidData["positive"]
                plt.bar(states, cases)
                plt.title("Hospitalized cases in each state of the US")
                plt.show()
            elif query == 5:
                states = covidData["state"]
                cases = covidData["positive"]
                plt.bar(states, cases)
                plt.title("Recovered cases in each state of the US")
                plt.show()
            elif query == 6:
                states = covidData["state"]
                casesPositive = covidData["positive"]
                casesNegative = covidData["negative"]
                casesDeaths = covidData["deaths"]
                casesHospitalized = covidData["hospitalized"]
                casesRecovered = covidData["recovered"]
                positiveBar = plt.bar(states, casesPositive)
                negativeBar = plt.bar(states, casesNegative)
                deathsBar = plt.bar(states, casesDeaths)
                hospitalizedBar = plt.bar(states, casesHospitalized)
                recoveredBar = plt.bar(states, casesRecovered)
                plt.title("COVID-19 cases in each state of the US")
                plt.legend(
                    (
                        positiveBar[0],
                        negativeBar[0],
                        deathsBar[0],
                        hospitalizedBar[0],
                        recoveredBar[0]
                    ),
                    (
                        "Positive",
                        "Negative",
                        "Deaths",
                        "Hospitalized",
                        "Recovered"
                    )
                )
                plt.show()
            elif query == 7:
                break
            else:
                print("Invalid option")

# rest of the code
while True:
    print(Fore.MAGENTA + pyfiglet.figlet_format("COVID DATA ANALYSIS", justify="center", font="slant"))
    print(mainMenu)
    choice = int(input('\nEnter your choice: \n'))

    if choice == 0:
        print(Fore.MAGENTA + """

            ABOUT THE PROJECT

    This COVID-19 Data Analysis Project is an initiative to research and understand the progression 
    and severity of the virus in each state of the United States of America in 2021 through analysis of the data-set acquired.
    This project is a useful tool for users to view the statistics in a clean and graphically attractive manner. 
    It allows users to view the statistics in the form of different graphical representations and integers. 
    The source code can be modified by the user as per their requirements.
        """)
    elif choice == 1:
        while True:
            print(Fore.MAGENTA + pyfiglet.figlet_format("MODIFY", justify="center", font="slant"))
            print(modifyMenu)
            choice = int(input('\nEnter your choice: \n'))

            if choice == 0:
                print(covidData)
            elif choice == 1:
                newEntry()
            elif choice == 2:
                deleteEntry()
            elif choice == 3:
                updateEntry()
            elif choice == 4:
                break
            else:
                print(Fore.RED + '\nInvalid option\n')
    elif choice == 2:
        while True:
            print(Fore.MAGENTA + pyfiglet.figlet_format("ANALYSE", justify="center", font="slant"))
            print(analyseMenu)
            choice = int(input('\nEnter your choice: '))

            if choice == 0:
                lineGraphMenu()
            elif choice == 1:
                barGraphMenu()
            elif choice == 2:
                break
            else:
                print(Fore.RED + '\nInvalid option\n')

    elif choice == 3:
        print("\n                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 👋 Bye-bye 👋 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        break

