from openai import OpenAI


class LLM:
    def __init__(self,config):
        self.module_name = config.get("model_name")
        self.api_key = config.get("api_key")
        self.url = config.get("url")
        self.client = OpenAI(api_key=self.api_key,base_url= self.url)
    def generate_response(self,dialogue):
        response = self.client.chat.completions.create(
            model=self.module_name,
            messages= dialogue,
            temperature=0.9,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
        )
        return response.choices[0].message.content
def run():
    config = {
        "model_name" : "GLM-4.5-Flash", 
        "api_key" : "fd56bcc454654c6c89414650d02b9cec.obSpoZ1P2S4cG9Wo",
        "url" : "https://open.bigmodel.cn/api/paas/v4" 
    }
    llm = LLM(config)
    user_dialogue = [
        {"role": "system", "content": "你是一名中文翻译"},
        {"role": "user", "content": "你好"},
    ]
    print(llm.generate_response(user_dialogue))


if __name__ == "__main__": 
    run()