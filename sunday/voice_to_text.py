import wave
import pyaudio
import numpy as np
from queue import Queue
from threading import Thread
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import time


class VoiceTranslator():

    def __init__(self) -> None:
        self.FRAMES_PER_BUFFER = 3200
        self.FORMAT = pyaudio.paInt16
        self.NUMPY_FORMAT = np.int16
        self.MODEL_FORMAT = np.float64
        self.CHANNELS = 1
        self.RATE = 16000

        self.recordings = []

    def record_micro(self, frames):
        p = pyaudio.PyAudio()
        stream = p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.FRAMES_PER_BUFFER
        )

        while not frames.empty():
            data = stream.read(self.FRAMES_PER_BUFFER)
            self.recordings.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def audio_to_file(self):
        obj = wave.open('test_1.wav', 'wb')

        obj.setnchannels(self.CHANNELS)
        #obj.setsampwidth(p.get_sample_size(self.FORMAT))
        obj.setframerate(self.RATE)
        obj.writeframes(b''.join(self.frames))
        obj.close()

    def file_to_audio(self):
        obj = wave.open("test_1.wav", "rb")

        sample_freq = obj.getframerate()
        n_samples = obj.getnframes()
        signal_wave = obj.readframes(-1)
        obj.close()
        
        return signal_wave, sample_freq

    def audio_to_text(self):
        if len(self.recordings) <= 0:
            return False, ""
        input_waves = np.frombuffer(b''.join(self.recordings), dtype=np.int16)
        input_waves = input_waves.astype(np.float64) / np.iinfo(np.int16).max

        processor = WhisperProcessor.from_pretrained("openai/whisper-small")
        model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
        input_features = processor(
        input_waves, sampling_rate=self.RATE, return_tensors="pt"
        ).input_features

        predicted_ids = model.generate(input_features)
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

        self.recordings = []
        return True, transcription[0]
    
if __name__ == '__main__':
    #micro_to_audio()
    frames = Queue()
    frames.put(True)

    voice = VoiceTranslator()
    print("Start Recording")
    record = Thread(target=voice.record_micro, args=(frames,))
    record.start()

    time.sleep(2)

    print("End Recording")
    frames.get()
    isSuccessful, text = voice.audio_to_text()

    print(text)