import os
import csv
import sys

path1 = 'C:/Users/user/Documents/python-workspace'
path2 = 'C:/Users/user/Documents/python_test'

def Find_Error(logfile):
    with open('RawLogs.csv', 'r') as kd:
        reader = csv.reader(kd, delimiter=',')
        for row in reader:
            if row[1] in logfile:
                sys.stdout = open('Result.txt', 'w')
                print("로그명 :", row[0], "\n에러 로그 :", row[1], "\n증상 요약 :", row[2], "\n관련 Works 번호 :https://works.ahnlab.com/", row[3], "\n\n")



def Log_Direcory(path_dir):
    for (path , dirs, files) in os.walk((path_dir)):
        for file in files:
            if file.lower().find('.txt') != -1:
                full_path=(path+'/'+file)
                with open(full_path, 'r') as log:
                    data = log.read()
                    Find_Error(data)

 
if __name__=="__main__": #왜 넣는거지??
    Log_Direcory(path1)
    Log_Direcory(path2)

    #git test 중입니다