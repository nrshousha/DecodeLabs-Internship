from src.preprocess import load_and_preprocess
from src.model import train_model, evaluate_model

<<<<<<< HEAD
X_train, X_test, Y_train,  Y_test = load_and_preprocess()
model = train_model(X_train, Y_train)
evaluate_model(model, X_test, Y_test)

=======
X_train, Y_train, X_test, Y_test = load_and_preprocess()
model = train_model(X_train, Y_train)
evaluate_model(model, X_test, Y_test)
>>>>>>> eaca8b12334cba499edb9dcc44f2b107ab468f07
