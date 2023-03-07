FROM python:slim

RUN useradd -m appuser
USER appuser
WORKDIR /chatgpt-html
ENV PATH="/home/appuser/.local/bin:$PATH"
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8088", "main:server", "--timeout", "200", "--worker-class", "gevent"]
