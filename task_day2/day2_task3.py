from langchain_openai import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

model = AzureChatOpenAI(
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT"), 
    temperature=1.0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer all questions to the best of your ability."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | model | output_parser

# 메모리 초기화
memory = ConversationBufferMemory(
            chat_memory=InMemoryChatMessageHistory(),
            return_messages=True #대화 기록이 메시지 객체(HumanMessage, AIMessage등)의 리스트로 반환
        )

print("챗봇이 시작되었습니다. 대화를 종료하려면 'quit'를 입력하세요.\n")

while True:
    user_input = input("YOU: ") # 사용자 입력 받기
    if user_input.lower() == 'quit': # 'quit' 입력 시 대화 기록 출력 및 종료
        print("\n대화 기록:")
        print(memory.chat_memory)
        break
    
    chat_history = memory.chat_memory.messages

    # 체인 실행
    output = chain.invoke({
        "input": user_input,
        "chat_history": chat_history        
    })

    print(f"AI: {output}\n") # AI 응답 출력

    # 메모리에 사용자 입력과 AI 응답 추가
    memory.chat_memory.add_user_message(user_input)
    memory.chat_memory.add_ai_message(output)
