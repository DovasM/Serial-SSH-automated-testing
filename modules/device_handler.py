class DeviceHandler:

     __devices = None

    def __init__(self, config):
        global __devices
        try:
            __devices = config.get_param("devices")
            
        except Exception as error:
            print(error)
        

    def __device_select(self):

        for device in __devices:
            

   