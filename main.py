from ai_core.llm.chatglm import ChatGLM_LLM
from ai_core.tts.edge import EdgeTTS
import asyncio
import os


if __name__ == "__main__": 
    llm = ChatGLM_LLM()
    response = llm.generate_response("你好")
    print(response)
    tts = EdgeTTS()
    output_file = asyncio.run(tts.text_to_speech(response, "output.mp3"))
    os.system(f"start {output_file}")
