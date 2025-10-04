FROM python:3-slim

ARG BUILD_ENV

ENV BUILD_ENV=${BUILD_ENV}

RUN apt update && \ 
	apt install -y python3 graphviz
	
RUN pip install poetry

WORKDIR /usr/src/app

COPY . .

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --only main
  
ENV FLASK_APP=wireviz_web

EXPOSE 3005

ENTRYPOINT ["python","-c","import wireviz_web.cli; wireviz_web.cli.run()"]
CMD ["--listen","0.0.0.0:3005"]
