from colorama import Fore
from time import sleep
import os
import sys

os.system("clear")

print (Fore.GREEN)

print ("""_ __ ___   ___ _ __ ___ | |__   ___ _ __
| '_ ` _ \ / _ \ '_ ` _ \| '_ \ / _ \ '__|
| | | | | |  __/ | | | | | |_) |  __/ |
|_| |_| |_|\___|_| |_| |_|_.__/ \___|_|\n""")
print (Fore.WHITE+"Phone number"+" . "+Fore.YELLOW+"09929115957\n"+Fore.WHITE+"Creator . Lockader :"+" "+Fore.YELLOW+"Mr . Weblog Or Mr . Black\n")

print (Fore.RED)

print ("""
                        1 = Enter the 0911=>
                        2 = Enter the 0933=>
                        3 = Enter the number =>
                        0 = exit=>""")

x = input ("Enter the member==> ")
print (Fore.RED+"\n.....\n")
sleep(1)
print (Fore.YELLOW+"..........\n")
sleep(1)
print (Fore.BLUE+"...............\n")
sleep(1)
print (Fore.WHITE+"....................\n")
sleep(1)
print (Fore.YELLOW+".........................\n")
sleep(1)
member = '1'
member_2 = '2'
member_3 = '3'
member_4 = '0'
print (Fore.YELLOW)
if x == member:
    f = open('/sdcard/members.txt')
    for i in f:
    	print (i)
if x == member_2:
    f2 = open('/sdcard/members2.txt')
    for i in f2:
    	print (i)
if x == member_3:
	f3 = open('/sdcard/members3.txt')
	for i in f3:
		print (i)
while x != member_4:
    x = input("\nTHE END")