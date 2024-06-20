::: MERHABA DUNYA :::
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask==1.1.4 markupsafe==1.1.1

CMD ["python", "app.py"]
