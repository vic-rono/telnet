import getpass
import telnetlib

HOST = "192.168.122.71"
user = input("Enter your telenet username ")
password = getpass.getpass()

telnet = telnetlib.Telnet(HOST)

telnet.read_until(b"Username: ")
telnet.write(user.encode('ascii') + b"\n")
if password:
    telnet.read_until(b"Password: ")
    telnet.write(password.encode('ascii') + b"\n")

telnet.write(b"enable\n")
telnet.write(b"cisco\n")
telnet.write(b"conf t\n")
telnet.write(b"int loop 0\n")
telnet.write(b"ip address 1.1.1.1 255.255.255.255\n")
telnet.write(b"int loop 1\n")
telnet.write(b"ip address 2.2.2.2 255.255.255.255\n")
telnet.write(b"router ospf 1\n")
telnet.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
telnet.write(b"end\n")
telnet.write(b"exit\n")

print(telnet.read_all().decode('ascii'))

