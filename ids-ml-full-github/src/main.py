from preprocessing import DataPreprocessor
from train_model import ModelTrainer
from evaluate_model import ModelEvaluator

def main():
    print("Running IDS ML Pipeline...")
    pre = DataPreprocessor()
    X_train, X_test, y_train, y_test = pre.run()

    trainer = ModelTrainer()
    trainer.train(X_train, y_train)
    results = trainer.evaluate(X_test, y_test)

    evaluator = ModelEvaluator()
    evaluator.visualize(results)

if __name__ == "__main__":
    main()
