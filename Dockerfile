FROM python:3.8-slim

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

EXPOSE 5000

ENTRYPOINT ["python", "run.py"]