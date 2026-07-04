def convert_days_to_seconds(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    milliseconds = seconds * 1000
    microsecond = milliseconds * 1000
    nanosecond = microsecond * 1000
    picosecond = nanosecond * 1000
    femtosecond = picosecond * 1000
    attosecond = femtosecond * 1000
    zeptosecond = attosecond * 1000
    yoctosecond = zeptosecond * 1000
    return yoctosecond

print(convert_days_to_seconds(1))