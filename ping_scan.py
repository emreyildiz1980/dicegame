import sys
import platform
import subprocess

def ping_scan(target_ip):
    try:
        if platform.system().lower() == "windows":
            ping_command = f"ping -n 1 {target_ip}"
        else:
            ping_command = f"ping -c 1 {target_ip}"
        output = subprocess.getoutput(ping_command)
        if "%0 packet loss" in output or "64 bytes" in output:
            return True
        else:
            return False
    except:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Please provide only one argument!')
    target_ip = str(sys.argv[1])
    is_alive = ping_scan(target_ip)

    if is_alive:
        print(f"The Ip address {target_ip} is alive.")
    else:
        print(f"The Ip address {target_ip} is unreachable.")


