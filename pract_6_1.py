# -*- coding: utf-8 -*-
"""pract_6_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AyAbZVAQ3orpoGTeRKhM4g0Ct5gDDISv
"""

#vigenere cipher
#pt= plain text
#ct=cipher text
#dt=decrypted text
#generating key
def gen_key(key,pt):
  key = list(key)
  if len(pt) == len(key):
    return(key)
  else:
    for i in range(len(pt) - len(key)):
      key.append(key[i % len(key)])
  return("" . join(key))

#encryption function
def encryption(pt,key):
  ct=[]
  for i in range(len(pt)):
    x= (ord(pt[i])+ord(key[i]))% 26
    x+=ord('A')
    ct.append(chr(x))
  return("".join(ct))

#decryption function
def decryption(ct,key):
  dt=[]
  for i in range(len(pt)):
    x= (ord(ct[i])-ord(key[i]) + 26)% 26
    x+=ord('A')
    dt.append(chr(x))
  return("".join(dt))

# Driver Code
ch=0
while(ch!=3):
  print("1.encryption\n2.decryption\n3.exit")
  ch=int(input("enter your choice from above:"))
  #encryption
  if ch==1:
    msg=input("enter file name for plain text:")
    try:
      with open(msg, 'r') as file:
        pt = file.read()
        print("File content:",pt)
    except FileNotFoundError:
      print("File not found.")
    print("plain text:",pt)
    k=input("enter key:")
    key=gen_key(k,pt)
    print("key:",key)
    cipher = encryption(pt,key)

    #printing encrypted text
    ct=input("enter the file name for cipher text:")
    try:
      with open(ct, 'w') as file:
        content = cipher
        file.write(content)
      print(f"File '{ct}' created and plain text is encrypted successfully.")
    except Exception as e:
      print("An error occurred:", e)
  #decryption
  if ch==2:
    dct=input("enter file name of which decryption is to be done:")
    try:
      with open(dct, 'r') as file:
        cipher_txt = file.read()
        print("File content:",cipher_txt)
    except FileNotFoundError:
      print("File not found.")
    decrypt=decryption(cipher_txt,key)
    dt=input("enter the file name for decrypted text:")
    try:
      with open(dt, 'w') as file:
        content1 = decrypt
        file.write(content1)
      print(f"File '{dt}' created and plain text is decrypted successfully.")
    except Exception as e:
      print("An error occurred:", e)
  if ch==3:
    print("exit!!")
    exit(0)