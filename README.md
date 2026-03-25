# 🔐 AI-Based Keylogger Detection System

## 📌 Overview

This project is a **real-time keylogger detection system** built using Python.
It monitors running processes, detects suspicious behavior, and alerts users using a GUI interface.

---

## 🚀 Features

* Real-time process monitoring
* AI-based risk detection (rule-based + ML)
* Suspicious process alert system ⚠️
* GUI interface using Tkinter
* Logging system for threat analysis
* Modular project structure

---

## 🛠️ Technologies Used

* Python
* psutil
* Tkinter
* scikit-learn

---

## 📁 Project Structure

```
keylogger_detector/
│
├── main.py
├── detector.py
├── ai_model.py
├── utils.py
├── logs/
│   └── alerts.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/KartikKD23/keylogger-detector.git
```

2. Navigate to project folder:

```
cd keylogger_detector
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```
python main.py
```

* The system scans processes every 5 seconds
* Alerts are shown for suspicious activity
* Logs are stored in `logs/alerts.txt`

---

## 🤖 How It Works

* Collects running processes using `psutil`
* Extracts features like CPU usage and keywords
* Applies ML model to classify processes
* Displays results in GUI and logs alerts

---

## 🔥 Future Improvements

* Advanced ML model with real dataset
* Dark mode UI
* Process termination feature
* Dashboard with graphs
* Integration with SIEM tools

---

## 📄 License

This project is for educational and ethical cybersecurity purposes only.

---

## 👨‍💻 Author

Kartik Deshmukh
