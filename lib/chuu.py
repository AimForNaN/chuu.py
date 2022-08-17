from PySide6.QtCore import QThread, Property, Signal, Slot

from .recorder import Recorder;
from .transcriber import Transcriber

class chuu(QThread):
    __recorder = None;
    __transcriber = None;
    
    recordingStateChanged = Signal();
    current = Signal(str, arguments=['string']); 
    transcribe = Signal(str, arguments=['string']); 

    def __init__(self, model='./models/model.tflite', scorer='./models/model.scorer'):
        super().__init__();

        self.__recorder = Recorder();
        self.__transcriber = Transcriber(model, scorer);

        self.finished.connect(self.recordingStateChanged);
        self.started.connect(self.recordingStateChanged);


    def getIsRecording(self):
        return self.isRunning();

    def run(self):
        self.__recorder.start();
        self.__transcriber.start();

        while self.isInterruptionRequested() is False:
            chunk = self.__recorder.chunk();
            if chunk is not None:
                self.__transcriber.push(chunk);
                self.current.emit(self.__transcriber.current());

        self.__recorder.stop();
        self.transcribe.emit(self.__transcriber.stop());

    @Slot()
    def stop(self):
        self.requestInterruption();

    isRecording = Property(bool, getIsRecording, notify=recordingStateChanged);
