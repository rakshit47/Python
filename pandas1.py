import pandas as pd

fun = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
a = [1, 7, 2]

myvar = pd.Series(a)
print(myvar)

myvar = pd.DataFrame(fun)
print(myvar)