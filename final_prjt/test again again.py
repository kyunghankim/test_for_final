print("확인용 print")
import pandas as pd
import numpy as np
testarr = np.array([[1,2,3,4],[2,3,6,7,10]])
testdf = pd.DataFrame(testarr)
print(testdf)
my_dict = {"a": ['1', '3'], "b": ['1', '2'], "c": ['2', '4']}
print(pd.DataFrame(my_dict))
