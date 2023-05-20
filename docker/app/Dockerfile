FROM python:3.11-slim

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	apt-utils \
	gcc \
	build-essential \
	gosu \
	# clean up
	&& apt-get autoremove -y \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/*

ARG WORKDIR
ENV PATH=${WORKDIR}/vendor/bin:$PATH \
	PYTHONPATH=${WORKDIR}/vendor/bin \
	PYTHONUSERBASE=${WORKDIR}/vendor

WORKDIR ${WORKDIR}

# Libraries used only when developing
RUN pip install --upgrade pip;\
	pip install --no-cache-dir \
	autopep8 \
	flake8 \
	pytest

# Create the user
COPY ./docker/app/createuser.sh /usr/bin/createuser.sh
RUN chmod +x /usr/bin/createuser.sh
ENTRYPOINT ["/usr/bin/createuser.sh"]
CMD ["/bin/bash"]
