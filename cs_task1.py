text = input("Type your message: ")
shift = int(input("Shift by how many letters? "))
new_encrypted_text = ""
new_decrypted_text = ""
for letter in text:
    if letter.isalpha():  # If it's a letter
        # Work with lowercase or uppercase correctly
        if letter.islower():
            base = ord('a')
        else:
            base = ord('A')

        #Encryption Shift the letter and wrap around the alphabet
        new_letter = chr((ord(letter) - base + shift) % 26 + base)
        new_encrypted_text += new_letter
        #Decryption Shift the letter and wrap around the alphabet
        new_deletter = chr((ord(new_letter) - base - shift) % 26 + base)
        new_decrypted_text += new_deletter
    else:
        # Keep spaces and symbols as they are
        new_encrypted_text += letter
        new_decrypted_text += letter
# Show the result
print("Your Encrypted message is:", new_encrypted_text)
print("Your decrypted message is:", new_decrypted_text)