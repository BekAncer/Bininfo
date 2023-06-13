FROM python:slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 5000

COPY ./src /code/src

CMD ["uvicorn", "src.main:setup_app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug", "--reload", "--factory"]
