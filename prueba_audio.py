import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    # Inicializamos el proceso de salida de texto a voz
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)
    engine.say(command)
    engine.runAndWait()

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

# En este ciclo esperaremos la entrada de audio a convertir
while (1):

    # Añadimos un try-except en caso de surgir errores
    try:
        # Usamos el microfono para recuperar voz
        with sr.Microphone() as source2:
            # Obtenemos el audio
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            # Ahora, usamos speech_recognition para convertir el audio a texto
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Intentaste decir: " + MyText)
            # Podemos convertir el texto a voz de nueva cuenta.
            SpeakText(MyText)

    except sr.RequestError as e:
        print("No existen resultados; {0}".format(e))

    except sr.UnknownValueError:
        print("Error desconocido")