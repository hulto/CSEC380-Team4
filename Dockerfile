FROM postgres
# RUN echo "hello world"
RUN apt-get update
RUN apt-get install -y python3 python3-pip
# RUN su postgres -c "pg_ctl init" && \
#     su postgres -c "pg_ctl -D /var/lib/postgresql/data start" && \
#     psql -U postgres -c "CREATE DATABASE thetube;" \
#     psql -U postgres -c "CREATE ROLE root" \
#     psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE thetube TO root"
EXPOSE "5432/tcp"
RUN mkdir -p /app/webserver
COPY ./app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY ./app /app
COPY ./setup_db.sh /setup_db.sh
RUN chmod +x /setup_db.sh
CMD ./setup_db.sh
