<<<<<<< HEAD
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import build_model
from src.evaluate import evaluate_model
from utils.config import IMG_SIZE, DATA_PATH, EPOCHS, BATCH_SIZE

from utils.plotting import (
    plot_training_history,
    plot_class_distribution,
    plot_sample_images,
    plot_confusion_matrix,
    plot_predictions
)


def main():
    print("🚀 Starting Brain Tumor Detection Pipeline...")

    # 1. Load Data
    print("📂 Loading data...")
    X, y = load_data(DATA_PATH, IMG_SIZE)

    # 👉 ADD HERE (before training)
    print("📊 Showing dataset insights...")
    plot_class_distribution(y)
    plot_sample_images(X, y)

    # 2. Preprocess Data
    print("🧼 Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(X, y)

    # 3. Build Model
    print("🧠 Building model...")
    model = build_model((IMG_SIZE, IMG_SIZE, 3))

    # 4. Train Model
    print("🏋️ Training model...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )

    # 👉 ADD HERE (after training)
    print("📈 Plotting training results...")
    plot_training_history(history)

    # 5. Evaluate Model
    print("📊 Evaluating model...")
    evaluate_model(model, X_test, y_test)

    # 👉 ADD HERE (after evaluation)
    print("📊 Showing confusion matrix...")
    plot_confusion_matrix(model, X_test, y_test)

    print("🔍 Showing predictions...")
    plot_predictions(model, X_test, y_test)

    print("✅ Pipeline completed successfully!")


if __name__ == "__main__":
=======
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model
from utils.config import IMG_SIZE, DATA_PATH, EPOCHS, BATCH_SIZE


def main():
    print("🚀 Starting Brain Tumor Detection Pipeline...")

    # 1. Load Data
    print("📂 Loading data...")
    X, y = load_data(DATA_PATH, IMG_SIZE)

    # 2. Preprocess Data
    print("🧼 Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(X, y)

    # 3. Build Model
    print("🧠 Building model...")
    model = build_model((IMG_SIZE, IMG_SIZE, 3))

    # 4. Train Model
    print("🏋️ Training model...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )

    # 5. Evaluate Model
    print("📊 Evaluating model...")
    evaluate_model(model, X_test, y_test)

    print("✅ Pipeline completed successfully!")


if __name__ == "__main__":
>>>>>>> 05f2a0cf494bf2db1b59f8431689f12b40618b05
    main()