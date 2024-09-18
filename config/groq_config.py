import os
from groq import Groq
import pandas as pd

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
def groq_call(message):
    user_data = pd.read_csv('./data/finance_data.csv')
    user_data = user_data.to_string(index=False)
    print(user_data)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"You are a finance assistant. You only clear up doubts on financial issues based on your user-provided database:\n{user_data}"
            },
            {
                "role": "user",
                "content": f"{message}"
            }
        ],
        model="llama3-70b-8192",
    )
    
    response = chat_completion.choices[0].message.content
    
    return response

