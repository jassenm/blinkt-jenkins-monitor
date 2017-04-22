FROM blinkt

RUN apt-get install -y python-urllib3

WORKDIR /root/
COPY *.py /root/

ENV JENKINS_BASE_URL=https://builds.apache.org

CMD ["python", "build_monitor.py"]
