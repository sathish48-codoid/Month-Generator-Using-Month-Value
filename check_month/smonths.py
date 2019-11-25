from datetime import datetime
# import gitubuntu.source_information
def month():
    print("dsadsad")
    tourmonth = ['ddummy', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December'];
    currentMonth = datetime.now().month
    # currentMonth = val2
    data = currentMonth;
    list = [];
    i = 0;
    j = 0;
    for i in range(12):
        if i > 0:
            if (currentMonth >= 12):
                if (j > data):
                    print("false")
                else:
                    list.append(tourmonth[j + 1]);
                    j += 1
            else:
                list.append(tourmonth[currentMonth + 1])
                currentMonth += 1
        else:
            list.append(tourmonth[currentMonth])
        i += 1
    return list

def monthvalue(val):
    print("dsadsad")
    tourmonth = ['ddummy', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December'];
    # currentMonth = datetime.now().month
    currentMonth = val
    data = currentMonth;
    list = [];
    i = 0;
    j = 0;
    for i in range(12):
        if i > 0:
            if (currentMonth >= 12):
                if (j > data):
                    print("false")
                else:
                    list.append(tourmonth[j + 1]);
                    j += 1
            else:
                list.append(tourmonth[currentMonth + 1])
                currentMonth += 1
        else:
            list.append(tourmonth[currentMonth])
        i += 1
    return list
