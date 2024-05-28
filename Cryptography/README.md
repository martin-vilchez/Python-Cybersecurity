# Cryptography with Python

This repository contains a set of Python scripts designed to introduce and explain the fundamental concepts of cryptography. Each script focuses on a specific cryptographic concept, offering hands-on experience. Each file includes additional comments to provide detailed explanations, insights, and educational context for people who are learning Python.

**Table of Contents**
1. [Script Descriptions](#Script-Descriptions)
    - [Symmetric Key Cryptography](#Symmetric-Key-Cryptography)
    - [Asymmetric Key Cryptography](#Asymmetric-Key-Cryptography)
    - [Real-World Scenario](#Real-World-Scenario)
2. [Getting Started](#Getting-Started)

---

## Script Descriptions

### Symmetric Key Cryptography

The first script use the concept of **Symmetric Key Cryptography**, a type of encryption where a single key is used to both encrypt and decrypt the information. This script demonstrates the entire process, from key generation to encryption and finally decryption. Using the `Fernet` symmetric encryption algorithm from the `cryptography` library, wich is designed for encrypting data that easily fits in memory and also supports key rotation, allowing for the replacement of old keys. It is known for its ease of deployment, making it a popular choice for developers seeking a reliable encryption solution.

### Asymmetric Key Cryptography

The second script works with **Asymmetric Key Cryptography**. Unlike symmetric key cryptography, this method employs two keys: a public key for encryption that can be shared openly, and a private key for decryption.  It also demonstrates the complete process of RSA asymmetric encryption: key generation, message encryption, and subsequent decryption, serving as a practical educational example of this cryptographic technique. The script utilizes the `rsa` library, which is designed to be a versatile and reliable tool for developers and security practitioners, offering functionalities like key generation, encryption, decryption, signing, and signature verification.


### Real-World Scenario

The third script simulates a **Real-World Scenario**, showcasing the practical application of asymmetric cryptography. It demonstrates the generation, serialization, saving to disk & loading from disk, encryption, and decryption of messages using the `cryptography` library in Python. This final script aims to bridge the gap between theoretical knowledge and practical implementation, to understand how cryptography can be utilized to secure information in real-world situations.

---

## Getting Started

**Prerequisites:** Python 3.6 or a later version, `cryptography` library & `rsa` library.

To begin, clone this repository to your local machine using the following command:

```
git clone https://github.com/martin-vilchez/Python-Cybersecurity.git

```

Next, navigate into the cloned repository:

```
cd Python-Cybersecurity/Cryptography
```

You can now execute each script individually with the following command:

```
python3 <script_name.py>
```

Replace `<script_name.py>` with the name of the script you wish to run.

---

Thank you for visiting this repository. Enjoy learning and exploring the fascinating world of cryptography!

---