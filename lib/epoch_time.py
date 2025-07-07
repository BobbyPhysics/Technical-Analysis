import datetime

# Define function to convert epoch time to date string
def epoch_to_datetime(epoch_time_ms):
    #epoch_time_s = epoch_time_ms / 1000
    #return datetime.datetime.fromtimestamp(epoch_time_s)
    return datetime.datetime.fromtimestamp(epoch_time_ms/1000)


def date_to_epoch(date_str):
    """
    Convert a date string in the format yyyymmdd to epoch time in milliseconds.

    Parameters:
    date_str (str): Date string in the format yyyymmdd

    Returns:
    int: Epoch time in milliseconds
    """
    # Parse the date string into a datetime object
    specific_date = datetime.datetime.strptime(date_str, "%Y%m%d")
    
    # Convert the datetime object to epoch time in seconds
    epoch_time_seconds = specific_date.timestamp()
    
    # Convert seconds to milliseconds
    epoch_time_milliseconds = int(epoch_time_seconds * 1000)
    
    return epoch_time_milliseconds

# Example usage
# date_str = 20190920
# epoch_time = date_to_epoch(date_str)
# print(f"Epoch time for {date_str} is {epoch_time} milliseconds.")

# test = epoch_to_datetime(1751855427)
# print(test)