import gradio as gr
from queue import Queue
from threading import Thread

import sunday.voice_to_text as vtt
import sunday.text_to_function as ttf
import sunday.function_to_action as fta

voice = vtt.VoiceTranslator()

frames = Queue()

button_name = "Record"

def display_text():
    if frames.empty():
        frames.put(True)

        gr.Info("Recording In Progress")

        # Start a thread that record the waveform audio
        record = Thread(target=voice.record_micro, args=(frames,))
        record.start()

        return "Start Recording"
    else:
        frames.get()

        gr.Info("Recording Stop")

        # Using the recording audio, start to translate it
        isSuccessful, text = voice.audio_to_text()

        gr.Info(f"Text: {text}")

        # Usign the text from your recording, get the fuction you request
        if (isSuccessful):
            function = ttf.get_function_from_text(text)

            gr.Info(f"Function: {function}")

            # Then evaluate the function
            fta.eval_function(function=function)
        
        return "Process Complete"
    

with gr.Blocks() as demo:
    gr.HTML("""
        <div style='text-align: center;'>
            <h1>S.U.N.D.A.Y</h1>
            <h3>(System Using Neural Development Apis Yield)</h3>
            <h2>Version 1.0</h2>
            <p>AI assistant that make your life easier, just life friday, but this is sunday.</p>
        </div>
    """)
    record_btn = gr.Button(button_name)
    record_btn.click(fn=display_text, inputs=None, outputs=None, api_name="record")

demo.launch()

        