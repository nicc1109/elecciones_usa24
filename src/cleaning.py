import pandas as pd

def nombres_columnas(df):
    """
    Limpia y normaliza los nombres de las columnas:
    - Elimina espacios en blanco al principio y al final.
    - Convierte a minúsculas.
    - Sustituye los espacios por guiones bajos.
    
    Args:
        df (pd.DataFrame): El DataFrame cuyo nombre de columnas se va a normalizar.
    
    Returns:
        pd.DataFrame: El DataFrame con los nombres de las columnas normalizados.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df


def cargar_csv(ruta):
    """
    Carga un archivo CSV y devuelve un DataFrame.
    
    Args:
        ruta (str): Ruta al archivo CSV.
    
    Returns:
        pd.DataFrame: El DataFrame cargado desde el archivo CSV.
    """
    return pd.read_csv(ruta)


def eliminar_duplicados(df):
    """
    Elimina las filas duplicadas de un DataFrame.
    
    Args:
        df (pd.DataFrame): El DataFrame del que se eliminarán los duplicados.
    
    Returns:
        pd.DataFrame: El DataFrame sin filas duplicadas.
    """
    return df.drop_duplicates()


def filtrar_anio(df, columna, anio):
    """
    Filtra un DataFrame para incluir solo las filas con el año especificado en una columna.
    
    Args:
        df (pd.DataFrame): El DataFrame a filtrar.
        columna (str): Nombre de la columna que contiene los años.
        anio (int): Año que se quiere filtrar.
    
    Returns:
        pd.DataFrame: El DataFrame con solo las filas del año especificado.
    """
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no está en el DataFrame.")
    return df[df[columna] == anio]


def validar_categoria(df, columna, categorias_validas):
    """
    Valida que los valores en una columna pertenezcan a un conjunto de categorías válidas.
    
    Args:
        df (pd.DataFrame): El DataFrame que contiene la columna a validar.
        columna (str): El nombre de la columna a validar.
        categorias_validas (list): Lista de categorías válidas para la columna.
    
    Returns:
        pd.DataFrame: El DataFrame con solo las filas cuya columna pertenezca a las categorías válidas.
    """
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no está en el DataFrame.")
    return df[df[columna].isin(categorias_validas)]


def filtrar_candidato(df, columna, candidato):
    """
    Filtra un DataFrame para incluir solo las filas donde una columna específica 
    tiene el valor de un candidato dado.
    
    Args:
        df (pd.DataFrame): El DataFrame a filtrar.
        columna (str): Nombre de la columna en la que se buscará el candidato.
        candidato (str): Valor del candidato a filtrar.
    
    Returns:
        pd.DataFrame: El DataFrame con solo las filas que contienen el candidato.
    """
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no está en el DataFrame.")
    return df[df[columna] == candidato]





def eliminar_columnas_na_completas(df):
    """
    Elimina las columnas de un DataFrame si todos sus valores son NaN.

    Parámetros:
        df (pd.DataFrame): DataFrame a procesar.

    Retorna:
        pd.DataFrame: DataFrame sin las columnas que tienen todos los valores como NaN.
    """
    return df.dropna(axis=1, how='all')

def fechas(df, *date_columns):
    """
    Formatea las columnas de fecha de un DataFrame al formato DD/MM/AAAA.

    Parameters:
    df (pd.DataFrame): El DataFrame que contiene las columnas de fecha.
    *date_columns: Nombres de las columnas de fecha a formatear.

    Returns:
    pd.DataFrame: El DataFrame con las columnas de fecha formateadas.
    """
    for col in date_columns:
        df[col] = pd.to_datetime(df[col]).dt.strftime('%d/%m/%Y')
    return df

