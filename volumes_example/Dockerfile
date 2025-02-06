FROM ubuntu:latest

WORKDIR /app
RUN apt-get update && apt-get install -y python3

COPY script.sh .
COPY script.py .

VOLUME ["/app/dados"]

RUN chmod +x script.sh

CMD ["/bin/bash", "-c", "./script.sh && python3 script.py"]
