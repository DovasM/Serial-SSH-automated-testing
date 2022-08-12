import imp
from logging import exception
import time
import os
import ftplib

class ServerHandler:

    __file = None
    __serverHandler = None
    __session = None

    def __init__(self):
        pass

    def __ftp_conn_open(self, address, username, password):
        try:
            self.__session = ftplib.FTP(address, username, password)
        except:
            raise Exception("Unable to connect to FTP server")

    def __ftp_conn_close(self):
        if self.__session:
            self.__session.quit()

    def ftp_save(self, file_name, path, file_info):
        try:
            self.__ftp_conn_open(file_info["address"],file_info["username"],file_info["password"])
            file = open(path, 'rb')                  # file to send
            self.__session.storbinary('STOR {}'.format(file_name), file)     # send the file
            file.close()                                    # close file and FTP
            self.__ftp_conn_close()
            os.remove(path)
        except:
            raise Exception("Unable to open file to save results to FTP server")
