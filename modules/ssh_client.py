import paramiko
import time


class ConnectionHandler:

    __ssh_client = None
    __ssh_channel = None

    def __init__(self, flags):

        if not flags.ip and not flags.username and not flags.password:
            raise Exception("fuhas esi")

        print(flags)
        

        # if not self.__open_connection(addr, username, password):
        #     raise Exception("Unable to connect to SSH server")
        

    def __close_connection(self):
        if self.__ssh_client:
            self.__ssh_client.close()

    def __open_connection(self, addr, username, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(addr, 22, username, password)
            self.__ssh_client = client
            return True
        except:
            return None

    def exec_command(self, command):
        success = True
        stdin, stdout, stderr = self.__ssh_client.exec_command(command)
        # print(''.join(stderr.readlines()))
        if stderr.readlines():
            success = False
        return success

    def __del__(self):
        self.__close_connection()

    def shell_exec_command(self, command, argument):
        try:
            self.__ssh_channel = self.__ssh_client.invoke_shell()
            time.sleep(1)
            self.__ssh_channel.send(
                "socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r")
            time.sleep(1)
            self.__ssh_channel.send(command + "\r")
            time.sleep(1)
            self.__ssh_channel.send(argument + "\r")
            time.sleep(1)
            self.__ssh_channel.send("\x1A\r")
            output = self.__ssh_channel.recv(9999).decode("ascii").splitlines()
            answer, output = self.wait_until(output, 90, 2)
            if answer:
                return output
            else:
                return output
        except Exception as error:
            print(error)

    def wait_until(self, output, timeout, period=0.25):
        mustend = time.time() + timeout
        while time.time() < mustend:
            if output[-2] == 'OK' or output[-2] == 'FAIL':
                return True, output[-2]
            output = self.__ssh_channel.recv(9999).decode("ascii").splitlines()
            # print(0)
            if output[-2] == []:
                continue
            output = self.__ssh_channel.recv(9999).decode("ascii").splitlines()
            time.sleep(period)
        return False, 'Error'
