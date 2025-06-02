#!/usr/bin/env python3
import argparse
import re
import subprocess
from termcolor import colored
def get_arguments():
    
    parser= argparse.ArgumentParser(description="Modificador de Mac de una interfaz de red")
    parser.add_argument("-i", "--interfaz", dest="interfaz", required=True, help="Nombre de  la interfaz de red")
    parser.add_argument("-m", "--mac", dest="mac__address",required=True,  help="Nueva direccion MAC para la interfaz de red")

    return parser.parse_args()


def is_valid_imput(interfaz, mac__address):
    
    is_valid_interface = re.match(r'^[e][n|t][s|h]\d{1,2}$', interfaz)
    is_valid_mac_address =  re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$',mac__address)

    return is_valid_mac_address and is_valid_mac_address

def change_mac_address(interfaz, mac__address):

    if is_valid_imput(interfaz, mac__address):
        subprocess.run(["ifconfig", interfaz, "down"])
        subprocess.run(["ifconfig", interfaz, "hw", "ether", mac__address])
        subprocess.run(["ifconfig", interfaz, "up"])
        print(colored(f"\n[+] La MAC se cambio exitosamente.\n", 'green'))

    else:
        print(colored(f"\n[!] No se introdujeron los datos adecuados.\n", 'red'))


def main():
    args = get_arguments()
    change_mac_address(args.interfaz, args.mac__address)

if __name__=='__main__':
    main()
