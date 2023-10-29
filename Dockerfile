# определяет базовый образ, на основе которого будет построен ваш образ.
FROM python:3.11

# устанавливаем рабочую директорию внутри контейнера.
WORKDIR /app

# копируем файл requirements.txt (список зависимостей Python) в текущую директорию.
COPY ./requirements.txt .

# выполняется установка зависимостей в контейнере.
RUN pip install -r requirements.txt

# Копируем все файлы из текущего каталога (где находится Docker-файл) в контейнер
COPY . .