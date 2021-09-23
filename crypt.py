from cryptography.fernet import Fernet
import os
def write_key():
# Создаем ключ и сохраняем его в файл
	key = Fernet.generate_key()
	with open('crypto.key', 'wb') as key_file:
		key_file.write(key)


def load_key():
# Загружаем ключ 'crypto.key' из текущего каталога
	return open('crypto.key', 'rb').read()

def encrypt(filename, key):
# Зашифруем файл и записываем его
	f = Fernet(key)
	with open(filename, 'rb') as file:
		# прочитать все данные файла
		file_data = file.read()
		encrypted_data = f.encrypt(file_data)
	with open('cr_'+filename, 'wb') as file:
		file.write(encrypted_data)
def decrypt(filename, key):
# Расшифруем файл и записываем его
	f = Fernet(key)
	with open(filename, 'rb') as file:
		# читать зашифрованные данные
		encrypted_data = file.read()
	# расшифровать данные
	decrypted_data = f.decrypt(encrypted_data)
	# записать оригинальный файл
	with open('de_'+filename, 'wb') as file:
		file.write(decrypted_data)
		
def decrypt_open(filename,key):
	f = Fernet(key)
	with open(filename, 'rb') as file:
		en_data = file.read()
		decrypt_data = f.decrypt(en_data)
	
	with open('temp_'+filename,'wb') as file:
		file.write(decrypt_data)
	
	os.system('python3 '+'temp_'+filename)
	os.system('rm '+'temp_'+filename)

key = load_key()
file = 'test.py'
decrypt_open('cr_'+file,key)