<<<<<<< HEAD
from sklearn.model_selection import train_test_split

def preprocess_data(X, y):
    X = X / 255.0

=======
from sklearn.model_selection import train_test_split

def preprocess_data(X, y):
    X = X / 255.0

>>>>>>> 05f2a0cf494bf2db1b59f8431689f12b40618b05
    return train_test_split(X, y, test_size=0.2, random_state=42)