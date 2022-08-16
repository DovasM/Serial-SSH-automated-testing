# Serial-SSH-automated-testing

**Description**

Iot testing program writen in python 3.9.5.

The goal of the project is to have the means to connect the IoT device using SSH or Serial connection
and using setuped AT commands test the device. 

## Usage
0. Download this package with `go get` or `git clone`
```
   go get -u github.com/goiiot/libserial
	 
	 git clone https://github.com/goiiot/libserial
```
1. In config.json set your device and command settings to test

```
"devices":[
       {
           "device":"RUTX11",
           "connection":"ssh",
           "commands":[
                {
                "command":"ATE1",
                "expects":"OK",
                "argument":""
                },
               {
                   "command":"ATI",
                   "expects":"OK",
                   "argument":""
               },
```
2. In config.json set your FTP server settings

```
"results":{
    "save_as":"csv",
    "path":""
 },
    "ftp_connection":{
        "address":"localhost",
        "username":"studentas",
        "password":"studentas"
    }
```

3. Start test with command

`sudo python3 main.py <settings>`

Settings you can use:

```
usage: main.py [-h] -n NAME [-pt PT] [-u USERNAME] [-p PASSWORD] [-b BAUDRATE] [-i IP] [-ftp FTP]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Routers model
  -pt PT, --port PT     Routers port
  -u USERNAME, --username USERNAME
                        User name
  -p PASSWORD, --password PASSWORD
                        Password
  -b BAUDRATE, --baudrate BAUDRATE
                        Serial baudrate
  -i IP, --ip IP        IP address
  -ftp FTP, --ftp FTP   Save FTP Y/N
```

## Examples

Testing with SSH connection:

`sudo python3 main.py -n RUTX11 -i 192.168.1.1 -u root -p Admin123`

Testing with Serial connection:

`sudo python main.py -n TRM240 -pt /dev/ttyDEV0`

Saving to FTP server:

`sudo python main.py -n TRM240 -pt /dev/ttyDEV0 -ftp Y`
