FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

EXPOSE 5000

# CMD ["uvicorn", "products_api.main:app", "--host", "0.0.0.0", "--port", "5000"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]