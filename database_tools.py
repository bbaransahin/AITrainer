import json
from datetime import datetime

def getDate():
    return str(datetime.today().date())

def getWeekDay():
    return datetime.today().date().strftime("%A")

def getPersonalDetails():
    try:
        pd_file = open('personal_details.json', 'r')
        pd = pd_file.read()
        pd_file.close()
    except:
        pd = 'Not provided'

    return pd

def updatePersonalDetails(personal_details_data):
    with open('personal_details.json', 'w+') as fo:
        json.dump(personal_details_data, fo)

def getWeeklyPlan():
    try:
        wp_file = open('weekly_plan.json', 'r')
        wp = wp_file.read()
        wp_file.close()
    except:
        wp = 'Not provided'
    
    return wp

def updateWeeklyPlan(weekly_plan_data):
    with open('weekly_plan.json', 'w+') as fo:
        json.dump(weekly_plan_data, fo)

def getGoals():
    try:
        g_file = open('goals.json', 'r')
        g = g_file.read()
        g_file.close()
    except:
        g = 'Not provided'
    
    return g 

def addGoal(goal_string):
    try:
        with open('goals.json', 'r') as fi:
            data = json.load(fi)
    except:
        data = []

    data.append(goal_string)
    
    with open('goals.json', 'w+') as fo:
        json.dump(data, fo)

def getPreviousWorkouts(n):
    try:
        with open('previous_workouts.json', 'r') as fi:
            data = json.load(fi)
            if (len(data) > n):
                return data[-n:]
            return data
    except:
        return 'Not provided'

def addWorkout(workout_data):
    try:
        with open('previous_workouts.json', 'r') as fi:
            data = json.load(fi)
    except:
        data = []

    data.append(workout_data)

    with open('previous_workouts.json', 'w+') as fo:
        json.dump(data, fo)

def addFeedbackToWorkout(feedback, idx)
    try:
        with open('previous_workouts.json', 'r') as fi:
            data = json.load(fi)
    except:
        print('ERROR: COULDN\'T READ THE PREVIOUS WORKOUTS DATABASE')

    data[idx]['user_feedback'] = feedback
    
    with open('previous_workouts.json', 'w+') as fo:
        json.dump(data, fo)