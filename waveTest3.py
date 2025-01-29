import sys
import pyaudio
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QPen
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

        # Audio stream and PyAudio setup
        self.audio = pyaudio.PyAudio()
        self.stream = None

        # Timer for updating the waveform
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)  # Update waveform every 50ms

        # Buttons for manipulation
        self.play_button = QPushButton("Play", self)
        self.play_button.clicked.connect(self.playAudio)
        self.play_button.setGeometry(20, 20, 80, 30)

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.clicked.connect(self.pauseAudio)
        self.pause_button.setGeometry(120, 20, 80, 30)

        self.mute_button = QPushButton("Mute", self)
        self.mute_button.clicked.connect(self.muteAudio)
        self.mute_button.setGeometry(220, 20, 80, 30)

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
        x_scale = 2*width / len(data)
        y_scale = height / 65536  # Maximum amplitude for 16-bit audio
        for i in range(len(data) - 1):
            x1 = int(i * x_scale)
            y1 = int(height / 2 - data[i] * y_scale)
            x2 = int((i + 1) * x_scale)
            y2 = int(height / 2 - data[i + 1] * y_scale)
            qp.drawLine(x1, y1, x2, y2)

    def playAudio(self):
        if self.stream is None:
            self.stream = self.audio.open(format=FORMAT,
                                          channels=self.num_channels,
                                          rate=self.sample_rate,
                                          output=True,
                                          stream_callback=self.callback)
            self.stream.start_stream()

    def pauseAudio(self):
        if self.stream is not None:
            self.stream.stop_stream()

    def muteAudio(self):
        pass  # Placeholder for mute functionality

    def callback(self, in_data, frame_count, time_info, status):
        data = self.audio_file.readframes(frame_count)
        return (data, pyaudio.paContinue)

    def closeEvent(self, event):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.audio_file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
