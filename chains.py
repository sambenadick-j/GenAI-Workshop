import models
import prompts

model=models.create_llm_model()
prompt_template=prompts.mcq_generator_prompt()

chain = prompt_template | model

def generate_mcq_chain(subject):
    """
    Generate mcq using basic prompt LLM chain

    Args:
        subject - subject for the mcq

    Returns:
        response.content -> str
    """
    response = chain.invoke({
        "subject" : subject
    })

    return response.content
    # task 1 import llm
    # task 2 import prompt
    # task 3 create chain
    # task 4 invoke chain with topic
    # task 5 return response content
    