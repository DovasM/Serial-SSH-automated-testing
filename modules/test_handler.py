

class TestHandler:

    __connection = None
    __termHandler = None
    __device = None
    __results = []

    def __init__(self, connection, device):
        self.__connection = connection
        self.__device = device
        
        self.__termHandler = self.__load_module()
        if not self.__termHandler:
            raise Exception("Unable to load terminal handler module")

    def __load_module(self):
        module = None
        try:
            module = __import__('modules.terminal_handler', fromlist=['modules'])
            return module.TerminalHandler()
        except:
            return False      

    def test_commands(self, commands):
        
        self.__connection.exec_command("/etc/init.d/gsmd stop\r")
        
        for command in commands:
            result = {}
            
            response = self.test_command(command["command"], command["expects"], command["argument"])
            result["command"] = command["command"]
            result["expects"] = command["expects"]
            result["status"] = response[0]
            result["response"] = response[1]
            result["device"] = self.__device
            result["connection"] = "SSH"
            result["count"] = len(commands)
            self.__termHandler.test_print(result)
            self.__results.append(result)
            
        self.__connection.exec_command("/etc/init.d/gsmd start\r")

    def test_command(self, command, expects, argument):
        # command = 'gsmctl -A ' + command
        response = self.__connection.shell_exec_command(command, argument)
        
        if response == expects:
            return "Passed", response
        else:
            return "Failed", response
    
    def get_results(self):
        return self.__results