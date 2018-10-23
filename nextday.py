def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    day = day + 1
    if day > 30:
        day = 1
        month = month + 1
        if month > 12:
            month = 1
            year = year + 1
    return(year, month, day)

print(nextDay(2018,12,30))