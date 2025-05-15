import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama import ChatOllama

from src.config.logger import logger
from src.config.settings import settings

st.set_page_config(
    'Assistente de IA',
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed',
)


st.title('Assistente de IA')

human_message = st.chat_input('Digite sua mensagem aqui...')

model = ChatOllama(
    model=settings.OLLAMA_AI_MODEL,
    temperature=settings.OLLAMA_AI_TEMPERATURE,
)
logger.info(f'Modelo de linguagem criado: {model}')

if 'chats' not in st.session_state:
    st.session_state.chats = []

if human_message:
    logger.info(f'Mensagem do usuário: {human_message}')

    st.session_state.chats.append({'role': 'user', 'content': human_message})
    logger.info(
        f'Mensagem do usuário adicionada ao histórico: '
        f'{st.session_state.chats}'
    )

    prompt = ChatPromptTemplate.from_messages([
        ('system', 'Você é um assistente de IA muito inteligente e útil.'),
        ('human', '{input}'),
    ])
    logger.debug(f'Prompt criado: {prompt}')

    chain = prompt | model | StrOutputParser()
    logger.debug(f'Cadeia de processamento criada: {chain}')

    response = chain.invoke({'input': human_message})
    logger.info(f'Resposta do modelo: {response}')

    st.session_state.chats.append({'role': 'assistant', 'content': response})
    logger.info(
        f'Resposta do modelo adicionada ao histórico: {st.session_state.chats}'
    )

for chat in st.session_state.chats:
    st.chat_message(chat['role']).markdown(chat['content'])
    logger.info(
        f'Mensagem do {chat["role"]} '
        f'adicionada ao histórico: {chat["content"]}'
    )
