<<<<<<< HEAD
def evaluate_model(model, X_test, y_test):
    loss, acc = model.evaluate(X_test, y_test)
=======
def evaluate_model(model, X_test, y_test):
    loss, acc = model.evaluate(X_test, y_test)
>>>>>>> 05f2a0cf494bf2db1b59f8431689f12b40618b05
    print(f"Test Accuracy: {acc}")