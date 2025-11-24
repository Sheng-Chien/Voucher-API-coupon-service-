# Voucher API

A simple coupon management RESTful API built with **APIFlask** and **SQLAlchemy**.

## 📁Project Structure

coupon-service/
├── app/
│ ├── init.py
│ ├── extensions.py
│ ├── models.py
│ ├── schemas.py
│ └── views/
│ ├── init.py
│ └── coupons.py
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── sql_init.sql

## 🚀 安裝方式 Installation

<!-- ### 1. Create virtual environment -->

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


# <!-- 2. Install dependencies -->

```bash
pip install -r requirements.txt


<!-- 3. Initialize the database -->
```bash
sqlite3 coupon.db < sql_init.sql


## ▶️ 如何啟動專案 Run the app

```bash
python main.py


# API runs at:
http://127.0.0.1:5000/

# API docs (APIFlask default):
http://127.0.0.1:5000/docs


##  API Endpoints

- `GET /coupons`  #List coupons
- `POST /coupons`   #Create a coupon
- `GET /`  #Health check

#Run with Docker

#1.Build image

```bash
docker build -t coupon-service .

#2.Run container

```bash
docker run -p 5000:5000 coupon-service

# Application will be available at:

http://127.0.0.1:5000/

# 3.Run container with mounted SQL data file (optional)

docker run -p 5000:5000 -v ./sql_init.sql:/opt/sql_init.sql coupon-service


# 🐳 docker-compose 

# If you use SQLite，you can use following 'docker-compose.yml'：

version: "3.9"

services:
  coupon-service:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./sql_init.sql:/opt/sql_init.sql
    environment:
      - FLASK_ENV=development

# 起動 start the docker compose
docker compose up --build

# 🐳 Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]


