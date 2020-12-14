#iseseisev ülessane nr 8
#Kirjuta programm, mis muudab lause tagurpidiseks.
#richard markus tins it20

#küsib lause
l = input("Sisesta lause mida tagurpidi pöörata: ")
#teeb lause listiks
s= l.split()
#keerab listi teistpidi
s=s[::-1]
#teeb listi lauseks
rl=" ".join(s)
#prindib tagurpidi lause
print(rl)