import sys
import torch
import playsound

# ['aidar', 'baya', 'kseniya', 'xenia', 'eugene']

speaker = "kseniya"
device = torch.device("cpu")
torch.set_num_threads(4)
sample_rate = 48000
speed = 90
model_path = "model.pt"

model_download = torch.package.PackageImporter(model_path).load_pickle("tts_models", "model")
model_download.to(device)
print("[~] Модель загружена")

def synthesize(text: str, path: str = "audio.wav", speed: int = 100) -> None:
    print("[~] Образование голоса")
    model_download.save_wav(ssml_text=f"<speak><prosody rate='{speed}%'>{text}</prosody></speak>",
        speaker=speaker,
        sample_rate=sample_rate,
        audio_path=path)
    playsound.playsound(path)
    print("[+] Готово")

def script():
    try:
        voice_text = input("Текст речи: ")
        file_name = input("name: ")

        if voice_text != "" and file_name != "":
            synthesize(text=voice_text, path=file_name, speed=speed)

        return script()
    except:
        sys.exit()

if __name__ == "__main__":
    script()