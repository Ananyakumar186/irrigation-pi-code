import pandas as pd
df=pd.read_csv(r"temp2.csv",header=0)
df=pd.get_dummies(df)
df = df[['temp','humid','moisture','crop_coconut','cropage_A','cropage_B','cropage_C','texture_clay','texture_silt','texture_sand','water']]
from sklearn.model_selection import train_test_split 
x=df.iloc[:,:10]
y=df.iloc[:,10]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x,y)
from sklearn.metrics import r2_score
y_pred=reg.predict(x_test)
print(r2_score(y_test,y_pred)*100)
import pickle as pkl
pkl.dump(reg,open("model_coconut.sav",'wb'))