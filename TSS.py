import requests
import time, requests, os
from colorama import Fore
os.system('pip install requests')
os.system('pip install colorama')
os.system('cls')
os.system('Title Token Server Spammer/By Qu3ti')
print(f"""{Fore.RED}
 @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@
============Token Server Spammer By Qu3ti============
========Github: https://github.com/qu3tiiii==========

""")
token = input(f"Token: {Fore.RESET}")
text = input(f"{Fore.RED}Nombre De Canales: {Fore.RESET}")
headers={
    "authorization": f"{token}",
    "content-type": "application/json"
    }
payload={
   "name": f"{text}"
    }
while True:
    requests.post("https://discord.com/api/v8/guilds",json=payload,headers=headers) 
    print(f"{Fore.GREEN}[+] - {Fore.RED}{text}{Fore.RESET}{Fore.GREEN} Creado ! - [+]")
