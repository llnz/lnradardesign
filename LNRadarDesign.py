#! /usr/bin/env python

"""
@author Lee Begg
"""

class CWFMRadarDesign(object):
    """
    This class calculates the key parameters for Continuous Wave
    Frequency Modulated Radar.
    """
    
    c = 3e8
    
    def __init__(self):
        self.sweep = 0.0
        self.modfreq = 0.0
        self.maxrange = 0.0
        self.centrefreq = 0.0
        self.fftpoints = 0
        self.precision = 0.0
        self.minrange = 0.0
        self.maxbeatfreq = 0.0
        
    def maxBeatFrequency(self):
        """Calculates the beat frequency at maximum range"""
        td = self.maxrange * 2.0 / self.c
        freqchange = self.sweep * (self.modfreq * 2.0)
        freqdiff = freqchange * td
        self.maxbeatfreq = freqdiff
        return self.maxbeatfreq
    
    def calcFFTTimeWindow(self):
        """Calculate the time window for a FFT"""
        sampleperiod = 1.0/(self.maxbeatfreq * 2)
        return sampleperiod * self.fftpoints
    
    def range(self, freq):
        """Calculate the range from the beat frequency
        @param freq The beat frequency
        @return The range in metres
        """
        return (freq * (1./(self.modfreq * 2.)) * self.c) / (2 * self.sweep)
    
    def beatFreq(self, range):
        """Calculate the beat frequency for a given range.
        @param range The range in metres
        @return The beat frequency
        """
        return (range * 2. * self.sweep) / (1./(self.modfreq * 2.) * self.c)
    
        
    