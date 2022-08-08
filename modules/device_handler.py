import os
import json


class DeviceHandler:

    __devices = None

    def __init__(self, config):
        global __devices
        try:
            __devices = config.get_param("devices")
        except Exception as error:
            print(error)
    
    def device_conn_select(self, device):
        conn = None
        for devices in __devices:
            if devices['device'] == device:
                conn = devices['connection'] + '_client'
        return conn
        
    # def __device_conn_select(self, device):
    #     conn = None
    #     for devices in __devices:
    #         if devices['device'] == device:
    #             conn = devices['connection']
    #     return conn