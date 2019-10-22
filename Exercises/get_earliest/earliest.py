

def get_earliest(*dates):
    """
    Find earliest date in list of provided date strings

    Parameters:
        dates (list): List of date strings in format "mm/dd/yyyy"

    Returns:
        str: Earliest date found in list of date strings

    """
    earliest = "99/99/9999"
    for date in list(dates):
        if date[-4:] < earliest[-4:]:
            earliest = date
        elif date[-4:] == earliest[-4:]:
            if date[0:2] < earliest[0:2]:
                earliest = date
            elif date[0:2] == earliest[0:2]:
                if date[3:5] < earliest[3:5]:
                    earliest = date
    return earliest


