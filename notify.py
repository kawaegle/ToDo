from pynotifier import Notification

def notification_desc(description):
	Notification(
		title="To Do List",
		description=description,
		duration=5,                              # Duration in seconds
	).send()

def notification_total(title, description):
	Notification(
		title=title,
		description=description,
		duration=5,                              # Duration in seconds
	).send()
