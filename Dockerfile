FROM python:3-onbuild

EXPOSE 8080

CMD ["python", "./run.py"]