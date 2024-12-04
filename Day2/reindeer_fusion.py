# report = row
# level column/entry in row
# sage = gradual increase/decrease
# max diff = 3
# min diff = 1
# load data

# test decending
def isdecending(array):
    isdecending = True
    for i in range(1,len(array)):
        if (0 < array[i-1] - array[i] < 4) :
            pass
        else:
            isdecending=False
    return isdecending

def isascending(array):
    isascending = True
    for i in range(1,len(array)):
        if (0< array[i] - array[i-1] < 4) :
            pass
        else:
            isascending=False
    return isascending
all_reports = []
with open('input.txt','r') as f:
    for line in f:
        report = line.split()
        int_report = [int(number) for number in report]
        all_reports.append(int_report)
safe_count = 0
for report in all_reports:
    if isascending(report) or isdecending(report):
        safe_count +=1
print(safe_count)
# part two with damper

safe_count_damped = 0
for report in all_reports:
    # remove a level
    print('-' * 10)
    print(report)
    mistake_test = True
    if  isascending(report) or isdecending(report):
        safe_count_damped += 1
        mistake_test = False
        print("true by default")
    if mistake_test:
        for i in range(0,len(report)):
            report_copy = report.copy()
            report_copy.pop(i)
            print(report_copy)
            if isascending(report_copy) or isdecending(report_copy):
                safe_count_damped +=1
                print("true by removal")
                break
    print(safe_count_damped)
print(safe_count_damped)


print("HoHoHo")
