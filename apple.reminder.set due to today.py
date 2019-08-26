import reminders
import datetime
from collections import Counter

# get uncomplete reminders
todo = reminders.get_reminders(completed=False)

# get reminders w dates
todo = [item for item in todo if item.due_date]

# get reminders due before today
todo = [item for item in todo if item.due_date < datetime.datetime.now()]

# make due date today
for r in todo:
  r.due_date = datetime.datetime.now()
  r.alarms[0].date = r.due_date
  r.save()
