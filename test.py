import os
import speech_recognition as sr

# r = sr.Recognizer()
# with sr.AudioFile('I-dont-know.wav') as source:
#     audio_text = r.listen(source)
#     try:
#         text = r.recognize_google(audio_text)
#         print('Converting audio transcripts into text ...')
#         print(text)
#     except:
#         print('Sorry.. run again...')


def audio_to_text():
    r = sr.Recognizer()
    # audio = download_audio(url,save_path)
    file = os.listdir('Downloads')
    l = []
    for i in file:
        if i.endswith('.webm'):
            l.append(i)
    return l

print(audio_to_text())