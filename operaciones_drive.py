

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