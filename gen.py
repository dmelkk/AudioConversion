import wave
import array
import math

# simple wave generation funtion
def gen(duration=5, freq=440, volume=100, sampleRate=44100, numOfChannels=1, dataSize=2):
    data = array.array('h')
    numSamplesPerCyc = int(sampleRate / freq)
    numSamples = sampleRate * duration
    for i in range(numSamples):
        sample = 32767 * float(volume) / 100
        sample *= math.sin(math.pi * 2 * (i % numSamplesPerCyc) / numSamplesPerCyc)
        data.append(int(sample))
    with wave.open('SineWave_' + str(freq) + 'Hz.wav', 'w') as output_file:
        output_file.setparams((numOfChannels, dataSize, sampleRate, numSamples, 'NONE', 'Uncompressed'))
        output_file.writeframes(data.tostring())


def main():
    gen()


if __name__ == '__main__':
    main()

