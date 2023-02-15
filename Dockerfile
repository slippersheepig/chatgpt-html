FROM rust:slim-bookworm

RUN apt update && apt install pip -y

WORKDIR /chatgpt-html
ENV PATH="${PATH}:/usr/local/bin:/usr/bin:/bin"
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:80", "main:server", "--timeout", "200", "--worker-class", "gevent"]
