#iseseisev ülesanne nr 5
#Leia jadamisi ja rööpselt ühendatud takistite kogutakistus. Takistite arv ei pea olema suur.
#richard markus tins it20

#takistused
U1=int(input("esimese takisti takistus: "))
U2=int(input("teise takisti takistus: "))
U3=int(input("kolmanda takisti takistus: "))

#kogutakkistus jadaühenduses
print(f"Kogutakistus jadaühenduses on: {U1+U2+U3}")
#kogutakk
print(f"Kogutakistus rööpühenduses on: {U1*U2*U3/U1+U2+U3}")
