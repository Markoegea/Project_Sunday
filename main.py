import gradio as gr

import sunday.voice_to_text as vtt
import sunday.text_to_function as ttf
import sunday.function_to_action as fta

voice = vtt.VoiceTranslator()

def display_text(input_audio):
    gr.Info("Recording Stop, processing audio")

    sr, audio = input_audio # (int, numpy.ndarray.int16)

    # Using the recording audio, start to translate it
    isSuccessful, text = voice.audio_to_text(sr, audio)

    gr.Info(f"Text: {text}")

    # Usign the text from your recording, get the fuction you request
    if (isSuccessful):
        function = ttf.get_function_from_text(text)

        gr.Info(f"Function: {function}")

        # Then evaluate the function
        fta.eval_function(function=function)
    
    return
    

with gr.Blocks() as demo:
    gr.HTML("""
        <div style='text-align: center;'>
            <h1>S.U.N.D.A.Y</h1>
            <h3>(System Using Neural Development Apis Yield)</h3>
            <h2>Version 1.0</h2>
            <p>AI assistant that make your life easier, just life friday, but this is sunday.</p>
        </div>
    """)
    input_audio = gr.Audio(sources=['microphone'], label="Input Audio", type="numpy", format="wav")
    input_audio.stop_recording(fn=display_text, inputs=input_audio, outputs=None, api_name="stop")

demo.launch(share=True)

        