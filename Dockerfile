# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем файл requirements.txt в текущую директорию контейнера
COPY requirements.txt .

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего контекста в /app
COPY . .

# Команда для запуска вашего приложения (замените "your_script.py" на ваш файл)
CMD ["python", "main.py"]
