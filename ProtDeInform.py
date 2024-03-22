from cryptography.fernet import Fernet

chave = Fernet.generate_key()

mensagem_criptografada = Fernet (chave).encrypt(b"Informação confidencial")

mensagem_descriptografada = Fernet(chave).decrypt(mensagem_criptografada)

print(f'Mensagem original: {mensagem_descriptografada.decode(utf-8)}')

