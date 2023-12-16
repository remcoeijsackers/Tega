FROM python:3.13-rc-bookworm

ADD requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /code

COPY . /code

ENV FLASK_APP tega

CMD ["python", "-m", "flask", "run", "--port", "9000","--host", "0.0.0.0", "--debug"]

