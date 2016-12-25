#Diffie Helman Key Exchange

#Author : Mohith Damarapati-BTech-3rd year-NIT Surat-Computer Science

#Establishment Of Key
#Functionalities :
#1. User can initiate communication through his private key to get secretly-shared-key
#2. User can get secretly shared-key through his private key


#For Simplicity Choose - 
#Prime Modulus - 10007 & Generator - 293
import sys


def findv(gen,prime,pkey):
	return pow(gen,pkey,prime)


print "Welcome!!! \n"
prime = raw_input("Enter Prime Modulus Value (Public) : ")
gen = raw_input("Enter Generator Value (Public) : ")
pkey = raw_input("Enter Your Private Key (Enter It Carefully): ")

print "\n"

while True:

	print "Select Your Choice : \n"
	print "1. Initiate Communication - Press 1"
	print "2. Get Shared-Key - Press 2"
	print "\n"
	while True:
		choice = raw_input("Enter Your Choice: ")
		print "\n"
		if choice=='1':
			val = findv(int(gen),int(prime),int(pkey))
			print "Value Sent Is : ",
			print val
			break

		elif choice=='2':
			valu = raw_input("Enter Value You Got From The Other Party : ")
			skey = findv(int(valu),int(prime),int(pkey))
			print "********Shared Key Is******** : ",
			print skey,
			print "   Keep It Secured !!! ****"
			break

		else:
			print "Enter Valid Choice"
	print "\n\n"

	print "Want to something else :"
	print "Press 'y'"
	print "Else to exit press any key"

	ch = raw_input("Choice : ")
	print "\n\n"
	if ch!='y':
		print "Program Exit ....."
		break


