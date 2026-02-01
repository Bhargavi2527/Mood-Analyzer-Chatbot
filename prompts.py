"""
Prompt Engineering Module for Mood Analyzer
Optimized prompts for accurate emotion and behavior detection
"""

def get_analysis_prompt(user_text: str, depth: str = "Standard", include_recommendations: bool = True) -> str:
    """
    Generate optimized analysis prompt based on depth and options
    
    Args:
        user_text: The message to analyze
        depth: Analysis depth (Quick, Standard, Deep)
        include_recommendations: Whether to include mood improvement recommendations
    
    Returns:
        Formatted prompt string
    """
    
    # Base instruction
    base_instruction = """You are an expert psychology-aware AI assistant specialized in emotional intelligence and behavioral analysis.

Your task is to analyze the emotional state, sentiment, and behavioral patterns of a person based on their written message.

Provide accurate, empathetic, and insightful analysis."""

    # Depth-specific instructions
    depth_instructions = {
        "Quick": "Provide a brief, focused analysis with key emotional indicators only.",
        "Standard": "Provide a balanced analysis with moderate detail on emotional patterns and behaviors.",
        "Deep": "Provide an in-depth analysis with comprehensive insights into emotional nuances, underlying patterns, and psychological indicators."
    }
    
    # Output format
    output_format = """
Return your analysis STRICTLY in valid JSON format with the following structure:

{
  "mood": "",
  "sentiment": "",
  "confidence": "",
  "behaviour_type": "",
  "explanation": ""
"""
    
    # Add recommendations field if requested
    if include_recommendations:
        output_format += """,
  "recommendations": []
"""
    
    output_format += "}"
    
    # Field definitions
    field_definitions = """

FIELD DEFINITIONS:
- "mood": Single word describing primary emotion (e.g., happy, sad, anxious, angry, stressed, calm, excited, overwhelmed, hopeful, frustrated, content, worried, confident, disappointed, grateful)
- "sentiment": Classification as "positive", "negative", or "neutral"
- "confidence": Your confidence level in the analysis - "High", "Medium", or "Low"
- "behaviour_type": Behavioral pattern observed (e.g., supportive, aggressive, passive, frustrated, optimistic, withdrawn, assertive, defensive, collaborative, isolated)
- "explanation": Brief 1-2 sentence explanation of your analysis
"""
    
    # Add recommendations definition if requested
    if include_recommendations:
        field_definitions += """- "recommendations": Array of 2-4 actionable suggestions to improve or maintain emotional wellbeing (only if sentiment is negative or neutral)
"""
    
    # Analysis guidelines
    guidelines = """
ANALYSIS GUIDELINES:
1. Be objective and evidence-based in your assessment
2. Consider context, word choice, and tone
3. Identify emotional intensity and urgency
4. Recognize both explicit and implicit emotional cues
5. Account for cultural and individual differences in expression
6. Maintain professional boundaries while being empathetic
"""
    
    # Additional depth-specific guidelines
    if depth == "Deep":
        guidelines += """7. Analyze underlying psychological patterns
8. Identify potential triggers or stressors
9. Consider long-term emotional trends if discernible
10. Note any cognitive distortions or thinking patterns
"""
    
    # Construct final prompt
    prompt = f"""{base_instruction}

{depth_instructions[depth]}

{output_format}

{field_definitions}

{guidelines}

CRITICAL RULES:
- Return ONLY valid JSON, no additional text or markdown formatting
- Do not use code blocks (no ```json or ```)
- Ensure all JSON strings are properly escaped
- Be concise but accurate
- Base analysis only on the provided text

TEXT TO ANALYZE:
<<<
{user_text}
>>>

Provide your analysis now in valid JSON format:"""
    
    return prompt


def get_batch_analysis_prompt(messages: list) -> str:
    """
    Generate prompt for batch analysis of multiple messages
    
    Args:
        messages: List of messages to analyze
    
    Returns:
        Formatted prompt for batch analysis
    """
    
    prompt = """You are analyzing multiple messages to identify emotional trends and patterns.

Analyze each message and return a JSON array where each element follows this structure:

{
  "message_id": 1,
  "mood": "",
  "sentiment": "",
  "confidence": "",
  "behaviour_type": ""
}

Messages to analyze:
"""
    
    for idx, msg in enumerate(messages, 1):
        prompt += f"\n{idx}. {msg}\n"
    
    prompt += "\nProvide analysis as a valid JSON array:"
    
    return prompt


# Example prompts for testing
EXAMPLE_PROMPTS = {
    "positive": "I just got promoted at work! I'm so excited and grateful for this opportunity. Can't wait to share the news with my family!",
    "negative": "I'm feeling overwhelmed with all the deadlines this week. Everything seems to be piling up and I don't know where to start.",
    "neutral": "I went to the store today and bought groceries. The weather was okay, nothing special.",
    "anxious": "I have a big presentation tomorrow and I'm really nervous. What if I mess up? I keep going over my notes but I still feel unprepared.",
    "mixed": "Got some good news about my project being approved, but I'm stressed about the tight timeline. It's exciting but also scary."
}


def get_example_prompt(emotion_type: str = "positive") -> str:
    """
    Get an example prompt for testing
    
    Args:
        emotion_type: Type of emotion to test (positive, negative, neutral, anxious, mixed)
    
    Returns:
        Example text
    """
    return EXAMPLE_PROMPTS.get(emotion_type, EXAMPLE_PROMPTS["neutral"])
