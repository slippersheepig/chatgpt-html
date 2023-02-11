FROM python:slim

RUN apt update && apt install chromium xvfb xauth -y

WORKDIR /chatgpt-html
ENV PATH="${PATH}:/usr/local/bin:/usr/bin:/bin"
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY :1
ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
