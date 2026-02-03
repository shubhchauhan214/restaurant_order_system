# 🍽️ Restaurant Order System (FastAPI + RabbitMQ)

A simple **backend-only restaurant order system** built to practice **RabbitMQ message queues** using **FastAPI**, **SQLite**, and **SQLAlchemy**.

This project demonstrates:
- How a producer publishes messages to RabbitMQ
- How a consumer listens and processes orders asynchronously
- Clean separation of API, database, and messaging logic

---


---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **RabbitMQ**
- **SQLite**
- **SQLAlchemy**
- **Pika (RabbitMQ client)**
- **Uvicorn**

---

## 📁 Project Structure
.
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── consumer.py
├── producer.py
├── routes/
│ └── orders.py
├── .env
├── .gitignore
├── README.md
└── order.db


---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL="sqlite:///./order.db"
RABBITMQ_HOST="localhost"
RABBITMQ_QUEUE="task_queue"




