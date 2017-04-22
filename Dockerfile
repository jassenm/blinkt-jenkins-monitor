FROM blinkt

WORKDIR /root/
COPY *.py /root/

CMD ["python", "build_monitor.py"]
