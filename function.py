import streamlit as st
import requests
from bmiv2 import *


def ai(bmi_overall, username):
    import requests

    url = "https://adult-gpt.p.rapidapi.com/adultgpt"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"Provide a medical advise for {username} with a bmi value of {bmi_overall}, address the name given"
            }
        ],
        "genere": "ai-gay-1",
        "bot_name": "",
        "temperature": 0.9,
        "top_k": 10,
        "top_p": 0.9,
        "max_tokens": 200
    }
    headers = {
        "x-rapidapi-key": "d1efda5bfcmshacb3daae72997eep11f3e5jsnbdaf2b87d985",
        "x-rapidapi-host": "adult-gpt.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    res = dict(response.json())
    for k, v in res.items():
        st.info(f"{k.upper()} : {v}")