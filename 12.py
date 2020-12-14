#iseseisev ülessane nr 12
#Koosta programm, mis joonistab tsüklite abil samasugused kolmnurgad
#richard markus tins it20
x=1
t="*"

#a)
for i in range(2):
    print(t*x)
    x=x+2
for i in range(3):
    print(t*x)
    x=x-2
    
print("\n")
#b)
z=5
for i in range(5):
    print(t*z)
    z=z-1

print("\n")
#c)
c=1
for i in range(6):
    print(t*z)
    z=z+1

print("\n")
#d)
v=5
for i in range(4):
    print(t*v)
    v=v-1
for i in range(5):
    print(t*v)
    v=v+1