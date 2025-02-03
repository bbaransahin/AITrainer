import get_personal_details
import set_goals
import generate_weekly_plan
import generate_workout
import database_tools

def printMenu():
    print('1-Update personal details')
    print('2-Set a new goal')
    print('3-Prepare a weekly plan')
    print('4-Get next workout')
    print('5-Give feedback to last workout')
    print('0-EXIT')

user_input = None
while (user_input != 0):
    printMenu()
    user_input = int(input('>>'))
    if (user_input == 1):
        messages = get_personal_details.getPersonalDetails()
        new_personal_data = get_personal_details.extractPersonalDetails(messages)
        database_tools.updatePersonalDetails(new_personal_data)
    elif (user_input == 2):
        messages = set_goals.bargainGoal()
        new_goal = set_goals.extractGoal(messages)
        database_tools.addGoal(new_goal)
    elif (user_input == 3):
        messages = generate_weekly_plan.discussWeeklyPlan()
        new_weekly_plan = generate_weekly_plan.extractWeeklyPlan(messages)
        database_tools.updateWeeklyPlan(new_weekly_plan)
    elif (user_input == 4):
        messages = generate_workout.suggestWorkout()
        new_workout = extract_workout(messages)
        database_tools.addWorkout(new_workout)
    elif (user_input == 5):
        last_workout = database_tools.getPreviousWorkouts()[-1]
        print(last_workout)
        feedback = input('Enter Feedback: ')
        database_tools.addFeedbackToWorkout(feedback, -1)
    else:
        print('INVALID INPUT')