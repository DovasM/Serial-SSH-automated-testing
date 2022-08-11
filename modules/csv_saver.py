import time
import ftplib

class ResultSaver:

    ___file = None
    __file_path = None
    __file_name = None

    def __init__(self):
        pass


    def open_file(self, path):
        if not path:
            self.__file_name =  str(time.time()) + "_test.csv"
            self.__file_path = "./results/" + self.__file_name
        try:
            log = open(self.__file_path, "w")
            self.__file = log
        except:
            raise Exception("Unable to open file to save results")

    def close_file(self):
        if self.__file:
            self.__file.close()
            

    def save_results(self, results):
        header = "Command,Expects,Status,Response\n"
        self.__write_to_file(header)
        for result in results:
            formatedString = self.__format_string(result)
            self.__write_to_file(formatedString)


    def __write_to_file(self, string):
        self.__file.write(string)

    def saved_file_info(self):
        arg = self.__file_name, self.__file_path
        return arg

    def __format_string(self, result):
        return result["command"] + "," + str(result["expects"]) + "," + result["status"] + "," + str(result["response"]) +"\n"

