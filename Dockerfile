FROM blinkt

RUN apt-get install python3

WORKDIR /root/
COPY *.py /root/

CMD ["python3", "build_monitor.py"]
