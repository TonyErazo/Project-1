def dayOfProgrammer(year):
    # Write your code here
    # its 243 when its NOT a leap year
    days = 243
    day_of_programmer = 256
    month = 9
    julian = False
    extra_days = 0
    if year < 1919:
        julian = True
    
    if julian and year % 4 == 0:
        days = 244
        extra_days = year / 400
    #gregorian rule
    elif year % 4 == 0 and year % 100 != 0:
        # leap year
        days = 244
    elif year % 400 == 0:
        # leap year
        days = 244
        extra_days = year / 400
    difference = day_of_programmer - days
    #print("extra days: " + str(extra_days))
    if julian:
        days += extra_days
    if difference < 10:
        return "0"+str(difference)+".0"+str(month)+"."+str(year)
    else:
        return(str(difference)+".0"+str(month)+"."+str(year))
    
print(dayOfProgrammer(1800))