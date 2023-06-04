import sys
import socket

def port_scan(target_host, target_ports):
    open_ports = []

    for port in target_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                open_ports.append(port)
        except:
            print("olmadi")

    return open_ports

if __name__ == "__main__":
    target_host = str(sys.argv[1])

    target_ports = []

    for port in range(0,int(sys.argv[2])):
        target_ports.append(port)

    open_ports = port_scan(target_host, target_ports)
    print(f"Open ports:  {open_ports}")
# "[80,22,21,1234]"
#  80,22,21,1234]
#  80,22,21,1234
#  80 22 21 1234
#  ["80","22","21","1234"]
#  [80,22,21,1234]
