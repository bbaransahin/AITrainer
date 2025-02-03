import prompts
import database_tools

def messages2string(messages):
    out = ''
    for m in messages:
        out += m['role']
        out += ': '
        out += m['content']
        out += '\n'
    return out

def discussWeeklyPlan():
    pd = database_tools.getPersonalDetails()
    g = database_tools.getGoals()

    extra_material = 'Personal Details:\n'+pd+'\n\nGoals:\n'+g

    client = OpenAI(api_key=api_key)

    messages=[
        {"role": "system", "content": prompts.generate_weekly_plan},
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

def extractWeeklyPlan(messages):
    client = OpenAI(api_key=api_key)

    dialogue = messages2string(messages)

    messages = [
        {'role': 'system', 'content': prompts.extract_weekly_plan},
        {'role': 'user', 'content': dialogue}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response.choices[0].message.content