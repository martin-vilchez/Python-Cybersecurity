# Import the necessary library
from cryptography.fernet import Fernet

def encrypt_message(message, key):
    # Convert the message to bytes
    message_bytes = message.encode()

    # Encrypt the message
    encrypted_message = cipher.encrypt(message_bytes)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Decrypt the message
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

print("="*50)

# Generate a key for encryption and decryption
key = Fernet.generate_key()
print("\nThe key is: ", key, "\n")
cipher = Fernet(key)
print("Object: ", cipher, "\n")

print("="*50)

# Sample message for encryption and decryption
original_message = str(input("Please enter the message to encrypt: "))

print("="*50)

# Encrypt the message
encrypted = encrypt_message(original_message, key)
print("\nEncrypted Message: \n", encrypted, "\n")

print("="*50)

# Decrypt the message
decrypted = decrypt_message(encrypted, key)
print("\nDecrypted Message: \n", decrypted, "\n")

print("="*50)