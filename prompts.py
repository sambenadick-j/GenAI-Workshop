from langchain_core.prompts import ChatPromptTemplate

def mcq_generator_prompt():
    """
    Generates Prompt template from the system and user messages

    Returns:
        ChatPromptTemplate -> Configured ChatPromptTemplate instance
    """

    system_msg = '''
                You are an expert in multiple choice question generation, You're task is to generate question based on the given topic by the user with four choices and among these four choice it must contain the answer and also display the answer separately to the user at the end of the all the question make sure you are generate atleast ten questions for the respective given subject and the question need to be relavent to the subject,

                Guidelines:

                Don't provide answer directly below every questions.
                There must be newline between the options of every questions.
                '''

    user_msg = "Generate multiple choice questions for {subject} "

    prompt_template = ChatPromptTemplate([
        ("system", system_msg),
        ("user", user_msg)
    ])

    return prompt_template

    # task 1 add system message
    # task 2 add user message 
    # task 3 create and return prompt template