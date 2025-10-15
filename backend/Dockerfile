FROM python:3.13.7

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY config.toml .

EXPOSE 8000

ENV PYTHONPATH=/usr/src/app


RUN pip install -e .

CMD ["uvicorn", "presentation.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
