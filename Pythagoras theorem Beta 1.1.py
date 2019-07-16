#Math project




#Teorema de pitagoras
#a**2 + b**2 = c**2

#variables



print ('||Beta 1.1 pythagoras theorem||')

print('')

print ('<Type 0 where x should be.>')

print('')

a = float(input(' -Length of the leg a- ' ))

b = float(input(' -Length of the leg b- ' ))

c = float(input(' -Length of the hypotenuse c- ' ))


if c == 0 :
    c_squared = a**2 + b**2
    print(c_squared)

elif a == 0 :

      cateto_1 = c**2 - b**2
      print(cateto_1)
      

elif b ==  0 :
     cateto_2 = c**2 - a**2
     print(cateto_2)
     


else :

    print ('Error')
    

