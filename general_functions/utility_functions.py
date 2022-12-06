import datetime
import re

def convert_to_datetime(date_str: str, time_str: str) -> datetime.datetime:
    '''
    function to convert date string in the format 'dd/mm/yyyy' and time string in the format 'hh:mm:ss tz' 
    into datetime object. currently ignores timezone
    '''
    format_str = '%m/%d/%Y %H:%M:%S' # The format
    time_str = re.sub('[A-Za-z\s]', '', time_str) # remove timezone, should find a way to add it some time in the future
    joined_string = ' '.join([date_str, time_str]) # joined string
    
    return datetime.datetime.strptime(joined_string, format_str)