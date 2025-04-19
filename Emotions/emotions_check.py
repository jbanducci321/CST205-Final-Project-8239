import string #Removes punctuation from the input text

#Creates a dictioanry to track the main emotion values in the emolex (initializes each one to 0)
emotion_scores = {
    "anger": 0,
    "anticipation": 0,
    "disgust": 0,
    "fear": 0,
    "joy": 0,
    "negative": 0,
    "positive": 0,
    "sadness": 0,
    "surprise": 0,
    "trust": 0
}

#Creates a dictionary to hold the emotion word set for each emotion
emotion_word_sets = {}

#Defines the emotion and the file path for the emotion's emolex
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

#Loops through each file and stores the words with a score of 1 into a set
for emotion, filename in emotion_files.items():
    with open(f"Emotions/OneFilePerEmotion/{filename}", 'r') as file:
        words = {line.split('\t')[0] for line in file if line.strip().endswith('1')}
        emotion_word_sets[emotion] = words

#Takes a sentence and detects emotions of that sentence
def detect_emotion(text):
    scores = emotion_scores.copy() #Creates a copy of the score dictionary
    
    #Removes punctuation and splits a sentence into individual words
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

    #Loops through each word to check if it is in any emotion set
    for word in words:
        for emotion, word_set in emotion_word_sets.items():
            if word in word_set:
                scores[emotion] += 1 #If the word is foudn then the related emotion score is incremented

    #Finds the emotion(s) with the top score
    max_score = max(scores.values())
    
    #If no word mathces were found, the emotion is regarded as neutral
    if max_score == 0:
        return f"The emotion is neutral"
    
    #Colelcts and stores all emotions with a top score into a list
    top_emotions = [emotion for emotion, score in scores.items() if score == max_score]

    #Evaluates if there was a tie between emotions and returs the top ones
    if len(top_emotions) == 1:
        return f'The emotion of the sentence is {top_emotions[0]}'
    else:
        return f"The emotions of the sentence are {', '.join(top_emotions)}"

def main():
    inputText = input("Enter a sentence: ")
    print(detect_emotion(inputText))

if __name__ == "__main__":
    main()