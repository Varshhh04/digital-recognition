# 🧠 Handwritten Digit Recognition with CNN

This project is a **Handwritten Digit Recognition System** built using **Convolutional Neural Networks (CNNs)** and the **MNIST dataset**. The model is trained to classify digits (0-9) from handwritten images.



## 🚀 **Features**
✅ Uses **TensorFlow** and **Keras** to build a CNN model  
✅ Trained on the **MNIST dataset** (70,000 images)  
✅ Achieves high accuracy on test data  
✅ Uses **Matplotlib** for visualization  

---

## 🛠 **Installation & Setup**
### 🔹 1. Clone the Repository
```bash
git clone https://github.com/your-username/digit-recognition.git
cd digit-recognition
```

### 🔹 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 🔹 3. Install Dependencies
```bash
pip install -r requirements.txt
```



## 🚀 **How to Run**
1️⃣ **Run the script**  
```bash
python digit_recognition.py
```
2️⃣ The model will train and display accuracy.  
3️⃣ A **random test image** will be shown along with the **predicted digit**.



## 📂 **Project Structure**
```
📦 digit-recognition
│-- 📜 digit_recognition.py    # Main Python script
│-- 📜 requirements.txt        # Dependencies
│-- 📜 README.md               # Project Documentation
│-- 📂 dataset                 # (Optional) If storing external datasets
│-- 📂 models                  # (Optional) Saved trained models
```


## 🏗 **Model Architecture**
- **Conv2D (32 filters, 3x3 kernel, ReLU)**
- **MaxPooling2D (2x2)**
- **Conv2D (64 filters, 3x3 kernel, ReLU)**
- **MaxPooling2D (2x2)**
- **Flatten Layer**
- **Dense Layer (128 neurons, ReLU)**
- **Output Layer (10 neurons, Softmax)**



## 📊 **Results**
- **Training Accuracy:** ~99%  
- **Test Accuracy:** ~98%  



## 📝 **To-Do / Future Improvements**
Add GUI using **Tkinter** or **Streamlit**  
Deploy model as a **Web App**  
Train on **custom handwritten images**  



## 💡 **Contributing**
Pull requests are welcome! Feel free to **fork** this repository and improve the project.





### 🔥 **How to Use This?**
1. **Copy this README.md** and update:  
   - **GitHub link** in `git clone https://github.com/your-username/digit-recognition.git`
   - **Your Name & Contact Info**  
2. Save it in your **GitHub repository**  
3. **Commit & Push** to GitHub:
   
   bash
   git add README.md
   git commit -m "Added README"
   git push origin main
   
