import prompts
import database_tools.py

def messages2string(messages):
    out = ''
    for m in messages:
        out += m['role']
        out += ': '
        out += m['content']
        out += '\n'
    return out

def suggestWorkout():
    pd = database_tools.getPersonalDetails()
    g = database_tools.getGoals()
    d = database_tools.getDate()+' '+database_tools.getWeekDay()
    pw = database_tools.getPreviousWorkouts(7)

    extra_material = 'Personal Details:\n'+pd+'\n\nGoals:\n'+g+'\n\Previous Workouts:\n'+pw+'\n\nDate:'+d

    client = OpenAI(api_key=api_key)

    messages=[
        {"role": "system", "content": prompts.generate_workout},
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

def extractWorkout(messages):
    client = OpenAI(api_key=api_key)

    dialogue = messages2string(messages)

    messages = [
        {'role': 'system', 'content': prompts.extract_workout},
        {'role': 'user', 'content': dialogue}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response.choices[0].message.content