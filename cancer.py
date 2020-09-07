import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,f1_score
import pickle
df=pd.read_csv('breast-cancer-wisconsin.txt')
#print(df.head())
#print(df.info())
## checking null values
#for i in df.columns:
    #print(f"{i}:{df[i].isnull().sum()}")
#for i in df.columns:
    #for ii in df[i].values:
        #if(ii=='?'):
           # print(i)
           # break
## handling the null values:
#print(df['Bare Nuclei'].unique())
##print(df['Bare Nuclei'].mode())
df['Bare Nuclei'].replace('?',df['Bare Nuclei'].mode().values[0],inplace=True)
#print(df['Bare Nuclei'].unique())
for i in df['Bare Nuclei'].values:
    df['Bare Nuclei'].replace(i,int(i),inplace=True)
#print(df['Bare Nuclei'].unique())
#print(df.info())
## DROP THE UNIQUE COLUMN
df.drop(['id'],axis=1,inplace=True)
## DIFFERENTIATE THE FEATURES AND LABELS
x=df.drop(['Class'],axis=1)
y=df['Class']
## TRAIN_TEST_SPLIT
#X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=42)
### converting the 2 to 0 and 4 to 1
d={
   2:0,
   4:1
   }
y.replace(d,inplace=True)
## SCALING THE FEATURRES
#x=scale(x)

## SELECT A MODEL
clf=RandomForestClassifier()
clf.fit(x,y)
#print(clf.score(x,y))

pickle.dump(clf,open('cancer.pkl','wb'))

clf=pickle.load(open('cancer.pkl','rb'))
#s=scale()
print(clf.predict([[5,1,1,1,2,1,3,1,1]]))
