import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Label {
    id: root
    color: "#0f172a"
    horizontalAlignment: Qt.AlignHCenter 
    bottomPadding: 8
    leftPadding: 10
    rightPadding: 10
    topPadding: 8

    property alias backgroundColor: bg.color
    property alias border: bg.border

    signal clicked()

    background: Rectangle {
        id: bg
        anchors.fill: parent
        border.color: "#cbd5e1"
        border.width: 1
        color: "transparent"
        implicitHeight: 32
        radius: 3
    }

    MouseArea {
        id: m
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor
        onClicked: root.clicked()
    }
}