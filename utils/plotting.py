import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix


# ✅ 1. Training History Plot
def plot_training_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))

    # Accuracy
    plt.figure()
    plt.plot(epochs, acc, label='Training Accuracy')
    plt.plot(epochs, val_acc, label='Validation Accuracy')
    plt.title('Training vs Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Loss
    plt.figure()
    plt.plot(epochs, loss, label='Training Loss')
    plt.plot(epochs, val_loss, label='Validation Loss')
    plt.title('Training vs Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.show()


# ✅ 2. Class Distribution
def plot_class_distribution(labels):
    unique, counts = np.unique(labels, return_counts=True)

    plt.figure()
    plt.bar(unique, counts)
    plt.title("Class Distribution")
    plt.xlabel("Class (0 = No Tumor, 1 = Tumor)")
    plt.ylabel("Count")
    plt.show()


# ✅ 3. Show Sample Images
def plot_sample_images(X, y, class_names=["No Tumor", "Tumor"]):
    plt.figure(figsize=(10, 10))

    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.imshow(X[i])
        plt.title(class_names[y[i]])
        plt.axis('off')

    plt.tight_layout()
    plt.show()


# ✅ 4. Confusion Matrix
def plot_confusion_matrix(model, X_test, y_test):
    y_pred = (model.predict(X_test) > 0.5).astype("int32")

    cm = confusion_matrix(y_test, y_pred)

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()


# ✅ 5. Prediction Visualization
def plot_predictions(model, X_test, y_test, class_names=["No Tumor", "Tumor"]):
    plt.figure(figsize=(10, 10))

    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.imshow(X_test[i])

        pred = model.predict(X_test[i].reshape(1, *X_test[i].shape))
        label = class_names[int(pred > 0.5)]

        plt.title(f"Pred: {label}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()