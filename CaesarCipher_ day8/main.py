from utilis import logo

print(logo)


def caesar(original_text, shift_count, encode_decode):
    cipher_text = ''
    if encode_decode == 'decode':
        shift_count *= -1
    elif encode_decode == 'encode':
        shift_count *= 1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            locate = alphabet.index(letter) + (shift_count % len(alphabet))
            final_result = alphabet[(locate % len(alphabet))]
            cipher_text += final_result
    print(f"your encoded text: {cipher_text}")


user_input = 'yes'
while user_input == 'yes':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    if direction == 'decode' or direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(original_text=text, shift_count=shift, encode_decode=direction)

    else:
        print('Invalid')

    user_input_update = input("would you like to go again, type 'yes' to go again and 'no' to quit: ").strip().lower()
    user_input = user_input_update

else:
    if user_input == 'no':
        print('Good bye')
