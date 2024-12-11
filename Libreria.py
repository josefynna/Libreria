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
  #eliminamos los valores que sean Nan
  vals=[v for v in vals_in if math.isfinite(v)]

    #ordenar lista
  vals.sort()
    #determinar si es par o impar
  if len(vals)%2 !=0:
    k=len(vals)//2 #valor de al medio mas uno
    mediana=vals[k]
  else:
    k=len(vals)//2 #si no es impar el
    mediana=(vals[k-1]+vals[k])/2.0
  return mediana
  
  
def moda(vals):
  """
  Calcula la moda de una lista de numeros
  Parametros
  ----------
  vals : list
    Lista de numeros
  Retorna
  -------
     Moda:str
    Moda de los numeros en la lista
  """
  #encontrar conjuto de elementos unicos
  categorias=[]
  for v in vals:
    if v not in categorias:
      categorias.append(v)

  #obtenr el numero de cuentass en la muestra
  #para cada una de las categorias
  cuentas=[]
  for c in categorias:
    n=0
    for v in vals:
      if v==c:
        n=n+1
    cuentas.append(n)

  #encontrar la posicion del valor de la lista con el maximo de cuenta
  # guess and check
  i_max=0
  val_max=cuentas[0]
  for i in range(1,len(cuentas)):
    if cuentas[i]>val_max:
      i_max=i
      val_max=cuentas[i]
  #determinar todas las categorias que tenga el numero maximo de cuentas,mas de una moda
  #val_max dice cual es el valor maximo en la tabla de frecuencia
  modas=[]#se guardan todas las categorias que tengan el mismo numero, nuermo maximo
  for i in range(len(cuentas)):
    if cuentas[i]==val_max:
      modas.append(categorias[i])
  #retorno la moda
  #moda=categorias[i_max]  , ya no se resporta sola una
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
  
  
def percentiles(vals_in):
  # se ordenan los valores
  vals_in.sort()

  percentiles_vals = []

  # se calculan los percentiles 25%, 50% y 75%
  for p in [25, 50, 75]:
 # índice del percentil p
      index = int(len(vals_in) * p / 100)

      # se asegura que no se exceda el valor de la lista
      index = min(index, len(vals_in) - 1)

      percentiles_vals.append(vals_in[index])

  return percentiles_vals
  
  
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
  
  
def mad(vals_in):
  """
  Calcula la desviacion media absoluta de una lista de numeros
  elimina y detecta los NANS
  Parametros
  ----------
  vals : list
    Lista de numeros
  Retorna
  -------
     Desviacion media absoluta:float
    Desviacion

  """
  #eliminamos los valores NANs
  vals = [v for v in vals_in if math.isfinite(v)]
  if len(vals) == 0:
    return None

  # promediooo
  promedio = sum(vals) / len(vals)

  mad = sum(abs(v - promedio) for v in vals) / len(vals)
  return mad
  
# Covarianza
def covarianza(vals_x, vals_y):
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
  
def correlacion(vals_x,vals_y):
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
  x=[]
  y=[]
  for i in range(len(vals_x)):
    if math.isfinite(vals_x[i]) and math.isfinite(vals_y[i]):
      x.append(vals_x[i])
      y.append(vals_y[i])

  rxy=covarianza(x,y)/(varianza(x)*varianza(y))
  return rxy  
  
  def cuartiles(vals_in):
  """
  Calcula el cuartil de una lista de numeros
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


  return Q1, Q3
