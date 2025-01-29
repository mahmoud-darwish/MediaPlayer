import sys
import pyaudio
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import wave
# Constants
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

 # Replace with the path to your audio file

AUDIO_FILE = "Hadded.wav"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-time Audio Waveform")
        self.setGeometry(100, 100, 800, 400)

        # Open audio file
        self.audio_file = wave.open(AUDIO_FILE, 'rb')
        self.sample_width = self.audio_file.getsampwidth()
        self.num_channels = self.audio_file.getnchannels()
        self.sample_rate = self.audio_file.getframerate()

        # Audio stream setup
        self.chunk_size = CHUNK_SIZE
        self.total_frames = self.audio_file.getnframes()
        self.frames_read = 0

        # Timer for updating the waveform
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)  # Update waveform every 50ms

    def read_audio_frames(self):
        frames_to_read = min(self.chunk_size, self.total_frames - self.frames_read)
        audio_data = self.audio_file.readframes(frames_to_read)
        self.frames_read += frames_to_read
        return audio_data

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QPen(Qt.black, 2))
        qp.fillRect(event.rect(), Qt.white)

        # Draw waveform
        data = np.frombuffer(self.read_audio_frames(), dtype=np.int16)
        width = self.width()
        height = self.height()
        x_scale = width / len(data)
        y_scale = height / 65536  # Maximum amplitude for 16-bit audio
        for i in range(len(data) - 1):
            x1 = int(i * x_scale)
            y1 = int(height / 2 - data[i] * y_scale)
            x2 = int((i + 1) * x_scale)
            y2 = int(height / 2 - data[i + 1] * y_scale)
            qp.drawLine(x1, y1, x2, y2)

    def closeEvent(self, event):
        self.audio_file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())