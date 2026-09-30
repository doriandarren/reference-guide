import schedule
import time
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from terminal import show_result


## Carga Env
load_dotenv()


history = [
    SystemMessage(
        content=(
            "Eres un asistente útil. "
            "Responde siempre en español de forma clara y breve."
        )
    )
]


# llama3:latest | gpt-oss:20b
llm = ChatOllama(
    model="llama3:latest",
    base_url="http://192.168.1.100:11434",
    #base_url="http://192.168.1.111:11434",
    temperature=0
)


question_lst = [
    "¿En qué año llegó el hombre a la luna?",
    "¿Quién fue el primero en pisarla?",
    "¿Cómo se llamaba la misión?"
]


i=0


def ask(q):
    
    history.append(
        HumanMessage(content=q)
    )
    
    answer = llm.invoke(history)
    
    history.append(answer)
    
    return answer.content
    
    
    
def send_next_question():
    global i
    
    if i < len(question_lst):
        q = question_lst[i]
        #print(f"Pregunta: {q}")
        answer = ask(q)
        #print(f"Respuesta: {answer}")
        
        show_result(q, answer)
        
        i += 1
    
    


if __name__ == "__main__":
    schedule.every(3).minutes.do(send_next_question)
            
        
    while True:
        schedule.run_pending()
        time.sleep(1)
