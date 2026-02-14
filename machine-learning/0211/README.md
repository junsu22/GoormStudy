# CNN Learning Mechanism Practice
> A minimal experiment to observe how CNN training updates model weights and shifts decision boundaries through gradient-based optimization.


This project demonstrates how a Convolutional Neural Network (CNN) learns through Gradient Descent and how Decision Boundaries change during training.


## 🧠 Model Architecture

CNN Structure:

Input (1×32×32)
→ Conv2D + ReLU
→ MaxPooling
→ Conv2D + ReLU
→ MaxPooling
→ Flatten
→ Fully Connected Layers
→ Logits Output

## ⚙️ Training Flow

1. Forward pass
2. Loss calculation (CrossEntropyLoss)
3. Backpropagation (`loss.backward()`)
4. Gradient Descent update (`optimizer.step()`)

## 🔍 Key Experiment

Weights of the final layer are printed before and after updates to verify that learning actually occurs.

This confirms that Gradient Descent modifies model parameters and shifts the Decision Boundary.

## 🛠 Tech Stack

- Python
- PyTorch

## 📁 File

- `cnn_gd_decisionboundary.py`

## 📌 Key Insight

Deep learning training can be interpreted as continuously adjusting Decision Boundaries through gradient-based optimization.
