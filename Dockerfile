FROM python:3-slim

ARG BUILD_ENV

ENV BUILD_ENV=${BUILD_ENV}

# Configure build environment.
ENV PIP_ROOT_USER_ACTION=ignore
ENV UV_COMPILE_BYTECODE=true
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_SYSTEM_PYTHON=true

RUN apt-get update && \
	apt-get install --yes python3 graphviz git

RUN pip install uv

WORKDIR /usr/src/app

COPY . .

RUN uv pip install --upgrade .

ENV FLASK_APP=wireviz_web
ENTRYPOINT ["wireviz-web"]
EXPOSE 3005
