# Caesar Cipher 1
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt , type 'decode' to decrypt : \n")
text=input("Type your message : \n").lower()
shift=int(input("Type the shift number : \n"))

def encrypt(original_text, shift_amount):
    cipher_text=""
    for letter in original_text:
        position=alphabet.index(letter)
        new_position=position + shift_amount
        if new_position >25:
            new_position=new_position -26
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
encrypt(original_text=text, shift_amount=shift)

def decrypt(original_text, shift_amount):
    decipher_text=""
    for letter in original_text:
        position=alphabet.index(letter)
        new_position=position - shift_amount
        if new_position <0:
            new_position=new_position +26
        decipher_text += alphabet[new_position]
    print(f"The decoded text is {decipher_text}")
decrypt(original_text=text, shift_amount=shift)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    # shift ko limit me lana (26 se zyada ho to)
    shift_amount = shift_amount % 26

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        if letter not in alphabet:
            end_text += letter   # space, number, symbol as-it-is
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount

            if new_position > 25:
                new_position -= 26
            elif new_position < 0:
                new_position += 26

            end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is: {end_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == 'no':
        should_continue = False
        print("Good bye Friends 👋")
