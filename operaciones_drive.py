import os
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload

def subir_archivo(servicio, ruta):
    if not os.path.isfile(ruta):
        print('El archivo no existe')
        return
    metadata = {
        'name': os.path.basename(ruta)
    }
    media = MediaFileUpload(
        ruta, 
        resumable=True
    )
    archivo = servicio.files().create(
        body=metadata,
        media_body=media,
        fields='id,name'
    ).execute()
    print('Archivo subido:', archivo['name'])
    print('ID:', archivo['id'])

def descargar_archivo(servicio, archivo_id, destino):
    solicitud = servicio.files().get_media(
        fileId=archivo_id
    )

    with open(destino, 'wb') as archivo:
        descarga = MediaIoBaseDownload(
            archivo,
            solicitud
        )

        terminado = False
        while not terminado:
            estado, terminado = descarga.next_chunk()
            if estado:
                porcentaje = int(estado.progress() *100)
                print('Descargando: ', porcentaje, '%')
    print('Archivo descargado:', destino)

def eliminar_archivo(servicio, archivo_id):
    confirmacion = input(
        'Escriba ELIMINAR para confirmar'
    )

    if confirmacion != 'ELIMINAR':
        print('Operación cancelada')
        return
    servicio.files().delete(
        fileId=archivo_id
    ).execute()
    print('Archivo eliminado correctamente')

def listar_archivos(servicio):
    respuesta = servicio.files().list(
        pageSize=100,
        fields='nextPageToken,files(id,name,mimeType,size)'
    ).execute()

    archivos = respuesta.get('files',[])
    if not archivos:
        print('No hay archivos disponibles')
        return

    for archivo in archivos:
        print(
            archivo['name'],
            '| ID:', archivo['id'],
            '| Tipo:', archivo['mimeType']
        )

def buscar_archivos(servicio, nombre):
    nombre_seguro = nombre.replace('\\', '\\')
    nombre_seguro = nombre_seguro.replace("'", "\'")
    consulta = (
        f"name contains '{nombre_seguro}' "
        "and trashed = false"
    )
    respuesta = servicio.files().list(
        q=consulta,
        fields='files(id,name,mimeType)',
        pageSize=100
    ).execute()
    archivos = respuesta.get('files', [])
    if not archivos:
        print('No se encontraron coincidencias')
        return
    for archivo in archivos:
        print(archivo['name'], '-', archivo['id'])