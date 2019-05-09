import smtplib
import mail
import config
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
	score = analyser.polarity_scores(sentence)
	compound = score.get('compound')
	return compound
	
def pos_scores(sentence):
	score = analyser.polarity_scores(sentence)
	compound = score.get('compound')
	pos = score.get('pos')
	if (pos >= 0.5):
		return 1
	else:
		return 0	

def test(name, reciever):
    c=0
    res = input('\nBotman : Do you find yourself worrying or being afraid alot?\n')
    if (pos_scores(res)):
        c=c+1
    res = input('\nBotman : Do you find yourself avoiding certain situations because they make you extremely uncomfortable?\n')
    if (pos_scores(res)):
        c=c+1
    res = input('\nBotman : Do you ever engage in repetitive behaviors?(i.e. checking the oven is off, '
           'locking doors, washing hands, counting, repeating words)\n')
    if (pos_scores(res)):
        c=c+1
    res = input('\nBotman : Are you generally impatient?\n')
    if (pos_scores(res)):
        c=c+1
    res = input('\nBotman : Do you often get bothered of feeling nervous, anxious or on edge over the last couple of days?\n')
    if (pos_scores(res)):
        c=c+1
    res = input("\nBotman : Do you often say to people's requests when you'd rather say no?\n")
    if (pos_scores(res)):
        c=c+1
    res = input('\nBotman : Do you have trouble in sleeping and relaxing in general?\n')
    if (pos_scores(res)):
        c=c+1
    res = input('\nBotman : Do you experience repetitive persistent thoughts that are upsetting and unwanted?\n')
    if (pos_scores(res)):
        c=c+1
    res = input('\nBotman : Do you obsess about your certain actions?\n')
    if (pos_scores(res)):
        c=c+1
    return c
#    if(c >= 1.0):
#        mail.send_email(name, reciever)		
#    else:
#       print('\nIt was really nice talking to you and I hope that now you'\
#            ' feel better after talking to me.\nBest of luck for your future '\
#            'endeavours. Bye!\n')

#name = 'Arnav'
#reciever='pragyashashwati5@gmail.com'        
#test(name, reciever)