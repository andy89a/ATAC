import threading
import paramiko
import time
paramiko.util.log_to_file('paramiko.log')

strdata=''
fulldata=''

class ssh:
    shell = None
    client = None
    transport = None

    def __init__(self, address, username, password):
        print("Connecting to server on ip", str(address) + ".")
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)
        self.transport = paramiko.Transport((address, 22))
        self.transport.connect(username=username, password=password)

        thread = threading.Thread(target=self.process)
        thread.daemon = True
        thread.start()

    def close_connection(self):
        if(self.client != None):
            self.client.close()
            self.transport.close()

    def open_shell(self):
        self.shell = self.client.invoke_shell()

    def send_shell(self, command):
        if(self.shell):
            self.shell.send(command + "\n")
        else:
            print("Shell not opened.")

    def process(self):
        global strdata, fulldata
        while True:
            # Print data when available
            if self.shell is not None and self.shell.recv_ready():
                alldata = self.shell.recv(1024)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(1024)
                strdata = strdata + str(alldata)
                fulldata = fulldata + str(alldata)
                strdata = self.print_lines(strdata) # print all received data except last line

    def print_lines(self, data):
        last_line = data
        if '\n' in data:
            lines = data.splitlines()
            for i in range(0, len(lines)-1):
                print(lines[i])
            last_line = lines[len(lines) - 1]
            if data.endswith('\n'):
                print(last_line)
                last_line = ''
        return last_line


# Open a transport
host = "10.10.50.11"
port = 50501
transport = paramiko.Transport((host, port))


# Auth
username = "scpuser"
password = "qjzmffl!!1"
transport.connect(username = username, password = password)

# Go!
sftp = paramiko.SFTPClient.from_transport(transport)


# # Download
# localpath = '/home/remotepasswd'
# filepath = '/etc/passwd'
# sftp.get(filepath, localpath)


# Upload
localpath = 'troubleshooting_1234.enc'
filepath = './troubleshooting_1234.enc'
sftp.put(localpath, filepath)


# Close
sftp.close() 
transport.close()


sshUsername = "manager"
sshPassword = "asd123!@#"
sshServer = "10.10.50.11"


connection = ssh(sshServer, sshUsername, sshPassword)
connection.open_shell()
connection.send_shell('$blackpinkwpsl$')
connection.send_shell('$twiceWmdnl$')
connection.send_shell('cd /file_db_hdd')
connection.send_shell('mkdir /file_db_hdd/test')
connection.send_shell('mv troubleshooting_1234.enc /file_db_hdd/test')
connection.send_shell('cd /file_db_hdd/test')
connection.send_shell('seeddecrypt troubleshooting_1234.enc test.tar 1234') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨 또는 매번 새로운 폴더를 생성하던지
time.sleep(30)  #문제점!!! time.sleep 을 이용해서 바로 직전의 seeddecrpyt 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯


connection.send_shell('tar -xvf test.tar')
time.sleep(1)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯
connection.send_shell('seeddecrypt atl_report.enc atl.tar ahnlab123\!\@\#') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(15)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯
connection.send_shell('seeddecrypt twc_report.enc twc.tar ahnlab123\!\@\#') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(2)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯
connection.send_shell('seeddecrypt zpx_report.enc zpx.tar ahnlab123\!\@\#') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(2)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯



connection.send_shell('tar -xvf twc.tar') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(3)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯
connection.send_shell('tar -xvf zpx.tar') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(3)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯
connection.send_shell('tar -xvf debuglog.tar.gz') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(10)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯
connection.send_shell('tar -xvf monitor.tar.gz') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(10)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯
connection.send_shell('tar -xvf update_log.tar.gz') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(5)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯
connection.send_shell('tar -xvf atl.tar') #실제로 사용될땐 압축을 푼 파일명을 유동적으로 가져 가야됨
time.sleep(120)  #문제점!!! time.sleep 을 이용해서 바로 직전의 명령어가 급 종료 되는 걸 막긴했는데, 나중에는 실제로 seeddecrpyt 작업이 끝난걸 인식하게 해야 될듯


connection.close_connection()