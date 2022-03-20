import os
import csv

months = 0
total = 0
difference = 0
increase = 0
monthIncrease = ""
decrease = 0
monthDecrease = ""
change = 0
monthList = []
changeList = []
differenceList = []
budget_data_csv = os.path.join("..", "PyBank/Resources", "budget_data.csv")

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader, None)
    for row in csv_reader:
        months = months + 1
        total = total + int(row[1])
        monthList.append(row[0])
        changeList.append(row[1])
    for x in range(1, len(changeList)):
        differenceList.append(int(changeList[x]) - int(changeList[x - 1]))
        difference = int(changeList[x]) - int(changeList[x - 1])
        if difference > increase:
            increase = difference
            monthIncrease = monthList[x]
        elif difference < decrease:
            decrease = difference
            monthDecrease = monthList[x]
    change = sum(differenceList) / (months - 1)
    print("Financial Analysis")
    print("-------------------------")
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${round(change,2)}')
    print(f'Greatest Increase in Profits: {monthIncrease} $({increase})')
    print(f'Greatest Decrease in Profits: {monthDecrease} $({decrease})')

    output_path = os.path.join("..", "PyBank/Analysis", "results.txt")

    with open(output_path, 'w') as f:
        f.write("Financial Analysis")
        f.write('\n')
        f.write("-------------------------")
        f.write('\n')
        f.write(f'Total Months: {months}')
        f.write('\n')
        f.write(f'Total: ${total}')
        f.write('\n')
        f.write(f'Average Change: ${round(change,2)}')
        f.write('\n')
        f.write(f'Greatest Increase in Profits: {monthIncrease} $({increase})')
        f.write('\n')
        f.write(f'Greatest Decrease in Profits: {monthDecrease} $({decrease})')


