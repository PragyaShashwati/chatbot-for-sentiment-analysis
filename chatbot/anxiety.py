import smtplib
import mail
import config
import test
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
	score = analyser.polarity_scores(sentence)
	compound = score.get('compound')
	return compound
	
finisher = '\nIt was really nice talking to you and I hope that now you'\
           ' feel better after talking to me.\nBest of luck for your future '\
           'endeavours. Bye!'

def work(name, reciever):
	score = test.test(name, reciever)
	if(score >= 1.0):
		mail.send_email(name, reciever)	
	print("\nBotman : "+name + ", don't take too much stress. I can list some really cool "\
          "ways to handle it.\nYou should develop healthy responses which "\
          "include doing regular exercise and taking good quality sleep. "\
          "You should have clear boundaries between your work or academic "\
          "life and home life so you make sure that you don't mix them.\n"\
          "Tecniques such as meditation and deep breathing exercises can be "\
          "really helping in relieving stress.\n  Always take time to "\
          "recharge so as to avoid the negative effects of chronic stress "\
          "and burnout. We need time to replenish and return to our pre-"\
          "stress level of functioning.")
	print(finisher)
	
def friends(name, reciever):
    response = input('\nBotman : How are your friends meeting up with your expectations?'\
                     '\n')
    if(sentiment_analyzer_scores(response) <=0.4):
        score = test.test(name, reciever)
        if(score >= 1.0):
            mail.send_email(name, reciever)
        response = input('Have you broken up with someone recently?\n')
        if(sentiment_analyzer_scores(response)<=0.4):
            print("\nBotman : "+name + ", don't feel sad. Take your time and heal properly,"\
                  " look at what's happened, learn from it, and find ways to "\
                  "build a new and healthy life.\nAll any of us wants is to "\
                  "be happy. For some, this requires the perfect person to "\
                  "be our other half, and for others, it means completing "\
                  "the equation yourself. Either way, to find the right "\
                  "person, you need to be the right person. And trust that "\
                  "in the long run, your efforts will lead to your own "\
                  "personal happy ending.")
            print(finisher)
        else:
            print("\nBotman : "+name + ", don't worry. You may be at a point where similar "\
                  "people are not in your life right now. That happens in "\
                  "life from time to time.\nIt is better to be away from "\
                  "incompatible people, and those people are attracted to "\
                  "you when you pretend to be someone you aren't.\nBe as "\
                  "different as you truly are, get to know yourself at a "\
                  "deep level, esteem your individuality, interact with "\
                  "pepole honestly, and eventually the people who appreciate "\
                  "you will notice and be drawn in.")
            print(finisher)
    else:
        print("\nBotman : Many people tend to expect too much of others, their family, "\
              "their friends or even just acquaintances. It's a usual mistake"\
              ", people don't think exactly the way you do.\nDon't let the "\
              "opinions of others make you forget what you deserve. You are "\
              "not in this world to live up to the expectations of others, "\
              "nor should you feel that others are here to live up to yours."\
              "\nThe first step you should take if you want to learn how to "\
              "stop expecting too much from people is to simply realize and "\
              "accept the fact that nobody is perfect and that everyone "\
              "makes mistakes every now and then.")
        print(finisher)
       

def family(name, reciever):
    score = test.test(name, reciever)
    if(score >= 1.0):
        mail.send_email(name, reciever)	
    print("\nBotman : "+name + ", don't take too much stress. All you need to do is adjust "\
          "your priorities. Don't take on unnecessary duties and "\
          "responsibilities.\nTake advice from people whose opinion you "\
          "trust, and get specific advice when issues arise.\nYou should "\
          "use stress management techniques and always hope for the best. "\
          "These situations arise in everyone's life and what matters the "\
          "most is taking the right decision at such moments.")
    print(finisher)
	
def sad1(name, reciever):
    response = input('\nBotman : I understand. Seems like something\'s bothering you. '\
                     'Could you further describe it, in short?\n')
    if(sentiment_analyzer_scores(response)>=0.4):
        response = input('\nBotman : It seems like though the issue might be a little '\
                         'worrisome, it might not actually be very serious. '\
                         'What are your thoughts on this?\n')
        if(sentiment_analyzer_scores(response)>=0.5):
            response = input('Botman : Looks like you agree with me. Wanna sign off?\n')
            if(sentiment_analyzer_scores(response)<0.55):
                print("\nBotman : That's okay. It was nice talking to you. You can chat "\
                      "with me anytime you want.\nBye" + name + "!")
            else:
                sad3(name, reciever)
        else:
            sad3(name, reciever)
    else:
        sad2(name, reciever)
		
def sad2(name, reciever):
    response = input('\nBotman : Please feel free to share your feelings '+name+\
                     ', think of me as your friend.\n')
    if(sentiment_analyzer_scores(response)<=0.3):
        response = input('\nBotman : I see. Among the thoughts occuring in your mind, '\
                         'which one upsets you the most?\n')
        response = input('Why do you think it upsets you?\n')
        print("\nBotman : Okay. You just identified what we call an automatic thought. "\
              "Everyone has them. They are thoughts that immediately pop to "\
              "mind without any effort on your part.\nMost of the time the "\
              "thought occurs so quickly you don't notice it, but it has an "\
              "impact on your emotions. It's usually the emotion that you "\
              "notice, rather than the thought.\nOften these automatic "\
              "thoughts are distorted in some way but we usually don't stop "\
              "to question the validity of the thought. But today, that's "\
              "what we are going to do.")
        response = input('\nBotman : So, '+name+', are there signs that contrary '\
                         'could be true?\n')
        if(sentiment_analyzer_scores(response)<=0.4):
            print("\nBotman : I'm glad that you realised that the opposite could be "\
                  "true. The reason these are called 'false beliefs' is "\
                  "because they are extreme ways of perceiving the world. "\
                  "They are black or white and ignore the shades of grey in "\
                  "between.\nNow that you have learned about this cool "\
                  "technique, you can apply it on most of the problems that "\
                  "you will face. If you still feel stuck at any point, you "\
                  "can always chat with me.\nBest of luck for your future "\
                  "endeavours. Bye!")
        else:
            sad4(name, reciever)
    else:
        sad4(name, reciever)

def sad3(name, reciever):
    response = input('\nBotman : Feel comfortable. Could you briefly explain about your '\
                     'day?\n')
    response = input('\nBotman : What are the activities that make up your most of the '\
                     'day?\n')
    response = input('\nBotman : It looks like you might be feeling comfortable talking '\
                     'about yourself. Could you share your feelings?\n')
    if(sentiment_analyzer_scores(response)>=0.3):
        sad2(name, reciever)
    else:
        sad4(name, reciever)

def sad4(name, reciever):
    print("\nBotman : My sympathies. Looks like it might be a point of concern. Don't "\
          "worry, that's what I'm here for!")
    response_friends = input('\nBotman : How are things going on with your friends?\n')
    response_family  = input('\nBotman : How is your relationship with your parents?\n')
    response_worklife = input('\nBotman : How is your work or academic life going on?\n')
    if(sentiment_analyzer_scores(response_friends)<=0.3):
        friends(name, reciever)
    else:
        if(sentiment_analyzer_scores(response_family)<=0.3):
            family(name, reciever)
        else:
            work(name, reciever)
			
print('\nBotman : Hello! Thanks for coming here. I am a chatbot. People say that '
      'I am a kind and approachable bot.')
name = input('\nBotman : Please tell me your name.\n')
try:
    preprocessed = [word for word in preprocess_string(name) if word not in (
                    'people', 'call', 'friend')][0]
    name = [word for word in strip_non_alphanum(name.lower()).split(
            ) if preprocessed in word][0]
except:
    name = name.split()[0]
name = name[0].upper() + name[1:]
email = input('\nBotman : Your email id\n')
reciever = input('\nBotman : Emergency email\n')
print("\nBotman : Hi " + name + "! My name's Botman. Let's start with our session.")
response = input("\nBotman : How are you doing?\n")
if (sentiment_analyzer_scores(response) >= 0.4):
    response = input('\nBotman : That is good. Are you usually this happy, or are there '\
                     'some worries that you want to talk about?\n')
    if (sentiment_analyzer_scores(response)<=0.7):
        response = input('\nBotman : You seem to be really content. Wanna sign off?\n')
        if(sentiment_analyzer_scores(response)>=0.7):
            print('\nBotman : Ok, bye ' + name + '!')
        else:
            response = input('\nBotman : Is there something bothering you? Would you '\
                             'share it with me?\n')
            if(sentiment_analyzer_scores(response)>=0.7):
                print("\nBotman : That's okay. It was nice talking to you. You can chat "\
                      "with me anytime you want.\n Bye" + name + "!")
            else:
                sad1(name, reciever)
    else:
        sad1(name, reciever)
else:
    sad3(name, reciever)
