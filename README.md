# Booking clone of starter-pack

This repository contains the foundations of your a custom assistant for booking and telling Chuck Norris jokes. This is a clone from the new rasa-stack starter-pack which also comes with a step-by-step video tutorial which you can find [here](https://youtu.be/lQZ_x0LRUbI).  

<p align="center">
  <img src="./rasa-stack-mockup.gif">
</p>


## Setup and installation

If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:  
```
pip install -r requirements.txt
```

You also need to install a spaCy English language model. You can install it by running:

```
python -m spacy download en
```


## What’s in this clone of the starter-pack?

This clone of the starter-pack contains some training data and the main files which you can use as the basis of your first custom assistant. It also has the usual file structure of the assistant built with Rasa Stack. It is different from the start-pack as far as action, stories and domain have been modified in order to be able to manage booking. Yet this clone of starter-pack still consists of the following files:

### Files for Rasa NLU model

- **data/nlu_data.md** file contains training examples of six intents: 
	- greet
	- goodbye
	- thanks
	- deny
	- joke
	- name (examples of this intent contain an entity called 'name')
	
- **nlu_config.yml** file contains the configuration of the Rasa NLU pipeline:  
```yaml
language: "en"

pipeline: spacy_sklearn
```	

### Files for Rasa Core model

- **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant. 
- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **actions.py** file contains the code of a custom action which retrieves a Chuck Norris joke by making an external API call as weel as storing booking in a SQL database.
- **endpoints.yml** file contains the webhook configuration for custom action.  
- **policies.yml** file contains the configuration of the training policies for Rasa Core model.

## How to use this starter-pack?
- NOTE: If running on Windows, you will either have to [install make](http://gnuwin32.sourceforge.net/packages/make.htm) or copy the following commands from the [Makefile](https://github.com/RasaHQ/starter-pack-rasa-stack/blob/master/Makefile)
1. You can train the Rasa NLU model by running:  
```make train-nlu```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. In a new terminal start the server for the custom action by running:  
```make action-server```  
This will start the server for emulating the custom action.

4. Test the assistant by running:  
```make cmdline```  
This will load the assistant in your terminal for you to chat.

## What's next?
Until now I'm not able to make the bot book another room and store it in the SQL database.