import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    Iso_Date = datetime.fromisoformat(iso_string)
    return(Iso_Date.strftime("%A %d %B %Y"))

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    celcius = (float(temp_in_fahrenheit) - 32) / (9/5)
    return (round(celcius,1))


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    len_data = len(weather_data)
    sum = 0
    for data in weather_data:
        int_data = float(data)
        sum = int_data + sum
    return (sum/len_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) # skip headers (first row)

        list = []
        for i in csv_reader:
            if i:
                formatted_row = [i[0]] + [int(x) for x in i[1:]]
                list.append(formatted_row)
        return (list)

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data:
        list = []
        for i in weather_data:

                float_data = float(i)
                list.append(float_data)
        min_value = min(list)
        return (min_value, len(list) - 1 - list[::-1].index(min_value))
    else:
        return ()


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data:
        list = []
        for i in weather_data:
            float_data = float(i)
            list.append(float_data)
        max_value = max(list)
        return (max_value, len(list) - 1 - list[::-1].index(max_value))
    else:
        return ()


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    len_list = len(weather_data)
    min_values = []
    max_values = []
    for i in weather_data:
        min_values.append(i[1])
        max_values.append(i[2])
    mini = convert_f_to_c(min(min_values))
    index = min_values.index(min(min_values))
    date = convert_date(weather_data[index][0])
    avg_low = convert_f_to_c(calculate_mean(min_values))

    maxi = convert_f_to_c(max(max_values))
    avg_max = convert_f_to_c(calculate_mean(max_values))
    index1 = max_values.index(max(max_values))
    date1 = convert_date(weather_data[index1][0])

    return(f"{len_list} Day Overview\n  The lowest temperature will be {mini}{DEGREE_SYMBOL}, and will occur on {date}.\n  The highest temperature will be {maxi}{DEGREE_SYMBOL}, and will occur on {date1}.\n  The average low this week is {avg_low}{DEGREE_SYMBOL}.\n  The average high this week is {avg_max}{DEGREE_SYMBOL}.\n")    

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for i in weather_data:
        value = convert_date(i[0])

        min_temp = convert_f_to_c(i[1])

        max_temp = convert_f_to_c(i[2])

        summary += (f"---- {value} ----\n  Minimum Temperature: {min_temp}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp}{DEGREE_SYMBOL}\n\n")
    return (summary)