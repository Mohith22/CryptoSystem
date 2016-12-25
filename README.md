Simple CryptoSystem :


This is a simple cryptosystem. Encryption of data given by user is done by running des_en.py and decryption by des_dc.py. Encryption and Decryption are done by Fiestel Network which almost resembles DES (Data Encryption Standard). Key used is 56 bit as in DES. Permutation boxes and substitution boxes are also used.

Initially key exchange is done by Diffi Helman Key Exchange (- Run key_est.py )

How to get the shared-key ? 



- Run key_est.py

- Enter prime modulus and generator values (which are public)

- Enter private key of User A (Assume there are two users A and B between whom key is shared)

- Select choice 1 - Initialise Communication

- A value will be generated - v1 (public - sent through communication channel)

- Come out of the program

- Run key_est.py again

- Enter prime modulus and generator values (public - and must be same)

- Enter private key of other User B

- Select choice 1 - Initialise Communication

- A value will be generated -v2 (public)

- Press 'y' key and select choice 2 

- Enter v1 here and "Shared - Key" is obtained for User B

- Come out of the program

- For User A to get "Shared - Key" , run the program again and here enter User A's private key and go to choice 2 and enter v2, User B will get a key which is same as key obtained by User A

- Hence Key - Establishment is done




Encryption And Decryption :




- Run des_en.py

- Enter Plain Text (That has to be decrypted)

- Enter Shared-Key (Obtained From Diffie Helman Key Exchange)

- Encrypted Data is in bits

- Copy it 

- Run des_dc.py

- Enter same Shared - Key

- Paste the copied cipher text

- Hurray !! You would have got your plain text (With some x's appeneded - which won't create much problem)



Future Plans :



- Input through Web-Camera using OCR

- I already used tesseract-ocr which didn't give me satisfactory results.

- So I'm planning to use a better method for OCR - (May be neural networks)

- To make the project more realistic, I'm planning to implement a chat application in which two users can share messages securely.


