#!/usr/bin/env python3

import socket
import argparse
import sys
from termcolor import colored

BANNER = r"""
                         _
  ,-.      __,---.__   ,',`\
 / `.`. ,-'         `-/ /   )
(    `,'             _ \   ;
 \  _( _           ,'  )/  :
  \ `-( `-.      ,'    /  /
   \   \ __`.___/_,-( /_,'
    `--'`,\_o,(_)o_,',
        (    /`-'\    )
         `--:\,m//`--'
             `--'  
    Fast TCP Port Scanner..."""



def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Victim target to scan (Ex: -t 192.168.10.1)")
    parser.add_argument("-p", "--port", dest="port", required = True, help="Port range to scan Ej: -p 10-100 ")
    options= parser.parse_args()
    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s


def port_scanner(port, host, s):

    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto", 'green'))
    except (socket.timeout, ConnectionRefusedError):
        s.close()

def scan_ports(ports, target):
    for port in ports:
        s = create_socket()
        port_scanner(port, target, s)

def parse_ports(ports_str):

    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int,ports_str.split(','))
    else:
        return (int(ports_str),)


def main():
    
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)
if __name__=='__main__':
    print(BANNER)
    main()
