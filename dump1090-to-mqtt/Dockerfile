FROM python:3.11-slim AS compile-image

RUN python -m venv /opt/venv
RUN /opt/venv/bin/python -m pip install --upgrade pip
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY setup.py .
COPY ./ .
RUN pip install .

FROM python:3.11-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
