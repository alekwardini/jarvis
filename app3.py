from openai import OpenAI 
import random
import time
import sys
from txt_to_audio import audio
from speech import *
from speech import transcribe_once 
#variables

api_key_var = ""
prompt = """Act as J.A.R.V.I.S. Address me as "Sir".
1. Tone: Dry British wit, hyper-competent, and understated.
2. Voice Optimization: Keep responses very short and conversational. Avoid long lists or formatting; summarize top points instead.
3. Behavior: Be proactive. Never break character. Never use standard AI disclaimers (e.g., "As an AI").
4. Goal: Execute tasks immediately with maximum efficiency.
"""

possible_phrases = ["loading, initializing program, successfully entered database ", "starting program, retreiving information", "trying to laod into database, succesfully entrered "]
client = OpenAI(api_key = api_key_var)

def robot():
    while True:
        answer = input("\nyou: ")
        if answer == "s":
            answer = transcribe_once()
        if answer in ["quit", "esc", "escape", "leave"]:
            break
        print("---initializing---", "\n---accessing_database_centers---")
        audio(random.choice(possible_phrases), 160)
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {"role": "system", "content" : prompt},
            {"role": "user", "content" : answer},
    
        ]
        )
        msg = response.choices[0].message.content
        time.sleep(0.5)
        print("---research complete---\n", "Jarvis: ", end=" ")
        audio(msg, 160)
        for i in msg:
            print(i, end = "", flush=True)
            time.sleep(0.03)
if __name__ == "__main__":
    robot()
