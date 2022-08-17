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

                onClicked: chuu.start()
            }

            Button {
                Layout.alignment: Qt.AlignBottom
                backgroundColor: "white"
                text: "Stop"
                width: 100
                visible: chuu.isRecording

                onClicked: chuu.stop()
            }
        }

        TextArea {
            id: inputCurrent
            Layout.fillHeight: true
            Layout.fillWidth: true
            font.pixelSize: 16
        }

        TextArea {
            id: inputFinal
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
        function onCurrent(txt) {
            inputCurrent.text = txt;
        }
        function onTranscribe(txt) {
            inputFinal.text = inputFinal.text + txt;
        }
    }
}