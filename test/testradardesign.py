#!/usr/bin/env python

import unittest
import sys

sys.path.append('../')

import LNRadarDesign

class TestRadarDesign(unittest.TestCase):
    def setUp(self):
        self.radar = LNRadarDesign.CWFMRadarDesign()
        self.radar.maxrange = 5000.0
        self.radar.sweep = 100e6
        self.radar.modfreq = 100.0
        self.radar.centrefreq = 4.3e9
        self.radar.fftpoints = 64
        self.radar.precision = 0.03
        self.radar.minrange = 2
    
    def testMaxBeatFreq(self):
        self.assertAlmostEqual(self.radar.maxBeatFrequency(), 666666.6666667)

if __name__ == '__main__':
    unittest.main()
