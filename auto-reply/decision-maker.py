from langchain_google_vertexai import VertexAI
from utils import *


def decideAutoReply(message, model):
    prompt = f""" Given the following message, determine whether it is worth replying to based on its content. Consider factors such as relevance, clarity, tone, and potential for further conversation. 
    Provide a binary response (yes/no) indicating whether the message warrants a reply. 

    Here is the message:
    {message}
"""
    res = model.invoke(prompt)

    return res


def decideAutoEmoji(message, model):
    prompt = f""" Given the following message, determine whether it is worth reacting to with an emoji based on its content. Consider factors such as relevance, clarity, tone, and potential for further conversation. 
    Provide a binary response (yes/no) indicating whether the message warrants a reply. 

    Here is the message:
    {message}
"""
    res = model.invoke(prompt)

    return res


def decideMessageFormality(message, model):
    prompt = f""" Given the following message, determine whether a reply to this message should be formal or informal based on its content. Consider factors such as language, tone, and context. 
    Provide a binary response (yes/no) indicating whether the message should be answered in a formal manner. 

    Here is the message:
    {message}
"""
    res = model.invoke(prompt)

    return res


def main():
    model = VertexAI(model_name="gemini-pro")
    messages = [
        "What are some of the pros and cons of Python as a programming language?",
        "I am not",
        "Still back in the game, like Jack LaLanne",
        "What is the capital of France?",
        "dsaf+oas jfd+soa jfsa+",  # gibberish
    ]

    for message in messages:
        print("\nMessage:")
        print(message)
        print("Auto-Emoji:")
        print(decideAutoEmoji(message, model))
        print("Auto-Reply:")
        print(decideAutoReply(message, model))
        print("--------------------------\n")


if __name__ == "__main__":
    main()
