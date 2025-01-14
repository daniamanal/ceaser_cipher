# Let user input a word and a shift number.
# Encode the message by shifting the letter by shift number. Write code to decode the message

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("type the shift number:\n"))


def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for i in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(i) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"here is the {encode_or_decode}d result: {output_text}")


ceaser(text, shift, direction)
