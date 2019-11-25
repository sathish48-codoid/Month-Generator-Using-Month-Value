from datetime import datetime

tourmonth = ['ddummy', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December'];
currentMonth = datetime.now().month
# currentMonth = 7
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

print(list)
