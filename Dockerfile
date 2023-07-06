# Image
FROM python:3.10 as base

# Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /code

# Linux packages
ADD ./docker-scripts.sh /code/docker-scripts.sh
RUN chmod +x /code/docker-scripts.sh && /code/docker-scripts.sh


FROM base as packages

# Python packages
COPY requirements.txt requirements-docker.txt /code/
RUN pip3 install --upgrade pip && pip3 install -r requirements-docker.txt


# Final Image
FROM base as final

# Coping packages to the final image
COPY --from=packages /opt/venv/ /opt/venv/

# Coping all files to the final image
COPY . /code/
