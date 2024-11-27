import matplotlib.pyplot as plt

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
