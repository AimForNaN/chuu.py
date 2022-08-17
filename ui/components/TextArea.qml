import QtQuick

FocusScope {
    height: 100
    width: 200

    property alias font: input.font
    property alias input: input
    property alias text: input.text

    Rectangle {
        anchors.fill: parent
        color: "white"
        border.color: parent.focus ? "#94a3b8" : "#cbd5e1"
        radius: 3
    }

    TextInput {
        id: input
        anchors.fill: parent
        bottomPadding: 8
        leftPadding: 8
        rightPadding: 8
        topPadding: 8
        wrapMode: TextInput.Wrap
        focus: true
    }
}