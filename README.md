# Federated Learning for Workload Prediction

## Project Overview

This project explores and compares different machine learning models—**Gated Recurrent Units (GRU)**, **Long Short-Term Memory (LSTM)**, and **Bidirectional LSTM (BiLSTM)**—within a federated learning setup. The primary objective is to predict **CPU utilization percentage** using various VM trace datasets and evaluate the models based on **Mean Squared Error (MSE)**, **Root Mean Squared Error (RMSE)**, and **Mean Absolute Error (MAE)**.

## Federated Learning Setup

The experimentation was conducted using a federated learning framework deployed in a realistic production environment on the **Google Cloud Platform (GCP)**. The federated setup consists of:
- **1 Master VM**
- **3 Worker VMs**

Each worker VM contains different datasets:
- **Materna**
- **PlanetLab**
- **Azure**

### Approach

We employed a **model-centric, cross-silo, Horizontal Federated Learning** approach:
- The central server (**Master VM**) coordinates with the worker VMs, each containing a horizontally split dataset.
- This setup preserves data privacy by keeping raw data localized, while enabling collaborative model training across different data environments.
- The goal is to enhance the model's generalization and robustness through collaborative learning.

## Evaluation Metrics

The models were evaluated using the following metrics:
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **Mean Absolute Error (MAE)**

## Deployment

The most promising model, identified through this comparative study, was deployed in a production environment on **GCP**. The deployment aimed to assess the model's performance and reliability in real-world conditions for workload prediction.

## Results & Insights

The results provide valuable insights into the practical application of advanced machine learning techniques in cloud-based environments. Our project aligns with cutting-edge practices in the field, demonstrating the efficacy and practicality of federated learning paradigms in real-world applications.

## Conclusion

This project highlights the potential of federated learning for workload prediction, emphasizing the balance between **data privacy**, **model accuracy**, and **computational efficiency** in a cloud-based setup.
