from enum import nonmember
from abc import ABC,abstractmethod
from openai import OpenAI


class LLM:
    def __init__(self,config):
        self.client = OpenAI(api_key=config.get("api_key"),base_url= config.get("url"))
        self.config = config.get("model_name")


def main():
    print("Hello World")

if __name__ == "__main__":
    main()
