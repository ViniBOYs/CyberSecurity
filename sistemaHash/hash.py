import hashlib #

def calcular_hash(texto):
    # Criar um objeto de hash MD5
    # hash_md5 = hashlib.md5() # Realiza a implementação
    # hash_sha256= hashlib.sha256()
    hash_sha512= hashlib.sha512()
    hash_sha512.update(texto.encode()) # criptografa o texto

    return hash_sha512.hexdigest() # Retorna o conteudo apos a criptografia


texto = "Olá, Mundo!"
hash_resultado = calcular_hash(texto)
print("Hash do texto '{}':".format(texto))
print(hash_resultado)
