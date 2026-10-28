from autenticacion import conectar_drive
from operaciones_drive import (
    listar_archivos, buscar_archivos, subir_archivo,
    descargar_archivo, eliminar_archivo
)
from integridad import verificar_integridad

def main():
    servicio = conectar_drive()
    while True:
        print('\n-- Gestor de Google Drive --')
        print('1. Listar archivos')
        print('2. Buscar archivos')
        print('3. Subir archivo')
        print('4. Descargar archivo')
        print('5. Eliminar archivo')
        print('6. Comprobar integridad (SHA-256)')
        print('7. Sarlir')
        opcion = input('Seleccione: ')
        try:
            if opcion == '1': listar_archivos(servicio)
            elif opcion == '2':
                nombre = input('Nombre: ')
                buscar_archivos(servicio, nombre)
            elif opcion == '3':
                ruta = input('Ruta local: ')
                subir_archivo(servicio, ruta)
            elif opcion == '4':
                archivo_id = input('ID: ')
                destino = input('Destino: ')
                descargar_archivo(servicio, archivo_id, destino)
            elif opcion == '5':
                archivo_id = input('ID: ')
                eliminar_archivo(servicio, archivo_id)
            elif opcion == '6': 
                original = input('Ruta del archivo original: ')
                copia = input('Ruta del archivo descargado en Drive: ')
                verificar_integridad(original, copia)
            elif opcion == '7': break
            else: print('Opción inválida')
        except Exception as error: print('Error:', error)

if __name__ == '__main__': main()