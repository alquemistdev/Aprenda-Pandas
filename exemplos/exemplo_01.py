# import os
# from pathlib import Path 
# p = Path(os.getcwd())
# print(p.parent.parent)

import numpy as np
import pandas as pd

# print(pd.Series([1, 63, 55, 88, 10])) dtype = int64
# print(pd.Series([1, 63, 55, 88, 10, 6.4])) dtype: float64
# print(pd.Series([1, 2, 99, 6.5, "90"])) dtype: object
# pd.Series(np.random.randn(5), index = ["a", "b", "c", "d", "e"])) indexs
# pd.Series({ "a" : 12,"b" : 90,"c" : 20,"d" : 123, })
# s = pd.Series({ "a" : 12,"b" : 90,"c" : 20, "d" : 123, })
# print(s[0]) print(s[0:3])
# print(s["a":"c"])
# print(s[["a","b"]])
# pd.Series(np.random.randn(5), index = ["a", "b", "c", "d", "e"], name = "valores" ))