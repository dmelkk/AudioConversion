import sys
import wave
import numpy as np

class Record(object):
    def __init__(self, file_name):
        self.record = wave.open(file_name, 'r')
        (self.nchannel, self.sampwidth, self.framerate, self.nframes, self.comptype, self.compname) = self.record.getparams()
        self.content = self.record.readframes(nframes)
        types = {
                1: np.int8,
                2: np.int16,
                4: np.int32
        }
        self.samples = np.fromstring(self.content, dtype=types[self.sempwidth])
        # now working only with one chennel, change this later
        for n in range(self.nchannels):
            self.channel = self.sample[n::nchannels]
        self.duration = self.nframes / self.framerate # duration in seconds


def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        print("No file name was given.")


if __name__ == '__main__':
    main()
