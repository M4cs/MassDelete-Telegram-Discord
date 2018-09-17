#!usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys, time, psutil, win32com.client

def main():
    print("""
Mass Discord Message Deleter by Macs

Delete Messages In Any Chat In Discord or Telegram Windows App.

With This You Will Be Able To Automate Deleting of Personal
Messages Without The Use Of A Selfbot.

Enjoy :)
    """)
    print("[?] How Many Messages Would You Like To Delete? [?]")
    num_of_msgs = input("[Int]» ")
    num_of_msgsq = int(num_of_msgs)
    os.system("cls")
    print("[?] How Quickly Would You Like To Delete? [?]")
    speed = input("[Fast, Medium, Slow]» ")
    if speed == "Fast" or "fast":
        speedq = 0.1
    elif speed == "Medium" or "medium":
        speedq = 0.5
    elif speed == "Slow" or "slow":
        speedq = 1
    os.system("cls")
    print("[!] Please Tab Into Discord... Waiting 5 Seconds... \ [!]\n[!] Please Don't Touch Anything After Going Into Discord [!]")
    time.sleep(1)
    os.system("cls")
    print("[!] Please Tab Into Discord... Waiting 4 Seconds... - [!]\n[!] Please Don't Touch Anything After Going Into Discord [!]")
    time.sleep(1)
    os.system("cls")
    print("[!] Please Tab Into Discord... Waiting 3 Seconds... / [!]\n[!] Please Don't Touch Anything After Going Into Discord [!]")
    time.sleep(1)
    os.system("cls")
    print("[!] Please Tab Into Discord... Waiting 2 Seconds... | [!]\n[!] Please Don't Touch Anything After Going Into Discord [!]")
    time.sleep(1)
    os.system("cls")
    print("[!] Please Tab Into Discord... Waiting 1 Seconds... \ [!]\n[!] Please Don't Touch Anything After Going Into Discord [!]")
    time.sleep(1)
    os.system("cls")
    print("[!] Starting to Delete " + num_of_msgs + " Number of Messages [!]")
    try:
        count = 0
        while count <= int(num_of_msgsq):
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys("{UP}")
            time.sleep(speedq)
            shell.SendKeys("^a")
            time.sleep(speedq)
            shell.SendKeys("{DELETE}")
            time.sleep(speedq)
            shell.SendKeys("{ENTER}")
            time.sleep(speedq)
            shell.SendKeys("{ENTER}")
            time.sleep(speedq)
            count = count + 1
    except KeyboardInterrupt:
        exit()
    os.system("cls")
    print("[!] Completed! The Evidence Has Been Destroyed. " + num_of_msgsq + " Messages Deleted Successfully! [!]")

main()
