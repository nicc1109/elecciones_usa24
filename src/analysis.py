import matplotlib.pyplot as plt

def graficar_tendencia_candidato(df, fecha_col, candidato_col, resultado_col, candidato, title="Tendencia por Candidato"):
    """
    Genera un gráfico de línea para un candidato específico mostrando cómo varían sus resultados en el tiempo.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        fecha_col (str): Nombre de la columna con las fechas.
        candidato_col (str): Nombre de la columna con los nombres de los candidatos.
        resultado_col (str): Nombre de la columna con los resultados.
        candidato (str): Nombre del candidato a analizar.
        title (str, opcional): Título del gráfico.
    """
    if candidato_col not in df.columns or fecha_col not in df.columns or resultado_col not in df.columns:
        raise ValueError("Columnas especificadas no están en el DataFrame.")
    
    # Filtrar por el candidato específico
    data_candidato = df[df[candidato_col] == candidato]
    data_candidato = data_candidato.sort_values(by=fecha_col)
    
    plt.plot(data_candidato[fecha_col], data_candidato[resultado_col], marker='o', label=candidato)
    plt.title(title)
    plt.xlabel(fecha_col)
    plt.ylabel(resultado_col)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graficar_distribucion_encuestadoras(df, encuestadora_col, resultado_col, title="Distribución de Resultados por Encuestadora"):
    """
    Genera un gráfico de cajas (boxplot) para mostrar la distribución de resultados por encuestadora.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        encuestadora_col (str): Nombre de la columna con las encuestadoras.
        resultado_col (str): Nombre de la columna con los resultados.
        title (str, opcional): Título del gráfico.
    """
    if encuestadora_col not in df.columns or resultado_col not in df.columns:
        raise ValueError("Columnas especificadas no están en el DataFrame.")
    
    df.boxplot(column=resultado_col, by=encuestadora_col, grid=False, rot=90)
    plt.title(title)
    plt.suptitle("")  # Remover el título por defecto de Pandas
    plt.xlabel("Encuestadora")
    plt.ylabel(resultado_col)
    plt.tight_layout()
    plt.show()

def graficar_comparacion_estado(df, estado_col, candidato_col, resultado_col, estado, title="Comparación de Candidatos por Estado"):
    """
    Genera un gráfico de barras apiladas para comparar los resultados de los candidatos en un estado específico.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        estado_col (str): Nombre de la columna con los estados.
        candidato_col (str): Nombre de la columna con los candidatos.
        resultado_col (str): Nombre de la columna con los resultados.
        estado (str): Nombre del estado a analizar.
        title (str, opcional): Título del gráfico.
    """
    if estado_col not in df.columns or candidato_col not in df.columns or resultado_col not in df.columns:
        raise ValueError("Columnas especificadas no están en el DataFrame.")
    
    # Filtrar por estado
    data_estado = df[df[estado_col] == estado]
    
    # Crear la tabla pivot para el gráfico apilado
    pivot_data = data_estado.pivot_table(index=candidato_col, values=resultado_col, aggfunc='sum')
    
    pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title(title)
    plt.xlabel("Candidato")
    plt.ylabel("Resultados")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

import seaborn as sns

def graficar_calor_resultados_estado(df, estado_col, candidato_col, resultado_col, title="Resultados por Estado"):
    """
    Genera un gráfico de calor mostrando los resultados promedio de los candidatos por estado.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        estado_col (str): Nombre de la columna con los estados.
        candidato_col (str): Nombre de la columna con los candidatos.
        resultado_col (str): Nombre de la columna con los resultados.
        title (str, opcional): Título del gráfico.
    """
    if estado_col not in df.columns or candidato_col not in df.columns or resultado_col not in df.columns:
        raise ValueError("Columnas especificadas no están en el DataFrame.")
    
    pivot_data = df.pivot_table(index=estado_col, columns=candidato_col, values=resultado_col, aggfunc='mean')
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_data, annot=True, cmap="YlGnBu", fmt=".1f", cbar_kws={'label': 'Promedio de Resultados'})
    plt.title(title)
    plt.xlabel("Candidato")
    plt.ylabel("Estado")
    plt.tight_layout()
    plt.show()

def graficar_tendencia_encuestadoras(df, fecha_col, encuestadora_col, resultado_col, title="Tendencia por Encuestadora"):
    """
    Genera un gráfico de líneas para comparar las tendencias de múltiples encuestadoras a lo largo del tiempo.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        fecha_col (str): Nombre de la columna con las fechas.
        encuestadora_col (str): Nombre de la columna con las encuestadoras.
        resultado_col (str): Nombre de la columna con los resultados.
        title (str, opcional): Título del gráfico.
    """
    if fecha_col not in df.columns or encuestadora_col not in df.columns or resultado_col not in df.columns:
        raise ValueError("Columnas especificadas no están en el DataFrame.")
    
    plt.figure(figsize=(10, 6))
    for encuestadora in df[encuestadora_col].unique():
        data_encuestadora = df[df[encuestadora_col] == encuestadora]
        data_encuestadora = data_encuestadora.sort_values(by=fecha_col)
        plt.plot(data_encuestadora[fecha_col], data_encuestadora[resultado_col], marker='o', label=encuestadora)
    
    plt.title(title)
    plt.xlabel(fecha_col)
    plt.ylabel(resultado_col)
    plt.legend(title="Encuestadora", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def graficar_tendencia_encuestadoras(df, fecha_col, encuestadora_col, resultado_col, title="Tendencia por Encuestadora"):
    """
    Genera un gráfico de líneas para comparar las tendencias de múltiples encuestadoras a lo largo del tiempo.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        fecha_col (str): Nombre de la columna con las fechas.
        encuestadora_col (str): Nombre de la columna con las encuestadoras.
        resultado_col (str): Nombre de la columna con los resultados.
        title (str, opcional): Título del gráfico.
    """
    if fecha_col not in df.columns or encuestadora_col not in df.columns or resultado_col not in df.columns:
        raise ValueError("Columnas especificadas no están en el DataFrame.")
    
    plt.figure(figsize=(10, 6))
    for encuestadora in df[encuestadora_col].unique():
        data_encuestadora = df[df[encuestadora_col] == encuestadora]
        data_encuestadora = data_encuestadora.sort_values(by=fecha_col)
        plt.plot(data_encuestadora[fecha_col], data_encuestadora[resultado_col], marker='o', label=encuestadora)
    
    plt.title(title)
    plt.xlabel(fecha_col)
    plt.ylabel(resultado_col)
    plt.legend(title="Encuestadora", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
