# importing all necessary modules
import cohere
import os
from dotenv import load_dotenv


def configure():
    load_dotenv()


configure()

_text = "If you’re trying to get yourself acquainted with the field of computer science and the tech world at large, it doesn’t take long to start feeling a little bit buried by the huge number of unfamiliar terms, acronyms and jargon used. Instead of getting flustered reading about the latest Agile Django bootstrapped platform or whatever it may be and having zero clue what they actually are, let’s take a step back and get familiar with some of the foundational computer science and tech terms you’ll likely encounter. Keep in mind, this list of computer science terms and definitions should serve more as a clarifying starting point. Much of what’s covered below will take further reading and learning to fully grasp what they are and how they’re used. Like with learning any new subject, you’ll want to take this step and get acquainted with the terminology before navigating the more complex concepts."
_key = os.getenv('api_key')


def importantTopicsFromText(_text):

    co = cohere.Client(_key)

    _prompt = 'This program will extract relevant topics from text. Here are some examples:\
            \n\nText: Android is an Open source, Linux-based software stack created for a wide array of devices and form factors. The following diagram shows the major components of the Android platform. The foundation of the Android platform is the Linux kernel. For example, the Android Runtime (ART) relies on the Linux kernel for underlying functionalities such as threading and low-level memory management. Prior to Android version 5.0 (API level 21), Dalvik was the Android runtime. If your app runs well on ART, then it should work on Dalvik as well, but the reverse may not be true.\n\n\
            Extracted Text:\nTopics: Android, Open source, Linux, Dalvik\
            \n--\nText: Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python. Python source code and installers are available for download for all versions! Documentation for Python\'s standard library, along with tutorials and guides, are available online. Looking for work or have a Python related position that you\'re trying to hire for? Our relaunched community-run job board is the place to go.\
            \n\nExtracted Text:\nTopics: Python, Python programming, Python source code, Tutorial, Job\n--\n\
            Text: An algorithm is a procedure used for solving a problem or performing a computation. Algorithms act as an exact list of instructions that conduct specified actions step by step in either hardware- or software-based routines. Algorithms are widely used throughout all areas of IT. An algorithm could be used for sorting sets of numbers or for more complicated tasks, like recommending user content on social media. Algorithms typically start with initial input and instructions that describe a specific computation. When the computation is executed, the process produces an output.\
            \n\nExtracted Text:\nTopics: Algorithms, Sorting, Computer science, IT, IT careers\n--\nText:'
    _prompt = _prompt + _text + "\n\nExtracted Text:\nTopics:"
    # print(_prompt)

    response = co.generate(
        model='large',
        prompt=_prompt,
        max_tokens=20,
        temperature=0.5,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    topics = response.generations[0].text.split(',')
    topics = [t.strip().lower() for t in topics]

    _topicDict = {}
    for i in range(len(topics)):
        _topicDict[i] = topics[i]

    print(_topicDict)
    return _topicDict
