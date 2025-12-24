from ai_core.llm.chatglm import ChatGLM_LLM


if __name__ == "__main__": 
    llm = ChatGLM_LLM()
    response = llm.generate_response("你好")
    print(response)