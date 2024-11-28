import os
import matplotlib.pyplot as plt

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

def guardar_graf_exploratorio(filename, folder="plots", subfolder="exploratorios", dpi=300, tight_layout=True, comentario=None, formato="png"):
    """
    Guarda el gráfico actual en una ubicación específica y opcionalmente agrega un comentario.
    
    Args:
        filename (str): Nombre del archivo (sin extensión).
        folder (str): Carpeta raíz donde se guardará el gráfico.
        subfolder (str): Subcarpeta dentro de la carpeta raíz.
        dpi (int): Resolución del gráfico.
        tight_layout (bool): Si True, ajusta automáticamente los márgenes.
        comentario (str): Comentario para agregar al gráfico como texto.
        formato (str): Formato del archivo (ej. 'png', 'pdf', 'svg').
    """
    # Crear las carpetas si no existen
    output_folder = os.path.join(folder, subfolder)
    os.makedirs(output_folder, exist_ok=True)
    
    # Ruta completa del archivo
    filepath = os.path.join(output_folder, f"{filename}.{formato}")
    
    # Depuración
    print(f"Guardando en: {filepath}")
    print(f"Carpeta existe: {os.path.exists(output_folder)}")
    
    # Agregar comentario al gráfico si se proporciona
    if comentario:
        plt.figtext(0.5, -0.1, comentario, wrap=True, horizontalalignment='center', fontsize=8)
    
    # Guardar el gráfico
    if tight_layout:
        plt.tight_layout()
    plt.savefig(filepath, dpi=dpi, bbox_inches="tight", format=formato)
    plt.close()
    print(f"Gráfico guardado exitosamente en: {filepath}")