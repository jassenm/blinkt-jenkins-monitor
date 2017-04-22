from xml.etree import ElementTree as etree
import lamps
import feed_source
import time
import xml
import os


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 190, 0)
pink = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)


class BuildMonitor():

    def __init__(self, lampsObj: lamps.Lamps=None, feedSrc: feed_source.FeedSource=None, refreshRate: int = 30):
        self.lamps = lampsObj
        self.feedSource = feedSrc
        self.refreshRate = refreshRate

    def start_timer(self, loopCount: int = -1):
        loopIndex = 0
        while (loopCount < 0) or (loopIndex != loopCount):
            colors = self.get_latest_feed_colors()
            for i in range(len(colors)):
                self.set_color(i, colors[i])
            loopIndex = loopIndex + 1
            time.sleep(self.refreshRate)

    def __get_color(self, title: str):
        if "(broken since this build)" in title:
            return red
        elif "(back to normal)" in title:
            return green
        elif "(stable)" in title:
            return green
        else:
            print("Unexpected title format: " + title)
            return yellow

    def get_latest_feed_colors(self):
        """Gets the colors to put on the lamps based on the latest feed"""
        feedData = self.feedSource.get_feed_data()
        root = xml.etree.ElementTree.fromstring(feedData)
        entries = root.findall("{http://www.w3.org/2005/Atom}entry")
        colors = []
        for entry in entries[:self.lamps.count_lights()]:
            title = entry.findtext("{http://www.w3.org/2005/Atom}title")
            color = self.__get_color(title)
            colors.append(color)
        while len(colors) < self.lamps.count_lights():
            colors.append(black)  # add black for remaining
        return colors

    def set_color(self, i, color):
        """Sets a particular color on a particular lamp"""
        self.lamps.set_light(i, color)

if __name__ == '__main__':
    jenkinsBaseUrl = os.environ.get("JENKINS_BASE_URL")
    if jenkinsBaseUrl is None or jenkinsBaseUrl == "":
        raise Exception("Please specify JENKINS_BASE_URL environment variable")
    feedSrc = feed_source.JenkinsFeedSource(jenkinsBaseUrl)

    lampsType = os.environ.get("LAMPS_TYPE", "BLINKT")
    if lampsType == "BLINKT":
        lampsObj = lamps.BlinktLamps()
    else:
        lampsObj = lamps.ConsoleLamps()

    refreshRate = int(os.environ.get("REFRESH_RATE", "30"))

    monitor = BuildMonitor(
        lampsObj=lampsObj, feedSrc=feedSrc, refreshRate=refreshRate)
    monitor.start_timer(-1)  # run infinitely
