mysp=__import__("my-voice-analysis")
                     
p="Pitch1" # Audio File title
c=r"/Users/malharshah/Desktop/Speech-Evaluation-Tool/SpeechAPI/wav" # Path to the Audio_File directory

#Gender recognition and mood of speech
myspgend = str(mysp.myspgend(p,c))
gender, speech_mood, p_value_ratio = myspgend.split(", ")

#Pronunciation posteriori probability score percentage
pronunciation_score = str(mysp.mysppron(p,c))

#Detect and count number of syllables
syllables_count = str(mysp.myspsyl(p,c))

#Detect and count number of fillers and pauses
filler_pause_count = str(mysp.mysppaus(p,c))

#Measure the rate of speech (speed)
#Syllables/sec original duration
speech_speed = str(mysp.myspsr(p,c))

#Measure the articulation (speed)
#Syllables/sec speaking duration
articulation_rating = str(mysp.myspatc(p,c))

#Measure speaking time (excl. fillers and pause)
#Sec only speaking duration without pauses
total_speech_time = str(mysp.myspst(p,c))

#Ratio (speaking duration)/(original duration)
speaking_ratio = str(mysp.myspbala(p,c))

#Store the processed input for the cohere api here
speechProcessedInput = speech_mood + "\n" + pronunciation_score + "\n" + filler_pause_count + "\n" + speech_speed + "\n" + speaking_ratio

print(speechProcessedInput)
#