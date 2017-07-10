import calendar


def days_since_1901(y):
    leap_days = sum([1 for x in range(1901, y) if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0])
    return 365 * (y - 1901) + leap_days


def update_calendar(c):
    day = c["day"]
    month = c["month"]
    year = c["year"]
    leap_year = c["leap_year"]

    day += 1

    if day == 31 and month in [4, 6, 9, 11] or day == 32 and month in [1, 3, 5, 7, 8, 10, 12] or \
            month == 2 and (day == 29 and not leap_year or day == 30 and leap_year):
        day = 1
        month += 1

    if month == 13:
        month = 1
        year += 1

        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            leap_year = 1
        else:
            leap_year = 0

    c["day"] = day
    c["month"] = month
    c["year"] = year
    c["leap_year"] = leap_year

    return c


def count_days(y):
    total_days = days_since_1901(y)

    c = {
        "day": 1,
        "month": 1,
        "year": 1901,
        "leap_year": 0
    }

    ct = 0

    for d in range(1, total_days):
        if d % 7 == 6 and c["day"] == 1:
            ct += 1
            print(c)

        c = update_calendar(c)

    return ct


def test():
    c = {
        "day": 1,
        "month": 1,
        "year": 1970,
        "leap_year": 0
    }

    for d in range(3, 100000):
        if calendar.weekday(c["year"], c["month"], c["day"]) != d % 7:
            print(c, d % 7, d)
            return

        c = update_calendar(c)


# test()

print(count_days(2001))

