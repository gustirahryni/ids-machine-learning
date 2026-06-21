from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class ModelTrainer:
    def __init__(self):
        self.models = {
            "DT": DecisionTreeClassifier(),
            "RF": RandomForestClassifier(),
            "KNN": KNeighborsClassifier()
        }

    def train(self, X, y):
        for m in self.models.values():
            m.fit(X, y)

    def evaluate(self, X, y):
        results = {}
        for name, m in self.models.items():
            pred = m.predict(X)
            results[name] = accuracy_score(y, pred)
        return results
