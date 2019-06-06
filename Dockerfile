FROM python:3.7

WORKDIR /director

COPY MANIFEST.in README.rst Pipfile Pipfile.lock setup.py /director/

COPY director /director/director

RUN pip install ./

CMD ["python", "-u", "-m", "director", "--config", "/domain-director/config.yml"]
