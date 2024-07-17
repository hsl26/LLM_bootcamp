from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from dotenv import load_dotenv
import os

load_dotenv()

model = AzureChatOpenAI(
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT"), 
    temperature=1.0
)

# 초기 messages 설정
messages = [
    SystemMessage(content="You are a helpful assistant. Answer all questions to the best of your ability.")
]

print("챗봇이 시작되었습니다. 대화를 종료하려면 'quit'를 입력하세요.\n")

while True:
    user_input = input("YOU: ") # 사용자 입력 받기
    if user_input.lower() == 'quit': # 'quit' 입력 시 종료
        break
    messages.append(HumanMessage(content=user_input)) # messages에 HumanMessage 추가 
    
    model_output = model.invoke(messages) # 모델 응답 받기

    messages.append(AIMessage(content=model_output.content)) # messages에 AIMessage 추가
    
    print(model_output.content) # 모델 응답 출력
    print("\n")