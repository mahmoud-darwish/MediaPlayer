import sys
import numpy as np
import sounddevice as sd
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

# Constants
CHUNK_SIZE = 1024

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-time System Audio Waveform")
        self.setGeometry(100, 100, 800, 400)

        # Timer for updating the waveform
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)  # Update waveform every 50ms

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QPen(Qt.black, 2))
        qp.fillRect(event.rect(), Qt.white)

        # Get audio data from system playback
        data = sd.rec(CHUNK_SIZE, channels=1, blocking=True)[:, 0]

        # Draw wavefor m
        width   = self.width()
        height  = self.height()
        x_scale = width / len(data)
        y_scale = height / 2
        for i in range(len(data) - 1):
            x1  = int(i * x_scale)
            y1  = int(height / 2 - data[i] * y_scale)
            x2  = int((i + 1) * x_scale)
            y2  = int(height / 2 - data[i + 1] * y_scale)
            qp.drawLine(x1, y1, x2, y2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
