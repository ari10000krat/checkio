import re
import datetime


def date_time(time: str) -> str:
    day, month, year, hour, minutes = [int(s) for s in re.split('\.|:|\s', time)]
    words = ['hour', 'minute']
    for key, value in {0: hour, 1: minutes}.items():
        if int(value) != 1:
            words[key] += "s"

    return f"{day} {datetime.datetime.strftime(datetime.datetime(year, month, day), '%B')} {year} year {hour} {words[0]} {minutes} {words[1]}"


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    print("Coding complete? Click 'Check' to earn cool rewards!")
