FROM pndf/my-py:latest
LABEL author='I'
COPY client.py /client/client.py
COPY wsgi.py /client/wsgi.py
WORKDIR /client
EXPOSE 8080
ENTRYPOINT ["uwsgi", "--socket", "0.0.0.0:8080", "--protocol=http", "-w", "wsgi:app"]