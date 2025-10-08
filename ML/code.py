import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from imblearn.over_sampling import RandomOverSampler

#knn import
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

#nb import
from sklearn.naive_bayes import GaussianNB

#logreg import
from sklearn.linear_model import LogisticRegression

#svm import
from sklearn.svm import SVC




cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("./magic04.data", names = cols)

df["class"] = (df["class"] == "g").astype(int)

train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

def scale_dataset(dataframe, oversample = False):
    X = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    if oversample:
        ros = RandomOverSampler()
        X, y = ros.fit_resample(X, y)

    data = np.hstack((X, y.reshape(-1, 1)))

    return data, X, y

train, X_train, y_train = scale_dataset(train, oversample=True)
valid, X_valid, y_valid = scale_dataset(valid, oversample=False)
test, X_test, y_test = scale_dataset(test, oversample=False)


#knn

knn_model = KNeighborsClassifier(n_neighbors=300)
knn_model.fit(X_train, y_train)

y_pred_knn = knn_model.predict(X_test)
print(classification_report(y_test, y_pred_knn)) 

#Naive Bayes
nb_model = GaussianNB()
nb_model = nb_model.fit(X_train, y_train)

y_pred_nb = nb_model.predict(X_test)
print(classification_report(y_test, y_pred_nb))

#Logistic Regression
lg_model = LogisticRegression()
lg_model = lg_model.fit(X_train, y_train)

y_pred_lg = lg_model.predict(X_test)
print(classification_report(y_test, y_pred_lg))

#SVM
svm_model = SVC()
svm_model = svm_model.fit(X_train, y_train)

y_pred_svm = svm_model.predict(X_test)
print(classification_report(y_test, y_pred_svm))