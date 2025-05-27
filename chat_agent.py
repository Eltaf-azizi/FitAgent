import os
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
from logger import log_message



load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    log_message("OpenAI API key missing!", "error")
    raise ValueError("OPENAI_API_KEY not found in .env")


llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=OPENAI_API_KEY)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm = llm, memory = memory)



def chat_with_ai(user_input):
    try:
        response = conversation.run(user_input)
        log_message(f"AI Response: {response}")
        return response
    
    except Exception as e:
        log_message(f"chat agent error: str{e}", "error")
        return "An Error occured while chatting with the AI"
    


if __name__ == '__main__':
    while True:
        user_input = input("\n You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = chat_with_ai(user_input)
        print("\nAI Coach: ", response)