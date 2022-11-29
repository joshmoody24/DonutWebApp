FROM python:3.120a2-alpine3.17
WORKDIR /app
COPY ./DonutWebApp .
RUN yum -y update
RUN python3 -m pip install django psycopg2-binary gunicorn
CMD ["gunicorn", "DonutWebApp.wsgi", "-D"]
EXPOSE 8000