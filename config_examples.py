"""
Example configurations and test cases for Mood Analyzer
"""

# Test messages for different emotions
TEST_MESSAGES = {
    "happy": "I just got promoted at work! I'm so excited and grateful for this opportunity. Can't wait to share the news with my family!",
    
    "sad": "I'm feeling down today. Everything seems grey and I don't have the energy to do much. Just want to stay in bed.",
    
    "anxious": "I have a big presentation tomorrow and I'm really nervous. What if I mess up? I keep going over my notes but I still feel unprepared.",
    
    "angry": "I can't believe they did that! This is so unfair and I'm furious. They had no right to treat me that way!",
    
    "stressed": "I'm feeling overwhelmed with all the deadlines this week. Everything seems to be piling up and I don't know where to start.",
    
    "calm": "I went for a walk in the park today. The weather was nice and I feel peaceful. Just taking things one day at a time.",
    
    "excited": "OMG! I can't believe this is happening! This is literally the best day ever! So many amazing things happening at once!",
    
    "neutral": "I went to the store today and bought groceries. The weather was okay, nothing special. Just a regular day.",
    
    "mixed": "Got some good news about my project being approved, but I'm stressed about the tight timeline. It's exciting but also scary.",
    
    "confused": "I don't really know how I feel right now. Things are okay I guess? But something feels off and I can't put my finger on it."
}

# Expected analysis for testing
EXPECTED_RESULTS = {
    "happy": {
        "mood": "happy",
        "sentiment": "positive",
        "behaviour_type": "optimistic"
    },
    "anxious": {
        "mood": "anxious",
        "sentiment": "negative",
        "behaviour_type": "stressed"
    },
    "neutral": {
        "mood": "neutral",
        "sentiment": "neutral",
        "behaviour_type": "passive"
    }
}

# Prompt templates for different scenarios
SCENARIO_PROMPTS = {
    "customer_support": """
        Customer message: {message}
        
        Analyze the customer's emotional state to help our support team respond appropriately.
    """,
    
    "journal_entry": """
        Journal entry: {message}
        
        Help me understand my emotional patterns and provide insights for self-reflection.
    """,
    
    "social_media": """
        Social media post: {message}
        
        Analyze the sentiment and emotional tone of this post.
    """
}

# Color schemes for different themes
COLOR_SCHEMES = {
    "default": {
        "primary": "#6366f1",
        "positive": "#10b981",
        "negative": "#ef4444",
        "neutral": "#f59e0b"
    },
    
    "dark": {
        "primary": "#818cf8",
        "positive": "#34d399",
        "negative": "#f87171",
        "neutral": "#fbbf24"
    },
    
    "pastel": {
        "primary": "#c4b5fd",
        "positive": "#86efac",
        "negative": "#fca5a5",
        "neutral": "#fde047"
    }
}

# API configuration examples
API_CONFIGS = {
    "quick": {
        "max_tokens": 500,
        "temperature": 0.3,
        "depth": "Quick"
    },
    
    "standard": {
        "max_tokens": 1000,
        "temperature": 0.5,
        "depth": "Standard"
    },
    
    "deep": {
        "max_tokens": 2000,
        "temperature": 0.7,
        "depth": "Deep"
    }
}
