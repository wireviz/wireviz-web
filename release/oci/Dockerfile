# This Dockerfile is meant for release build purposes.
# https://github.com/wireviz/wireviz-web

# syntax=docker/dockerfile:1

# The recipe uses BuildKit's build-time cache mounts, which makes a huge difference on rebuilds.
# - https://vsupalov.com/buildkit-cache-mount-dockerfile/
# - https://github.com/FernandoMiguel/Buildkit#mounttypecache

FROM python:3.14-slim-bookworm

# Enable concurrent multi-arch builds.
# https://github.com/docker/buildx/issues/549#issuecomment-1788297892
ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH
ARG TARGETVARIANT

# Configure operating system.
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=linux

# Configure build environment.
ENV PIP_ROOT_USER_ACTION=ignore
ENV UV_COMPILE_BYTECODE=true
ENV UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_SYSTEM_PYTHON=true

# Install Git, it is needed for `versioningit`.
RUN rm -f /etc/apt/apt.conf.d/docker-clean; echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
RUN --mount=type=cache,id=apt-cache-${TARGETARCH}${TARGETVARIANT},target=/var/cache/apt \
    --mount=type=cache,id=apt-lists-${TARGETARCH}${TARGETVARIANT},target=/var/lib/apt \
    true \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests --yes curl git graphviz

# Install the `uv` package manager.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy sources
COPY . /src

# Install package.
RUN \
    --mount=type=cache,id=pip-${TARGETARCH}${TARGETVARIANT},target=/root/.cache/pip \
    --mount=type=cache,id=uv-${TARGETARCH}${TARGETVARIANT},target=/root/.cache/uv \
    true \
    && uv tool install --upgrade /src

# Copy `selftest.sh` to the image.
COPY release/oci/selftest.sh /usr/local/bin
RUN chmod +x /usr/local/bin/selftest.sh

# Uninstall Git again.
RUN apt-get --yes remove --purge git && apt-get --yes autoremove
# Purge /src and /tmp directories.
RUN rm -rf /src /tmp/*

# Configure runtime environment.
ENV PATH=/root/.local/bin:$PATH
ENV FLASK_APP=wireviz_web
EXPOSE 3005
ENTRYPOINT ["wireviz-web"]
