# blinkt-jenkins-monitor

A Jenkins status indicator for Blinkt! LED lamps on a Raspberry Pi.

## How to use

On your raspberry, check out the `pimoroni/blinkt` repo (https://github.com/pimoroni/blinkt) and `docker build` it.

```
cd ~
git clone https://github.com/pimoroni/blinkt.git
cd blinkt
docker build -t blinkt .
```

Now check out this repo and build it:

```
cd ~
git clone https://github.com/kaspersorensen/blinkt-jenkins-monitor.git
cd blinkt-jenkins-monitor
docker build -t jenkins-monitor .
```

And now run it, parameterized with the `JENKINS_BASE_URL` of choice:

```
docker run -rm -e JENKINS_BASE_URL=[your jenkins server's base URL] jenkins-monitor
```