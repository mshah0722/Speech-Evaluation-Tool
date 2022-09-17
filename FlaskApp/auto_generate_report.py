# importing all necessary modules
import cohere
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

_text = "Facial Expression Score: 8/10\nTonal Expressions Score: 5/10\nContent Score: 2/10"
_key = os.getenv('api_key')

def generateEvaluation(_text):
    
    co = cohere.Client(_key)

    _prompt='This program will generate an evaluation from the scores. Here are some examples:\n\nScore: \nFacial Expression Score: 7/10\nTonal Expressions Score: 3/10\nContent Score: 9/10\n\nExtracted Text:\nEvaluation: The content is clear and understandable. It covers relevant topics. You are expressive and engaging. However, tonal expressions are poor and require improvement.  \n--\nScore: \nFacial Expression Score: 10/10\nTonal Expressions Score: 10/10\nContent Score: 10/10\n\nExtracted Text: \nEvaluation: You are an excellent tutor. The lessons are engaging and clear. The quality of the content is amazing. \n--\nScore:\nFacial Expression Score: 8/10\nTonal Expressions Score: 8/10\nContent Score: 0/10\n\nExtracted Text: \nEvaluation: The facial expressions and tone displays passion and interest for tutoring, but need to work on the content. The content is not understandable.\n--\nScore:\nFacial Expression Score: 3/10\nTonal Expressions Score: 5/10\nContent Score: 2/10\n\nExtracted Text: \nEvaluation: Your session requires work. Content has to be improved. Facial Expressions are also bad.\n--\nScore:\nFacial Expression Score: 6/10\nTonal Expressions Score: 7/10\nContent Score: 8/10\n\nExtracted Text:\nEvaluation: You need to work on your confidence and focus. Good job with the content. \n--\nScore:\nFacial Expression Score: 9/10\nTonal Expressions Score: 9/10\nContent Score: 8/10\n\nExtracted Text:\nEvaluation: Brilliant! The mentor picks positive traits of the tutors. However, there are still room for improvement. \n--\nScore:\nFacial Expression Score: 7/10\nTonal Expressions Score: 7/10\nContent Score: 4/10\n\nExtracted Text:\nEvaluation: The passion and commitment is shown by the tutor. However, the voice fluctuates up and down a bit. There are opportunities for improvement on the content. \n--\nScore:\nFacial Expression Score: 5/10\nTonal Expressions Score: 5/10\nContent Score: 5/10\n\nExtracted Text:\nEvaluation: This session is a bit quiet. The tutor can work on his enthusiasm, facial expressions, vocal range, and content. \n--\nScore:\nFacial Expression Score: 10/10\nTonal Expressions Score: 10/10\nContent Score: 10/10\n\nExtracted Text:\nEvaluation: The tutor has done a great job. The tutor fulfilled the session request by demonstrating key conversation strategies.\n--\nScore:\nFacial Expression Score: 9/10\nTonal Expressions Score: 10/10\nContent Score: 2/10\n\nExtracted Text:\nEvaluation: The tutor has done well. Please do work on the content.\n--\nScore:\n'
    _prompt = _prompt + _text + "\n\nExtracted Text:\nEvaluation:"
    print(_prompt)

    response = co.generate(
    model='xlarge',
    prompt=_prompt,
    max_tokens=30,
    temperature=1,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=["--"],
    return_likelihoods='NONE')
    print('Evaluation: {}'.format(response.generations[0].text))

generateEvaluation(_text)

