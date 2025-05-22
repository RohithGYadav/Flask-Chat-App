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

flask_chat_app/ <br>
│<br>
├── app/<br>
│ ├── init.py<br>
│ ├── routes/<br>
│ │ ├── api.py<br>
│ │ └── views.py<br>
│ ├── sockets/<br>
│ │ └── chat.py<br>
│ ├── templates/<br>
│ │ └── index.html<br>
│ └── static/<br>
│<br>
├── run.py<br>
├── requirements.txt<br>
└── README.md
