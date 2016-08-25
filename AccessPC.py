import telepot
import sys
import time
import subprocess
import os 
TOKEN = '***Add your token***'  

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    message = msg['text']
    if message.split(' ')[0] == 'ls':
       if len(message.split(' ')) > 1: #if command has options
          p = subprocess.Popen(['ls', message[3:]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       else:
          p = subprocess.Popen(['ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          print "In 2"
       output, err = p.communicate()
       bot.sendMessage(chat_id, output)
    elif message.split(' ')[0] == 'cd':
       if len(message) <= 3:
          bot.sendMessage(chat_id, 'Usage : cd [path]')
       else:
          os.chdir(message[3:])
          bot.sendMessage(chat_id, 'Changed directory to ' + message[3:])
    elif message.split(' ')[0] == 'upload':
       path = message[7:]
       with open(path, 'r') as f:
          bot.sendDocument(chat_id, f.read())

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
