# Import the necessary cryptography libraries
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Function to generate private and public keys
def generate_keys():
    # Generate a private key with a public exponent of 65537 (common choice in cryptography)
    # and a key size of 2048 bits (standard for RSA)
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()  # Use default backend
    )
    
    # Generate the corresponding public key
    public_key = private_key.public_key()
    return private_key, public_key

# Function to save keys to disk
def save_keys_to_disk(private_key, public_key):
    # Save the private key to disk in PEM format 
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()  # No password protection
        ))

    # Save the public key to disk in PEM format
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# Function to load keys from disk
def load_keys_from_disk():
    # Load the private key from disk
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()  # Use default backend
        )

    # Load the public key from disk
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()  # Use default backend
        )

    return private_key, public_key

# Function to encrypt a message
def encrypt_message(message, public_key):
    # Convert the message to bytes
    message_bytes = message.encode()
    
    # Encrypt the message bytes using public key and OAEP padding
    encrypted_message = public_key.encrypt(
        message_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Use SHA256 hash function for Mask Generation Function
            algorithm=hashes.SHA256(),  # Use SHA256 hash function
            label=None  # No label used
        )
    )
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, private_key):
    # Decrypt the encrypted message bytes using private key and same OAEP padding
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Use SHA256 hash function for Mask Generation Function
            algorithm=hashes.SHA256(),  # Use SHA256 hash function
            label=None  # No label used
        )
    )
    
    # Convert the decrypted message bytes back into a string
    return decrypted_message.decode()

# Generate and save keys
private_key, public_key = generate_keys()
save_keys_to_disk(private_key, public_key)

# Load keys
private_key, public_key = load_keys_from_disk()

# Message for encryption and decryption
original_message = str(input("Please enter the message to encrypt: "))

# Encrypt the message
encrypted = encrypt_message(original_message, public_key)
print("\nEncrypted Message: \n", encrypted, "\n")

# Decrypt the message
decrypted = decrypt_message(encrypted, private_key)
print("\nDecrypted Message: \n", decrypted, "\n")
