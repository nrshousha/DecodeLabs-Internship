from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def train_model(X_train, Y_train):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, Y_train)

    return model

def evaluate_model(model, X_test, Y_test):
    y_pred = model.predict(X_test)

    print("model accuracy: ", accuracy_score(Y_test, y_pred))
    print("\nconfusion matrix: ", confusion_matrix(Y_test, y_pred))
    print("\nclassification_report: ", classification_report(Y_test, y_pred))