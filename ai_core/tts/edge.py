import edge_tts

class EdgeTTS:
    def __init__(self):
        self.voice = "zh-CN-XiaoxiaoNeural"

    async def text_to_speech(self, text,audio_file_path):
         communicate = edge_tts.Communicate(text, self.voice)
         await communicate.save(audio_file_path)
         return audio_file_path
  
        




