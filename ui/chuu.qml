import QtQuick
import QtQuick.Window

import "views"

Window {
    color: "#f8fafc"
    width: 640
    height: 480
    visible: true
    title: qsTr("chuu")

    Index {
        anchors.fill: parent
        anchors.margins: 96
    }
}