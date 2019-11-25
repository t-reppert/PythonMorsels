import datetime
from calendar import Calendar
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=3):
    """Generate meetup date for given year, month, optional week, optional weekday

    :param year:
    :param month:
    :param nth:
    :param weekday:
    :return: meetup date in datetime.date format
    """
    cal = Calendar()
    week = 0
    dates = []
    for day in cal.itermonthdates(year, month):
        if day.weekday() == weekday and day.year == year and day.month == month:
            week += 1
            dates.append(datetime.date(year, month, day.day))
    if nth > 0:
        return dates[nth-1]
    else:
        return dates[nth]
