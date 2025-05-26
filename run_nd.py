import os
import cryptocode
import streamlit as st

from dotenv import load_dotenv
load_dotenv()


if not os.environ.get("DECRYPT_CODE"):
  os.environ["DECRYPT_CODE"] = st.secrets["DECRYPT_CODE"]
  password = st.secrets["DECRYPT_CODE"]
else:
    password = os.environ["DECRYPT_CODE"]

with open('nd_crypted.py', 'r', encoding='utf-8') as f:
    encoded = f.read()

decoded = cryptocode.decrypt(encoded, password)
eval(compile(decoded,'<string>','exec'))
