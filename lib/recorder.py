from PySide6.QtCore import QThread, Signal;
import pyaudio;

class Recorder(QThread):
    Channels = 1; # mono
    Chunks = 320;
    Format = pyaudio.paInt16;
    Rate = 16000;

    recording = Signal(object, arguments=['object']);
    
    def run(self):
        chunks = [];
        p = pyaudio.PyAudio();
        stream = p.open(
            format=Recorder.Format,
            channels=Recorder.Channels,
            rate=Recorder.Rate,
            input=True,
            frames_per_buffer=Recorder.Chunks
        );

        # self = QThread.currentThread();
        while self.isInterruptionRequested() is False:
            chunk = stream.read(Recorder.Chunks);
            chunks.append(chunk);

        stream.stop_stream();
        stream.close();
        p.terminate();

        data = b''.join(chunks);
        self.recording.emit(data);