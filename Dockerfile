FROM python:3.10-slim

WORKDIR /home

COPY requirements.txt /home/

RUN pip install --no-cache-dir -r requirements.txt

COPY interfaces.py /home/
COPY embedding_service.py /home/
COPY job_matcher.py /home/
COPY src/ /home/src/

COPY data/ /home/data/

CMD ["pytest"]