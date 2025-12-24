from enum import nonmember
from abc import ABC,abstractmethod
from openai import OpenAI


class LLM:
    def __init__(self,config):
        self.client = OpenAI(api_key=config.get("api_key"),base_url= config.get("url"))
        self.module_name = config.get("model_name")

class Coniguration:
    def __init__(self,api_key:str,url:str,model_name:str):
        self.api_key = api_key
        self.url = url
        self.model_name = model_name


def main():
    print("Hello World")

if __name__ == "__main__":
    main()
