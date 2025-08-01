import pandas as pd
import numpy as np
import requests
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import json
import re
import random
from .models import *

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_position(query):
    map = np.array([
        ["start", "trawa", "drzewo", "budynek"],
        ["trawa", "młyn", "trawa", "trawa"],
        ["trawa", "trawa", "skały", "dwa drzewa"],
        ["skały", "skały", "auto", "jaskinia"]
    ])
    response = client.responses.parse(
        model="gpt-4.1",  # lub np. "gpt-4o", zależnie od dostępności
        input=[
            {"role": "system", "content": f"Twoim zadaniem jest określić gdzie aktualnie znajduje się użytkownik, masz zwrócić wyłącznie aktualną pozycję na podstawie mapy. Użytkownik zawsze zaczyna z pola START, czyli lewy gorny rog (pozycja 0,0). Gdy uzytkownik powie polecialem 2 razy w prawo, to przesuwa sie o 2 pola, czyli (2,0), to jest drzewo. Zawsze zwracaj pozycje z mapy, a nie współrzędne.\n Mapa: {str(map)}"},
            {"role": "user", "content": query}
             ],
        text_format=S04E04_AI_DEVS_OUTPUT
    )
    return response

def get_answer_with_position(user_input):
    response = get_position(user_input.instructions)
    print(response.output_parsed)
    return response.output_parsed
