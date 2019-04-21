# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
import mysql

import dateutil.parser as dparser

from rasa_core_sdk import Action
from booking import make_a_booking
from mysql import connector



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

        print("before booking_answer")        
        booking_answer = make_a_booking(name_room, day, hour_start, duration)
        print("booking_answer : " + str(booking_answer))
        if booking_answer:
            booking_answer = 'The reservation has been made'
        else:
            booking_answer = 'The room is taken at this hour'
        
        response = """You want to book the {} room on {} at {} for {}. Is it correct ?""".format(name_room, day, hour_start, duration)
        
        name_room = str(name_room)
        day = str(day)
        hour_start = str(hour_start)
        duration = str(duration)
        print("before connexion")
        #SQL queries#
        try:
            cnx = mysql.connector.connect(password='MySQL.2019', user="root", database="alex")
            print("before execute")
            cursor = cnx.cursor()

            # add new booking
            add_booking = ("INSERT INTO reservations "
                          "(name_room, hour_start, hour_end) "
                          "VALUES (%s, %s, %s)")
            print("before execute")
            cursor.execute(add_booking)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
        print("after connexion")

        dispatch = dispatcher.utter_message(response)
        dispatch = dispatcher.utter_message(str(booking_answer))
        
        return dispatch
