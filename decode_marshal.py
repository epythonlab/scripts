from cryptography.fernet import Fernet

# def encrypt_file(file_path, encryption_key):
#     with open(file_path, 'rb') as file:
#         plaintext = file.read()
    
#     cipher = Fernet(encryption_key)
#     encrypted_data = cipher.encrypt(plaintext)
    
#     encrypted_file_path = file_path + '.encrypted'
#     with open(encrypted_file_path, 'wb') as file:
#         file.write(encrypted_data)
    
#     return encrypted_file_path

def decrypt_file(encrypted_file_path, encryption_key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    
    cipher = Fernet(encryption_key)
    decrypted_data = cipher.decrypt(encrypted_data)
    
    decrypted_file_path = encrypted_file_path[:-10]  # Remove the '.encrypted' extension
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)
    
    return decrypted_file_path

# Example usage:
encryption_key = Fernet.generate_key()

# Encrypt a Python file
file_path = 'm.py'
# encrypted_file_path = encrypt_file(file_path, encryption_key)
# print('Encrypted file:', encrypted_file_path)

# Decrypt the encrypted file
decrypted_file_path = decrypt_file(file_path, encryption_key)
print('Decrypted file:', decrypted_file_path)
