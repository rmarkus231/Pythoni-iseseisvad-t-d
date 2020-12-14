#iseseisev ülessane nr 4
#Väljasta samasugune “Eesti lipp”
#richard markus tins it20
from colorama import Fore
#tekst
a="*"
b="="
c="-"

#prindib igat asja 4 rida 30 korda vajalikus värvis
for i in range(4):
    print(f"{Fore.BLUE}{a*30}")
for i in range(4):
    print(f"{Fore.BLACK}{b*30}")
for i in range(4):
    print(f"{Fore.WHITE}{c*30}")
