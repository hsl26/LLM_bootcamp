import streamlit as st
from openai import AzureOpenAI

# Azure OpenAI API 키 설정
str_api_key = "2374f2c1a634407387e2fb2fbba5e7fe"
str_api_version ="2024-02-01"
str_endpoint = "https://magicecoleai.openai.azure.com/"

str_api_key_img ="e5b5706650e4420ab9ccdd5a06fc9184"
str_endpoint_img = "https://magicecole.openai.azure.com/"

client = AzureOpenAI(
    api_key = str_api_key,  #Azure Open AI Key
    api_version = str_api_version,  #Azue OpenAI API model
    azure_endpoint = str_endpoint #Azure Open AI end point(매직에꼴)
)

# Streamlit 앱 생성
st.title('ChatGPT와 대화하기')
st.write('Azure OpenAI를 이용하여 ChatGPT로부터 답변을 받아보세요.')

# 사용자 입력 받기
user_input = st.text_input("질문을 입력하세요:")

messages = [{"role": "user", "content": user_input}] 

if user_input:
    # OpenAI API를 통해 답변 요청
    response = client.chat.completions.create(
                model="gpt-4o", # 모든 사용자 설정 가능
                # model="gpt-3.5-turbo-16k", # gpt-3.5-turbo 대비 4배 긴 토큰 처리
                # model="gpt-4", # GPT-4 모델 사용
                messages=messages, # 전달할 메시지 지정
                max_tokens=1000, # 응답 최대 토큰 수 지정
                temperature=0.8, # 완성의 다양성을 조절하는 온도 설정
                n=1 # 생성할 완성의 개수 지정
    )
    
    # 응답 출력
    answer = response.choices[0].message.content.strip()
    st.write("ChatGPT의 답변:")
    st.write(answer)
