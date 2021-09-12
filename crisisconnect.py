#
# Katherine Sanders - "CrisisConnect"
# Creatica 2021
# Congressional App Challenge 2021
# August 22
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
#------------chat bot or coping mechanisms
hotline = "HOTLINE"
helpline = "HELPLINE"
coping = "COPING"
cope = "COPE"
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
write = "WRITE"
sleep = "SLEEP"
eat = "EAT"
food = "FOOD"
nothing = "NOTHING"
prompts = ["Challenges", "Gratitude", "Elementary School", "Fear", "The Past", "The Present", "The Future", "Religion", "Environment"]
activities = ["Paint a random object", "Go outside without shoes on", "Sew something"]
activities1 = ["Meditate", "Online shop", "Organize your space", "Redecorate"]
activities2 = ["Learn a new skill", "Play video games"]

#-------------------------------NEW VARIABLES-----------------------
#----------------general terms
hate = "HATE"
myself = "MYSELF"
cantLive = "CANT LIVE"
dont = "DONT"
idk = "IDK"
feel = "FEEL"
not1 = "NOT"
im = "IM"
#----------------domestic abuse
girlfriend = "GIRLFRIEND"
boyfriend = "BOYFRIEND"
bf = "BF"
gf = "GF"
partner = "PARTNER"
wife = "WIFE"
husband = "HUSBAND"
spouse = "SPOUSE"
mom = "MOM"
mother = "MOTHER"
dad = "DAD"
father = "FATHER"
sister = "SISTER"
brother = "BROTHER"
grandma = "GRANDMA"
grandpa = "GRANDPA"
hit = "HIT"
hurt = "HURT"
#---------------Rape, Incest 
touch = "TOUCH"
nonconsensual = "NONCONSENSUAL"
consent = "CONSENT"
grope = "GROPE"
make = "MAKE"
#---------------LGBTQ & identity 
like = "LIKE"
love = "LOVE"
gay = "GAY"
#----------------substance abuse
drugs = "DRUGS"
alcohol = "ALCOHOL"
vape = "VAPE"
vaping = "VAPING"
#-----------------eating disorder/body image issues
cantEat = "CANT EAT"
wontEat = "WONT EAT"
throwUp = "THROW UP"
body = "BODY"
fat = "FAT"
disgusting = "DISGUSTING"
gross = "GROSS"
#--------------------------------


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
    interestsQ = raw_input("> ")
    interests = interestsQ.upper()

    interestsResponse = interests.split()

    if sleep in interestsResponse:
        print("\n")
        print("Ah yes. Sleep is really nice.")
        time.sleep(2)
        print("\n")
        print("I recommend you draw, write, watch a show, or listen to some music before you sleep if you aren't feeling completely well.")
        time.sleep(4)
        print("\n")
        print("After that, you should take a big, long nap: you deserve it.")
        time.sleep(2.5)
        print("\n")

        
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
        another1ActivityQ = raw_input("> ")
        another1Activity = another1ActivityQ.upper()

        if yes in another1Activity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            another1Activity1Q = raw_input("> ")
            another1Activity1 = another1Activity1Q.upper()

            if yes in another1Activity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in another1Activity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif no in another1Activity1:
                pass
            elif stopConnect in another1Activity1:
                exit()
            else: 
                pass

        elif yea in another1Activity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            another1Activity1Q = raw_input("> ")
            another1Activity1 = another1Activity1Q.upper()

            if yes in another1Activity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in another1Activity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif no in another1Activity1:
                pass
            elif stopConnect in another1Activity1:
                exit()
            else: 
                pass
        elif stopConnect in another1Activity:
            exit()
        elif no in another1Activity1:
                pass
        else: 
            pass
    elif stopConnect in interestsResponse:
        exit()
    else:
        pass

    if shows in interestsResponse:
        print("\n")
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
        print("\n")
        print("Try to dig up an old book from your childhood and reread it.")
        time.sleep(4)
        print("\n")
    else: 
        pass

    if music in interestsResponse: 
        print("\n")
        print("Treat yourself to 30 minutes of listening to music.")
        time.sleep(2)
        print("\n")
        print("Or, create your own music!")
        time.sleep(4)
        print("\n")
    else:
        pass

    if write in interestsResponse: 
        print("\n")
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
        print("\n")
        print("Draw for 30 minutes. I will randomly choose a word for you, and you draw what comes to mind:")
        time.sleep(3)
        print("\n")
        print("Your prompt is:")
        print(random.choice(prompts))
        time.sleep(4)
        print("\n")
    else:
        pass

    if eat in interestsResponse:
        print("\n")
        print("I challenge you to create something knew.")
        time.sleep(2.5)
        print("What's something you've always wanted to try? Try to create a new meal out of the things you have at home!")
        time.sleep(4)
        print("\n")
    else:
        pass

    if dontKnow in interestsResponse:
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
        anotherActivityQ = raw_input("> ")
        anotherActivity = anotherActivityQ.upper()

        if yes in anotherActivity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            anotherActivity1Q = raw_input("> ")
            anotherActivity1 = anotherActivity1Q.upper()

            if yes in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif stopConnect in anotherActivity1:
                exit()
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
            anotherActivity1Q = raw_input("> ")
            anotherActivity1 = anotherActivity1Q.upper()

            if yes in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif stopConnect in anotherActivity1:
                exit()
            else: 
                pass
        elif stopConnect in anotherActivity:
            exit()
        else: 
            pass

    #or isnt working
    elif nothing in interestsResponse:
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
        anotherActivityQ = raw_input("> ")
        anotherActivity = anotherActivityQ.upper()

        if yes in anotherActivity:
            print("\n")
            print("I challenge you to:")
            time.sleep(2)
            print(random.choice(activities1))
            time.sleep(4)
            print("\n")

            print("Do you want another activity?")
            anotherActivity1Q = raw_input("> ")
            anotherActivity1 = anotherActivity1Q.upper()

            if yes in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif stopConnect in anotherActivity1:
                exit()
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
            anotherActivity1Q = raw_input("> ")
            anotherActivity1 = anotherActivity1Q.upper()

            if yes in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities2))
                time.sleep(4)
                print("\n")
            elif yea in anotherActivity1:
                print("\n")
                print("I challenge you to:")
                time.sleep(2)
                print(random.choice(activities1))
                time.sleep(4)
                print("\n")
            elif stopConnect in anotherActivity1:
                exit()
            else: 
                pass
        elif stopConnect in anotherActivity:
            exit()
        else: 
            pass
    elif stopConnect in interestsResponse:
        exit()
    else:
        pass


    if stopConnect in interestsResponse: 
        exit()
    else:
        pass

    if abuseWord in interestsResponse:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()
    else:
        pass

    if suicideWord in interestsResponse:
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

    if helpWord in interestsResponse:
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

def goodbye():
    print("\n")
    print("I hope you found the help you needed. You are an important part of this world. <3")
    time.sleep(2)
    print("\n")
    print("Goodbye!")
    print("\n")
    exit()

def checkRightGeneral():
    print("Was this information helpful, or would you like to keep talking?")
    checkRightGeneralResponse = raw_input("> ")
    checkRightGeneralAnswer = checkRightGeneralResponse.upper()
    
    if wasHelpful in checkRightGeneralAnswer:
        print("\n")
        print("I hope you found the help you needed. You are an important part of this world. <3")
        time.sleep(2)
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()
    elif isHelpful in checkRightGeneralAnswer:
        print("\n")
        print("I hope you found the help you needed. You are an important part of this world. <3")
        time.sleep(2)
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()
    elif yes in checkRightGeneralAnswer:
        print("I'm sorry, I didn't quite get that - would you like to continue talking?")
        generalCheckRightAgainQ = raw_input("> ")
        generalCheckRightAgain = generalCheckRightAgainQ.upper()

        if yes in generalCheckRightAgain:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

        elif yea in generalCheckRightAgain:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

        elif no in generalCheckRightAgain:
            print("\n")
            print("I hope you found the help you needed. You are an important part of this world. <3")
            time.sleep(2)
            print("\n")
            print("Goodbye!")
            print("\n")
            exit()

        elif abuseWord in generalCheckRightAgain:
            print("\n")
            domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif suicideWord in generalCheckRightAgain:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif helpWord in generalCheckRightAgain:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif stopConnect in generalCheckRightAgain:
            exit()

        else: 
            print("\n")
            print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
            time.sleep(4)
            print("\n")

    elif yea in checkRightGeneralAnswer:
        print("I'm sorry, I didn't quite get that - would you like to continue talking?")
        generalCheckRightAgain2Q = raw_input("> ")
        generalCheckRightAgain2 = generalCheckRightAgain2Q.upper()

        if yes in generalCheckRightAgain2:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

        elif yea in generalCheckRightAgain2:
            print("\n")
            print("Alright, we will continue to talk.")
            time.sleep(2)
            print("\n")

        elif no in generalCheckRightAgain2:
            print("\n")
            print("I hope you found the help you needed. You are an important part of this world. <3")
            time.sleep(2)
            print("\n")
            print("Goodbye!")
            print("\n")
            exit()

        elif abuseWord in generalCheckRightAgain2:
            print("\n")
            domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif suicideWord in generalCheckRightAgain2:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif helpWord in generalCheckRightAgain2:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif stopConnect in generalCheckRightAgain2:
            exit()
            
        else: 
            print("\n")
            print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
            time.sleep(4)
            print("\n")

    elif keepTalking in checkRightGeneralAnswer:
        print("\n")
        print("Alright, we will continue to talk.")
        time.sleep(2)
        print("\n")
    elif no in checkRightGeneralAnswer:
        print("\n")
        print("Alright, we will continue to talk.")
        time.sleep(2)
        print("\n")

    elif abuseWord in checkRightGeneralAnswer:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif suicideWord in checkRightGeneralAnswer:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif helpWord in checkRightGeneralAnswer:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif stopConnect in checkRightGeneralAnswer:
        exit()
    else: 
        print("\n")
        print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
        time.sleep(4)
        print("\n")

def checkRight():
    print("Was this information helpful, or would you like to keep talking?")
    checkRightResponse = raw_input("> ")
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

    elif abuseWord in checkRightAnswer:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif suicideWord in checkRightAnswer:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif helpWord in checkRightAnswer:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif stopConnect in checkRightAnswer:
        exit()
    else: 
        print("\n")
        print("I'm sorry, I didn't quite get that. We will continue to talk. Remember, if you would like to stop, type 'quit' at anytime.")
        time.sleep(4)
        print("\n")


#------------------------introduction
print("\n")
print("Welcome to CrisisConnect. I will be here to guide you through your crisis.")
time.sleep(3.75)
print("\n")
print("Throughout this process, I will ask simple questions that will help clear your mind and lead you to the right helpline.")
time.sleep(4.25)
print("\n")
print("If you want to stop talking, type and enter 'quit' at anytime.")
time.sleep(3.75)
print("\n")

#------------------------chat bot or coping mechanisms?
print("Would you like to find a hotline, or look at some coping mechanisms today?")
chatDecideQ = raw_input("> ")
chatDecide = chatDecideQ.upper()

if coping in chatDecide:

    breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    interestsFunction()

    goodbye()

elif cope in chatDecide:

    breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    interestsFunction()

    goodbye()

elif stopConnect in chatDecide:
    exit()

elif abuseWord in chatDecide:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in chatDecide:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in chatDecide:
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
    print("I'm glad you reached out for help. I will ask you some questions to help guide you to the correct hotline.")
    time.sleep(4.75)
    print("\n")
    pass

#----------------------------what is the situation - see what it can do with a description. 
print("What is your situation, and how are you feeling?")
generalSituationQ = raw_input("> ")
generalSituation = generalSituationQ.upper()


if stopConnect in generalSituation:
    exit()
elif mom in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()

    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel1Q = raw_input("> ")
        howFeel1 = howFeel1Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel1:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel1Q = raw_input("> ")
            generalCrisisYouthFeel1 = generalCrisisYouthFeel1Q.upper()

            if yes in generalCrisisYouthFeel1:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel1:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel1:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel1:
                exit()

            elif abuseWord in generalCrisisYouthFeel1:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel1:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel1:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif mother in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel2Q = raw_input("> ")
        howFeel2 = howFeel2Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel2:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel2Q = raw_input("> ")
            generalCrisisYouthFeel2 = generalCrisisYouthFeel2Q.upper()

            if yes in generalCrisisYouthFeel2:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel2:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel2:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel2:
                exit()

            elif abuseWord in generalCrisisYouthFeel2:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel2:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel2:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif father in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel3Q = raw_input("> ")
        howFeel3 = howFeel3Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel3:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel3Q = raw_input("> ")
            generalCrisisYouthFeel3 = generalCrisisYouthFeel3Q.upper()

            if yes in generalCrisisYouthFeel3:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel3:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel3:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel3:
                exit()

            elif abuseWord in generalCrisisYouthFeel3:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel3:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel3:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif grandma in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel4Q = raw_input("> ")
        howFeel4 = howFeel4Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel4:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel4Q = raw_input("> ")
            generalCrisisYouthFeel4 = generalCrisisYouthFeel4Q.upper()

            if yes in generalCrisisYouthFeel4:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel4:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel4:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel4:
                exit()

            elif abuseWord in generalCrisisYouthFeel4:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel4:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel4:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif grandpa in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel6Q = raw_input("> ")
        howFeel6 = howFeel6Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel6:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel6Q = raw_input("> ")
            generalCrisisYouthFeel6 = generalCrisisYouthFeel6Q.upper()

            if yes in generalCrisisYouthFeel6:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel6:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel6:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel6:
                exit()

            elif abuseWord in generalCrisisYouthFeel6:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel6:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel6:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif dad in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel7Q = raw_input("> ")
        howFeel7 = howFeel7Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel7:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel7Q = raw_input("> ")
            generalCrisisYouthFeel7 = generalCrisisYouthFeel7Q.upper()

            if yes in generalCrisisYouthFeel7:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel7:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel7:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel7:
                exit()

            elif abuseWord in generalCrisisYouthFeel7:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel7:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel7:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif sister in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel8Q = raw_input("> ")
        howFeel8 = howFeel8Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel8:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel8Q = raw_input("> ")
            generalCrisisYouthFeel8 = generalCrisisYouthFeel8Q.upper()

            if yes in generalCrisisYouthFeel8:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel8:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel8:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel8:
                exit()

            elif abuseWord in generalCrisisYouthFeel8:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel8:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel8:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif brother in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel9Q = raw_input("> ")
        howFeel9 = howFeel9Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel9:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel9Q = raw_input("> ")
            generalCrisisYouthFeel9 = generalCrisisYouthFeel9Q.upper()

            if yes in generalCrisisYouthFeel9:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel9:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel9:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel9:
                exit()

            elif abuseWord in generalCrisisYouthFeel9:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel9:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel9:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif wife in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel10Q = raw_input("> ")
        howFeel10 = howFeel10Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel1:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel10Q = raw_input("> ")
            generalCrisisYouthFeel10 = generalCrisisYouthFeel10Q.upper()

            if yes in generalCrisisYouthFeel10:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel10:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel10:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel10:
                exit()

            elif abuseWord in generalCrisisYouthFeel10:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel10:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel10:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif husband in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel11Q = raw_input("> ")
        howFeel11 = howFeel11Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel11:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel11Q = raw_input("> ")
            generalCrisisYouthFeel11 = generalCrisisYouthFeel11Q.upper()

            if yes in generalCrisisYouthFeel11:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel11:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel11:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel11:
                exit()

            elif abuseWord in generalCrisisYouthFeel11:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel11:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel11:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif spouse in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel12Q = raw_input("> ")
        howFeel12 = howFeel12Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel12:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel12Q = raw_input("> ")
            generalCrisisYouthFeel12 = generalCrisisYouthFeel12Q.upper()

            if yes in generalCrisisYouthFeel12:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel12:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel12:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel12:
                exit()

            elif abuseWord in generalCrisisYouthFeel12:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel12:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel12:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif body in generalSituation: 
    if hate in generalSituation:
        print("\n")
        eatingDisorderFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif gross in generalSituation:
        print("\n")
        eatingDisorderFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel13Q = raw_input("> ")
        howFeel13 = howFeel13Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel1:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel13Q = raw_input("> ")
            generalCrisisYouthFeel13 = generalCrisisYouthFeel13Q.upper()

            if yes in generalCrisisYouthFeel13:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel13:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel13:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel13:
                exit()

            elif abuseWord in generalCrisisYouthFeel13:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel13:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel13:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif family in generalSituation:
    if hurt or hit in generalSituation:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    elif touch or grope in generalSituation:
        print("\n")
        rainnFunction()
        print("\n")
        time.sleep(2)
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)

        checkRight()
        
    else: 
        print("\n")
        print("I'm sorry that's happening.")
        time.sleep(2)
        print("\n")
        print("How is this making you feel?")
        howFeel14Q = raw_input("> ")
        howFeel14 = howFeel14Q.upper()

        if sad or depressed or empty or numb or bad or useless in howFeel14:
            print("\n")
            print("Would you like to talk to another teen about your feelings?")
            generalCrisisYouthFeel14Q = raw_input("> ")
            generalCrisisYouthFeel14 = generalCrisisYouthFeel14Q.upper()

            if yes in generalCrisisYouthFeel14:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif yea in generalCrisisYouthFeel14:
                print("\n")
                youthLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif no in generalCrisisYouthFeel14:
                print("\n")
                namiFunction()
                time.sleep(2)
                print("\n")
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

            elif stopConnect in generalCrisisYouthFeel14:
                exit()

            elif abuseWord in generalCrisisYouthFeel14:
                print("\n")
                domesticAbuseFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif suicideWord in generalCrisisYouthFeel14:
                print("\n")
                immediateEmergencyFunction()
                print("\n")
                time.sleep(2)
                suicidePrevention()
                print("\n")
                time.sleep(2)

                checkRight()

            elif helpWord in generalCrisisYouthFeel14:
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
                textLineFunction()
                time.sleep(2)
                print("\n")

                checkRight()

        else:
            print("\n")
            print("I will ask you some yes or no questions to help guide you to the correct hotline.")
            time.sleep(4.75)
            print("\n")
            pass

elif grope or nonconsensual:
    print("\n")
    rainnFunction()
    print("\n")
    time.sleep(2)

    checkRight()

elif fat or wontEat or throwUp or cantEat in generalSituation: 
    print("\n")
    eatingDisorderFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif sad or depressed or empty or numb or bad or useless in generalSituation:
    print("\n")
    print("Would you like to talk to another teen about your feelings?")
    generalCrisisYouthFeel15Q = raw_input("> ")
    generalCrisisYouthFeel15 = generalCrisisYouthFeel15Q.upper()

    if yes in generalCrisisYouthFeel15:
        print("\n")
        youthLineFunction()
        time.sleep(2)
        print("\n")

        checkRight()

    elif yea in generalCrisisYouthFeel15:
        print("\n")
        youthLineFunction()
        time.sleep(2)
        print("\n")

        checkRight()

    elif no in generalCrisisYouthFeel15:
        print("\n")
        namiFunction()
        time.sleep(2)
        print("\n")
        textLineFunction()
        time.sleep(2)
        print("\n")

        checkRight()

    elif stopConnect in generalCrisisYouthFeel15:
        exit()

    elif abuseWord in generalCrisisYouthFeel15:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif suicideWord in generalCrisisYouthFeel15:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif helpWord in generalCrisisYouthFeel15:
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
        textLineFunction()
        time.sleep(2)
        print("\n")

        checkRight()

elif abuseWord in generalSituation:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in generalSituation:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in generalSituation:
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
    print("I'm sorry that's happening to you.")
    time.sleep(2)
    print("\n")
    print("I'll be asking some yes or no questions to help you to the best of my abilities.")
    time.sleep(2)
    print("\n")


#-------------------------------------are you in immediate danger?
print("Are you currently thinking about hurting yourself or others?")
emergencyQ = raw_input("> ")
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

elif abuseWord in immediateEmergency:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in immediateEmergency:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in immediateEmergency:
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
talkAloudQ = raw_input("> ")
talkAloud = talkAloudQ.upper()

if no in talkAloud:
    print("\n")
    cantTalk()
    print("\n")

    #check right

    print("Are you completely sure you still cannot talk aloud?")
    checkTalkAloudQ = raw_input("> ")
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

    elif abuseWord in checkTalkAloud:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif suicideWord in checkTalkAloud:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif helpWord in checkTalkAloud:
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

elif abuseWord in talkAloud:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in talkAloud:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in talkAloud:
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
safeEnvironmentQ = raw_input("> ")
safeEnvironment = safeEnvironmentQ.upper()

if no in safeEnvironment: 
    print("\n")
    print("Is a family member, romantic partner, or platonic partner causing you to be in danger?")
    domesticAbuseQ = raw_input("> ")
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
        abuseQ = raw_input("> ")
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
        
        elif abuseWord in abuse:
            print("\n")
            domesticAbuseFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif suicideWord in abuse:
            print("\n")
            immediateEmergencyFunction()
            print("\n")
            time.sleep(2)
            suicidePrevention()
            print("\n")
            time.sleep(2)

            checkRight()

        elif helpWord in abuse:
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
    
    elif abuseWord in domesticAbuse:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif suicideWord in domesticAbuse:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif helpWord in domesticAbuse:
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

elif abuseWord in safeEnvironment:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in safeEnvironment:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in safeEnvironment:
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
othersSafetyQ = raw_input("> ")
othersSafety = othersSafetyQ.upper()

if no in othersSafety:
    print("\n")
    pass

elif yes in othersSafety:
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

elif abuseWord in othersSafety:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in othersSafety:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in othersSafety:
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


#------------------------identity issues
print("Are you or someone you know dealing with any identity issues?")
identityIssuesQ = raw_input("> ")
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

elif abuseWord in identityIssues:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in identityIssues:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in identityIssues:
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
substanceAbuseQ = raw_input("> ")
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

elif abuseWord in substanceAbuse:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in substanceAbuse:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in substanceAbuse:
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
eatingDisorderQ = raw_input("> ")
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

elif abuseWord in eatingDisorder:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in eatingDisorder:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in eatingDisorder:
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
runawayQ = raw_input("> ")
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

elif abuseWord in runaway:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in runaway:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in runaway:
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
racialEquityQ = raw_input("> ")
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

elif abuseWord in racialEquity:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in racialEquity:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in racialEquity:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()


elif no in racialEquity:
    print("\n")
    pass

else: 
    print("\n")
    pass


#------------------------general crisis - asking emotions
print("How are you feeling right now?")
generalCrisisQ = raw_input("> ")
generalCrisis = generalCrisisQ.upper()

if sad or depressed or empty or numb or bad or useless in generalCrisis:
    print("\n")
    print("Would you like to talk to another teen about your feelings?")
    generalCrisisYouthQ = raw_input("> ")
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

    elif no in generalCrisisYouth:
        print("\n")
        namiFunction()
        time.sleep(2)
        print("\n")
        textLineFunction()
        time.sleep(2)
        print("\n")

        checkRight()

    elif stopConnect in generalCrisisYouth:
        exit()

    elif abuseWord in generalCrisisYouth:
        print("\n")
        domesticAbuseFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif suicideWord in generalCrisisYouth:
        print("\n")
        immediateEmergencyFunction()
        print("\n")
        time.sleep(2)
        suicidePrevention()
        print("\n")
        time.sleep(2)

        checkRight()

    elif helpWord in generalCrisisYouth:
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
        textLineFunction()
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

elif abuseWord in generalCrisis:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in generalCrisis:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in generalCrisis:
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
feelingOverallQ = raw_input("> ")
feelingOverall = feelingOverallQ.upper()

if yes in feelingOverall:
    #------------------------final support/coping mechanisms
    print("\n")
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
    print("\n")
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

elif stopConnect in feelingOverall:
    exit()

elif abuseWord in feelingOverall:
    print("\n")
    domesticAbuseFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif suicideWord in feelingOverall:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

elif helpWord in feelingOverall:
    print("\n")
    immediateEmergencyFunction()
    print("\n")
    time.sleep(2)
    suicidePrevention()
    print("\n")
    time.sleep(2)

    checkRight()

else:
    print("Before you go, let's walk through some coping mechanisms.")
    time.sleep(3)

    breathingExercise478()

    print("It isn't selfish to do things you love when you aren't feeling good.")
    time.sleep(2)
    print("\n")

    interestsFunction()

    goodbye()
