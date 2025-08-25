FROM python:3.13

WORKDIR /app

RUN apt update && apt upgrade -y && \
    apt install -y \
        libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
        libxkbcommon0 libxcomposite1 libxdamage1 libxrandr2 libgbm1 \
        libasound2 libpangocairo-1.0-0 libpango-1.0-0 libgtk-3-0 \
        libx11-xcb1 libxcb-dri3-0 libxshmfence1 libxrender1 libxext6 \
        libxfixes3 libx11-6 libxtst6 libglib2.0-0 fonts-liberation \
        libappindicator3-1 lsb-release xdg-utils wget curl

RUN pip install playwright==1.54.0
RUN playwright install chromium

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python", "main.py"]