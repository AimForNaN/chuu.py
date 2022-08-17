import QtQuick
import QtQuick.Controls

FocusScope {
    id: root
    height: 100
    width: 200

    property alias font: input.font
    property alias input: input
    property alias text: input.text

    ScrollView {
        anchors.fill: parent
        focusPolicy: Qt.ClickFocus

        background: Rectangle {
            color: "white"
            border.color: root.focus ? "#94a3b8" : "#cbd5e1"
            border.width: 1
            radius: 3
        }

        TextArea {
            id: input
            background: Item {}
            wrapMode: TextEdit.Wrap
            focus: true
        }
    }
}