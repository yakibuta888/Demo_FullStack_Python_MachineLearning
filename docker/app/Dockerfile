# syntax=docker/dockerfile:1.4.1
FROM python:3.11-slim

ENV PATH=/workspace/vendor/bin:$PATH \
	PYTHONPATH=/workspace/vendor/bin \
	PYTHONUSERBASE=/workspace/vendor

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	apt-utils \
	gcc \
	build-essential \
	curl \
	uidmap \
	dbus-user-session \
	fuse-overlayfs \
	slirp4netns \
	&& apt-get autoremove -y \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/*

RUN <<-EOF
	curl -fsSL https://get.docker.com/rootless | sh
	cat <<-'_DOC_' >> $HOME/.bashrc
		export PATH=/home/docker_user/bin:$PATH
		export DOCKER_HOST=unix:///run/user/1002/docker.sock
	_DOC_
	. $HOME/.bashrc
	export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock
EOF

RUN pip install --upgrade pip;\
	pip install --no-cache-dir \
	autopep8 \
	flake8 \
	pytest

WORKDIR /workspace
