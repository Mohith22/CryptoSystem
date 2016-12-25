# Encryption Using Fiestel Network - DES Like Algorithm :

#Author : Mohith Damarapati-BTech-3rd year-NIT Surat-Computer Science

import sys
import math
import Image
import pytesseract
import cv2

# Taking Plain Text As Input ::: 
text = raw_input("Enter The Text To Be Encrypted (Plain Text) : ")

# Taking Input Through An Image (Either From Web Camera Or Already Saved Image)
# I used pytesseract which seems to be less efficient. More efficient OCR system need to be used here


#text = pytesseract.image_to_string(Image.open('sample3.jpg'))
key = raw_input("Enter Otainded Shared-Key (From Diffie Helman) : ")

#Key conversion Into 56 Bit
key = format(int(key),'056b')  #56 Bit key is stored in key variable

#print key
#print "\n"

#Padding to get 64 bit - Pad with character 'x'
rem = 8 - (len(text)%8)
for i in range(rem):
	text+='x'

#print text
#print "\n"

#Ascii conversion (Conversion into bits)
bits = []


i=0
while True:
	st = ''
	stext = text[i:i+8]
	for j in range(len(stext)):
		st+=format(ord(stext[j]),'08b')
	bits.append(st)
	i=i+8
	if i==len(text):
		break

#print bits 
#print "\n\n"
ans_bits = ''


for i in bits:
	# Initial Permutation
	a_1p = ''
	a_fp = ''

	a_1p += i[57]
	a_1p += i[49]
	a_1p += i[41]
	a_1p += i[33]
	a_1p += i[25]
	a_1p += i[17]
	a_1p += i[9]
	a_1p += i[1]

	a_1p += i[59]
	a_1p += i[51]
	a_1p += i[43]
	a_1p += i[35]
	a_1p += i[27]
	a_1p += i[19]
	a_1p += i[11]
	a_1p += i[3]

	a_1p += i[61]
	a_1p += i[53]
	a_1p += i[45]
	a_1p += i[37]
	a_1p += i[29]
	a_1p += i[21]
	a_1p += i[13]
	a_1p += i[5]

	a_1p += i[63]
	a_1p += i[55]
	a_1p += i[47]
	a_1p += i[39]
	a_1p += i[31]
	a_1p += i[23]
	a_1p += i[15]
	a_1p += i[7]

	a_1p += i[56]
	a_1p += i[48]
	a_1p += i[40]
	a_1p += i[32]
	a_1p += i[24]
	a_1p += i[16]
	a_1p += i[8]
	a_1p += i[0]

	a_1p += i[58]
	a_1p += i[50]
	a_1p += i[42]
	a_1p += i[34]
	a_1p += i[26]
	a_1p += i[18]
	a_1p += i[10]
	a_1p += i[2]

	a_1p += i[60]
	a_1p += i[52]
	a_1p += i[44]
	a_1p += i[36]
	a_1p += i[28]
	a_1p += i[20]
	a_1p += i[12]
	a_1p += i[4]

	a_1p += i[62]
	a_1p += i[54]
	a_1p += i[46]
	a_1p += i[38]
	a_1p += i[30]
	a_1p += i[22]
	a_1p += i[14]
	a_1p += i[6]
	

	#Key Generation

	keys = []

	kl , kr = key[:len(key)/2] , key[len(key)/2:]
	for x in range(16):

		kl_2 = kl[1:len(kl)] + kl[0]
		kr_2 = kr[1:len(kr)] + kr[0]

		kl_3 = kl_2[:7] + kl_2[8:]
		kl_3 = kl_3[:16] + kl_3[17:]
		kl_3 = kl_3[:20] + kl_3[21:]
		kl_3 = kl_3[:23] + kl_3[24:]

		kr_3 = kr_2[:5] + kr_2[6:]
		kr_3 = kr_3[:8] + kr_3[9:]
		kr_3 = kr_3[:13] + kr_3[14:]
		kr_3 = kr_3[:24] + kr_3[25:]

		keys.append(kl_3 + kr_3) #48 bit round key

		kl=kl_2
		kr=kr_2

	#print keys
	#print "\n"

	# Rounds 1-16
	l , r = a_1p[:len(a_1p)/2] , a_1p[len(a_1p)/2:]

	for q in range(16):

		pb1 = r
		y=0
		pb = pb1[31]
		for x in range(7):
			pb += pb1[y:y+5] + pb1[y+3]
			y+=4
		pb += pb1[28:32]
		pb += pb1[0] 


		# 48 bit Output of Permutation Box is pb

		# XOR with key
		px = ''
		for x in range(48):
			px+=str((int(keys[q][x]))^(int(pb[x]))) # px is 48 bit Output after Xoring

		# SBox

		se = [] # 6 bit entries of sbox
		y=0
		for x in range(8):
			se.append(px[y:y+6])
			y+=6

		# a_sb is output after sbox - 32 bit

		#sbox values
		sbox = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,10,3,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
		a_sb =''
		for x in se:
			sr = x[0:2]
			sc = x[2:6]
			dsr = int(sr,2)
			dsc = int(sc,2)
			sval = sbox[dsr][dsc]
			a_sb+=format(sval,'04b') # a_sb is output after S-box

		fx = ''
		for x in range(32):
			fx+=str((int(l[x]))^(int(a_sb[x]))) # px is 48 bit Output after Xoring


		#print fx
		#print "\n"

		l = r #L - Final
		r = fx #R - Final

	a_r = r + l

	# Final Permutation
	a_fp += a_r[39]
	a_fp += a_r[7]
	a_fp += a_r[47]
	a_fp += a_r[15]
	a_fp += a_r[55]
	a_fp += a_r[23]
	a_fp += a_r[63]
	a_fp += a_r[31]

	a_fp += a_r[38]
	a_fp += a_r[6]
	a_fp += a_r[46]
	a_fp += a_r[14]
	a_fp += a_r[54]
	a_fp += a_r[22]
	a_fp += a_r[62]
	a_fp += a_r[30]

	a_fp += a_r[37]
	a_fp += a_r[5]
	a_fp += a_r[45]
	a_fp += a_r[13]
	a_fp += a_r[53]
	a_fp += a_r[21]
	a_fp += a_r[61]
	a_fp += a_r[29]

	a_fp += a_r[36]
	a_fp += a_r[4]
	a_fp += a_r[44]
	a_fp += a_r[12]
	a_fp += a_r[52]
	a_fp += a_r[20]
	a_fp += a_r[60]
	a_fp += a_r[28]

	a_fp += a_r[35]
	a_fp += a_r[3]
	a_fp += a_r[43]
	a_fp += a_r[11]
	a_fp += a_r[51]
	a_fp += a_r[19]
	a_fp += a_r[59]
	a_fp += a_r[27]

	a_fp += a_r[34]
	a_fp += a_r[2]
	a_fp += a_r[42]
	a_fp += a_r[10]
	a_fp += a_r[50]
	a_fp += a_r[18]
	a_fp += a_r[58]
	a_fp += a_r[26]

	a_fp += a_r[33]
	a_fp += a_r[1]
	a_fp += a_r[41]
	a_fp += a_r[9]
	a_fp += a_r[49]
	a_fp += a_r[17]
	a_fp += a_r[57]
	a_fp += a_r[25]

	a_fp += a_r[32]
	a_fp += a_r[0]
	a_fp += a_r[40]
	a_fp += a_r[8]
	a_fp += a_r[48]
	a_fp += a_r[16]
	a_fp += a_r[56]
	a_fp += a_r[24]

	ans_bits+=a_fp

print "DeCrypted Text Is : "
# In bits:

print ans_bits

# In String:

'''i=0
sol=''
for x in range(len(ans_bits)/8):
	stx = ans_bits[i:i+8]
	i+=8
	sol+=chr(int(stx,2))

print sol'''

print "Copy This Cipher Text And Give It As Input In Decrytion Program"




	





