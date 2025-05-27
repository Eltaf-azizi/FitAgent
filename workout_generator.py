import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from logger import log_message


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    log_message("OpenAI API key missing!", "error")
    raise ValueError("OPENAI_API_KEY not found in .env")



try:
    llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=OPENAI_API_KEY)

except Exception as e:
    log_message(f"OpenAI Initialization Error: {str(e)}", "error")
    raise e



workout_prompt = PromptTemplate(
    input_variables = ["fitness_level", "goal", "duration", "equipment"],
    template = (
        "Create a personalized workout plan for a {fitness_level} individual "
        "whose goal is {goal}. The workout should last {duration} minutes "
        "and use {equipment} equipment. Provide step-by-step excercises."
    ),
)



def generate_workout(fitness_level, goal, duration, equipment):
    prompt = workout_prompt.format(
        fitness_level = fitness_level,
        goal = goal,
        duration = duration,
        equipment = equipment
    )

    try:
        response = llm.invoke(prompt)
        log_message("workout plan generated successfully")
        return response.content
    
    except Exception as e:
        log_message(f" workout generation failed: {str(e)}", "error")
        return f"error: {str(e)}"
    



if __name__ == '__main__':
    test_workout = generate_workout("Beginner", "Weight loss", "30", "Bodyweight")
    print(test_workout)