FROM pndf/my-py:latest
LABEL author='Sergey'
COPY server.py /server/server.py
COPY wsgi.py /server/wsgi.py
WORKDIR /server
EXPOSE 8080
ENTRYPOINT ["uwsgi", "--socket", "0.0.0.0:8080", "--protocol=http", "-w", "wsgi:app"]