FROM python:3
WORKDIR /app
COPY ./DonutWebApp .
COPY ./start.sh .
RUN python3 -m pip install django psycopg2-binary gunicorn
RUN chmod +x ./start.sh
CMD ["./start.sh"]
EXPOSE 8000