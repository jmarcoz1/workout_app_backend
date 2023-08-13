FROM python:3.8

ARG UNAME=developer
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID -o $UNAME

RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

RUN apt-get update \
    && apt-get install libpq-dev nginx vim -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt-get/lists/*

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app \
    && mkdir -p /opt/app/pip_cache \
    && mkdir -p /opt/app/backend \
    && chown -R :www-data /opt/app

RUN mkdir -p /home/app/web/staticfiles \
    && mkdir -p /home/app/web/mediafiles/ \
    && chmod 0755 -R /home/app/web/staticfiles

COPY scripts/entrypoint.sh /opt/app/entrypoint.sh

# COPY main/ /opt/app/backend/
# COPY workout_api/ /opt/app/backend/
# COPY db.sqlite3 /opt/app/backend/
# COPY manage.py /opt/app/backend/
# COPY requirements.txt /opt/app/backend/

WORKDIR /opt/app/backend

# RUN pip install -r requirements.txt

EXPOSE 8001

STOPSIGNAL SIGTERM

CMD ["/opt/app/entrypoint.sh"]