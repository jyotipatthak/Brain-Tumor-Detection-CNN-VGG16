from sklearn.model_selection import train_test_split

def preprocess_data(X, y):
    X = X / 255.0

    return train_test_split(X, y, test_size=0.2, random_state=42)