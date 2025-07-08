from telegram.ext import Updater, CommandHandler
from moviepy.editor import *
from gtts import gTTS
import os

TOKEN = "7302510558:AAHTVCJ4Nh5Wa121JnFFs7-0PfVQbeytHtU"

def start(update, context):
    update.message.reply_text("Send /make followed by your message to create a video.")

def make(update, context):
    text = ' '.join(context.args)
    if not text:
        update.message.reply_text("Please provide text after /make")
        return

    tts = gTTS(text)
    tts.save("voice.mp3")

    clip = VideoFileClip("background.mp4").subclip(0, 10)
    audio = AudioFileClip("voice.mp3").set_duration(clip.duration)

    txt = TextClip(text, fontsize=40, color='white')
    txt = txt.set_position('center').set_duration(clip.duration)

    video = CompositeVideoClip([clip, txt])
    video = video.set_audio(audio)

    video.write_videofile("final.mp4", fps=24)

    context.bot.send_video(chat_id=update.effective_chat.id, video=open("final.mp4", 'rb'))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("make", make))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
