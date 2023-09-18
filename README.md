# vigenere-cipher
Python program that implements the Vigenère Cipher for both encryption and decryption. The Vigenère Cipher is a polyalphabetic substitution cipher that uses a keyword to shift characters in the plaintext.

#gen_key(key, pt) Function:

This function generates a key that is as long as the plaintext.
It takes two arguments: key, which is the keyword, and pt, which is the plaintext.
If the length of the key is already equal to the length of the plaintext, it returns the key as is.
Otherwise, it extends the key by repeating it to match the length of the plaintext.

encryption(pt, key) Function:

This function performs the encryption of the plaintext.
It takes two arguments: pt, which is the plaintext, and key, which is the generated key.
It iterates through each character in the plaintext and shifts it by the corresponding character in the key.
The modulo operation % 26 ensures that the result stays within the range of the alphabet (A-Z).
The shifted character is then converted back to uppercase and added to the ciphertext.

decryption(ct, key) Function:

This function performs the decryption of the ciphertext.
It takes two arguments: ct, which is the ciphertext, and key, which is the generated key.
Similar to encryption, it iterates through each character in the ciphertext.
However, it shifts the character in the opposite direction by subtracting the key character.
The modulo operation % 26 and conversion back to uppercase are also applied to obtain the decrypted character.

Driver Code:

The program provides a menu-driven interface where the user can choose between encryption, decryption, or exiting the program.

For encryption:

It reads plaintext from a file (specified by the user).
Asks for a keyword (the key).
Generates a key of the same length as the plaintext using the gen_key function.
Encrypts the plaintext using the encryption function and writes the ciphertext to a file.

For decryption:

It reads ciphertext from a file (specified by the user).
Uses the same key as was used for encryption (generated using the gen_key function).
Decrypts the ciphertext using the decryption function and writes the plaintext to a file.

The code provides a simple way to encrypt and decrypt text using the Vigenère Cipher with a specified key.





