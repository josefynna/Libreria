import math

def promedio(vals_in):
  """
  Calcula el promedio de una lista de numeros
  Parametros
  ----------
  vals_in : list
    Lista de numeros
  Retorna
  -------
     Promedio:float
    Promedio de los numeros en la lista
  """
  vals=[]
  for v in vals_in:
    if math.isfinite(v):
      vals.append(v)

  promedio=sum(vals)/len(vals)
  return promedio
  

  
def moda(vals):
    """
    Calcula la moda de una lista de valores (pueden ser números o cadenas)
    Parametros
    ----------
    vals : list
        Lista de valores
    Retorna
    -------
    Moda : list
        Lista con los valores que más se repiten
    """
    # Diccionario para contar las ocurrencias
    frecuencia = {}

    # Contamos las ocurrencias de cada valor
    for v in vals:
        if v in frecuencia:
            frecuencia[v] += 1
        else:
            frecuencia[v] = 1

    # Encontramos el valor máximo de ocurrencias
    if len(frecuencia) == 0:  # Si la lista está vacía
        return []

    max_freq = max(frecuencia.values())

    # Encontramos todas las categorías que tengan el valor máximo de ocurrencias
    modas = [k for k, v in frecuencia.items() if v == max_freq]

    return modas
    
def rango(vals_in):
  """
  Calcula el rango de una lista
  Detecta y elimina los NaN
  Parametros
  ----------
  vals : list
    Lista de numeros
  Retorna
  -------
     Rango:float
    Rango de los numeros (excluyendo NANs)
  """
  #eliminar los Nans
  vals = [v for v in vals_in if math.isfinite(v)]
  #determinar maximo y minimo desde 0
  # forma 2- gues and check adivino luego rectifico
  if not vals:
    return None
  calRango = max(vals) - min(vals)
  return calRango

def varianza(vals_in):
  """
  Calcula la varianza de una lista de numeros
  elimina y detecta los NANS
  Parametros
  ----------
  vals : list
    Lista de numeros
  Retorna
  -------
     Varianza:float
    Varianza de los numeros en la lista
  """
  # eliminamos los valores de NANs
  vals = [v for v in vals_in if math.isfinite(v)]

  if len(vals) == 0:
      return None

  # promediooo
  promedio = sum(vals) / len(vals)

  # se calcula las desviaciones cuadráticas medias
  dcm = [(v - promedio)**2 for v in vals]

  # varianza
  varianza = sum(dcm)/(len(vals) -1)

  return varianza
  
def std(vals_in):
  """
  Calcula la desviacion estandar de una lista de numeros
  elimina y detecta los NANS
  Parametros
  ----------
  vals : list
    Lista de numeros
  Retorna
  -------
     Desviacion estandar:float
    Desviacion estandar de los numeros en la lista
  """
  #eliminamos los valores NANs
  vals = [v for v in vals_in if math.isfinite(v)]
  if len(vals) == 0:
    return None

  # promediooo
  promedio = sum(vals) / len(vals)

  # se calcula las desviaciones cuadráticas medias
  dcm = [(v - promedio)**2 for v in vals]

  # varianza
  varianza = sum(dcm)/(len(vals) -1)
  # desvuación estandar
  return varianza**0.5
  
  
def calcular_percentil(p, vals_in):
    """
        Calcula un percentil p de los valores dados.
        Utiliza la lógica de interpolación simple.

        Parámetros:
        p (int): El percentil deseado (ejemplo: 5, 50, 95, etc.)
        vals_in (list): Lista de valores sobre los cuales calcular el percentil

        Retorna:
        float: El valor correspondiente al percentil p
    """
 
    vals_in.sort()
    # Número de elementos
    n = len(vals_in)

    k = (p / 100) * (n - 1)

    f = int(k)
    c = k - f
    if f + 1 < n:
        return vals_in[f] + c * (vals_in[f + 1] - vals_in[f])
    else:
        return vals_in[f]
  
def iqr(vals_in):
  """
  Calcula el rango intercuartil de una lista de numeros
  elimina y detecta los NANS
  Parametros
  ----------
  vals : list
    Lista de numeros
  Retorna
  -------
     Rango intercuartil:float
    Rango
  """
  # eliminamos los nans
  vals = [v for v in vals_in if math.isfinite(v)]

  if len(vals) == 0:
      return None

  vals.sort()

  # Calculamos los percentiles 25% (Q1) y 75% (Q3)
  Q1 = vals[int(len(vals) * 25 / 100)]
  Q3 = vals[int(len(vals) * 75 / 100)]

  # Calculamos el rango intercuartil (IQR)
  iqr_r = Q3 - Q1

  return iqr_r
  
  
# Covarianza
def covarianza(x, y):
    """
    Calcula la covarianza de dos listas de números.
    Detecta y elimina los NaNs.
    Parámetros
    ----------
    vals_x, vals_y : list
        Listas de números.
    Retorna
    -------
    float
        Covarianza entre las dos listas.
    """
    x, y = [], []
    for i in range(len(vals_x)):
        if math.isfinite(vals_x[i]) and math.isfinite(vals_y[i]):
            x.append(vals_x[i])
            y.append(vals_y[i])

    mean_x = promedio(x)
    mean_y = promedio(y)
    return sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / len(x) if x else 0.0
  
def correlacion(x,y):
  """
  Calcula la correlacion de dos listas de numeros
  elimina y detecta los NANS
  Parametros
  ----------
  vals1,vals2 : list
    Listas de numeros
  Retorna
  -------
     Correlacion:float
    Correlacion de
  """
  if (len(x) != len(y)):
    return None  

  n = len(x)
  mean_x = sum(x) / n
  mean_y = sum(y) / n

  num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
  denom_x = sum((x[i] - mean_x) ** 2 for i in range(n))
  denom_y = sum((y[i] - mean_y) ** 2 for i in range(n))
  denominator = math.sqrt(denom_x * denom_y)

  if denominator == 0:
    return None 

  return num / denominator

def cuartiles(vals_in):
    """
    Calcula los cuartiles (Q1, Q3) de una lista de números.
    Elimina valores NaN e infinitos.
    
    Parámetros
    ----------
    vals_in : list
        Lista de números.
        
    Retorna
    -------
    tuple
        Un tuple con el cuartil 1 (Q1) y cuartil 3 (Q3).
        Si no se puede calcular, retorna None.
    """
    # Eliminar NaNs y valores infinitos
    vals = [v for v in vals_in if math.isfinite(v)]
    
    if len(vals) == 0:
        return None  # Si no hay datos válidos
    
    # Ordenar los valores
    vals.sort()
    
    # Calcular Q1 (percentil 25) y Q3 (percentil 75)
    n = len(vals)
    
    # Cálculo del cuartil 1 (Q1)
    pos_Q1 = (n + 1) * 25 / 100
    if pos_Q1.is_integer():
        Q1 = vals[int(pos_Q1) - 1]
    else:
        lower = vals[int(math.floor(pos_Q1)) - 1]
        upper = vals[int(math.ceil(pos_Q1)) - 1]
        Q1 = lower + (upper - lower) * (pos_Q1 - math.floor(pos_Q1))
    
    # Cálculo del cuartil 3 (Q3)
    pos_Q3 = (n + 1) * 75 / 100
    if pos_Q3.is_integer():
        Q3 = vals[int(pos_Q3) - 1]
    else:
        lower = vals[int(math.floor(pos_Q3)) - 1]
        upper = vals[int(math.ceil(pos_Q3)) - 1]
        Q3 = lower + (upper - lower) * (pos_Q3 - math.floor(pos_Q3))
    
    return Q1, Q3
  
  
# Función para calcular el percentil
def calcular_percentil(p, vals_in):
    """
        Calcula un percentil p de los valores dados.
        Utiliza la lógica de interpolación simple.

        Parámetros:
        p (int): El percentil deseado (ejemplo: 5, 50, 95, etc.)
        vals_in (list): Lista de valores sobre los cuales calcular el percentil

        Retorna:
        float: El valor correspondiente al percentil p
    """
 
  vals_ordenada = sorted(vals)
  n = len(vals_ordenada)
  k = (p / 100) * (n - 1)
  f = math.floor(k)
  c = math.ceil(k)

  if f == c:
    return vals_ordenada[int(k)]
  else:
    d0 = vals_ordenada[f] * (c - k)
    d1 = vals_ordenada[c] * (k - f)
    return d0 + d1

# Función para calcular la mediana
def mediana(vals_in):
  """
      Calcula la mediana de una lista de numeros
      Parametros
      ----------
      vals : list
        Lista de numeros
      Retorna
      -------
         Mediana:float
    Mediana de los numeros en la lista excluyendo Nans
  """
  vals_ordenada = sorted(vals_in)
  n = len(vals_ordenada)
  if n % 2 == 1:
    return vals_ordenada[n // 2]
  else:
    return (vals_ordenada[(n // 2) - 1] + vals_ordenada[n // 2]) / 2

# Función para calcular MAD (Desviación Absoluta Mediana)
def mad(vals_in):
  """
    Calcula la desviación media absoluta de una lista de números
    elimina y detecta NANAs
    -------
    vals:list
        LiSsta de números
    retorna
    -------
    Desviación media absoluta : float
        desviación media absoluta de los números en la lista
  """
  m = mediana(vals_in)
  diferencias_absolutas = [abs(x - m) for x in vals_in]
  return mediana(diferencias_absolutas)
