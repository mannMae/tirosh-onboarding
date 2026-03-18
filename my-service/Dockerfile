FROM python:3.14-rc-slim

WORKDIR /app

COPY dist/*.whl .

RUN pip install *.whl

CMD ["my-service"]