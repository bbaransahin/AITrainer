def getPersonalDetails():
    try:
        pd_file = open('personal_details.json', 'r')
        pd = pd_file.read()
        pd_file.close()
    except:
        pd = 'Not provided'

    return pd

def getWeeklyPlan():
    try:
        wp_file = open('weekly_plan.json', 'r')
        wp = wp_file.read()
        wp_file.close()
    except:
        wp = 'Not provided'
    
    return wp

def getGoals():
    try:
        g_file = open('goals.json', 'r')
        g = g_file.read()
        g_file.close()
    except:
        g = 'Not provided'
    
    return g 