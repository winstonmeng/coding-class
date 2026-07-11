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

message = "happy"
print(message.replace("a","o").upper())
countdown = [1,2,3]
print(countdown.reverse())
print(countdown)

list_A = [1,5,2,4,7]
print(list_A.reverse())
print(list_A)
print(list_A.sort())
print(list_A)
list_A.reverse()
print(list_A)
list_A.append(9)
print(list_A)
list_A.insert(2,10)
print(list_A)
list_A.clear()
print(list_A)