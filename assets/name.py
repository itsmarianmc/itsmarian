import random
import string

length = 32
loginID = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

nameAsk = input("Seid gegrüßt euer Herr,\nmöget ihr mir verraten, was euer Name sei?\n>> ")

if nameAsk == 'Ja':
    name = input("Füget euren Namen ein\n>> ")
    
    birth = input("Und dein Geburtstag?\n>> ")
elif nameAsk == 'Nein':
    print("Schade :(")
elif nameAsk == 'nein':
    print("Schade :(")


print("Du heißt " + name + " und hast am " + birth + " Geburtstag! \n\nLogin ID: " + loginID)
