def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Jika karakter adalah huruf
            shift_base = ord('A') if char.isupper() else ord('a')
            # Geser posisi karakter dan wrap-around jika melebihi 'Z' atau 'z'
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Jika bukan huruf, tidak dienkripsi
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            # Menggeser kembali karakter sesuai shift
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

# Contoh penggunaan
plain_text = "Hello World!"
shift = 3

encrypted = caesar_cipher_encrypt(plain_text, shift)
decrypted = caesar_cipher_decrypt(encrypted, shift)

print("Plain text: ", plain_text)
print("Encrypted text: ", encrypted)
print("Decrypted text: ", decrypted)
