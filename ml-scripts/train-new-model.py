"""
After change detection, we have to train a new ML Model to capture the new
pattern between elements and their locators.
"""
import pickle
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

DF_FILE = 'locator_label_data.csv'
df = pd.read_csv(DF_FILE)

x = df.drop(['target'])
y = df['target']
train_x, test_x, train_y, test_y = train_test_split(x,
                                                    y,
                                                    test_size=0.15,
                                                    random_state=42)

model = SVC(kernel='linear')
model.fit(train_x, train_y)
train_pred_y = model.predict(train_x)
pred_y = model.predict(test_x)

print("CONFUSION MATRIX (test)")
print(confusion_matrix(test_y, pred_y))

print("CLASSIFICATION REPORT (test)")
print(classification_report(test_y, pred_y))

print(f"Accuracy (test): {accuracy_score(pred_y, test_y)}")
print(f"Accuracy (train): {accuracy_score(train_pred_y, train_y)}")

"""
Now we have the new model available to us.
Let us save it to file.
""""

pickle.dump(model, open('web-locator-identifier-model.sav', 'wb'))
