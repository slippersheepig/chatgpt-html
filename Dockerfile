FROM python:3.10-slim

WORKDIR /chatgpt-html
ENV PATH="${PATH}:/usr/local/bin:/usr/bin:/bin"

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install chromium xvfb xauth -y

CMD ["gunicorn", "-b", "0.0.0.0:80", "main:server", "--timeout", "200", "--worker-class", "gevent"]
