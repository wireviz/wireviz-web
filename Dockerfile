FROM python:3-slim

ARG BUILD_ENV

ENV BUILD_ENV=${BUILD_ENV}

# Configure build environment.
ENV PIP_ROOT_USER_ACTION=ignore
ENV UV_COMPILE_BYTECODE=true
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_SYSTEM_PYTHON=true

RUN apt update && \ 
	apt install -y python3 graphviz git
	
RUN pip install uv

WORKDIR /usr/src/app

COPY . .

RUN uv pip install .
  
ENV FLASK_APP=wireviz_web

EXPOSE 3005

ENTRYPOINT ["python","-c","import wireviz_web.cli; wireviz_web.cli.run()"]
CMD ["--listen","0.0.0.0:3005"]
