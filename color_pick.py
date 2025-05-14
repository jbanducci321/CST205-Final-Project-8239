'''Title: Emotion Color Picker
CST-205
Takes a string input and uses the emolex to pick an appropriate background color for the collage
Worked on by: Jacob Banducci
5/11/2025'''

import random

#Defines emotion categories to help with sorting
positive_emotions = {"joy", "trust", "anticipation", "positive"}
negative_emotions = {"anger", "fear", "sadness", "disgust", "negative"}
mixed_emotions = {"surprise"}

#Defines colors for each emotion in the emolex
emotion_colors = {
    "anger": (220, 20, 60),
    "anticipation": (255, 215, 0),
    "disgust": (85, 107, 47),
    "fear": (128, 0, 128),
    "joy": (255, 200, 100),
    "sadness": (100, 149, 237),
    "surprise": (255, 255, 102),
    "trust": (144, 238, 144),
    "neutral": (200, 200, 200)
}

#Loads each of the emolex word sets
emotion_word_sets = {}
file_prefix = "OneFilePerEmotion/"
emotion_files = {
    "anger": "anger-NRC-Emotion-Lexicon.txt",
    "anticipation": "anticipation-NRC-Emotion-Lexicon.txt",
    "disgust": "disgust-NRC-Emotion-Lexicon.txt",
    "fear": "fear-NRC-Emotion-Lexicon.txt",
    "joy": "joy-NRC-Emotion-Lexicon.txt",
    "negative": "negative-NRC-Emotion-Lexicon.txt",
    "positive": "positive-NRC-Emotion-Lexicon.txt",
    "sadness": "sadness-NRC-Emotion-Lexicon.txt",
    "surprise": "surprise-NRC-Emotion-Lexicon.txt",
    "trust": "trust-NRC-Emotion-Lexicon.txt"
}

#Creates a dictioanry with sets of words associated with a given emotion
for emotion, filename in emotion_files.items():
    with open(file_prefix + filename, 'r') as f:
        words = {line.split('\t')[0] for line in f if line.strip().endswith('1')}
        emotion_word_sets[emotion] = words

def get_emotion_color(emotion):

    #Checks if the passed word is in any of the emolex sets and stores them in a list
    matched_emotions = [emo for emo, word_set in emotion_word_sets.items() if emotion in word_set]
    
    #If the list is empty then the emotion is considered neutral
    if not matched_emotions:
        return emotion_colors["neutral"]

    #Check if the word is in the positive or negative sets
    is_positive = any(e in positive_emotions for e in matched_emotions)
    is_negative = any(e in negative_emotions for e in matched_emotions)

    #If a word is both positive and negative then it is considered positive
    if is_positive and is_negative:
        return emotion_colors["neutral"]

    #Filters out general positive/negative labels and focuses on specific ones
    specific_emotions = [emo for emo in matched_emotions if emo in emotion_colors]

    #Will randomly select one of the associated emotions for a word and then returns the color
    if specific_emotions:
        selected_emotion = random.choice(specific_emotions)
        return emotion_colors[selected_emotion]

    #If all else fails then neutral color is returned
    return emotion_colors["neutral"]