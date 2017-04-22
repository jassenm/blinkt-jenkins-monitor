FROM blinkt

WORKDIR /root/
COPY *.py .

CMD ["python", "build_monitor.py"]
