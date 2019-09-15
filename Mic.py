import speech_recognition as sr

def mic():
    # obtain audio from the microphone
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        #recognize speech using Google Speech Recognition

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)

            print("Вы сказали:" + r.recognize_google(audio, language="ru-RU"))
        except sr.UnknownValueError:

            print("Google Speech Recognition не смог разобрать аудиозапись")
        except sr.RequestError as e:

            print("Could not request results from Google Speech Recognition service; {0}".format(e))



if __name__ == '__main__':
    mic()



