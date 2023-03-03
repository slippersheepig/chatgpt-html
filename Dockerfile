FROM python:slim

RUN apt update && apt install git -y
RUN git clone https://github.com/slippersheepig/ChatGPT.git
RUN cd ChatGPT && pip install .
RUN cd .. && rm -rf ChatGPT
RUN apt autoremove git -y

RUN useradd -m appuser
USER appuser
WORKDIR /chatgpt-html
ENV PATH="/home/appuser/.local/bin:$PATH"
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8088", "main:server", "--limit-request-line", "0", "--timeout", "200", "--worker-class", "gevent"]
