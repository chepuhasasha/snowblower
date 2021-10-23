FROM python:3

WORKDIR /usr/src/app

COPY ./code/api/ .

RUN ls && \
    python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r ./requirements.txt && \
    pip install --no-cache-dir gunicorn

CMD [ "gunicorn", "-w 2", "-b 0.0.0.0:8000", "wsgi:app"]