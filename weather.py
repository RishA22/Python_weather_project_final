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
    """Converts and ISO-8601 formatted date into a human-readable format.

    Args:
        iso_string: An ISO-8601 date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    Iso_Date = datetime.fromisoformat(iso_string)
    return(Iso_Date.strftime("%A %d %B %Y"))

    #ERROR HANDLING
    # try:
    #     Iso_Date = datetime.fromisoformat(iso_string)
    #     return(Iso_Date.strftime("%A %d %B %Y"))
    # except ValueError:
    #     return None


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    to_celcius = (float(temp_in_fahrenheit) - 32) / (9/5)
    return (round(to_celcius,1)) #round temperature value to first decimal place


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    len_data = len(weather_data) #length of list
    sum = 0
    for data in weather_data:
        float_data = float(data) #converting each element to float
        sum = float_data + sum #getting sum of elements of list
    return (sum/len_data) #return mean of elements of list

    #use of list comprehension
    # return sum([float(item) for item in weather_data]) / len(weather_data))


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    #open csv file and use it
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) # skip headers (first row)

        list = []
        for row in csv_reader:
            if row:
                formatted_row = [row[0]] + [int(x) for x in row[1:]] #we need first element of row as string and others as int
                list.append(formatted_row)
        return (list)
    
    #use of list comprehension
    # with open(csv_file) as csv_file:
    #     csv_dictreader = csv.DictReader(csv_file)
    #     return([row["date"], float(row["min"]), float(row["max"])] for row in csv_dictreader if row) 

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data:
        list = []
        for data in weather_data:

                float_data = float(data) #convert each element of list to float
                list.append(float_data) #append the list with floated elements
        min_value = min(list) #get min value of weather data
        return (min_value, len(list) - 1 - list[::-1].index(min_value)) #to get the index of max element which is occuring at last of the list
    else:
        return ()
    
    #Another way of doing
    # if not weather_data:
    #     return ()
    
    # temps = [float(item) for item in reversed(weather_data)]
    # min_value = min(temps)
    # min_value_index = len(weather_data) -1 - temps.index(min_value)
    # return min_value, min_value_index



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data:
        list = []
        for data in weather_data:
            float_data = float(data) #convert each element of list to float
            list.append(float_data) #append the list with floated elements
        max_value = max(list) #get maximum value of weather data
        return (max_value, len(list) - 1 - list[::-1].index(max_value)) #to get the index of max element which is occuring at last of the list
    else:
        return ()


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    len_list = len(weather_data) #length of weather data
    min_values = [] #empty list to put min temperature values from each day
    max_values = [] #empty list to put max temperature values from each day
    for i in weather_data:
        min_values.append(i[1]) #list of min temp values for each day
        max_values.append(i[2]) #list of max temp values for each day

    to_celsius_min_values = convert_f_to_c(min(min_values)) #converting min temp to celsius
    index = min_values.index(min(min_values)) #getting index of row where min value occur
    date = convert_date(weather_data[index][0]) #getting date where min value occur
    avg_low = convert_f_to_c(calculate_mean(min_values)) #getting mean of min values and converting to celsius

    to_celsius_max_values = convert_f_to_c(max(max_values))
    avg_max = convert_f_to_c(calculate_mean(max_values))
    index1 = max_values.index(max(max_values))
    date1 = convert_date(weather_data[index1][0])

    return(f"{len_list} Day Overview\n  The lowest temperature will be {to_celsius_min_values}{DEGREE_SYMBOL}, and will occur on {date}.\n  The highest temperature will be {to_celsius_max_values}{DEGREE_SYMBOL}, and will occur on {date1}.\n  The average low this week is {avg_low}{DEGREE_SYMBOL}.\n  The average high this week is {avg_max}{DEGREE_SYMBOL}.\n")    

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = "" #empty string

    for row in weather_data:
        value = convert_date(row[0]) #convert 
        min_temp = convert_f_to_c(row[1]) #convert min temp to Celsius
        max_temp = convert_f_to_c(row[2]) #convert max temp to Celsius

        summary += (f"---- {value} ----\n  Minimum Temperature: {min_temp}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp}{DEGREE_SYMBOL}\n\n")
    return (summary)