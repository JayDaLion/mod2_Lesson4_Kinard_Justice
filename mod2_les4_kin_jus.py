"""#range riddle
import random
moods = ['Calm','Glad','Mad','Sad']
days = ['Monday','Tuesday','Wednesday','Thursday','Friday']

for i in range(len(days)):
    ran_mood = random.choice(moods)
    print(f"On {days[i]}, you were feeling {ran_mood}")
"""

"""#nested practice
import random
moods = ['Calm','Glad','Mad','Sad']
days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
time_of_day = ['morning', 'afternoon', 'evening']
for i in range(len(days)):
    for j in range(len(time_of_day)):
        ran_mood = random.choice(moods)
        print(f"On {days[i]} during the {time_of_day[j]}, you were feeling {ran_mood}")"""