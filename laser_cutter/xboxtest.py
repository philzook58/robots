from legopi.lib import xbox_read

for event in xbox_read.event_stream(deadzone=DEADZONE):
	#print "Xbox event: %s" % (event)

	# Special-case the LB button, if it's been pressed, then toggle the light
	if(event.key=='LB'):
		if(event.value>0):
			arm.toggleLight()
		continue

	# Special-case the RB button, if it's being held, then we want the light
	if(event.key=='RB'):
		if(event.value>0):
			direction=1
		else:
			direction=0
		arm.setLight(direction)
		continue

	# Special case directions for RT and LT, as we want the grip to move depending on which is used
	if(event.key=='RT'):
		direction=1
	elif(event.key=='LT'):
		direction=2
	else:
		# For all other cases, base direction on the value (negative = up, positive = down)
		if(event.value<0):
			direction = 2
		elif(event.value>0):
			direction = 1

	# If our axis has returned to zero, then stop moving
	if(event.value==0):
		direction = 0
