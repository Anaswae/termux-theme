import os
import time
import sys

r="\x1b[91;1m"
g="\x1b[32;1m"
y="\x1b[33;1m"
p="\x1b[34;1m"
c="\x1b[36;1m"
o="\x1b[37;1m"
w="\x1b[00m"
u="\x1b[4m"
b="\x1b[5m"

def sprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

logo = """
████████ ██   ██ ███████ ███    ███ ███████ 
   ██    ██   ██ ██      ████  ████ ██      
   ██    ███████ █████   ██ ████ ██ █████   
   ██    ██   ██ ██      ██  ██  ██ ██      
   ██    ██   ██ ███████ ██      ██ ███████ 
                                            
   \033[41m    TERMUX THEME BY SAYDOG OFFICIAL    \033[00m"""
def mainmenu():
        try:
                os.system ("clear")
                sprint (o+logo)
                print ("")
                print (w+"this tool is made to facilitate terminal users")
                print (w+"hopefully useful, thanks!")
                print ("")
                print ("01"+r+")"+w+" ascii logo")
                print ("02"+r+")"+w+" font style")
                print ("03"+r+")"+w+" background colors")
                print ("04"+r+")"+w+" prompt style")
                print ("05"+r+")"+w+" zsh theme")
                print ("06"+r+")"+w+" open zshrc")
                print ("00"+r+")"+w+" exit")
                print("")
                saydog()
        except KeyboardInterrupt:
                sys.exit(1)

def saydog():
        pil = str(input("["+r+"~"+w+"]"+r+" > "+w))
        if pil == "0" or pil == "00":
                sys.exit(1)
        elif pil == "1" or pil == "01":
                print ("")
                print ("\033[41mASCII LOGO\033[00m")
                print ("customize ascii logo for terminal theme")
                print ("")
                print ("01"+r+")"+w+" get ascii logo from list")
                print ("02"+r+")"+w+" generate ascii logo from files")
                print ("03"+r+")"+w+" set logo manually")
                print ("")
                pil = str(input("["+r+"~/"+w+"asciilogo"+r+"/"+w+"]"+r+" > "+w))
                if pil == "back":
                        saydog()
                elif pil == "1" or pil == "01":
                        os.system("cd lib;python ascii.py")
                        print ("")
                        print (r+"HOW TO USE"+w)
                        print ("copy your favorite logo")
                        print ("then put your logo in the logo.txt file ")
                        print ("you can provide a color for the logo")
                        print ("that you have saved before")
                        print ("")
                        pil = str(input("do you want to open logo.txt file ? (y/n) "))
                        if pil == "y" or pil == "Y":
                                print ("")
                                print (c+"[+]"+w+" opening logo.txt")
                                print (c+"[+]"+w+" paste your logo in this file")
                                print (c+"[+]"+w+" and save your logo with CTRL + X + Y and ENTER")
                                print ("")
                                time.sleep(6)
                                os.system("nano cache/logo.txt")
                                os.system("cat cache/d1 > logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                print (c+"[+]"+w+" files saved as cache/logo.txt")
                                print (c+"[+]"+w+" success")
                                print ("")
                                pil = str(input("do you want to add color ? (y/n) "))
                                if pil == "y" or pil == "Y":
                                        print ("")
                                        print (w+"01"+r+")"+w+" red")
                                        print (w+"02"+r+")"+w+" yellow")
                                        print (w+"03"+r+")"+w+" green")
                                        print (w+"04"+r+")"+w+" purple")
                                        print (w+"05"+r+")"+w+" cyan")
                                        print (w+"06"+r+")"+w+" blue")
                                        print (w+"07"+r+")"+w+" dark red")
                                        print (w+"08"+r+")"+w+" dark yellow")
                                        print (w+"09"+r+")"+w+" dark green")
                                        print (w+"10"+r+")"+w+" dark purple")
                                        print (w+"11"+r+")"+w+" dark cyan")
                                        print (w+"12"+r+")"+w+" dark blue")
                                        print ("")
                                        pil = str(input("color number"+r+" => "+w))
                                        if pil == '1' or pil == "01":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '2' or pil == "02":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '3' or pil == "03":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '4' or pil == "04":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '5' or pil == "05":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '6' or pil == "06":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '7' or pil == "07":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '8' or pil == "08":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '9' or pil == "09":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '10':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '11':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '12':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                else:
                                        mainmenu()
                        else:
                                mainmenu()
                elif pil == "2":
                        print ("")
                        print (c+"[+]"+w+" image to ascii")
                        print (c+"[+]"+w+" checking access to storage")
                        os.system("termux-setup-storage")
                        print (c+"[+]"+w+" make sure the image type is jpg / jpeg")
                        print ("")
                        print (r+"HOW TO USE")
                        print (w+"please input the image directory")
                        print (w+"example: /sdcard/download/image.jpg")
                        print ("")
                        img = input(w+"choose files"+r+" => ")
                        print (c+"[+]"+w+" generating ascii")
                        os.system("jp2a "+img)
                        pil = str(input("do you want to use this logo ? (y/n) "))
                        if pil == "y" or pil == "Y":
                                print ("")
                                os.system("jp2a "+img+" > cache/logo.txt")
                                print (c+"[+]"+w+" file saved as cache/logo.txt")
                                print ("")
                                pil = str(input("do you want to add color ? (y/n) "))
                                if pil == "y" or pil == "Y":
                                        print ("")
                                        print (w+"01"+r+")"+w+" red")
                                        print (w+"02"+r+")"+w+" yellow")
                                        print (w+"03"+r+")"+w+" green")
                                        print (w+"04"+r+")"+w+" purple")
                                        print (w+"05"+r+")"+w+" cyan")
                                        print (w+"06"+r+")"+w+" blue")
                                        print (w+"07"+r+")"+w+" dark red")
                                        print (w+"08"+r+")"+w+" dark yellow")
                                        print (w+"09"+r+")"+w+" dark green")
                                        print (w+"10"+r+")"+w+" dark purple")
                                        print (w+"11"+r+")"+w+" dark cyan")
                                        print (w+"12"+r+")"+w+" dark blue")
                                        print ("")
                                        pil = str(input("color number"+r+" => "+w))
                                        if pil == '1' or pil == "01":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '2' or pil == "02":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '3' or pil == "03":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '4' or pil == "04":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '5' or pil == "05":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '6' or pil == "06":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '7' or pil == "07":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '8' or pil == "08":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '9' or pil == "09":
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '10':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '11':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                                        elif pil == '12':
                                                os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                                print ("")
                                                print (c+"[+]"+w+" color has been added")
                                                print (c+"[+]"+w+" generating python file")
                                                time.sleep(3)
                                                print (c+"[+]"+w+" your file has been generated")
                                                print (c+"[+]"+w+" file saved as mylogo.py")
                                                print ("")
                                                pil = str(input(r+"["+w+"  enter "+r+"]"))
                                                if pil == '':
                                                        mainmenu()
                                                else:
                                                        mainmenu()
                        elif pil == "n" or pil == "N":
                                mainmenu()
                elif pil == "3" or pil == "03":
                        print ("")
                        print (c+"[+]"+w+" please put your logo in logo.txt files")
                        print (c+"[+]"+w+" save with CTRL + X + Y and ENTER")
                        print (c+"[+]"+w+" opening logo.txt")
                        time.sleep(6)
                        os.system("nano cache/logo.txt")
                        print (c+"[+]"+w+" file saved as cache/logo.txt")
                        print ("")
                        pil = str(input("do you want to add color ? (y/n) "))
                        if pil == "y" or pil ==  "Y":
                                print ("")
                                print (w+"01"+r+")"+w+" red")
                                print (w+"02"+r+")"+w+" yellow")
                                print (w+"03"+r+")"+w+" green")
                                print (w+"04"+r+")"+w+" purple")
                                print (w+"05"+r+")"+w+" cyan")
                                print (w+"06"+r+")"+w+" blue")
                                print (w+"07"+r+")"+w+" dark red")
                                print (w+"08"+r+")"+w+" dark yellow")
                                print (w+"09"+r+")"+w+" dark green")
                                print (w+"10"+r+")"+w+" dark purple")
                                print (w+"11"+r+")"+w+" dark cyan")
                                print (w+"12"+r+")"+w+" dark blue")
                                print ("")
                                pil = str(input("color number"+r+" => "+w))
                                if pil == '1' or pil == "01":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '2' or pil == "02":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '3' or pil == "03":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '4' or pil == "04":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '5' or pil == "05":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '6' or pil == "06":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34;1m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '7' or pil == "07":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '91m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '8' or pil == "08":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '33m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '9' or pil == "09":
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '32m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '10':
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '35m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '11':
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '36m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                                elif pil == '12':
                                        os.system("cat cache/d1 > logo.txt;cat cache/garing >> logo.txt;echo '34m' >> logo.txt;cat cache/logo.txt >> logo.txt;cat cache/d2 >> logo.txt;cat logo.txt > mylogo.py;rm logo.txt")
                                        print ("")
                                        print (c+"[+]"+w+" color has been added")
                                        print (c+"[+]"+w+" generating python file")
                                        time.sleep(3)
                                        print (c+"[+]"+w+" your file has been generated")
                                        print (c+"[+]"+w+" file saved as mylogo.py")
                                        print ("")
                                        pil = str(input(r+"["+w+"  enter "+r+"]"))
                                        if pil == '':
                                                mainmenu()
                                        else:
                                                mainmenu()
                        else:
                                mainmenu()
                else:
                        mainmenu()
        elif pil == "2" or pil == "02":
                print ("")
                print ("\033[041mFONT STYLE\033[00m")
                print ("customize font style for terminal")
                os.system ("~/.termux/fonts.sh")
                mainmenu()
        elif pil == "3" or pil == "03":
                print ("")
                print ("\033[041mBACKGROUND COLOR\033[00m")
                print ("Customize background color for terminal")
                os.system ("~/.termux/colors.sh")
                mainmenu()
        elif pil == "4" or pil == "04":
                print ("")
                print ("\033[41mPROMPT STYLE\033[00m")
                print ("Customize prompt style for terminal")
                print ("")
                print (w+"[1] Yourname@root:~#")
                print (w+"[2] Custom manually")
                print ("")
                pil = str(input("Enter a number, leave blank to not to change: "))
                if pil == "back":
                        saydog()
                elif pil == "1" or pil == "01":
                        name = str(input(w+"please input your username here: "))
                        print ("")
                        print (c+"[+]"+w+" generate prompt style")
                        print (c+"[+]"+w+" use username "+name)
                        print ("")
                        os.system("echo "+'"PS1='+"'"+name+"@root:~# '"+'"'+" >> ~/.zshrc")
                        time.sleep(3)
                        print (c+"[+]"+w+" success")
                        print (c+"[+]"+w+" please restart your terminal")
                        print ("")
                        pil = str(input("do you want to exit this tool ? (y/n) "))
                        if pil == "y" or pil == "Y":
                                sys.exit(0)
                        else:
                                mainmenu()
                elif pil == "2" or pil == "02":
                        print ("")
                        print (c+"[+]"+w+" opening files myprompt.txt")
                        print (c+"[+]"+w+" please put your prompt code in this file")
                        print (c+"[+]"+w+" save file with CTRL + X + Y and ENTER")
                        time.sleep(6)
                        print ("")
                        os.system("nano cache/myprompt.txt")
                        print ("")
                        print (c+"[+]"+w+" file saved as cache/myprompt.txt")
                        print (c+"[+]"+w+" cloning into zshrc ...")
                        os.system("cat cache/myprompt.txt >> ~/.zshrc")
                        time.sleep(3)
                        print (c+"[+]"+w+" success, please restart your terminal")
                        pil = str(input("do you want to exit this tool ? (y/n) "))
                        if pil == "y" or pil == "Y":
                                sys.exit(0)
                        else:
                                mainmenu()
                else:
                        time.sleep(1)
                        mainmenu()
        elif pil == "5" or pil == "05":
                print ("")
                try:
                        os.system("cd /data/data/com.termux/files/home/.oh-my-zsh/tools;./theme_chooser.sh")
                        pil = str(input("do you want to back to mainmenu ? (y/n) "))
                except KeyboardInterrupt:
                        time.sleep(1)
                        mainmenu()
        elif pil == "6" or pil == "06":
                print ("")
                print (c+"[+]"+w+" opening zshrc files")
                print (c+"[+]"+w+" please wait ...")
                time.sleep(1)
                print (c+"[+]"+w+" success")
                os.system('nano ~/.zshrc')
                print ("")
                pil = str(input("back to mainmenu ? (y/n) "))
                if pil == "y" or pil == "Y":
                        mainmenu()
                else:
                        sys.exit(0)
        else:
                saydog()

## MAIN
os.system("curl -s ifconfig.co > cache/ip.txt")
mainmenu()