#!/usr/bin/env python3

import os
import random
from uiautomator import device as d





def swipe_up():
	ui_ball.swipe.up(steps=10)

def shoot_to(x, y):
	print("target", x, y)
	d.drag(get_ball_middle_x(), get_ball_middle_y(), x, y, steps=10)


def shoot_to_x(x):
	shoot_to(x, get_rim_middle_y())

def shoot_0_10():
	if ui_ball.exists:
		shoot_to_x(get_rim_middle_x())
		# ui_ball.drag.to(resourceId="com.facebook.orca:id/rim", steps=10)
		return BallStatus.SHOT_ALREADY
	else:
		return BallStatus.NO_SHOT


def loop_shooting():
	print("start loop shooting")
	while 0 <= get_score() < 50:
		shoot_when_ready()

		print("finish a shot")
	else:
		print("end shooting")



def start():
	#print(ui_score.exists)
	if ui_score.exists():
		print("uspjelo")
		loop_shooting()
	else:
		shoot_0_10()
		sleep(0.5)
		loop_shooting()
#test commit

def print_dumb():
	while True:
		print(get_rim_middle_x(), get_rim_middle_y())


def get_ui_object(string_id_name):
	print("com.facebook.orca:id/" + string_id_name) 
	return d(resourceId="com.facebook.orca:id/" + string_id_name)


def get_bound(view_object):
	return view_object.info.get("visibleBounds")


def get_middle(a, b):
	return int((a + b) / 2)


def get_ball_bound_side(string_side):
	return get_bound(ui_ball).get(string_side)


def get_rim_bound_side(string_side):
	return int(get_bound(ui_rim).get(string_side))


def get_ball_left():
	return get_ball_bound_side("left")


def get_ball_right():
	return get_ball_bound_side("right")


def get_ball_top():
	return get_ball_bound_side("top")


def get_ball_bottom():
	return get_ball_bound_side("bottom")


def get_ball_middle_x():
	return get_middle(get_ball_left(), get_ball_right())


def get_ball_middle_y():
	return get_middle(get_ball_top(), get_ball_bottom())


def get_rim_left():
	return get_rim_bound_side("left")


def get_rim_right():
	return get_rim_bound_side("right")


def get_rim_top():
	return get_rim_bound_side("top")


def get_rim_bottom():
	return get_rim_bound_side("bottom")


def get_rim_middle_x():
	return get_middle(get_rim_left(), get_rim_right())


def get_rim_middle_y():
	return get_middle(get_rim_top(), get_rim_bottom())



int_screen_width = 768

ui_ball = get_ui_object("ball")
ui_bottom = get_ui_object("bottom")
# ui_backboard_target = get_ui_object("backboard_target")
ui_rim = get_ui_object("rim")
ui_score = get_ui_object("score")
ui_best_score = get_ui_object("best_score")



#int_screen_width = int(get_bound(ui_bottom).get("right"))
print("tusam")
#int_screen_height = int(get_bound(ui_bottom).get("bottom"))
print("tusam")
int_middle_screen_horizontal = int_screen_width / 2
int_screen_height = 1184
#print(int_screen_width)



start()