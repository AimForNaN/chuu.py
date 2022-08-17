import numpy;
from stt import Model as SttModel;
from PySide6.QtCore import QObject, Property, Signal, Slot

from .recorder import Recorder;

class chuu(QObject):
    __recorder = None;
    __stt = None;
    
    recordingStateChanged = Signal();
    transcribe = Signal(str, arguments=['string']); 

    def __init__(self, model='./models/model.tflite', scorer='./models/model.scorer'):
        super().__init__();

        self.__recorder = Recorder();
        self.__stt = SttModel(model);
        self.__stt.enableExternalScorer(scorer);

        self.__recorder.finished.connect(self.recordingStateChanged);
        self.__recorder.recording.connect(self.parse);
        self.__recorder.started.connect(self.recordingStateChanged);

    def getIsRecording(self):
        return self.__recorder.isRunning();

    @Slot()
    def endRecording(self):
        self.__recorder.requestInterruption();

    @Slot(object)
    def parse(self, audio):
        audio = numpy.frombuffer(audio, dtype=numpy.int16);
        self.transcribe.emit(self.__stt.stt(audio));

    @Slot()
    def startRecording(self):
        self.__recorder.start();

    isRecording = Property(bool, getIsRecording, notify=recordingStateChanged);
