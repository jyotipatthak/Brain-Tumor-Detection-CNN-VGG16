<<<<<<< HEAD
def train_model(model, X_train, y_train, X_val, y_val):
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=10,
        batch_size=32
    )

=======
def train_model(model, X_train, y_train, X_val, y_val):
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=10,
        batch_size=32
    )

>>>>>>> 05f2a0cf494bf2db1b59f8431689f12b40618b05
    return history