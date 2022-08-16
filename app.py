import imp
import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from lib.chuu import chuu

if __name__ == '__main__':
    app = QGuiApplication(sys.argv);
    engine = QQmlApplicationEngine();

    chuuRef = chuu();
    engine.rootContext().setContextProperty("chuu", chuuRef);

    engine.load(QUrl('ui/chuu.qml'));

    sys.exit(app.exec());
