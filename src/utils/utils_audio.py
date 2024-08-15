def get_audio_model(conversion_type):
    match conversion_type:
        case "stt":
            print("Trascrizione audio (speech-to-text) non ancora supportata.")
            return None
        case "tts":
            print("Generazione audio (text-to-speech) non ancora supportata.")
            return None
        case _:
            print("Tipo di conversione non supportato.")
            return None
        
