mysp=__import__("my-voice-analysis")
                     
p="Pitch1" # Audio File title
c=r"C:\\Users\\lenovo\\Desktop\\HTN\\Speech-Evaluation-Tool\\FlaskApp\\assets" # Path to the Audio_File directory

#Store the processed input for the speech here
speechProcessedInput = ""

#Gender recognition and mood of speech
speechProcessedInput = (speechProcessedInput + str(mysp.myspgend(p,c)) + "\n")

print(speechProcessedInput)

#Pronunciation posteriori probability score percentage
speechProcessedInput = (speechProcessedInput + str(mysp.mysppron(p,c)) + "\n")

#Detect and count number of syllables
speechProcessedInput = (speechProcessedInput + str(mysp.myspsyl(p,c)) + "\n")

#Detect and count number of fillers and pauses
speechProcessedInput = (speechProcessedInput + str(mysp.mysppaus(p,c)) + "\n")

#Measure the rate of speech (speed)
speechProcessedInput = (speechProcessedInput + str(mysp.myspsr(p,c)) + "\n")

#Measure the articulation (speed)
speechProcessedInput = (speechProcessedInput + str(mysp.myspatc(p,c))+ "\n")

#Measure speaking time (excl. fillers and pause)
speechProcessedInput = (speechProcessedInput + str(mysp.myspst(p,c)) + "\n")

#

print(speechProcessedInput)
#