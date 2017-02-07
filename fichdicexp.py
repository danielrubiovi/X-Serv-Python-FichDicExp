#!-/usr/bin/python3

fich = open('/etc/passwd','r')
lista_lineas = fich.readlines()
dic_logins = {}

for usuario in lista_lineas:
    lista_split = usuario.split(":")
    login = lista_split[0]
    shell = lista_split[-1][:-1]
    dic_logins[login] = [shell]

print ('root: ', dic_logins['root'])
try:
    print ('imaginario: ', dic_logins['imaginario'])

except:
    print ("ERROR, user don't found")

print ('Numero de usuarios: ', len(dic_logins))

fich.close()
