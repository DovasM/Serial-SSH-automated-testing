import argparse
from colorama import Fore, Back, Style
import colorama
import time
import sys
import curses

class TerminalHandler:

    __passed = 1
    __test_pass = 0

    def __init__(self):
        colorama.init()
        pass

    def get_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("-n", "--name", dest = "name", default = "", help="Routers model", required=True)
        parser.add_argument("-pt", "--port", dest = "pt", help="Routers port", default=argparse.SUPPRESS)
        parser.add_argument("-u", "--username",dest ="username", help="User name", default=argparse.SUPPRESS)
        parser.add_argument("-p", "--password",dest = "password", help="Password", default=argparse.SUPPRESS)
        parser.add_argument("-b", "--baudrate",dest = "baudrate", help="Serial baudrate", type=int, default=argparse.SUPPRESS)
        parser.add_argument("-i", "--ip",dest = "ip", help="IP address", default=argparse.SUPPRESS)

        args = parser.parse_args()

        return args

    def test_print(self, results):
        if self.__passed == 1:
            print('{}:Testing device                '.format(results["device"]))
            print('{}:Connection type               '.format(results["connection"]))
            print('{}/{}:Tests Count                  '.format(self.__passed, results["count"]))
            print(Fore.BLUE + '{}/{}:Tests passed             '.format(self.__test_pass,results["count"])+Style.RESET_ALL )
            print('{}:The command under the test                '.format(results['command']))
            print('{}:Result              '.format(results['response']))
            if results['status'] == 'Passed':
                print(Fore.GREEN + '{}:Test            '.format(results['status'])+Style.RESET_ALL , end="")
                self.__test_pass = self.__test_pass + 1
            else:
                print(Fore.RED + '{}:Test               '.format(results['status'])+Style.RESET_ALL , end="")
            sys.stdout.flush()
            self.__passed = self.__passed + 1

        else:
            if results['status'] == 'Passed':
                print(Fore.GREEN + '\r{}:Test             '.format(results['status'])+Style.RESET_ALL )
                self.__test_pass = self.__test_pass + 1
            else:
                print(Fore.RED + '\r{}:Test                    '.format(results['status'])+Style.RESET_ALL )
            print('\033[F\033[F{}:Result                   '.format(results['response']))
            print('\033[F\033[F{}:The command under the test                '.format(results['command']))
            print('\033[F\033[F{}/{}:Tests Passed/Count                     '.format(self.__passed, results["count"]))
            print(Fore.BLUE + '\033[F\033[F{}/{}:Tests passed                      '.format(self.__test_pass,results["count"])+Style.RESET_ALL )
            print('\033[F\033[F{}:Connection type                  '.format(results["connection"]))
            print('\033[F\033[F{}:Testing device              '.format(results["device"]))
            print()
            print()
            print()
            print()
            print()
            self.__passed = self.__passed + 1
            
        if self.__passed == results["count"]+1:
            print()