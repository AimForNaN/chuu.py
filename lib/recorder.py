import numpy;
import pyaudio;

class Recorder:
    Channels = 1; # mono
    Chunks = 320;
    Format = pyaudio.paInt16;
    Rate = 16000;

    __audio = None;
    __stream = None;

    def start(self):
        self.__audio = pyaudio.PyAudio();
        self.__stream = self.__audio.open(
            format=Recorder.Format,
            channels=Recorder.Channels,
            rate=Recorder.Rate,
            input=True,
            frames_per_buffer=Recorder.Chunks
        );

    def chunk(self):
        data = self.__stream.read(Recorder.Chunks);
        return numpy.frombuffer(data, dtype=numpy.int16);

    def stop(self):
        self.__stream.stop_stream();
        self.__stream.close();
        self.__audio.terminate();