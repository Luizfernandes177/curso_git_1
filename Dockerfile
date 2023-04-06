FROM python:3

WORKDIR /carguru

COPY . .

EXPOSE 80

CMD ["python", "carguru.py"]