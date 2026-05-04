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
    main()