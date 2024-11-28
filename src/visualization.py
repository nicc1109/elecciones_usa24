import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import seaborn as sns
import pandas as pd


def configurar_estilo():
    """
    Configura un estilo base para los gráficos.
    """
    plt.style.use('seaborn-darkgrid')
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 12

# Función para gráficos de barras
def plot_bar(df, x, y, title="", xlabel="", ylabel="", color="blue"):
    """
    Crea un gráfico de barras con personalización.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        x (str): Nombre de la columna para el eje X.
        y (str): Nombre de la columna para el eje Y.
        title (str): Título del gráfico.
        xlabel (str): Etiqueta para el eje X.
        ylabel (str): Etiqueta para el eje Y.
        color (str): Color de las barras.
    """
    ax = df.plot(kind='bar', x=x, y=y, color=color, legend=False)
    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else x)
    ax.set_ylabel(ylabel if ylabel else y)
    plt.show()

# Función para gráficos de líneas
def plot_line(df, x, y, title="Gráfico de Línea", xlabel="", ylabel="", color="blue"):
    """
    Crea un gráfico de línea con puntos marcados.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        x (str): Nombre de la columna para el eje X.
        y (str): Nombre de la columna para el eje Y.
        title (str): Título del gráfico.
        xlabel (str): Etiqueta para el eje X.
        ylabel (str): Etiqueta para el eje Y.
        color (str): Color de la línea.
    """
    plt.plot(df[x], df[y], marker='o', color=color, label=y)
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x)
    plt.ylabel(ylabel if ylabel else y)
    plt.legend()
    plt.show()


# Función para gráficos de líneas múltiples
def plot_multi_lines(df, x, y_columns, title="Gráfico de Líneas", xlabel="", ylabel="", colors=None, linewidth=1):
    """
    Crea un gráfico de líneas para múltiples columnas en el eje Y, con mejor manejo de colores y fechas.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        x (str): Nombre de la columna para el eje X.
        y_columns (list): Lista de nombres de columnas para el eje Y.
        title (str): Título del gráfico.
        xlabel (str): Etiqueta para el eje X.
        ylabel (str): Etiqueta para el eje Y.
        colors (list): Lista de colores para las líneas (opcional). Usa colores de seaborn si no se especifica.
        linewidth (float): Grosor de las líneas.
    """
    # Convertir x a datetime si es necesario
    if df[x].dtype != 'datetime64[ns]':
        df[x] = pd.to_datetime(df[x])
    
    # Crear paleta de colores si no se especifican
    if colors is None:
        palette = sns.color_palette("husl", len(y_columns))  # Husl da colores muy distintos
        colors = palette
    
    plt.figure(figsize=(12, 6))  # Ajustar tamaño del gráfico
    
    for idx, y in enumerate(y_columns):
        plt.plot(df[x], df[y], marker='o', color=colors[idx % len(colors)], label=y, linewidth=linewidth)
    
    # Formatear fechas en el eje X
    plt.gca().xaxis.set_major_formatter(DateFormatter("%b %Y"))  # Formato Mes Año
    plt.gcf().autofmt_xdate()  # Rotar etiquetas para mejor legibilidad
    
    # Agregar título y etiquetas
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x)
    plt.ylabel(ylabel if ylabel else "Valores")
    
    plt.legend()  # Mostrar leyenda
    plt.grid(True, linestyle='--', alpha=0.6)  # Mejorar visibilidad de la cuadrícula
    plt.show()
    

def plot_multi_lines_pivot(df, filter_col, filter_value, pivot_col, value_col, index_col, title="Gráfico de Líneas", xlabel="", ylabel="", colors=None, linewidth=1):
    """
                Crea un gráfico de líneas múltiples, incluyendo el pivoteo de datos internamente.
                
                Args:
                    df (pd.DataFrame): DataFrame con los datos.
                    filter_col (str): Columna para filtrar (e.g., 'politician/institution').
                    filter_value (str): Valor para filtrar (e.g., 'Joe Biden').
                    pivot_col (str): Columna para pivotar (e.g., 'answer').
                    value_col (str): Columna con los valores numéricos (e.g., 'pct_estimate').
                    index_col (str): Columna para el índice del pivote (e.g., 'date').
                    title (str): Título del gráfico.
                    xlabel (str): Etiqueta para el eje X.
                    ylabel (str): Etiqueta para el eje Y.
                    colors (list): Lista de colores para las líneas.
                    linewidth (float): Grosor de las líneas.
                """
    # Filtrar el DataFrame
    df_filtrado = df[df[filter_col] == filter_value]

    # Crear el pivote
    df_pivot = df_filtrado.pivot_table(
        index=index_col,
        columns=pivot_col,
        values=value_col
    ).reset_index()

    # Convertir index_col a datetime si es necesario
    if df_pivot[index_col].dtype != 'datetime64[ns]':
        df_pivot[index_col] = pd.to_datetime(df_pivot[index_col])

    # Crear paleta de colores si no se especifican
    if colors is None:
        palette = sns.color_palette("husl", len(df_pivot.columns) - 1)  # Husl da colores muy distintos
        colors = palette

    # Gráfico
    plt.figure(figsize=(12, 6))
    for idx, col in enumerate(df_pivot.columns[1:]):  # Ignorar la columna de fechas
        plt.plot(df_pivot[index_col], df_pivot[col], marker='o', color=colors[idx % len(colors)], label=col, linewidth=linewidth)

    # Configuración del gráfico
    plt.title(title)
    plt.xlabel(xlabel if xlabel else index_col)
    plt.ylabel(ylabel if ylabel else value_col)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%b %Y"))
    plt.gcf().autofmt_xdate()  # Rotar etiquetas del eje X
    plt.show()


# Función para gráficos de barras apiladas
# Función para gráficos de barras apiladas con porcentajes
def plot_stacked_bar(df, group_col, stack_col, value_col, title="Gráfico de Barras Apiladas", xlabel="", ylabel="", colors=None):
    """
    Crea un gráfico de barras apiladas con etiquetas de porcentaje dentro de las barras.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        group_col (str): Columna para agrupar en el eje X.
        stack_col (str): Columna para apilar.
        value_col (str): Columna con los valores a graficar.
        title (str): Título del gráfico.
        xlabel (str): Etiqueta para el eje X.
        ylabel (str): Etiqueta para el eje Y.
        colors (list): Lista de colores para las barras apiladas (opcional).
    """
    # Pivotear los datos para barras apiladas
    df_pivot = df.pivot_table(
        index=group_col,
        columns=stack_col,
        values=value_col,
        aggfunc="sum",
        fill_value=0
    )

    # Crear paleta de colores si no se especifica
    if colors is None:
        palette = sns.color_palette("husl", len(df_pivot.columns))
        colors = palette

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(12, 6))

    # Apilar barras manualmente
    bottom_values = None
    for idx, col in enumerate(df_pivot.columns):
        ax.bar(
            df_pivot.index,
            df_pivot[col],
            label=col,
            bottom=bottom_values,
            color=colors[idx % len(colors)]
        )
        # Actualizar los valores acumulados para la base de las barras
        if bottom_values is None:
            bottom_values = df_pivot[col]
        else:
            bottom_values += df_pivot[col]

    # Agregar etiquetas de porcentaje dentro de las barras
    for i, (group, row) in enumerate(df_pivot.iterrows()):
        cumulative = 0
        for j, value in enumerate(row):
            percentage = value / row.sum() * 100
            ax.text(
                i, 
                cumulative + value / 2, 
                f"{percentage:.1f}%", 
                ha='center', 
                va='center', 
                fontsize=10, 
                color="white" if percentage > 10 else "black"
            )
            cumulative += value

    # Configuración del gráfico
    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel else group_col)
    ax.set_ylabel(ylabel if ylabel else "Valores")
    ax.legend(title=stack_col, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()


def plot_trend_direct(df, x, y_columns, title="Tendencia Temporal", xlabel="", ylabel="", colors=None, linewidth=1.0, linestyles=None):
    """
    Crea un gráfico de líneas para tendencias temporales con columnas separadas para los valores.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos.
        x (str): Nombre de la columna para el eje X (e.g., 'start_date').
        y_columns (list): Lista de columnas para el eje Y (e.g., ['approve', 'disapprove']).
        title (str): Título del gráfico.
        xlabel (str): Etiqueta para el eje X.
        ylabel (str): Etiqueta para el eje Y.
        colors (list): Lista de colores para las líneas.
        linewidth (float): Grosor de las líneas.
        linestyles (list): Lista de estilos de línea (e.g., ['-', '--']).
    """
    # Convertir x a datetime si es necesario
    if df[x].dtype != 'datetime64[ns]':
        df[x] = pd.to_datetime(df[x])
    
    # Crear paleta de colores si no se especifican
    if colors is None:
        colors = sns.color_palette("husl", len(y_columns))
    
    plt.figure(figsize=(12, 6))
    
    # Crear líneas para cada columna en y_columns
    for idx, col in enumerate(y_columns):
        linestyle = linestyles[idx % len(linestyles)] if linestyles else '-'
        plt.plot(df[x], df[col], color=colors[idx % len(colors)], 
                 label=col, linewidth=linewidth, linestyle=linestyle)
    
    # Configuración del gráfico
    plt.title(title)
    plt.xlabel(xlabel if xlabel else x)
    plt.ylabel(ylabel if ylabel else "Valores")
    plt.legend(title="Tendencia")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%b %Y"))
    plt.gcf().autofmt_xdate()  # Rotar etiquetas del eje X
    plt.show()

