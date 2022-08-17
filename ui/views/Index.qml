import QtQuick
import QtQuick.Layouts

import "../components"

Rectangle {
    color: "transparent"
    
    ColumnLayout {
        anchors.fill: parent
        spacing: 8

        RowLayout {
            spacing: 8

            Text {
                Layout.fillWidth: true
                text: "chuu"
                font.pixelSize: 36
            }

            Button {
                Layout.alignment: Qt.AlignBottom
                backgroundColor: "white"
                text: "Record"
                width: 100
                visible: !chuu.isRecording

                onClicked: chuu.startRecording()
            }

            Button {
                Layout.alignment: Qt.AlignBottom
                backgroundColor: "white"
                text: "Stop"
                width: 100
                visible: chuu.isRecording

                onClicked: chuu.endRecording()
            }
        }

        TextArea {
            id: input
            Layout.fillHeight: true
            Layout.fillWidth: true
            font.pixelSize: 16
        }

        Button {
            Layout.fillWidth: true
            border.color: "#334155"
            backgroundColor: "#334155"
            color: "white"
            text: "Copy Text"
        }
    }

    Connections {
        target: chuu
        function onTranscribe(txt) {
            input.text = input.text + txt;
        }
    }
}