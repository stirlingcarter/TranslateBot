#Python Reddit API Wrapper
import praw 
#translate API (not affiliated with Google)
from googletrans import Translator 

#make a translator object
translator = Translator()

#bot constructor 
bot = praw.Reddit(user_agent='Translate_Bot_',
                  client_id='hidden',
                  client_secret='hidden',
                  username='translate_bot_',
                  password='hidden')

#subreddit contructor 
sub = bot.subreddit('all')

#supported languages
languages = [
"afrikaans",
"albanian",
"amharic",
"arabic",
"armenian",
"azerbaijani",
"basque",
"belarusian",
'bengali',
"bosnian",
"bulgarian",
'kriolu',
"catalan",
"cebuano",
"chichewa",
"chinese",
'corsican',
"croatian",
'czech',
"danish",
"dutch",
"english",
"esperanto",
'estonian',
'filipino',
'finnish',
'french',
'frisian',
'galician',
'georgian',
'german',
'greek',
'gujarati',
'haitian creole',
'hausa',
'hawaiian',
'hebrew',
'hindi',
'hmong',
'hungarian',
'icelandic',
'igbo',
'indonesian',
'irish',
'italian',
'japanese',
'javanese',
'kannada',
'kazakh',
'khmer',
'korean',
'kurdish',
'kyrgyz',
'lao',
'latin',
'latvian',
'lithuanian',
'luxembourgish',
'macedonian',
'malagasy',
'malay',
'malayalam',
'maltese',
'maori',
'marathi',
'mongolian',
'myanmar',
'nepali',
'norwegian',
'pashto',
'persian',
'polish',
'portuguese',
'punjabi',
'romanian',
'russian',
'samoan',
'scots gaelic',
'serbian',
'sesotho',
'shona',
'sindhi',
'sinhala',
'slovak',
'slovenian',
'somali',
'spanish',
'sundanese',
'swahili',
'swedish',
'tajik',
'tamil',
'telugu',
'thai',
'turkish',
'ukrainian',
'urdu',
'uzbek',
'vietnamese',
'welsh',
'xhosa',
'yiddish',
'yoruba',
'zulu']

#instantiates a comment stream 
sub_comments = sub.stream.comments()

#combs through stream
for comment in sub_comments:
    
    text = comment.body
    text = text.split(" ")

    if (text[0].upper() == 'TRANSLATE' and 
        text[1].lower() in languages and
        len(text) == 2):

            original = comment.parent().body
            explanation = 'This message was produced by a bot! For more information please visit https://github.com/stirlingcarter/TranslateBot'
            transMsg = translator.translate(original, dest= text[1]).text
            msg = "Translated comment:\n\n\""+transMsg+"\"\n\n" + explanation
         
            comment.parent().reply(msg)
            print("replied \n") 

	

                            
