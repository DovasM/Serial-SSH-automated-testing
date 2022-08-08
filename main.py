from sqlite3 import connect
from unittest import result
import modules.config_handler as ConfigHandler
import modules.ssh_client as SshHandler
import modules.test_handler as TestHandler
import modules.device_handler as DeviceHandler
import modules.result_handler as ResultHandler
import modules.serial_client as SerialHandler
import modules.terminal_handler as TerminalHandler

config = None
ssh = None
tester = None
resulter = None
device = None
flags = None
__connHandler = None

def __load_module(type, flags, config):
        module = None
        try:
            module = __import__('modules.{type}'.format(type=type), fromlist=['modules'])
            return module.ConnectionHandler(flags, config)
        except Exception as error:
            raise Exception (error)  

def init_modules():
    global config, tester, resulter, terminal_flags, device
    try:
        terminal_flags = TerminalHandler.TerminalHandler()
        flags = terminal_flags.get_args()
        config = ConfigHandler.ConfigHandler("config.json")
        device = DeviceHandler.DeviceHandler(config)
        __connHandler = __load_module(device.device_conn_select(flags.name), flags, config)
        tester = TestHandler.TestHandler(ssh, flags.name)
        resulter = ResultHandler.ResultHandler(config.get_param("results")["save_as"])
        
        
    except Exception as error:
        raise Exception (error)



def main():
    try:
        init_modules()
        
        resulter.open_file(config.get_param("results")["path"])
        resulter.save_results(tester.get_results())
        resulter.close_file()
        
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()