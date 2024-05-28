# Import the necessary library
import rsa

def encrypt_message(message, public_key):
    # Convert the message to bytes
    message_bytes = message.encode()

    # Encrypt the message
    encrypted_message = rsa.encrypt(message_bytes, public_key)
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    # Decrypt the message
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    return decrypted_message.decode()

print("="*50)

# Create a key pair
print("Generating a key pair for encryption and decryption...")
public_key, private_key = rsa.newkeys(2048)

# Convert the public key to a string
public_key_str = public_key.save_pkcs1().decode('utf8')
print("\nThe public key is:\n", public_key_str[:150], "...", "\n")

# Convert the private key to a string
private_key_str = private_key.save_pkcs1().decode('utf8')
print("The private key is:\n", private_key_str[:150], "...", "\n")

print("="*50)

# Message for encryption and decryption
original_message = str(input("Please enter the message to encrypt: "))

print("="*50)

# Encrypt the message
encrypted = encrypt_message(original_message, public_key)
print("\nEncrypted Message: \n", encrypted, "\n")

print("="*50)

# Decrypt the message
decrypted = decrypt_message(encrypted, private_key)
print("\nDecrypted Message: \n", decrypted, "\n")

print("="*50)