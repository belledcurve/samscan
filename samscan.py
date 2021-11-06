#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import _thread
import time

class roloc:
    HAD = '\033[95m'
    BLU = '\033[94m'
    GRE = '\033[92m'
    WAR = '\033[93m'
    WARN = '\033[91m'
    PCXS = '\033[0m'
    GUL = '\033[1m'
    ULE = '\033[4m'

class Core(object):
    ipurl=0
    mode=1024
    menu1=False
    f=None
    network_speed=" - LAN -"
    menu2=False
    def GetData(self, url):
        self.url = url
        try:
            self.ipurl = socket.gethostbyname(self.url)
        except Exception as e:
            print ("! -- INVALID -- !")
            exit(0)
        Core.ipurl=self.ipurl
        print (20*"\n")
        print (40*" -")
        print (15*" ",roloc.WARN,"💤 THE MOST LAZY PORT SCANNER - < S A M S C A N > 💤",roloc.PCXS)
        print (40*" -")
        print (5*"\n")
        while Core.menu1 is not True:
            choice = input("\n  1 - SAMSCAN 🦥 \n  2 - Advanced & Extended Scan 🔎 \n\n\n 🦥 > ")
            if choice == "1":
                Core.mode=1024
                menu=True
                break
            elif choice == "2":
                Core.mode=64000
                menu = True
                break
            else:
                print("🦥 INVALID 🦥")
        while Core.menu2 is not True:
            choice = input("\n  1 - LOCAL 🏠🦥💤\n  2 - GLOBAL 🌏🦥💤\n\n 🦥 > ")
            if choice == "1":
                Core.network_speed=0.05
                menu2=True
                break
            elif choice == "2":
                Core.network_speed=0.3
                menu2 = True
                break
            else:
                print("🦥 INVALID 🦥")

    def Start_Scan(self, port_start, port_end):
        Core.f = open(Core.ipurl, "a")
        try:
            for x in range(port_start,port_end):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = sock.connect_ex((Core.ipurl,x))
                if res == 0:
                    tmp=" 💤 Port ",x,"is open !", socket.getservbyport(x)
                    tmp1=str(tmp[0])+" "+str(tmp[1])+" "+str(tmp[2])+" "+str(tmp[3])
                    print(roloc.GRE,tmp1)
                    Core.f.write(str(tmp)+"\n")
            Core.f.close()
        except Exception as e:
            print (e)
try:
    scan = Core()
    scan.GetData(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                💤 🦥 SAMSCAN - The Lazy Port Scanner 🦥 💤  \n\n                                                    ver 1.5.8.0 \n\n\n\n\n\n\n\n   > Type in IP or URL below <\n\n\n\n 🦥 > "))
    print(roloc.WAR,"scan range:",Core.mode,"\n target:",Core.ipurl,"\n current speed:",Core.network_speed,roloc.PCXS)
    print(roloc.GUL,"please wait...",roloc.PCXS)
    for count in range(0,Core.mode):
        #print (Core.mode)
        time.sleep(Core.network_speed)
        _thread.start_new_thread(scan.Start_Scan, (count,count+1))
        if count > Core.mode:
            exit(0)
except Exception as e:
    print (e)
