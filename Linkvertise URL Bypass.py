import requests, argparse, sys, os
from colorama import Fore, Style

if sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", dest="urltobypass", help="Linkvertise URL")
args = parser.parse_args()

print("""\033[34m
                ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝""")
print(Fore.WHITE + """                                
                            Author : """ + Fore.GREEN + """@ASR827                                                                            
""")


def bypass(url):
    if url:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Referer': 'https://thebypasser.com/','Origin': 'https://thebypasser.com','DNT': '1','Connection': 'keep-alive','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'cross-site'}
        response = requests.get('https://bypass.bot.nu/bypass2?url='+url, headers=headers, allow_redirects=True)
        if response.status_code == 200:
            if response.json()["success"]:
                print(Fore.WHITE + "\n┌[" + Fore.RED + "LB API" + Fore.WHITE + "]─[" + Fore.RED + "SCARLETTA'S LOUNGE" + Fore.WHITE + "]\n│\n" +Fore.WHITE + "└[" + Fore.GREEN + "*" + Fore.WHITE + "] Successfully bypassed: " + Style.BRIGHT+  Fore.GREEN + response.json()["destination"] + Style.RESET_ALL)
            else:
                print("\n┌[" + Fore.BLUE + "LB API" + Fore.WHITE + "]─[" + Fore.BLUE + "SCARLETTA'S LOUNGE" + Fore.WHITE + "]\n│\n" +Fore.WHITE + "└[" + Fore.RED + "!" + Fore.WHITE + "] Not bypassed: " + Style.BRIGHT + Fore.RED + url+ Style.RESET_ALL)
        else:
            print("\n┌[" + Fore.BLUE + "LB API" + Fore.WHITE + "]─[" + Fore.BLUE + "SCARLETTA'S LOUNGE" + Fore.WHITE + "]\n│\n" +Fore.WHITE + "└[" + Fore.RED + "!" + Fore.WHITE + "] Not bypassed: " + Style.BRIGHT + Fore.RED + url + Style.RESET_ALL)

    else:
        return False


if args.urltobypass:
    bypass(args.urltobypass)
else:
    bypass(input(Fore.YELLOW + ">> " + Fore.CYAN + "Give linkvertise url : "))
