#!/usr/bin/env python3
"""
Comprehensive test sentences for emotion classification model verification
"""

# Test sentences organized by emotion category
TEST_SENTENCES = {
    "joy": [
        "I feel absolutely wonderful and excited about this amazing opportunity!",
        "This is the best day of my life, I'm so happy!",
        "I'm thrilled to celebrate this incredible achievement with everyone!",
        "What a fantastic surprise, I'm overjoyed!",
        "I feel like I'm on top of the world right now!",
        "This brings me so much happiness and delight!",
        "I'm bursting with joy and enthusiasm!",
        "Life is beautiful and I feel amazing today!",
        "I'm so grateful and blessed, this makes me incredibly happy!",
        "I can't stop smiling, this is absolutely wonderful!"
    ],
    
    "sadness": [
        "I feel so lonely and heartbroken right now.",
        "This devastating news has left me completely shattered.",
        "I'm overwhelmed with grief and sorrow.",
        "I feel empty and hopeless about everything.",
        "The loss has left me feeling deeply sad and lost.",
        "I'm crying because I feel so disappointed and hurt.",
        "This melancholy feeling won't go away.",
        "I feel abandoned and forgotten by everyone.",
        "The pain in my heart is unbearable.",
        "I'm drowning in sadness and despair."
    ],
    
    "anger": [
        "I'm absolutely furious about this unfair treatment!",
        "This makes me so angry and frustrated!",
        "I'm outraged by this completely unacceptable behavior!",
        "I'm livid and can't believe how badly this was handled!",
        "This injustice makes my blood boil!",
        "I'm fed up with these constant problems and delays!",
        "I'm enraged by their disrespectful attitude!",
        "This situation is infuriating and completely wrong!",
        "I'm burning with anger over this betrayal!",
        "I'm absolutely mad about these ridiculous rules!"
    ],
    
    "fear": [
        "I'm terrified of what might happen next.",
        "This situation fills me with dread and anxiety.",
        "I'm scared and worried about the future.",
        "I feel paralyzed by fear and uncertainty.",
        "This gives me chills and makes me very nervous.",
        "I'm frightened by the thought of failure.",
        "I'm trembling with fear about this dangerous situation.",
        "I'm panicking and don't know what to do.",
        "This nightmare scenario keeps me awake at night.",
        "I'm petrified and can't stop worrying about it."
    ],
    
    "surprise": [
        "I can't believe this incredible news, what a shock!",
        "This unexpected turn of events has left me speechless!",
        "I'm amazed and completely caught off guard!",
        "What a stunning revelation, I never saw this coming!",
        "This is so surprising, I'm absolutely astonished!",
        "I'm flabbergasted by this sudden development!",
        "This twist has left me in complete disbelief!",
        "I'm shocked and amazed by this incredible discovery!",
        "This came out of nowhere, what a surprise!",
        "I'm stunned by this unexpected announcement!"
    ],
    
    "love": [
        "I love spending quality time with my family and friends.",
        "My heart is full of love and affection for you.",
        "I cherish every moment we share together.",
        "I'm deeply in love and feel so connected to you.",
        "I adore everything about this beautiful relationship.",
        "My love for you grows stronger every single day.",
        "I feel so much warmth and love in my heart.",
        "I'm passionate about the people I care about most.",
        "This fills my heart with pure love and joy.",
        "I'm devoted to you and treasure our bond together."
    ]
}

# Mixed/ambiguous sentences for testing edge cases
MIXED_SENTENCES = [
    "I'm happy but also worried about the future.",
    "This news is shocking but also makes me sad.",
    "I love you but I'm angry about what happened.",
    "I'm excited but also scared about this opportunity.",
    "I feel grateful yet heartbroken at the same time.",
    "This is surprising and disappointing simultaneously.",
    "I'm joyful yet anxious about tomorrow.",
    "I feel loved but also lonely sometimes.",
    "This makes me angry but I understand why it happened.",
    "I'm sad but hopeful things will get better."
]

# Neutral/challenging sentences
NEUTRAL_SENTENCES = [
    "The weather is nice today.",
    "I went to the store to buy groceries.",
    "The meeting is scheduled for 3 PM.",
    "Please send me the report by Friday.",
    "The book is on the table.",
    "I need to finish this project soon.",
    "The train arrives at 9:30 AM.",
    "She works in the marketing department.",
    "The conference room is available now.",
    "I'll call you back later this evening."
]

def print_test_sentences():
    """Print all test sentences organized by category"""
    print("🎭 EMOTION CLASSIFICATION TEST SENTENCES")
    print("=" * 60)
    
    for emotion, sentences in TEST_SENTENCES.items():
        print(f"\n😊 {emotion.upper()} SENTENCES:")
        print("-" * 30)
        for i, sentence in enumerate(sentences, 1):
            print(f"{i:2d}. {sentence}")
    
    print(f"\n🤔 MIXED EMOTION SENTENCES:")
    print("-" * 30)
    for i, sentence in enumerate(MIXED_SENTENCES, 1):
        print(f"{i:2d}. {sentence}")
    
    print(f"\n😐 NEUTRAL/CHALLENGING SENTENCES:")
    print("-" * 30)
    for i, sentence in enumerate(NEUTRAL_SENTENCES, 1):
        print(f"{i:2d}. {sentence}")

def get_sentences_by_emotion(emotion):
    """Get sentences for a specific emotion"""
    return TEST_SENTENCES.get(emotion.lower(), [])

def get_all_sentences():
    """Get all test sentences as a flat list"""
    all_sentences = []
    for sentences in TEST_SENTENCES.values():
        all_sentences.extend(sentences)
    all_sentences.extend(MIXED_SENTENCES)
    all_sentences.extend(NEUTRAL_SENTENCES)
    return all_sentences

if __name__ == "__main__":
    print_test_sentences()
    
    print(f"\n📊 SUMMARY:")
    print(f"Total emotion-specific sentences: {sum(len(sentences) for sentences in TEST_SENTENCES.values())}")
    print(f"Mixed emotion sentences: {len(MIXED_SENTENCES)}")
    print(f"Neutral sentences: {len(NEUTRAL_SENTENCES)}")
    print(f"Grand total: {len(get_all_sentences())} test sentences")
