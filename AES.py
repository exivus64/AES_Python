from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a random encryption key
key = get_random_bytes(32)

# The message to be encrypted
message = b"Hello, world!"

# The initialization vector (IV) should be unique and random for each message
iv = get_random_bytes(16)

# Create a new AES cipher object with a 256-bit key in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad the message to be a multiple of 16 bytes (the block size of AES)
padded_message = message + b"\0" * (16 - len(message) % 16)

# Encrypt the padded message
encrypted_message = cipher.encrypt(padded_message)

# Print the encrypted message and the IV
print("Encrypted message: ", encrypted_message)
print("IV: ", iv)

# Create a new AES cipher object withthe same key and IV
decipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the encrypted message
decrypted_message = decipher.decrypt(encrypted_message)

# Remove the padding from the decrypted message
unpadded_message = decrypted_message.rstrip(b"\0")

# Print the decrypted message
print("Decrypted message: ", unpadded_message)