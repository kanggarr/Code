# # Multi-column-sorting

# import pandas as pd

# No = ({
#     'A':[1,3,4,2,3,4,1,2,3,1,1,4,5,3],
#     'B':[1,1,4,4,5,3,3,4,3,5,1,1,2,5],
#     'C':[4,1,4,4,3,3,3,3,5,3,4,1,3,2]
#                })
# df = pd.DataFrame(No)
# print(df)

# df2 = df.sort_values(['A', 'B','C'], ascending=[True, True, True])
# print(df2)


import pandas as pd
technologies = ({
    'Courses':["Spark","Hadoop","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,20000],
    'Duration':['30days','35days','40days','50days','60days'],
    'Discount':[1000,2300,1500,1200,2500]
               })
df = pd.DataFrame(technologies, index = ['r1','r2','r3','r4','r0'])
print(df)
