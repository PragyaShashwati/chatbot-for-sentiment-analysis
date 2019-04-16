import smtplib
import mail
import config
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
	score = analyser.polarity_scores(sentence)
	compound = score.get('compound')
	return compound

def test(name, reciever):
    c=0
    res = input('\nBotman : Do you find yourself worrying or being afraid alot?\n')
    c=c+sentiment_analyzer_scores(res)
    res = input('\nBotman : Do you find yourself avoiding certain situations because they make you extremely uncomfortable?\n')
    c=c+sentiment_analyzer_scores(res)
    res = input('\nBotman : Do you ever engage in repetitive behaviors?(i.e. checking the oven is off, '
           'locking doors, washing hands, counting, repeating words)\n')
    c=c+sentiment_analyzer_scores(res)
    res = input('\nBotman : Are you generally impatient?\n')
    c=c+sentiment_analyzer_scores(res)
    res = input('\nBotman : Do you worry about the same things over and over again / obsess a lot?\n')
    c=c+sentiment_analyzer_scores(res)
	res = input('\nBotman : Do you find it difficult to control your emotions?')
	c=c+sentiment_analyzer_scores(res)
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