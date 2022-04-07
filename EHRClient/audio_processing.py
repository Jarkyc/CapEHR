from google.cloud import speech
import pyaudio
import wave
import threading
import main as home

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

st = 0

def main():
    pass

if __name__ == "__main__":
    main()

def transcribe_file(speech_file):
    """Transcribe the given audio file asynchronously."""

    client = speech.SpeechClient()

    # [START speech_python_migration_async_request]
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=44100,
        language_code="en-US",
        use_enhanced=True,
        model="command_and_search"
    )

    # [START speech_python_migration_async_response]

    operation = client.long_running_recognize(config=config, audio=audio)
    # [END speech_python_migration_async_request]

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        return(result.alternatives[0].transcript)
    # [END speech_python_migration_async_response]


# [END speech_transcribe_async]

def record_audio():

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording started")

    frames = []

    global st
    st = 1
    try:
        while st == 1:
            data = stream.read(CHUNK)
            frames.append(data)
    except Exception as e:
        print(str(e))

    sample_width = p.get_sample_size(FORMAT)

    stream.stop_stream()
    stream.close()
    p.terminate()

    return sample_width, frames


def record_to_file():
    print("running")
    file_path="audio.wav"
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    sample_width, frames = record_audio()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    home.make_request()


def stop_recording():
    global st
    st = 0


def start_recording():
    x = threading.Thread(target=record_to_file)
    x.start()

