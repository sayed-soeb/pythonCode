'''
Q9.
Write a func that takes 3 args:
from_date - string representing a date in the form of 'yy-mm-dd'
to_date - string representing a date in the form of 'yy-mm-dd'
difference - int
Returns True if from_date and to_date are less than difference days away from each other, else
returns False.
'''

from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert date strings to datetime objects
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')
    
    # Calculate the difference between dates
    date_difference = to_date_obj - from_date_obj
    
    # Check if the difference is less than the specified value
    if date_difference < timedelta(days=difference):
        return True
    else:
        return False

# Example usage
from_date = '21-05-15'
to_date = '21-05-25'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)
