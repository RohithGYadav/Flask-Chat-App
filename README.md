# 🧠 Flask Real-Time Chat App

A lightweight, real-time chat application built using **Flask**, **SocketIO**, **MongoDB**, and **REST API**.

---

## 🚀 Features

- Real-time chat using WebSocket (`Flask-SocketIO`)
- REST API for messages (GET, POST)
- MongoDB integration via `pymongo`
- Simple frontend to test WebSocket
- JWT-ready backend structure (extendable)
- Clean, professional project layout

---

## 📁 Project Structure

flask_chat_app/
│
├── app/
│ ├── init.py
│ ├── routes/
│ │ ├── api.py
│ │ └── views.py
│ ├── sockets/
│ │ └── chat.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│
├── run.py
├── requirements.txt
└── README.md
