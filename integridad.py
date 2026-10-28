import hashlib

def calcular_sha256(ruta):
    hash_archivo = hashlib.sha256()
    with open(ruta, 'rb') as archivo:
        while True:
            bloque = archivo.read(65536)
            if not bloque:
                break;
        hash_archivo.update(bloque)
    return hash_archivo.hexdigest()

def verificar_integridad(original, copia):
    hash_original = calcular_sha256(original)
    hash_copia = calcular_sha256(copia)
    print('Original:', hash_original)
    print('Copia:', hash_copia)
    if hash_original == hash_copia:
        print('Integridad verificada')
    else:
        print('los archivos son diferentes')