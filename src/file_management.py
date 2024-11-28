import os

def guardar_csv(df, nombre_archivo, carpeta="data"):
    """
    Guarda un DataFrame como archivo CSV en la carpeta especificada.

    Parámetros:
        df (pd.DataFrame): El DataFrame a guardar.
        nombre_archivo (str): El nombre del archivo CSV (incluye la extensión .csv).
        carpeta (str): La carpeta donde se guardará el archivo (por defecto 'data').

    Retorna:
        str: La ruta completa donde se guardó el archivo.
    """
    # Crear la carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    # Ruta completa del archivo
    ruta_completa = os.path.join(carpeta, nombre_archivo)
    
    # Guardar el DataFrame como CSV
    df.to_csv(ruta_completa, index=False)
    
    print(f"Archivo guardado en: {ruta_completa}")
    return ruta_completa
