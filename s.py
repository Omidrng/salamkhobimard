import os, sys ,platform , socket , subprocess , time , json
from requests import get , post
from colorama import Fore , init
os.system('clear')
baner = '''
  ██████  ███▄    █   ██ ██▓███  ▓█████ ██▀███  
▒██    ▒  ██ ▀█   █ ▒▓██▓██░  ██ ▓█   ▀▓██ ▒ ██▒
░ ▓██▄   ▓██  ▀█ ██▒░▒██▓██░ ██▓▒▒███  ▓██ ░▄█ ▒
  ▒   ██▒▓██▒  ▐▌██▒ ░██▒██▄█▓▒ ▒▒▓█  ▄▒██▀▀█▄  
▒██████▒▒▒██░   ▓██░ ░██▒██▒ ░```   ░░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ░▓ ▒▓▒░ ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░  ░ ░░   ░ ▒░  ▒ ░▒ ░      ░ ░    ░▒ ░ ▒░
░  ░  ░     ░   ░ ░   ▒ ░░          ░     ░   ░ 
      ░           ░   ░             ░     ░     

1.SmsBomber
2.Ip Target 
'''
print(baner)
def Exit():
    input_exit = input('\nExit (Y/N) : ')
    if input_exit == 'Y' or input_exit == 'y':
        sys.exit()
    else:
        start()

def start():
    try:
      def smsBomber():
          os.chdir('bomber')
          os.system('python3 mian.py')
      def Ip_Target():
          os.chdir('IP')
          port = input('Enter Port : ')
          os.system(f'sudo python3 IP.py 127.0.0.1:{port}')
      def Hack_Instagram_Gmail():
          os.system('clear')
          print('''
1.instagram

          2.Gmailz

          99.Back
          ''')
          x=input('Enter >> ')
          if x == "1":           
            port = input('Enter Port : ')
            os.chdir('instagram')
            os.system(f'sudo python3 instagram.py 127.0.0.1:{port}')
            
          






















      x = input('Enter : ')
      if x == "1":
        smsBomber()
      elif x == "2":
          Ip_Target()
      elif x == "3":
          Hack_Instagram_Gmail()
    except KeyboardInterrupt:
        Exit()

start()