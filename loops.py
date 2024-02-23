import matplotlib.pyplot as plt
import pandas as pd

a = {
    'Keshu':[91425,14521,47856,14254],
    'Fhanes':[65754,14521,47856,14254]
}   

b = pd.DataFrame(a)
b.plot()
b.show()