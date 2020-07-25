import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': "chicago.csv",
              'new york city': "new_york_city.csv",
              'washington': "washington.csv" }

months = ["january","february","march","april","may","june"]
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington).
    while True:
        city = input("Choose your city. Currently we only have raw bikeshare data of these three US cities - Chicago,New York City and Washington\n").lower()
        if city not in CITY_DATA.keys():
            print("You entered wrong city kindly Choose any one city Among Chicago, New York City, Washington\n")
            continue
        else:
            break
    #get user input for month (all, january, february, ... , june)
    while True: 
        month = input("Choose any one month among January, February, March, April, May and June\n").lower()
        if month not in months:
            print("You entered wrong month kindly Choose any one month Among January, February, March, April, May and June\n")
            continue
        else:
            break
    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("choose any one day among monday, tuesday, wednesday, thursday, friday, saturday, sunday\n").lower()
        if day not in days:
            print("You entered wrong day kindly choose any one day among monday, tuesday, wednesday, thursday, friday, saturday, sunday\n")
            continue
        else:
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #Converted Start Time column to Date Time format using (to_datetime() function in pandas)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    #Created a new column "Month" to extract month from start time
    df["Month"] = df["Start Time"].dt.month
    #Created a new column "Hour" to extract month from start time 
    df["Hour"] = df["Start Time"].dt.hour
    #Created a new column "Day" to extract day name from start time column
    df["Day"] = df["Start Time"].dt.weekday_name
    
    #display the most common month
    common_month = df["Month"].mode()[0]
    print("The most common month is:",months[common_month-1])

    #display the most common day of week
    common_day = df["Day"].mode()[0]
    print("The Most common day of the week is:",common_day)

    #display the most common start hour
    common_hour = df["Hour"].mode()[0]
    print("The most common start hour is:",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    common_start = df["Start Station"].mode()[0]
    print("The common start station is:",common_start)

    #display most commonly used end station
    common_end = df["End Station"].mode()[0]
    print("The most common end station is:",common_end)
    
    #display most frequent combination of start station and end station trip
    df['Frequent_Stations'] = df['Start Station'] +" - "+df['End Station']
    frequent = df['Frequent_Stations'].mode()[0]
    print("The most frequent combination of start station and end station is:",frequent)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_time = df["Trip Duration"].sum()
    print("Total travel time in seconds is:",total_time)
    
    #display mean travel time
    avg_time = df["Trip Duration"].mean()
    print("Average time of the trips in seconds:",avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df["User Type"].value_counts()
    print("Types of users in numbers")
    print(user_types)
    print()

    #Display counts of gender
    if "Gender" in df:
        gender_count = df["Gender"].value_counts()
        print("Number of users gender wise")
        print(gender_count)
        print()
    else:
        print("Sorry currently we don't have gender information in this city.")

    #Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        eldest = int(df["Birth Year"].min())
        print("The eldest user by birth year :",eldest)
        print()
        recent = int(df["Birth Year"].max())
        print("The youngest user by birth year :",recent)
        print()
        common_year = int(df["Birth Year"].mode()[0])
        print("The most common birth year among bikeshare users is :",common_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("Oops currently we don't have user birth year information in this city")
#Created new function show_data(df) to show the data to the user
#This Function helps in Showing Data to the user
def show_data(df):
    print("Hey, user - Would you like to see some raw data for the city you've chosen\n")
    #have set the default to 5, when user entered yes next 5 rows will be shown to the user
    default = 5
    start = 0
    end = default -1
    while True:
        #taking input from a user whether they want to the data or not
        show_results = str(input("Kindly Type either yes or no\n"))
        if show_results.lower() == "yes":
            #Displays the data to the user
            print(df.iloc[start:end+1])
            
            if end >= 1000: #passed this argument to terminate the loop when the user reached the row limit of 1000 
                print("Hey user now you have reached the maximum limit of number of rows you can see. Thank you.\n")
                break
            else:
                print("Now that you've seen rows between {} and {}, Would you want to see next five rows\n".format(start+1,end+1))
                start += default
                end += default
                continue
        elif show_results.lower() not in ["yes","no"] :
            print("Kindly enter either yes or no\n")
            continue
        elif show_results.lower() == "no":
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
