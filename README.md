# Speech-Evaluation-Tool

## What it does
1. Instant multimodal feedback for speakers to help improve their presentation skills: Giving presentations, speeches or awesome elevator pitches can often be a daunting task. By getting instant feedback on their presentations, speakers can either practice long stretches at once or complete crucial last-minute preparation for that pitch. Using a congregation of NLP, image and audio processing tools, our software provides instant feedback to the speakers and helps them improve their presentation in three different aspects, namely expressions, tone, and content.

2. Help speakers be more expressive and engaging: We use TensorFlow library, which uses its eye tracking and sentiment analysis capabilities to measure the speaker's engagement. The software helps the speaker feel more natural with their facial expressions and eye-movement during important presentations.

3. Provide feedback to make speakers sound more confident and relaxed: Several metrics such as the pace of speaking, number of pauses & usage of filler words, and pronunciation score can indicate the quality of a presentation. We use audio processing APIs to extract the relevant metrics and use Cohere’s generative model to analyze metrics to present personalized actionable methods of improvement in a concise manner.

4. Making sure that the content is on-point and free of unfavourable speech patterns: Using Cohere’s API for Topic extraction and content summarization, our software highlights the main ideas that are being put forward in your presentation. Our software is also able to detect speech patterns which are unfavourable during presentations. For example, we detect persistent repetition of the same ideas using cohere’s semantic search model.

## Technologies Used
**Front-end development**: React, Javascript  
**Back-end development**: Python with Flask
**Image Processing**: Tensor-flow  
**Audio Processing**: AssemblyAI API, My-Voice-Analysis API Built upon Praatscript based library  
**Natural Language Processing**: Cohere API  

## How it works
User selects a speech video they want to analyze. Instantly, TensorFlow library uses eye tracking and sentiment analysis capabilities to measure the speaker's engagement. Next, the video is transcribed using Assembly-API. The text is used by Cohere's API for analysis such as speech summarization and topic extraction. Then, My-Voice-Analysis is used to extract key metrics such as speech mood, pace, and clarity. Finally, Cohere's API is utilized again for overall analysis and to provide actionable feedback.

## Devpost Link
https://devpost.com/software/oratorme
