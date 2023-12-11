import wave
import librosa
import numpy as np
from transformers import WhisperProcessor, WhisperForConditionalGeneration


class VoiceTranslator():

    def __init__(self) -> None:
        self.FRAMES_PER_BUFFER = 3200
        self.NUMPY_FORMAT = np.int16
        self.MODEL_FORMAT = np.float64
        self.CHANNELS = 1
        self.RATE = 16000

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

    def audio_to_text(self, sample_rate:int, waveforms=None):
        if type(waveforms) == None:
            return False, ""
        
        input_waves = np.frombuffer(waveforms, dtype=np.int16)
        input_waves = input_waves.astype(np.float64) / np.iinfo(np.int16).max

        if sample_rate != self.RATE:
            input_waves = librosa.resample(input_waves, orig_sr=sample_rate, target_sr=self.RATE)

        processor = WhisperProcessor.from_pretrained("openai/whisper-small")
        model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
        model.config.forced_decoder_ids = None

        input_features = processor(
        input_waves, sampling_rate=self.RATE, return_tensors="pt"
        ).input_features

        predicted_ids = model.generate(input_features)
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

        return True, transcription[0]