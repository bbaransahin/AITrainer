import prompts
import database_tools

from openai import OpenAI # type: ignore

with open('openai.key', 'r') as key_file:
    api_key = key_file.read()

def messages2string(messages):
    out = ''
    for m in messages:
        out += m['role']
        out += ': '
        out += m['content']
        out += '\n'
    return out

def bargainGoal():
    pd = database_tools.getPersonalDetails()
    wp = database_tools.getWeeklyPlan()
    g = database_tools.getGoals()

    extra_material = 'Personal Details:\n'+pd+'\n\nWeekly Plan:\n'+wp+'\n\nGoals:\n'+g

    client = OpenAI(api_key=api_key)

    messages=[
        {"role": "system", "content": prompts.goal_setting},
        {'role': 'system', 'content': extra_material}
    ]

    while (True):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                stream=True,
            )
            
            out = ''
            print('Assistant: ', end='')
            for chunk in response:
                if hasattr(chunk, "choices") and chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    out += content
            print()

            if ('DONE' in out):
                break

            messages.append({
                'role': 'assistant',
                'content': out,
            })

            user_input = input('User: ')
            messages.append({
                'role': 'user',
                'content': user_input,
            })

        except Exception as e:
            print(f"An error occurred: {str(e)}")
    return messages

def extractGoal(messages):
    client = OpenAI(api_key=api_key)

    dialogue = messages2string(messages)

    messages = [
        {'role': 'system', 'content': prompts.extract_goal},
        {'role': 'user', 'content': dialogue}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response.choices[0].message.content