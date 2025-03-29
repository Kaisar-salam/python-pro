import telebot 
import os
import random
import requests
images = (os.listdir('photo'))


bot=telebot.TeleBot("")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    image = random.choice(images)
    with open(f'photo/{image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
@bot.message_handler(commands=['duck'])
def duck(message):
        '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)
bot.polling()
