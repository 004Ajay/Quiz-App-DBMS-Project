# lst = [('AJAY', 'AJAY@GMAIL.COM', 'SJC'), ('JUDIN', 'JUDIN@GMAIL.COM', 'sjc'), ('JUSTIN', 'JUSTIN@GMAIL.COM', 'SJC'), ('NOYAL', 'NOYAL@GMAIL.COM', 'SJC'), ('tester', 'tester@gmail.com', 'tester'), ('VISHNU', 'VISHNU@GMAIL.COM', 'SJC')]

import pandas as pd
date = ['1/12/2022','13/12/2022','27/12/2022']
cate = ['Nature', 'Computer', 'GK']
score = [76,95,77]
GradeList = zip(date, cate, score)
df = pd.DataFrame(data = GradeList, columns=['Date', 'Category', 'Score'])
print(df.to_string(index=False))