import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import DataHandler as dh


class KMeans: 
    def __init__(self, n_clusters=2, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None

    def fit(self, X):
        X = np.array(X)

        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

        for _ in range(self.max_iter):
            labels = self._assign_labels(X)

            self._update_centroids(X, labels)

        self._plot_clusters(X, labels)

    def _assign_labels(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)

        labels = np.argmin(distances, axis=1)

        return labels

    def _update_centroids(self, X, labels):
        for i in range(self.n_clusters):
            self.centroids[i] = np.mean(X[labels == i], axis=0)

    def _plot_clusters(self, X, labels):
        plt.scatter(X[:, 0], X[:, 1], c=labels)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], marker='x', color='red')
        plt.title("K-Means Clustering")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.show()
if __name__ == "__main__":
    datasets = dh.read_data("data/full")

    X = datasets["winequality-red"].values

    kmeans = KMeans(n_clusters=2, max_iter=100)

    kmeans.fit(X)
