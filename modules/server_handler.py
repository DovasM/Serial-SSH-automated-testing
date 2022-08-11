from logging import exception
import time
import ftplib

class ServerHandler:

    __file = None
    __serverHandler = None
    __session = None

    def __init__(self):
        pass

    def ftp_conn_open(self, address, username, password, port=20):
        try:
            self.__session = ftplib.FTP(address, username, password)
        except:
            raise Exception("Unable to connect to FTP server")

    # def open_file(self, path):
    #     try:
    #         log = open(path, "w")
    #         self.__file = log
    #     except:
    #         raise Exception("Unable to open file to save results to server") 

    def ftp_conn_close(self):
        if self.__session:
            self.__session.quit()

    def save_ftp(self, file_info, *connection):
        try:
            print(0)
            self.ftp_conn_open(connection["address"],connection["username"],connection["password"])
            print(1)
            file = open(file_info[1], 'rb')                  # file to send
            print(2)
            self.__session.storbinary('STOR ' + file_info[0], file)     # send the file
            print(3)
            file.close()                                    # close file and FTP
            print(4)
            self.ftp_conn_close()
        except:
            raise Exception("Unable to open file to save results to FTP server")