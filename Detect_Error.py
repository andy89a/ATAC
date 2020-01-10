import os
import csv
import sys

path1 = 'C:/Users/user/Documents/python-workspace/gatheredlog'
# path2 = 'C:/Users/user/Documents/python_test'
# path3 = '10.10.50.11/file_db_hdd/test/data/syslog/appl'

def Find_Error(logfile, filename):
    with open('RawLogs.csv', 'r') as kd:
        reader = csv.reader(kd, delimiter=',')
        for row in reader:
            if row[1] in logfile:
                sys.stdout = open('Result.txt', 'a+')
                print("로그명:", filename, "\n에러 로그:", row[1], "\n증상 요약:", row[2], "\n관련 Works 번호: https://works.ahnlab.com/browse/" + row[3], "\n\n")

def Log_Direcory(path_dir):
    for (path , dirs, files) in os.walk((path_dir)):
        for file in files:
            full_path=(path+'/'+file)
            with open(full_path, 'rt', encoding='latin-1') as log: #UTF8 로 하니까 에러나서 구글링해서 latin-1로 바꿈
                data = log.read()
                logfilename = file
                Find_Error(data, logfilename)

if __name__=="__main__": #이 모듈은 다른 py 스크립트에서 호출했을 때는 실행되지 않도록함.
    Log_Direcory(path1)