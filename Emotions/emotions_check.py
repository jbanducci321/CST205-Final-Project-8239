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

#Emotional groupings for simplifying final decision logic
positive_emotions = {"joy", "trust", "anticipation", "positive"}
negative_emotions = {"anger", "fear", "sadness", "disgust", "negative"}
mixed_emotions = {"surprise"}

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

#Takes a sentence and detects emotional sentiment of that sentence
def detect_emotion(text):
    scores = emotion_scores.copy() #Creates a copy of the score dictionary
    
    #Creates sets to store individual words
    positive_words = set()
    negative_words = set()
    mixed_words = set()
    
    #Removes punctuation and splits a sentence into individual words
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

    #Loops through each word to collect total emotion scores also tracks which words matched
    for word in words:
        for emotion, word_set in emotion_word_sets.items():
            if word in word_set:
                scores[emotion] += 1 #If the word is found then the related emotion score is incremented
                
                #Track which group the matched word came from
                if emotion in positive_emotions:
                    positive_words.add(word)
                elif emotion in negative_emotions:
                    negative_words.add(word)
                elif emotion in mixed_emotions:
                    mixed_words.add(word)

    
    #Handles cases with 0 emotion score (neutral emotion)
    if all(score == 0 for score in scores.values()):
        return f"The emotion is neutral"
    
    #Gets the top scoring emotions
    max_score = max(scores.values()) #Stores the highest number of the emotion count
    #Stores all emotions that have the max score in top_emotions
    top_emotions = [emotion for emotion,score in scores.items() if score == max_score]
    
    #If there is a single top emotion then it is immediately returned
    if len(top_emotions) == 1:
        return f'The emotion of the sentence is {top_emotions[0]}'
    
    #Collects word counts for the different groups
    postive_word_count = len(positive_words)
    negative_word_count = len(negative_words)
    
    #Handles surprised words (surprise words have mixed emotional spread)
    if mixed_words and not positive_words and not negative_words:
        if len(mixed_words) == 1:
            return f'The emotion of the sentence is surprised'
        else:
            return f'The emotions of the sentence is surprised (context-dependent)'
    
    #Lean negative if there is a tie between positive and negative emotions
    if negative_word_count >= postive_word_count:
        top_emotions = [e for e in scores if scores[e] > 0 and e in negative_emotions]
        return f"The emotion(s) of the sentence are: {', '.join(top_emotions)}"
    elif postive_word_count > negative_word_count:
        top_emotions = [e for e in scores if scores[e] > 0 and e in positive_emotions]
        return f"The emotion(s) of the sentence are: {', '.join(top_emotions)}"
    else:
        return f"The emotions of the sentence are {', '.join(top_emotions)}"
    

def main():
    inputText = input("Enter a sentence: ")
    print(detect_emotion(inputText))

if __name__ == "__main__":
    main()