import unittest
from build_monitor import BuildMonitor
from feed_source import FeedSource, TestFeedSource
from lamps import Lamps, ConsoleLamps


class BuildMonitorTest(unittest.TestCase):
    """My unit test"""

    def _get_test_feed(self):
        file = open("rss-formatted.xml")
        # remove trailing '\n' newline character.
        feedData = file.read().rstrip()
        file.close()
        return feedData

    def testStartLoop(self):
        """Runs a small example loop"""

        feedData = self._get_test_feed()
        self.assertTrue(len(feedData) > 100)
        svr = BuildMonitor(lampsObj=ConsoleLamps(num_lights=3),
                           feedSrc=TestFeedSource(feedData), refreshRate=1)
        svr.start_timer(loopCount=3)

    def testGetLatestFeedColorsWithFewerLampsThanBuilds(self):
        """My test method"""

        feedData = self._get_test_feed()

        self.assertTrue(len(feedData) > 100)
        svr = BuildMonitor(lampsObj=ConsoleLamps(num_lights=5),
                           feedSrc=TestFeedSource(feedData))
        colors = svr.get_latest_feed_colors()
        self.assertEqual(5, len(colors))  # we only have 5 lamps defined
        self.assertEqual((0, 255, 0), colors[0])  # first build is good
        self.assertEqual((255, 0, 0), colors[1])  # second build is broken

    def testGetLatestFeedColorsWithMoreLampsThanBuilds(self):
        """My test method"""

        feedData = self._get_test_feed()

        self.assertTrue(len(feedData) > 100)
        svr = BuildMonitor(lampsObj=ConsoleLamps(num_lights=500),
                           feedSrc=TestFeedSource(feedData))
        colors = svr.get_latest_feed_colors()
        self.assertEqual(500, len(colors))  # we only have 5 lamps defined
        self.assertEqual((0, 255, 0), colors[0])  # first build is good
        self.assertEqual((255, 0, 0), colors[1])  # second build is broken
        # 300th build does not exist, so it's black
        self.assertEqual((0, 0, 0), colors[300])


if __name__ == '__main__':
    unittest.main()
