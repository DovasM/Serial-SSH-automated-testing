from ast import arg
import io
from itertools import count
from re import T
from tarfile import ENCODING
from urllib import response
import serial
import time
from curses import ascii   
import os


class ConnectionHandler:

    __results = []
    __configHandler = None
    __termHandler = None
    __device = None
    __sio = None

    def __init__(self, flags, config):
        if (not(hasattr(flags, "pt"))):
            raise Exception("Need attributes [Port] for Serial server connection")

        os.system("systemctl stop ModemManager")
        self.__sio = serial.Serial(flags.pt, 115200, timeout=1)
        self.__device = flags.name
        self.__termHandler = self.__load_module()
        if not self.__termHandler:
            raise Exception("Unable to load terminal handler module")
        try:
            __configHandler = config
        except Exception as error:
            print(error)
        self.test_commands(__configHandler.get_comm(flags.name))

    def __load_module(self):
        module = None
        try:
            module = __import__('modules.terminal_handler', fromlist=['modules'])
            return module.TerminalHandler()
        except:
            return False        

    def test_commands(self, arg):
        for command in arg:
                result = {}
                comm = command['command'] + '\r'
                argument = command['argument'] + '\r'
                # self.send_message(argument, comm)
                response = self.exec_command(comm, argument, command["expects"])
                result["command"] = command["command"]
                result["expects"] = command["expects"]
                result["status"] = response[0]
                result["response"] = response[1]
                result["device"] = self.__device
                result["connection"] = "Serial"
                result["count"] = len(arg)
                self.__termHandler.test_print(result)
                self.__results.append(result)

    def test_comm(self, command, argument):
        
        self.__sio.write(bytes(command, 'utf8'))
        self.__sio.write(b'\r')
        self.__sio.write(bytes(argument, 'utf8'))
        self.__sio.write(b'\x1A\r')
        
        
        answer = None
        # self.__sio.flush() # it is buffering. required to get the data out *now*

            
        at_value = self.__sio.readlines()

        dec_at_value = at_value[-1].decode('utf-8')
        respons = dec_at_value.strip(".\r\n")
        
        answer, respons = self.wait_until(respons,90,2)
        
        if answer:
            return respons
        else:
            return respons
        # print(at_value[-1])       
            

    def exec_command(self, command, argument,expects):
        response = self.test_comm(command, argument)

        if response == expects:
            return "Passed", response
        else:
            return "Failed", response

    def get_results(self):
        return self.__results

    def wait_until(self, kfind, timeout, period=0.25):
        mustend = time.time() + timeout
        while time.time() < mustend:
          if kfind == 'OK' or kfind == 'FAIL': return True, kfind
          
          at_value = self.__sio.readlines()
        #   print(at_value)
          if at_value == []:
            continue

          dec_at_value = at_value[-1].decode('utf-8')
          
          
          kfind = dec_at_value.strip(".\r\n")
          
          time.sleep(period)
        return False, 'Error'
    
    def send_message(self, argument, command):
        try:
            self.__sio.write(command)
            time.sleep(5)

            self.__sio.write(argument)
            
            self.__sio.write('\x1A\r')
            self.__sio.write(ascii.ctrl('Z'))
            # self.__sio.write(("aaa" +"\r").encode)
            # self.__sio.write(bytes[26])
            time.sleep(5)
            # self.__sio.flush() # it is buffering. required to get the data out *n
    
            # at_value = self.__sio.readlines()
            # respons = at_value[-1].strip(".\n")

        except Exception as error:
            raise Exception (error)


