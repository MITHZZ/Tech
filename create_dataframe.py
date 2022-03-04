#Benchmarking different methods for creating empty dataframes from scratch

import pandas as pd
import perfplot

def append(n):
  df = pd.DataFrame(columns=['A', 'B', 'C'])
  for _ in range(n):
    df = df.append({'A': 1, 'B': 12.3, 'C': 'xyz'}, ignore_index=True) # yuck
  return df

def list_append(n):
  data = []
  for _ in range(n):
    data.append([1, 12.3, 'xyz'])

  return pd.DataFrame(data, columns=['A', 'B', 'C'])

def loc_append(n):
  df = pd.DataFrame(columns=['A', 'B', 'C'])
  for _ in range(n):
    df.loc[len(df)] = [1, 12.3, 'xyz']

  return df

kernels = [append, list_append, loc_append]
perfplot.show(
    setup=lambda n: n,
    kernels=kernels,
    labels=[k.__name__ for k in kernels],
    n_range=[i for i in range(0, 1000, 50)],
    xlabel='N',
    logx=True,
    logy=True,
    equality_check=None)
