import os
import urllib3
import json

def lambda_handler(event, context):
     return dispatch(event)
    
def get_slots(intent_request):
    return intent_request['currentIntent']['slots']
    
def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }
    
def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    return response
    
def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }
    
def dispatch(intent_request):
    intent_name = intent_request['currentIntent']['name']
    if intent_name == 'Weather':
        return get_weather(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')
    
    
def get_weather(intent_request):
    location = get_slots(intent_request)["Location"]
    source = intent_request['invocationSource']
    weather = get_weather1(location)
    
    if source == 'DialogCodeHook':
        session_attributes=intent_request['sessionAttributes']
        return delegate(session_attributes, get_slots(intent_request))   
          
    print(location)
    print(source)
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'The weather today in {} is {}'.format(location,weather)})
    
def get_weather1(location):
    api_key=os.environ.get('api_key')
    http = urllib3.PoolManager()
    r = http.request('GET', "http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=yes".format(api_key,location))
    response=json.loads(r.data.decode('utf-8'))
    weather=response['current']['condition']['text']
    print(weather)
    return weather;
