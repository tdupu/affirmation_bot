import zulip
import random

# Pass the path to your zuliprc file here.

#testing
#client = zulip.Client(config_file="/Users/taylordupuy/Dropbox/computing/dupuy-zulip-bots/zuliprc")

client = zulip.Client(config_file="/Users/taylordupuy/Dropbox/computing/dupuy-zulip-bots/affirmation-live/zuliprc")
#admin_client = zulip.Client(config_file="/Users/taylordupuy/Dropbox/computing/dupuy-zulip-bots/taylor-bot/zuliprc")

m = 2
user_list = [313513,312329,326226,320828,312334,313092]

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def motivate(msg):
    zulip_id = msg['sender_id']
    stream_id = msg['stream_id']
    topic = msg['subject']
    print('message in: \n')
    print(msg)
    print('\n')
    
    x=random.randint(0,m)
    if x==1:
        if user_list.count(zulip_id)>0:
            affirmation = random_line('affirmations.txt')
            bot_request = {
                 "type": "stream",
                 "to": stream_id,
                 "topic": topic,
                 "content": affirmation,
             }
            result = client.send_message(bot_request)
            print('result of out: \n')
            print(result)
            print('\n')
    else:
        result = "Did nothing. \n"
        print('result of out: \n')
        print(result)
 
#client.call_on_each_message(lambda msg: motivate(msg))
client.call_on_each_message(motivate)
