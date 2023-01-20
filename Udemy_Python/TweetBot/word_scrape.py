import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H%M")

print(current_time)

negative_words = ['appalling', 'atrocious', 'abominable', 'deplorable', 'despicable', 'dreadful', 'enraged', 'harmful', 
'hurtful', 'insidious', 'malicious', 'offensive', 'poisonous', 'sinister', 'shocking', 'pleasant', 'vindictive', 
'aggressive', 'barbarous', 'cantankerous', 'choleric', 'craven', 'deceitful', 'detestable', 'dishonorable', 'egotistical', 
'gauche', 'harsh', 'hostile', 'inhumane', 'irascible', 'narcissistic', 'obnoxious', 'ornery', 'pitiless', 'ruthless', 
'saturnine', 'treacherous', 'vicious', 'arrogant', 'avaricious', 'belligerent', 'boorish', 'churlish', 'crotchety', 'crude', 
'curmudgeonly', 'dour', 'duplicitous', 'grim', 'gross', 'implacable', 'miserly', 'morose', 'nasty', 'notorious', 'pompous', 
'quarrelsome', 'savage', 'selfish', 'vainglorious', 'vile', 'vulgar', 'abysmal', 'adverse', 'alarming', 'angry', 'annoy', 
'anxious', 'apathy', 'awful', 'bad', 'banal', 'barbed', 'bemoan', 'beneath', 'boring', 'broken', 'callous', 'clumsy', 
'coarse', 'cold', 'collapse', 'confused', 'contradictory', 'contrary', 'corrosive', 'corrupt', 'coward', 'crazy', 'creep', 
'criminal', 'cruel', 'cry', 'cutting', 'damage', 'dastardly', 'dead', 'decay', 'deform', 'deny', 'depressed', 'deprived', 
'detrimental', 'dirty', 'disease', 'disgusting', 'disheveled', 'dishonest', 'dismal', 'distress', 'dreary', 'erode', 'evil', 
'fail', 'fat', 'faulty', 'fear', 'feeble', 'fight', 'filthy', 'foul', 'frighten', 'frightfully', 'gawky', 'ghastly', 
'grave', 'greed', 'grimace', 'grotesque', 'gruesome', 'guilty', 'haggard', 'hard', 'hate', 'hideous', 'homely', 'horrendous', 
'horrible', 'hurt', 'icky', 'idiot', 'ignorant', 'ignore', 'ill', 'immature', 'imperfect', 'impossible', 'inane', 
'inelegant', 'infernal', 'injure', 'injurious', 'insane', 'insipid', 'jealous', 'junky', 'kill', 'life', 'lose', 'louse', 
'lump', 'mean', 'menacing', 'messy', 'misshapen', 'missing', 'misunderstood', 'moan', 'moldy', 'monstrous', 'moron', 'naive', 
'naughty', 'negate', 'negative', 'never', 'no', 'nobody', 'nondescript', 'nonsense', 'not', 'noxious', 'objectionable', 
'odious', 'old', 'oppressive', 'pain', 'perturb', 'pessimistic', 'petty', 'pity', 'plain', 'poor', 'prejudice', 
'questionable', 'quirky', 'quit', 'reject', 'renege', 'repellant', 'reptilian', 'repugnant', 'repulsive', 'revenge', 
'revolting', 'rocky', 'rotten', 'rude', 'sad', 'scare', 'scary', 'scream', 'severe', 'shoddy', 'sick', 'sickening', 'slimy', 
'smelly', 'sob', 'sorry', 'spiteful', 'stab', 'sticky', 'stink', 'stormy', 'stressful', 'stuck', 'stupid', 'substandard', 
'suspect', 'suspicious', 'tense', 'terrible', 'terrify', 'threaten', 'torture', 'ugly', 'undermine', 'fair', 'favorable', 
'unhappy', 'healthy', 'unintelligent', 'unjust', 'unlucky', 'satisfactory', 'unsightly', 'untoward', 'unwanted', 'unwelcome', 
'wholesome', 'unwieldy', 'wise', 'upset', 'vice', 'villainous', 'wary', 'weary', 'wicked', 'woeful', 'worthless', 'wound', 
'yell', 'yucky', 'zero']


# driver = webdriver.Firefox()
# driver.get("https://www.vocabulary.com/lists/2606724")
# driver.set_window_size(1280, 1440)


# time.sleep(2)
# words = []

# definitions = driver. find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section[2]/ol/li/a")

# for word in definitions:
#     if word.text not in negative_words:
#         negative_words.append(word.text)
#         print(word.text)



# print(negative_words)



