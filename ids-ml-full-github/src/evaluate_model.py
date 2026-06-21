import matplotlib.pyplot as plt

class ModelEvaluator:
    def visualize(self, results):
        plt.bar(results.keys(), results.values())
        plt.title("Accuracy Comparison")
        plt.show()
