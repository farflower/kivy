#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 09:54:27 2022

@author: fariborz
"""

import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Label

# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class HelloKivy(App):

	# This returns the content we want in the window
	def build(self):

		# Return a label widget with Hello Kivy
		return Label(text ="Hello Geeks")

helloKivy = HelloKivy()
helloKivy.run()
