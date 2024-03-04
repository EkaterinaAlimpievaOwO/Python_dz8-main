from input import *
import phonebook

pb = phonebook.Phonebook('data.txt')

flag = True
while(flag):
    flag = menuHello(pb)