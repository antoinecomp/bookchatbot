# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class ActionBookRoom(Action):
    def name(self):
        return 'action_room'

    def run(self, dispatcher, tracker, domain):
        print("inside run")
        name_room = tracker.get_slot('name_room')
        day = tracker.get_slot('day')
        hour_start = tracker.get_slot('hour_start')
        duration = tracker.get_slot('duration')
        
        booking_answer = make_a_booking(name_room, day, hour_start, duration)
        
        if booking_answer:
            booking_answer = 'The reservation has been made'
        else:
            booking_answer = 'The room is taken at this hour'
        
        response = """You want to book the {} room on {} at {} for {}. Is it correct ?""".format(name_room, day, hour_start, duration)
        
        name_room = str(name_room)
        day = str(day)
        hour_start = str(hour_start)
        duration = str(duration)
        
        #SQL queries#
        cnx = mysql.connector.connect(host='35.189.228.223', password='SQL.2019', user="root", database="alex")
             

        dispatch = dispatcher.utter_message(response)
        dispatch = dispatcher.utter_message(str(booking_answer))
        
        return dispatch
