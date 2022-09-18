from dotenv import load_dotenv
import cohere
import os

def configure():
    load_dotenv()

def main():
    configure()
    input = ''
    prompt='Input:\nSpeech Mood: Speaking passionately\nPronunciation Posteriori Probability Score Percentage = 94.91\nNumber of Fillers and Pauses = 11\nRate of Speech = 4\nRatio of speaking time to total time = 0.8\n\nOutput:\nPerfect Speech Mood. \nPerfect Pronunciation Score.\nLow Number of Fillers and Pauses.\nPerfect Rate of Speech.\nPerfect Ratio of speaking time to total time.\nAmazing pitch. \nNo improvement needed.\n\n--\nInput:\nSpeech Mood: Reading\nPronunciation Posteriori Probability Score Percentage = 92\nNumber of Fillers and Pauses = 30\nRate of Speech = 4\nRatio of speaking time to total time = 0.6\n\nOutput:\nYou used a Reading Speed Mood. Aim to speak more passionately.\nPerfect Pronunciation Score.\nYou used 30 fillers and pauses while presenting. Aim to user less filler words and pauses.\nPerfect Rate of Speech.\nLow Ratio of speaking time to total time. Aim to speak more during pitch.\nAverage pitch.\nImprovement needed.\n\n--\nInput:\nSpeech Mood: Reading\nPronunciation Posteriori Probability Score Percentage = 70\nNumber of Fillers and Pauses = 50\nRate of Speech = 2\nRatio of speaking time to total time = 0.4\n\nOutput:\nYou used a Reading Speed Mood. Aim to speak more passionately.\nLow Pronunciation Score. Try to pronounce more clearly.\nYou used 50 fillers and pauses while presenting. Aim to user less filler words and pauses.\nLow Rate of Speech. Speak faster.\nLow Ratio of speaking time to total time. Aim to speak more during pitch.\nBad pitch.\nImprovement needed.\n\n--\nInput:\nSpeech Mood: Speaking passionately\nPronunciation Posteriori Probability Score Percentage = 85\nNumber of Fillers and Pauses = 40\nRate of Speech = 3\nRatio of speaking time to total time = 0.75\n\nOutput:\nPerfect Speech Mood. \nPerfect Pronunciation Score.\nYou used 40 fillers and pauses while presenting. Aim to user less filler words and pauses.\nPerfect Rate of Speech.\nPerfect Ratio of speaking time to total time.\nGreat pitch. \nImprovement needed.\n\n--\nInput:\nSpeech Mood: Speaking passionately\nPronunciation Posteriori Probability Score Percentage = 90\nNumber of Fillers and Pauses = 11\nRate of Speech = 2\nRatio of speaking time to total time = 0.5\n\nOutput:\nPerfect Speech Mood. \nPerfect Pronunciation Score.\nLow Number of Fillers and Pauses.\nLow Rate of Speech. Speak faster.\nLow Ratio of speaking time to total time. Aim to speak more during pitch.\nAverage pitch. \nImprovement needed.\n\n--\nInput:\nSpeech Mood: Speaking passionately\nPronunciation Posteriori Probability Score Percentage = 96\nNumber of Fillers and Pauses = 30\nRate of Speech = 4\nRatio of speaking time to total time = 0.6\n\nOutput:\nPerfect Speech Mood. \nPerfect Pronunciation Score.\nYou used 30 fillers and pauses while presenting. Aim to user less filler words and pauses.\nPerfect Rate of Speech.\nLow Ratio of speaking time to total time. Aim to speak more during pitch.\nAverage pitch. \nImprovement needed.\n\n--\nInput:\nSpeech Mood: Speaking passionately\nPronunciation Posteriori Probability Score Percentage = 97\nNumber of Fillers and Pauses = 11\nRate of Speech = 2\nRatio of speaking time to total time = 0.5\n\nOutput:\nPerfect Speech Mood. \nPerfect Pronunciation Score.\nYou used 11 fillers and pauses while presenting. Aim to user less filler words and pauses.\nLow Rate of Speech. Speak faster.\nLow Ratio of speaking time to total time. Aim to speak more during pitch.\nAverage pitch. \nImprovement needed.\n\n--'
    co = cohere.Client(os.getenv('api_key'))
    response = co.generate(
        model='xlarge',
        prompt=prompt+input,
        max_tokens=135,
        temperature=0.3,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))

main()