#
# Katherine Sanders - "CrisisConnect"
# Creatica 2021
#

import time
import random

#------------------------possible responses
stopConnect = "QUIT"
#------------yes or no
yes = "YES"
yea = "YEA"
no = "NO"
dontKnow = "DONT KNOW"
dontKnow1 = "DON'T KNOW"
#------------chat bot or coping mechanisms
hotline = "HOTLINE"
helpline = "HELPLINE"
coping = "COPING"
#------------emotions
#---bad
sad = "SAD"
depressed = "DEPRESSED"
empty = "EMPTY"
numb = "NUMB"
bad = "BAD"
useless = "USELESS"
#---good
good = "GOOD"
okay = "OK"
better = "BETTER"
happy = "HAPPY"
calm = "CALM"
#------------check right responses
isHelpful = "IS HELPFUL"
wasHelpful = "WAS HELPFUL"
keepTalking = "KEEP TALKING"
#------------key words 
abuseWord = "ABUSE"
suicideWord = "SUICID"
helpWord = "HELP"
#------------interests responses
shows = "SHOWS"
movies = "MOVIES"
reading = "READING"
music = "MUSIC"
draw = "DRAW"
write = "WRITING"
sleep = "SLEEP"
eat = "EAT"
food = "FOOD"
nothing = "NOTHING"
prompts = ["Challenges", "Gratitude", "Elementary School", "Fear", "The Past", "The Present", "The Future", "Religion", "Environment"]
activities = ["Paint a random object", "Go outside without shoes on", "Sew something"]
activities1 = ["Meditate", "Online shop", "Organize your space", "Redecorate"]
activities2 = ["Learn a new skill", "Play video games"]

#------------------------Requesting Hotlines
def immediateEmergencyFunction():
    print("If you or someone else is in serious danger, contact 911.")

def suicidePrevention():
    print("If you are thinking of hurting yourself, are worried about a loved one, or need emotional support, the National Suicide Prevention Hotline is available at all times in the US.")
    time.sleep(5)
    print("\n")
    print("NATIONAL SUICIDE PREVENTION HOTLINE: (800) 273-8255")

def domesticAbuseFunction():
    print("The domestic abuse hotline will connect you to a professional to have a conversation about how you are being treated by those you currently live with.")
    time.sleep(5)
    print("\n")
    print("When you call, you can talk about your situation without fear of judgement, and brainstorm ideas on how to help you become safe.")
    time.sleep(4.25)
    print("\n")
    print("DOMESTIC ABUSE HOTLINE: (800) 799-7233 or Text 'LOVEIS' to 22522")

def abuseFunction():
    print("If you or someone you know is being abused:")
    time.sleep(2)
    print("\n")
    print("CALL or TEXT the CHILD ABUSE HOTLINE: (800) 422-4453")

def rainnFunction():
    print("RAINN, or the Rape, Abuse & Incest National Network, offers a 24/7 hotline to support survivors of sexual violence.")
    time.sleep(3.5)
    print("\n")
    print("RAINN HOTLINE: 1-800-656-4673")

def identityIssuesFunction():
    print("The Trevor Project is a non-profit focused on preventing suicide among LGBTQ+ and questioning youth.")
    time.sleep(3.25)
    print("\n")
    print("They offer a free 24/7 confidential hotline.")
    time.sleep(2.25)
    print("\n")
    print("TREVOR PROJECT HOTLINE: 1-866-488-7386")
    time.sleep(1.5)
    print("\n")
    print("TREVOR PROJECT TEXT-LINE: Text 'START' to 678678")

def lgbtqFunction():
    print("The LGBTQ+ Hotline is a free hotline for teens with questions about their sexuality.")
    time.sleep(3.25)
    print("\n")
    print("This hotline is available for certain hours on certain days.")
    time.sleep(2)
    print("\n")
    print("MONDAY - FRIDAY: 1:00pm to 9:00pm PST")
    print("SATURDAY: 9:00am to 2:00pm PST")
    time.sleep(3)
    print("\n")
    print("LGBTQ HOTLINE: 1-888-843-4564")

def substanceAbuseFunction():
    print("SAMHSA stands for 'Substance Abuse and Mental Health Services Administration'.")
    time.sleep(3.5)
    print("\n")
    print("They offer a free 24/7 confidential hotline.")
    time.sleep(2)
    print("\n")
    print("SAMHSA HELPLINE: 1-800-662-4357")

def eatingDisorderFunction():
    print("The National Eating Disorders Association, or NEDA, is a nonprofit organization that works to help teens struggling with eating disorders and body image.")
    time.sleep(5)
    print("\n")
    print("The hotline is open Monday through Friday.")
    time.sleep(2)
    print("\n")
    print("NEDA HELPLINE: 1-800-931-2237")

def namiFunction():
    print("NAMI is the National Alliance on Mental Illness.")
    time.sleep(2.25)
    print("\n")
    print("It is a peer support hotline, and can offer care and identify resources.")
    time.sleep(3)
    print("\n")
    print("This hotline is available only for certain hours on certain days.")
    time.sleep(2)
    print("\n")
    print("MONDAY - FRIDAY: 7:00am to 5:00pm PST")
    time.sleep(3)
    print("\n")
    print("NAMI HOTLINE: 1-800-950-6264")

def runawayFunction():
    print("If you or someone you know needs help with finding a home or has runaway from home, contact the National Runaway Safeline.")
    time.sleep(3.5)
    print("\n")
    print("NATIONAL RUNAWAY SAFELINE: 1-800-786-2929")

def racialEquityFunction():
    print("The Racial Equity Support Line offers support to those who are experience discrimination due to their background.")
    time.sleep(3.5)
    print("\n")
    print("RACIAL EQUITY SUPPORT LINE: 503-575-3764")

def youthLineFunction():
    print("The Youth Line is a crisis hotline for teens to talk to other teens while in a crisis.")
    time.sleep(2.75)
    print("\n")
    print("YOUTH HOTLINE: 877-968-8491")
    time.sleep(2)
    print("\n")
    print("YOUTH TEXT LINE: Text 'teen2teen' to 839863")

def textLineFunction():
    print("The crisis text-line is a 24 hour text service for every crisis. A trained responder will help guide you.")
    time.sleep(3.25)
    print("\n")
    print("CRISIS TEXT-LINE: Text 'HOME' or 'LEV' to 741741")
    time.sleep(2.5)

def cantTalk():
    print("If you cannot talk, the crisis text-line is a 24 hour text service for all crisis, and will guide you through yours.")
    time.sleep(4.25)
    print("\n")
    print("CRISIS TEXT-LINE: Text 'HOME' or 'LEV' to 741741")
    time.sleep(2.5)

def breathingExercise478():
    print("\n")
    print("First, let's do some breathing exercises:")
    time.sleep(2)
    print("\n")
    print("Breathe in...")
    time.sleep(1.5)
    print("\n")
    print("2")
    time.sleep(1)
    print("\n")
    print("3")
    time.sleep(1)
    print("\n")
    print("4")
    time.sleep(1.75)
    print("\n")
    print("Hold...")
    time.sleep(1.5)
    print("\n")
    print("2")
    time.sleep(1)
    print("\n")
    print("3")
    time.sleep(1)
    print("\n")
    print("4")
    time.sleep(1)
    print("\n")
    print("5")
    time.sleep(1)
    print("\n")
    print("6")
    time.sleep(1)
    print("\n")
    print("7")
    time.sleep(1.75)
    print("\n")
    print("And release...")
    time.sleep(1)
    print("\n")
    print("2")
    time.sleep(1)
    print("\n")
    print("3")
    time.sleep(1)
    print("\n")
    print("4")
    time.sleep(1)
    print("\n")
    print("5")
    time.sleep(1)
    print("\n")
    print("6")
    time.sleep(1)
    print("\n")
    print("7")
    time.sleep(1)
    print("\n")
    print("8")
    time.sleep(1.75)
    print("\n")

def interestsFunction():
    print("What are some things that make you happy?")
    interestsQ = input("> ")
    interests = interestsQ.upper()

    interestsResponse = interests.split()

    if shows in interestsResponse:
        print("Spoil yourself to your favorite movie or rewatch your favorite TV show - or start a new one.")
        time.sleep(3)
        print("\n")
        print("If you don't have anything to watch right now, here are some of my favorite shows right now:")
        time.sleep(2.5)
        print("\n")
        print("Never Have I Ever - Netflix \n") 
        time.sleep(1)
        print("Get Even - Netflix \n")
        time.sleep(1)
        print("You - Netflix, Prime \n")
        time.sleep(1)
        print("Making the Cut - Prime \n")
        time.sleep(1)
        print("Manifest - Netflix, Hulu \n")
        time.sleep(4)
        print("\n")
    else: 
        pass
    
    if reading in interestsResponse: 
        print("Try to dig up an old book from your childhood and reread it.")
        time.sleep(4)
        print("\n")
    else: 
        pass

    if music in interestsResponse: 
        print("Treat yourself to 30 minutes of listening to music.")
        time.sleep(2)
        print("\n")
        print("Or, create your own music!")
        time.sleep(4)
        print("\n")
    else:
        pass

    if write in interestsResponse: 
        print("Journal for 5 minutes. I will randomly choose a word for you, and you write what comes to mind:")
        time.sleep(3)
        print("\n")
        print("Your prompt is:")
        print(random.choice(prompts))
        time.sleep(4)
        print("\n")
    else:
        pass

    if draw in interestsResponse:
        print("Draw for 30 minutes. I will randomly choose a word for you, and you draw what comes to mind:")
        time.sleep(3)
        print("\n")
        print("Your prompt is:")
        print(random.choice(prompts))
        time.sleep(4)
        print("\n")
    else:
        pass

    if sleep in interestsResponse:
        print("Ah yes. Sleep is really nice.")
        time.sleep(2)
        print("I recommend you draw, write, watch a show, or listen to some music before you sleep if you aren't feeling completely well.")
        time.sleep(4)
        print("\n")
        print("After that, you should take a big, long nap: you deserve it.")
        time.sleep(2.5)
        print("\n")
    else:
        pass

    if eat in interestsResponse:
        print("I challenge you to create something knew.")
        time.sleep(2.5)
        print("What's something you've always wanted to try? Try to create a new meal out of the things you have at home!")
        time.sleep(4)
        print("\n")
    else:
        pass

    if dontKnow or dontKnow1 or nothing in interestsResponse:
        print("\n")
        print("I challenge you to do something knew.")
        time.sleep(2.5)
        print("\n")
        print("I will randomize an easy activity for you to do:")
        time.sleep(2)
        print(random.choice(activities))
        time.sleep(4)
        print("\n")

        print("Do you want another activity?")
        anotherActivityQ = input("> ")
        anotherActivity = anotherActivityQ.upper()

        if yes in anotherActivity:
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            anotherActivity1Q = input("> ")
            anotherActivity1 = anotherActivity1Q.upper()

            if yes in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            else: 
                pass

        elif yea in anotherActivity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            anotherActivity1Q = input("> ")
            anotherActivity1 = anotherActivity1Q.upper()

            if yes in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            else: 
                pass

        else: 
            pass

    else:
        pass

def goodbye():
    print("I hope you found the help you needed. You are an important part of this world. <3")
    time.sleep(2)
    print("\n")
    print("Goodbye!")
    print("\n")
    exit()

def checkRight():
    print("Was this information helpful, or would you like to keep talking?")
    checkRightResponse = input("> ")
    checkRightAnswer = checkRightResponse.upper()
    
    if wasHelpful in checkRightAnswer:
        print("\n")
        print("I hope you found the help you needed. You are an important part of this world. <3")
        time.sleep(2)
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()
    elif isHelpful in checkRightAnswer:
        print("\n")
        print("I hope you found the help you needed. You are an important part of this world. <3")
        time.sleep(2)
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()
    elif yes in checkRightAnswer:
        print("\n")
        print("I hope you found the help you needed. You are an important part of this world. <3")
        time.sleep(2)
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()
    elif yea in checkRightAnswer:
        print("\n")
        print("I hope you found the help you needed. You are an important part of this world. <3")
        time.sleep(2)
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()
    elif keepTalking in checkRightAnswer:
        print("\n")
        print("Alright, we will continue to talk.")
        time.sleep(2)
        print("\n")
    elif no in checkRightAnswer:
        print("\n")
        print("Alright, we will continue to talk.")
        time.sleep(2)
        print("\n")
    elif stopConnect in checkRightAnswer:
        exit()
    else: 
        pass


#------------------------introduction
print("\n")
print("Welcome to CrisisConnect. My name is Cami, and I will be here to guide you through your crisis.")
time.sleep(3.75)
print("\n")
print("Throughout this process, I will ask simple questions that will help clear your mind and lead you to the right helpline.")
time.sleep(4.25)
print("\n")
print("For the best and easiest experience, I recommend responding with 'yes', 'no', or the options I provide.")
time.sleep(3.75)
print("\n")
print("If you want to stop talking, type and enter 'quit' at anytime.")
time.sleep(3.75)
print("\n")

#------------------------chat bot or coping mechanisms?
print("Would you like to find a hotline, or look at some coping mechanisms today?")
chatDecideQ = input("> ")
chatDecide = chatDecideQ.upper()

if coping in chatDecide:

    breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    interestsFunction()

    goodbye()
else:
    print("\n")
    pass


#------------------------are you in immediate danger?
print("Are you currently thinking about hurting yourself or others?")
emergencyQ = input("> ")
immediateEmergency = emergencyQ.upper()

if yes in immediateEmergency:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(3.5)
    suicidePrevention()
    print("\n")
    time.sleep(3.5)

    checkRight()

elif yea in immediateEmergency:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(3.5)
    suicidePrevention()
    print("\n")
    time.sleep(3.5)

    checkRight()


elif no in immediateEmergency:
    print("\n")
    print("I am glad you're keeping yourself and others safe.")
    print("\n")
    time.sleep(2.5)

elif stopConnect in immediateEmergency:
    exit()

elif abuseWord or suicideWord or helpWord in immediateEmergency:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else:
    pass 


#------------------------check if they can talk 
print("Are you able to talk out loud?")
talkAloudQ = input("> ")
talkAloud = talkAloudQ.upper()

if no in talkAloud:
    print("\n")
    cantTalk()
    print("\n")

    #check right

    print("Are you completely sure you still cannot talk aloud?")
    checkTalkAloudQ = input("> ")
    checkTalkAloud = checkTalkAloudQ.upper()

    if no in checkTalkAloud:
        print("The text hotline is a great resource for when you cannot talk aloud on the phone.")
        time.sleep(2)
        print("\n")
        print("Text 'HOME' to 741741")
        time.sleep(1.75)
        print("\n")
        print("The following questions will provide hotlines that require you to talk aloud. However, we will continue to chat.")
        time.sleep(2)
        print("\n")
    elif yes in checkTalkAloud: 
        print("\n")
        print("The following questions will provide hotlines that require you to talk aloud. We will continue to chat.")
        time.sleep(2)
    elif yea in checkTalkAloud: 
        print("\n")
        print("The following questions will provide hotlines that require you to talk aloud. We will continue to chat.")
        time.sleep(2)
    elif stopConnect in checkTalkAloud:
        exit()
    elif abuseWord or suicideWord or helpWord in checkTalkAloud:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

elif yea in talkAloud:
    pass

elif yes in talkAloud:
    pass

elif stopConnect in talkAloud:
    exit()

elif abuseWord or suicideWord or helpWord in talkAloud:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else:
    pass


#------------------------domestic abuse
print("\n")
print("Are you in a safe environment with people you trust?")
safeEnvironmentQ = input("> ")
safeEnvironment = safeEnvironmentQ.upper()

if no in safeEnvironment: 
    print("\n")
    print("Is a family member, romantic partner, or platonic partner causing you to be in danger?")
    domesticAbuseQ = input("> ")
    domesticAbuse = domesticAbuseQ.upper()

    if yes in domesticAbuse:
        print("\n")
        domesticAbuseFunction()
        time.sleep(3.5)
        print("\n")

        print("\n")
        rainnFunction()
        time.sleep(3.5)
        print("\n")
        
        checkRight()

    elif yea in domesticAbuse:
        print("\n")
        domesticAbuseFunction()
        time.sleep(3.5)
        print("\n")

        print("\n")
        rainnFunction()
        time.sleep(3.5)
        print("\n")
        
        checkRight()
        
    elif no in domesticAbuse:
        print("\n")
        print("Are you fearful for the safety of yourself or others?")
        abuseQ = input("> ")
        abuse = abuseQ.upper()

        if yes or yea in abuse:
            print("\n")
            abuseFunction()
            time.sleep(3.5)
            print("\n")

            print("\n")
            rainnFunction()
            time.sleep(3.5)
            print("\n")
            
            checkRight()

        elif yea in abuse:
            print("\n")
            abuseFunction()
            time.sleep(3.5)
            print("\n")

            print("\n")
            rainnFunction()
            time.sleep(3.5)
            print("\n")
            
            checkRight()

        elif stopConnect in abuse:
            exit()
        
        elif abuseWord or suicideWord or helpWord in abuse:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()
        
        else:
            pass

    elif stopConnect in domesticAbuse:
        exit()
    
    elif abuseWord or suicideWord or helpWord in domesticAbuse:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

elif yes in safeEnvironment: 
    print("\n")
    print("I'm glad you're in a safe environment.")
    time.sleep(1.5)

elif yea in safeEnvironment: 
    print("\n")
    print("I'm glad you're in a safe environment.")
    time.sleep(1.5)

elif stopConnect in safeEnvironment:
    exit()

elif abuseWord or suicideWord or helpWord in safeEnvironment:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else:
    pass 


#------------------------hurting others
print("\n")
print("Do you fear that you are putting others in danger?")
othersSafetyQ = input("> ")
othersSafety = othersSafetyQ.upper()

if yes in othersSafety:
    print("\n")
    print("The National Domestic Hotline can also be used if you feel you are causing pain and want to stop.")
    time.sleep(3.75)
    print("\n")
    print("When you call, you can talk about your situation without fear of judgement, and brainstorm ideas on how to help you be safe.")
    time.sleep(4.25)
    print("\n")
    print("DOMESTIC ABUSE HOTLINE: (800) 799-7233 or Text 'LOVEIS' to 22522")

    checkRight()

elif yea in othersSafety:
    print("\n")
    print("The National Domestic Hotline can also be used if you feel you are causing pain and want to stop.")
    time.sleep(3.75)
    print("\n")
    print("When you call, you can talk about your situation without fear of judgement, and brainstorm ideas on how to help you be safe.")
    time.sleep(4.25)
    print("\n")
    print("DOMESTIC ABUSE HOTLINE: (800) 799-7233 or Text 'LOVEIS' to 22522")

    checkRight()

elif stopConnect in othersSafety:
    exit()

elif abuseWord or suicideWord or helpWord in othersSafety:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif no in othersSafety:
    pass

else:
    print("\n")
    pass


#------------------------identity issues
print("Are you or someone you know dealing with any identity issues?")
identityIssuesQ = input("> ")
identityIssues = identityIssuesQ.upper()

if yes in identityIssues:
    print("\n")
    identityIssuesFunction()
    time.sleep(3)
    print("\n")

    lgbtqFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif yea in identityIssues:
    print("\n")
    identityIssuesFunction()
    time.sleep(3)
    print("\n")

    lgbtqFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif no in identityIssues: 
    print("\n")
    pass

elif stopConnect in identityIssues:
    exit()

elif abuseWord or suicideWord or helpWord in identityIssues:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else: 
    print("\n")
    pass 


#------------------------substance abuse
print("Are you or someone you know struggling with substance issues: drinking excessively, smoking, etc.?")
substanceAbuseQ = input("> ")
substanceAbuse = substanceAbuseQ.upper()

if yes in substanceAbuse:
    print("\n")
    substanceAbuseFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif yea in substanceAbuse:
    print("\n")
    substanceAbuseFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif no in substanceAbuse: 
    print("\n")
    pass

elif stopConnect in substanceAbuse:
    exit()

elif abuseWord or suicideWord or helpWord in substanceAbuse:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else: 
    print("\n")
    pass 


#------------------------eating disorder
print("Are you or someone you know struggling with an eating disorder or body image?")
eatingDisorderQ = input("> ")
eatingDisorder = eatingDisorderQ.upper()

if yes in eatingDisorder:
    print("\n")
    eatingDisorderFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif yea in eatingDisorder:
    print("\n")
    eatingDisorderFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif no in eatingDisorder: 
    print("\n")
    pass

elif stopConnect in eatingDisorder:
    exit()

elif abuseWord or suicideWord or helpWord in eatingDisorder:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else: 
    print("\n")
    pass 


#------------------------runaway/homelessness
print("Have you or someone you know ran away from home or do not have a home to go to?")
runawayQ = input("> ")
runaway = runawayQ.upper()

if yes in runaway:
    print("\n")
    immediateEmergencyFunction()
    time.sleep(2)
    print("\n")

    print("\n")
    runawayFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif yea in runaway:
    print("\n")
    immediateEmergencyFunction()
    time.sleep(2)
    print("\n")

    print("\n")
    runawayFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif no in runaway: 
    print("\n")
    pass

elif stopConnect in runaway:
    exit()

elif abuseWord or suicideWord or helpWord in runaway:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else: 
    print("\n")
    pass 


#------------------------racial discrimination
print("Are you being discriminated against due to your race?")
racialEquityQ = input("> ")
racialEquity = racialEquityQ.upper()

if yes in racialEquity:
    print("\n")
    racialEquityFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif yea in racialEquity:
    print("\n")
    racialEquityFunction()
    time.sleep(2)
    print("\n")

    checkRight()

elif stopConnect in racialEquity:
    exit()

elif abuseWord or suicideWord or helpWord in racialEquity:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else: 
    print("\n")
    pass


#------------------------general crisis - asking emotions
print("How are you feeling right now?")
generalCrisisQ = input("> ")
generalCrisis = generalCrisisQ.upper()

if sad or depressed or empty or numb or bad or useless in generalCrisis:
    print("Would you like to talk to another teen about your feelings?")
    generalCrisisYouthQ = input("> ")
    generalCrisisYouth = generalCrisisYouthQ.upper()

    if yes in generalCrisisYouth:
        print("\n")
        youthLineFunction()
        time.sleep(2)
        print("\n")

        checkRight()

    elif yea in generalCrisisYouth:
        print("\n")
        youthLineFunction()
        time.sleep(2)
        print("\n")

        checkRight()

    elif stopConnect in generalCrisisYouth:
        exit()

    elif abuseWord or suicideWord or helpWord in generalCrisisYouth:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    else: 
        print("\n")
        namiFunction()
        time.sleep(2)
        print("\n")

        checkRight()



elif good or okay or better or happy or calm in generalCrisis:
    print("I am so glad you are feeling better!")
    time.sleep(2)
    print("\n")
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    interestsFunction()

    goodbye()

elif stopConnect in generalCrisis:
    exit()

elif abuseWord or suicideWord or helpWord in generalCrisis:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else: 
    print("\n")
    pass 


# add an overall question about mood that directly points to the previous hotlines 
print("Are you feeling better?")
feelingOverallQ = input("> ")
feelingOverall = feelingOverallQ.upper()

if yes in feelingOverall:
    #------------------------final support/coping mechanisms
    print("I am so glad you are feeling better!")
    time.sleep(2)
    print("\n")
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    interestsFunction()

    goodbye()

elif yea in feelingOverall:
    #------------------------final support/coping mechanisms
    print("I am so glad you are feeling better!")
    time.sleep(2)
    print("\n")
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    interestsFunction()

    goodbye()


else:
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    interestsFunction()

    goodbye()
