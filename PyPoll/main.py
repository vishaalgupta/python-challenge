import os
import csv

total = 0
candidateList = []
voteList = []
index = 0
election_data_csv = os.path.join("..", "PyPoll/Resources", "election_data.csv")

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader, None)
    for row in csv_reader:
        total = total + 1
        if row[2] not in candidateList:
            candidateList.append(row[2])
            voteList.append(1)
        else:
            for candidate in candidateList:
                if row[2] == candidate:
                    voteList[candidateList.index(candidate)] = int(voteList[candidateList.index(candidate)]) + 1

    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {total}')
    print("-----------------------")
    for candidate in candidateList:
        print(f'{candidate}: {round((int(voteList[candidateList.index(candidate)]) / total)*100,3)}% ({voteList[candidateList.index(candidate)]})')
    print("-----------------------")
    print(f'Winner: {candidateList[voteList.index(max(voteList))]}')
    print("-----------------------")

    output_path = os.path.join("..", "PyPoll/Analysis", "results.txt")

    with open(output_path, 'w') as f:
        f.write("Election Results")
        f.write('\n')
        f.write("-----------------------")
        f.write('\n')
        f.write(f'Total Votes: {total}')
        f.write('\n')
        f.write("-----------------------")
        f.write('\n')
        for candidate in candidateList:
            f.write(f'{candidate}: {round((int(voteList[candidateList.index(candidate)]) / total)*100,3)}% ({voteList[candidateList.index(candidate)]})')
            f.write('\n')
        f.write("-----------------------")
        f.write('\n')
        f.write(f'Winner: {candidateList[voteList.index(max(voteList))]}')
        f.write('\n')
        f.write("-----------------------")
