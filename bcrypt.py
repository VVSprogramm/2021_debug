#Datu šifrēšana

import bcrypt

parole = b'abols'

salt = bcrypt.gensalt() 
#ģenerējam salt

savienots = bcrypt.hashpw(parole,salt)

print(parole)
print(salt)
print(savienots)