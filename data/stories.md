## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet

## Generated Story 2282590227326597901
* greet
    - utter_greet
* book_room{"name_room": "blue", "day": "2018 - 09 - 20", "hour_start": "10:00", "duration": "1"}
    - slot{"day": "2018 - 09 - 20"}
    - slot{"duration": "1"}
    - slot{"hour_start": "10:00"}
    - slot{"name_room": "blue"}
    - action_room
* goodbye
    - utter_goodbye
    - export

## Generated Story 3779637259476718718
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "green"}
    - slot{"name_room": "green"}
    - utter_ask_day
* book_room{"day": "3rd december"}
    - slot{"day": "3rd december"}
    - utter_ask_hour_start
* book_room{"hour_start": "16h"}
    - slot{"hour_start": "16h"}
    - utter_ask_duration
* book_room{"duration": "30 min"}
    - slot{"duration": "30 min"}
    - action_room
    - export

## Generated Story -4257668575535966047
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "green"}
    - slot{"name_room": "green"}
    - utter_ask_day
* book_room{"day": "3rd december"}
    - slot{"day": "3rd december"}
    - utter_ask_hour_start
* book_room{"hour_start": "10h"}
    - slot{"hour_start": "10h"}
    - utter_ask_duration
* book_room{"duration": "30 min"}
    - slot{"duration": "30 min"}
    - action_room
* goodbye
    - utter_goodbye
    - export

## Generated Story 3675490599265025711
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "green"}
    - slot{"name_room": "green"}
    - utter_ask_day
* book_room{"day": "tomorrow"}
    - slot{"day": "tomorrow"}
    - utter_ask_hour_start
* book_room{"hour_start": "10h"}
    - slot{"hour_start": "10h"}
    - utter_ask_duration
* book_room{"duration": "1 h"}
    - slot{"duration": "1 h"}
    - action_room
* goodbye
    - utter_goodbye
    - export


## Generated Story -2068499667002963570
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "tomorrow"}
    - slot{"day": "tomorrow"}
    - utter_ask_hour_start
* book_room{"hour_start": "10h"}
    - slot{"hour_start": "10h"}
    - utter_ask_duration
* book_room{"duration": "45 min"}
    - slot{"duration": "45 min"}
    - action_room
* goodbye
    - utter_goodbye
    - export

## Generated Story 3640234118169274367
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "green"}
    - slot{"name_room": "green"}
    - utter_ask_day
* book_room{"day": "3rd september"}
    - slot{"day": "3rd september"}
    - utter_ask_hour_start
* book_room{"hour_start": "11h"}
    - slot{"hour_start": "11h"}
    - utter_ask_duration
* book_room{"duration": "15 min"}
    - slot{"duration": "15 min"}
    - action_room
* goodbye
    - utter_goodbye
    - export

## Generated Story -1156170051981377013
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "tomorrow"}
    - slot{"day": "tomorrow"}
    - utter_ask_hour_start
* book_room{"hour_start": "13h"}
    - slot{"hour_start": "13h"}
    - utter_ask_duration
* book_room{"duration": "1 h"}
    - slot{"duration": "1 h"}
    - action_room
* goodbye
    - utter_goodbye
    - export
	
## Generated Story 7889435598882720442
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "tomorrow"}
    - slot{"day": "tomorrow"}
    - utter_ask_hour_start
* book_room{"hour_start": "10h"}
    - slot{"hour_start": "10h"}
    - utter_ask_duration
* book_room{"duration": "30 min"}
    - slot{"duration": "30 min"}
    - action_room
* goodbye
    - utter_goodbye
    - export


 

## story_joke_01
* joke
 - action_joke
 
## story_joke_02
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 

## Generated Story 8070679053955036713
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room
    - utter_ask_day
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "tomorrow"}
    - slot{"day": "tomorrow"}
    - utter_ask_hour_start
* book_room{"hour_start": "1pm"}
    - slot{"hour_start": "1pm"}
    - utter_ask_duration
* book_room{"duration": "30 min"}
    - slot{"duration": "30 min"}
    - action_room
* goodbye
    - utter_goodbye
    - export

## Generated Story -5977270671181011094
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "tomorrow"}
    - slot{"day": "tomorrow"}
    - utter_ask_hour_start
* book_room{"hour_start": "1pm"}
    - slot{"hour_start": "1pm"}
    - utter_ask_duration
* book_room{"duration": "30 min"}
    - slot{"duration": "30 min"}
    - action_room
* goodbye
    - utter_goodbye
    - export
## Generated Story -5991671691308871044
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "tomorrow"}
    - slot{"day": "tomorrow"}
    - utter_ask_hour_start
* book_room{"hour_start": "1pm"}
    - slot{"hour_start": "1pm"}
    - utter_ask_duration
* book_room{"duration": "30 minutes"}
    - slot{"duration": "30 minutes"}
    - action_room
* goodbye
    - utter_goodbye

## Generated Story -2720950560744020465
* greet
    - utter_name
* name
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "tomorrow"}
    - slot{"day": "tomorrow"}
    - utter_ask_hour_start
* book_room{"hour_start": "14h"}
    - slot{"hour_start": "14h"}
    - utter_ask_duration
* book_room{"duration": "30 minutes"}
    - slot{"duration": "30 minutes"}
    - action_room

## Generated Story 413668697040995566
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "4-12-2019"}
    - slot{"day": "4-12-2019"}
    - utter_ask_hour_start
* book_room{"hour_start": "1pm"}
    - slot{"hour_start": "1pm"}
    - utter_ask_duration
* book_room{"duration": "30 minutes"}
    - slot{"duration": "30 minutes"}
    - action_room

## Generated Story -6594185736277895606
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "red"}
    - slot{"name_room": "red"}
    - utter_ask_day
* book_room{"day": "4-17-2019"}
    - slot{"day": "4-17-2019"}
    - utter_ask_hour_start
* book_room{"hour_start": "1pm"}
    - slot{"hour_start": "1pm"}
    - utter_ask_duration
* book_room{"duration": "30 minutes"}
    - slot{"duration": "30 minutes"}
    - action_room
* goodbye
    - utter_goodbye

## Generated Story -4247033572764885338
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "4-17-2019"}
    - slot{"day": "4-17-2019"}
    - utter_ask_hour_start
* book_room{"hour_start": "1pm"}
    - slot{"hour_start": "1pm"}
    - utter_ask_duration
* book_room{"duration": "30 minutes"}
    - slot{"duration": "30 minutes"}
    - action_room

## Generated Story -5799271407599581035
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "4-17-2019"}
    - slot{"day": "4-17-2019"}
    - utter_ask_hour_start
* book_room{"hour_start": "2pm"}
    - slot{"hour_start": "2pm"}
    - utter_ask_duration
* book_room{"duration": "30 minutes"}
    - slot{"duration": "30 minutes"}
    - action_room

## Generated Story -3820423260628444889
* greet
    - utter_greet
* book_room
    - utter_ask_room
* book_room{"name_room": "blue"}
    - slot{"name_room": "blue"}
    - utter_ask_day
* book_room{"day": "4-17-2019"}
    - slot{"day": "4-17-2019"}
    - utter_ask_hour_start
* book_room{"hour_start": "3pm"}
    - slot{"hour_start": "3pm"}
    - utter_ask_duration
* book_room{"duration": "30 minutes"}
    - slot{"duration": "30 minutes"}
    - action_room

