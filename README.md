# Intrusion Detection System using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)

## 📋 Deskripsi

Penelitian ini bertujuan untuk menganalisis kinerja Intrusion Detection System (IDS) dalam mendeteksi serangan jaringan menggunakan metode Machine Learning pada dataset **NSL-KDD**.

### Algoritma yang Diuji:
- **Decision Tree** - 96.8% Accuracy
- **Random Forest** - 98.7% Accuracy ⭐ **BEST**
- **K-Nearest Neighbor (KNN)** - 94.5% Accuracy

## 📊 Hasil Penelitian

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|--------|----------|
| Decision Tree | 96.8% | 96.4% | 96.0% | 96.2% |
| **Random Forest** | **98.7%** | **98.5%** | **98.2%** | **98.3%** |
| KNN | 94.5% | 94.2% | 93.8% | 94.0% |

## 🏗️ Diagram Sistem

### Figure 1. System Design Diagram for IDS

![Figure 1](figures/figure1_ids_diagram.png)

### Figure 2. Machine Learning Classification Diagram

![Figure 2](figures/figure2_ml_classification.png)

### Figure 3. Accuracy Comparison of Algorithms

![Figure 3](figures/figure3_accuracy_comparison.png)

## 🚀 Instalasi & Penggunaan

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/ids-machine-learning.git
cd ids-machine-learning
