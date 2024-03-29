# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate




#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def is_phrase_in(self, phrase, text):
        phrase = phrase.lower()
        phrasewords_list = phrase.split()
        phrase_length = len(phrasewords_list)
        text = text.lower()
        for letter in text:
            if letter not in string.ascii_lowercase:
                text = text.replace(letter,' ',1)
        textwords_list = text.split()
        for word in textwords_list:
            i = textwords_list.index(word)
            if word == phrasewords_list[0] and i + phrase_length <= len(textwords_list):
                try:
                    textwords_sliced = textwords_list[i:i+phrase_length]
                except:
                    print("can't slice a list like this [:]")
                if textwords_sliced == phrasewords_list:
                    return True
        return False

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self,story):
        return PhraseTrigger.is_phrase_in(self,self.phrase,story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self,story):
        return PhraseTrigger.is_phrase_in(self,self.phrase,story.get_description())        

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self,dt_string):
        dt = datetime.strptime(dt_string,"%d %b %Y %H:%M:%S")
        self.dt = dt 
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate().tzinfo != None:
            self.dt = self.dt.replace(tzinfo = pytz.timezone("EST"))            
        if self.dt < story.get_pubdate():
            return False
        return True

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate().tzinfo != None:
            self.dt = self.dt.replace(tzinfo = pytz.timezone("EST"))            
        if self.dt < story.get_pubdate():
            return True
        return False
        

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, t):
        self.trigger = t
    def evaluate(self, x):
        result = not (self.trigger.evaluate(x))
        return result

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    def evaluate(self, story):
        if self.t1.evaluate(story) and self.t2.evaluate(story):
            return True
        else:
            return False

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
    def evaluate(self, story):
        if self.t1.evaluate(story) or self.t2.evaluate(story):
            return True
        else:
            return False


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    list_filter_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                list_filter_stories.append(story)
                break
    return list_filter_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    list_triggers = []
    dict_stored_triggers = {}
    dict_triggers = {'TITLE':TitleTrigger, 'DESCRIPTION':DescriptionTrigger, 
    'AFTER':AfterTrigger, 'BEFORE':BeforeTrigger, 'NOT':NotTrigger, 'AND':AndTrigger, 
    'OR':OrTrigger}
    for line in lines:
        line_words = line.split(',')
        if line_words[0] != 'ADD':
            if len(line_words) == 3 and line_words[1] != 'NOT':
                t = dict_triggers[line_words[1]](line_words[2])
            if line_words[1] == 'NOT':
                t = dict_triggers[line_words[1]](dict_stored_triggers[line_words[2]])
            if len(line_words) == 4:
                t = dict_triggers[line_words[1]](dict_stored_triggers[line_words[2]],dict_stored_triggers[line_words[3]])
            dict_stored_triggers[line_words[0]] = t
        else:
            for i in range(1, len(line_words)):
                list_triggers.append(dict_stored_triggers[line_words[i]])
    return list_triggers
               





SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")



            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

