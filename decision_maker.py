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


def decideAutoEmojiReaction(message, model):
    prompt = f""" Given the following message, determine whether it is worth reacting to with an emoji based on its content. Consider factors such as relevance, clarity, tone, and potential for further conversation. 
    Provide a binary response (yes/no) indicating whether the message warrants a reply. 

    Here is the message:
    {message}
"""
    res = model.invoke(prompt)

    return res


def decideMessageFormality(message, model):
    prompt = f""" Given the following message, determine whether a reply to this message should be formal or informal based on its content. Consider factors such as language, tone, and context. 
    Provide a binary response (formal/informal) indicating whether the message should be answered in a formal manner. 

    Here is the message:
    {message}
"""
    res = model.invoke(prompt)

    return res


def generateReply(message, formality, model):
    prompt = f""" Given the following message, generate a reply in a {formality} and is appropriate for the context and content of the message. 

    Here is the message:
    {message}
    """
    res = model.invoke(prompt)

    return res

    # After mapping the emoji to business actions, type "done" to proceed and show the mapping you have done for all default face emojis."""


def decideEmoji(message, model):
    # Map emoji to business actions
    # prompt = f"""Please define how emojis are typically used in a work environment for software engineering in Slack. Provide descriptions and their corresponding Slack emoji codes.
    # For example, you can enter "read message" for :t+1:, "Approved Branch" or "Approved plan"for :white_check_mark:, if the message is about a bug, react with a bug emoji, etc.
    emojis = [":+1:", ":-1:", ":smile:", ":bug:", ":white_check_mark:"]
    str_emojis = ", ".join(emojis)
    prompt = f"""Select an emoji from this list {str_emojis} to reply to the following message:
    Provide only a single emoji code as a response.

    {message}

    """
    res = model.invoke(prompt)
    return res


def autoReply(message, formality, model):
    # Generate the most basic autoreply reply
    prompt = f""" Given the following message, generate a reply in a {formality} and is appropriate for the context and content of the message.
    Consider factors such as language, tone, and context.
    Only provide the reply text, do not include any additional information or context.
    
    Here is the message:
    {message}
    """
    res = model.invoke(prompt)
    return res


def decisionFlowDebug(message, model):

    print("\nMessage:")
    print(message)
    # Decide whether to use an emoji
    print("\nAuto-Emoji-Reaction:")
    aux = decideAutoEmojiReaction(message, model)
    print(aux)
    emoji = BinaryResponseToBool(aux)
    if emoji:
        print("React with this emoji")
        print(decideEmoji(message, model))
        print("--------------------------\n")

    aux = decideAutoReply(message, model)
    print(aux)
    reply = BinaryResponseToBool(aux)
    # Decide whether to reply
    if reply:
        # Decide whether to use a formal tone
        aux = decideMessageFormality(message, model)
        print("\nMessage-Formality:")
        print(aux)
        print("\nAuto-Reply:")
        print(generateReply(message, aux, model))
        print("--------------------------\n")


def autoReply(message, model):

    aux = decideAutoReply(message, model)
    print(aux)
    reply = BinaryResponseToBool(aux)
    # Decide whether to reply
    if reply:
        # Decide whether to use a formal tone
        formality = decideMessageFormality(message, model)
        return generateReply(message, formality, model)


def main():
    model = VertexAI(model_name="gemini-1.0-pro-vision-001")
    messages = [
        "What are some of the pros and cons of Python as a programming language?",
        "I am not",
        "Still back in the game, like Jack LaLanne",
        "What is the capital of France?",
        "dsaf+oas jfd+soa jfsa+",  # gibberish
        "Could you please review my pull request?",
    ]

    for message in messages:
        decisionFlowDebug(message, model)


if __name__ == "__main__":
    main()
