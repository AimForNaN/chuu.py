from stt import Model as SttModel;

class Transcriber():
    __stream = None;
    __stt = None;

    def __init__(self, model, scorer):
        self.__stt = SttModel(model);
        self.__stt.enableExternalScorer(scorer);

    def current(self):
        if self.__stream is not None:
            return self.__stream.intermediateDecode();

    def push(self, chunk):
        if self.__stream is not None:
            self.__stream.feedAudioContent(chunk);

    def start(self):
        self.__stream = self.__stt.createStream();

    def stop(self):
        if self.__stream is not None:
            return self.__stream.finishStream();
        return '';

    def stt(self, data):
        return self.__stt.stt(data);