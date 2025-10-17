FROM python:3.13.7

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV PYTHONPATH=/app


RUN pip install -e .

RUN sh ./scripts/startup.sh

CMD ["uvicorn", "presentation.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
