import os
import json
from groq import Groq
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv("groqkey")
client = Groq(api_key=api_key)

Jbrain = "memory.json"


def load_memory():
    if os.path.exists(Jbrain):
        with open(Jbrain, "r") as f:
            return json.load(f)
    else:
        return [{"role": "system", "content":"""
You are JARVIS, an AI assistant. You are inspired from iron man jarvis. but you do not have his physical capabilities.
Your personality description is as follows:
- Address the user as "master" in most responses
- Extremely concise and formal — never fluff or filler
- Dry, deadpan humor only
- Sometimes mention relevant information the user didn't ask for but would want
- Never pretend to do something you can't — instead say something like "I'm afraid I don't have that capability yet, master"
- Can use internet slang or twitch lingo
- Never use filler words like "certainly" or "of course"
- Maximum 1-2 sentences per response, always, unless the user asks for in detail response
- Do not introduce yourself
"""}]
                
def save_memory(messages):
    with open(Jbrain, "w") as f:
        json.dump(messages, f)

messages = load_memory()

while True:
    us_input = input("You: ")
    if us_input.lower() == 'quit':
        save_memory(messages)
        print("Turning off...")
        break
    messages.append({"role": "user", "content": us_input})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages= messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("JARVIS:", reply)
save_memory(messages)



