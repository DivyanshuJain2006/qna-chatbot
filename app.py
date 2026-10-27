# from dotenv import load_dotenv
# load_dotenv()
# import streamlit as st

# from langchain_groq import ChatGroq

# llm = ChatGroq(model="openai/gpt-oss-20b")

# history=[]
# #ui- 
# st.subheader("🤖Qna Bot")
# query = st.chat_input("Ask Anything...")

# if query:
#     print("User ",query)
#     history.append({"role":"user","content":query})
#     res = llm.invoke(history)
#     print("AI: ",res.content)
#     history.append({"role":"ai","content":res.content})
# this above code works on backend
'''from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
llm = ChatGroq(
    model="openai/gpt-oss-20b"
)
history = []
while 1:
    query = input("User: ")
    if(query=="exit"):
        break
    history.append({"role":"user","content":query})
    res = llm.invoke(history)
    print("AI: ",res.content)
    history.append({"role":"assistant","content":res.content})

'''
   



from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st


llm = ChatGroq(model="openai/gpt-oss-20b")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
# ui
st.subheader("🤖 Qna Bot")


if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
    
for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))
    


query = st.chat_input("Ask anything ....")
if query:
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)
    
    res = llm.invoke(st.session_state.messages)
    st.session_state.messages.append({"role":"assistant", "content":res.content})
    st.chat_message("assistant").markdown(res.content)
    
    
print(st.session_state.messages)
   


   

