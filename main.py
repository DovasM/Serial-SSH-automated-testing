from sqlite3 import connect
from unittest import result
import modules.config_handler as ConfigHandler
import modules.ssh_client as SshHandler
import modules.test_handler as TestHandler
import modules.result_handler as ResultHandler
import modules.serial_client as SerialHandler
import modules.terminal_handler as TerminalHandler

config = None
ssh = None
tester = None
resulter = None

def init_modules():
    global config, ssh, tester, resulter, conn, terminal_flags, term_args
    try:
        terminal_flags = TerminalHandler.TerminalHandler()
        term_args = terminal_flags.get_args()
        config = ConfigHandler.ConfigHandler("config.json")
        conn = SerialHandler.ConnectionHandler(term_args.name, term_args.pt)
        # ssh = SshHandler.SshHandler(config)
        tester = TestHandler.TestHandler(ssh)
        resulter = ResultHandler.ResultHandler(config.get_param("results")["save_as"])
        
        
    except Exception as error:
        raise Exception (error)


def main():
    try:
        init_modules()
        resulter.open_file(config.get_param("results")["path"])
        # tester.test_commands(config.get_param("commands"))
        # conn.send_message("tekstas")
        conn.exec_commands(config.get_comm(term_args.name))
        # print(conn.get_results())
        # resulter.save_results(conn.get_results())
        # resulter.close_file()
        
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()