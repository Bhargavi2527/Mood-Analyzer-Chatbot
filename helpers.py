"""
Utility Functions for Mood Analyzer
Helper functions for data processing, visualization, and file operations
"""

import streamlit as st
import pandas as pd
import json
import plotly.graph_objects as go
from datetime import datetime
from typing import List, Dict
import os

# File paths
HISTORY_FILE = "data/analysis_history.json"
CSS_FILE = "static/css/style.css"


def load_custom_css():
    """Load custom CSS styling for the application"""
    css_path = os.path.join(os.path.dirname(__file__), CSS_FILE)
    
    if os.path.exists(css_path):
        with open(css_path, 'r') as f:
            css_content = f.read()
            st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
    else:
        # Fallback inline CSS if file doesn't exist
        st.markdown("""
            <style>
            .stApp {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .main .block-container {
                background: white;
                border-radius: 1rem;
                padding: 2rem;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            }
            </style>
        """, unsafe_allow_html=True)


def get_mood_emoji(mood: str) -> str:
    """
    Get appropriate emoji for a given mood
    
    Args:
        mood: The mood string
    
    Returns:
        Emoji character
    """
    mood = mood.lower()
    
    emoji_map = {
        'happy': '😊',
        'sad': '😢',
        'anxious': '😰',
        'angry': '😠',
        'stressed': '😓',
        'calm': '😌',
        'excited': '🤩',
        'overwhelmed': '😵',
        'hopeful': '🙂',
        'frustrated': '😤',
        'content': '😊',
        'worried': '😟',
        'confident': '😎',
        'disappointed': '😞',
        'grateful': '🙏',
        'neutral': '😐',
        'joyful': '😄',
        'depressed': '😔',
        'nervous': '😬',
        'peaceful': '☮️',
        'energetic': '⚡',
        'tired': '😴',
        'bored': '😑',
        'confused': '😕',
        'surprised': '😲',
        'scared': '😨',
        'proud': '😌',
        'embarrassed': '😳',
        'guilty': '😔',
        'relieved': '😅'
    }
    
    return emoji_map.get(mood, '💭')


def get_sentiment_color(sentiment: str) -> str:
    """
    Get color code for sentiment
    
    Args:
        sentiment: The sentiment (positive, negative, neutral)
    
    Returns:
        Hex color code
    """
    sentiment = sentiment.lower()
    
    color_map = {
        'positive': '#10b981',  # Green
        'negative': '#ef4444',  # Red
        'neutral': '#f59e0b'    # Orange
    }
    
    return color_map.get(sentiment, '#6b7280')


def save_to_history(history: List[Dict]):
    """
    Save analysis history to JSON file
    
    Args:
        history: List of analysis records
    """
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        st.error(f"Error saving history: {str(e)}")


def load_history() -> List[Dict]:
    """
    Load analysis history from JSON file
    
    Returns:
        List of analysis records
    """
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            st.warning(f"Could not load history: {str(e)}")
            return []
    return []


def create_mood_chart(history: List[Dict]) -> go.Figure:
    """
    Create an interactive mood trend chart using Plotly
    
    Args:
        history: List of analysis records
    
    Returns:
        Plotly figure object
    """
    df = pd.DataFrame(history)
    
    # Convert timestamps
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    
    # Map sentiments to numeric values for plotting
    sentiment_map = {'positive': 1, 'neutral': 0, 'negative': -1}
    df['sentiment_value'] = df['sentiment'].map(sentiment_map)
    
    # Create figure
    fig = go.Figure()
    
    # Add line trace
    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['sentiment_value'],
        mode='lines+markers',
        name='Mood Trend',
        line=dict(color='#6366f1', width=3, shape='spline'),
        marker=dict(
            size=10,
            color=df['sentiment_value'],
            colorscale=[[0, '#ef4444'], [0.5, '#f59e0b'], [1, '#10b981']],
            showscale=False,
            line=dict(width=2, color='white')
        ),
        hovertemplate='<b>%{customdata[0]}</b><br>' +
                      'Sentiment: %{customdata[1]}<br>' +
                      'Time: %{x|%Y-%m-%d %H:%M}<br>' +
                      '<extra></extra>',
        customdata=list(zip(df['mood'], df['sentiment']))
    ))
    
    # Add sentiment zones
    fig.add_hrect(y0=0.5, y1=1, fillcolor="#10b981", opacity=0.1, line_width=0)
    fig.add_hrect(y0=-0.5, y1=0.5, fillcolor="#f59e0b", opacity=0.1, line_width=0)
    fig.add_hrect(y0=-1, y1=-0.5, fillcolor="#ef4444", opacity=0.1, line_width=0)
    
    # Update layout
    fig.update_layout(
        title={
            'text': '📈 Mood Trend Over Time',
            'font': {'size': 20, 'color': '#0f172a', 'family': 'Inter'},
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis=dict(
            title='Date & Time',
            showgrid=True,
            gridcolor='#e2e8f0',
            zeroline=False
        ),
        yaxis=dict(
            title='Sentiment',
            ticktext=['Negative', 'Neutral', 'Positive'],
            tickvals=[-1, 0, 1],
            showgrid=True,
            gridcolor='#e2e8f0',
            zeroline=True,
            zerolinecolor='#94a3b8',
            range=[-1.2, 1.2]
        ),
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Inter', color='#475569'),
        margin=dict(l=60, r=40, t=60, b=60),
        height=400
    )
    
    return fig


def export_history_to_csv(history: List[Dict]) -> pd.DataFrame:
    """
    Export history to CSV format
    
    Args:
        history: List of analysis records
    
    Returns:
        Pandas DataFrame
    """
    df = pd.DataFrame(history)
    
    # Format timestamp
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
    
    return df


def calculate_mood_statistics(history: List[Dict]) -> Dict:
    """
    Calculate statistical insights from mood history
    
    Args:
        history: List of analysis records
    
    Returns:
        Dictionary of statistics
    """
    if not history:
        return {}
    
    df = pd.DataFrame(history)
    
    stats = {
        'total_analyses': len(df),
        'sentiment_distribution': df['sentiment'].value_counts().to_dict(),
        'most_common_mood': df['mood'].mode()[0] if not df['mood'].empty else 'N/A',
        'most_common_behavior': df['behaviour'].mode()[0] if 'behaviour' in df.columns and not df['behaviour'].empty else 'N/A'
    }
    
    # Calculate sentiment percentages
    total = stats['total_analyses']
    stats['positive_percentage'] = (stats['sentiment_distribution'].get('positive', 0) / total) * 100
    stats['negative_percentage'] = (stats['sentiment_distribution'].get('negative', 0) / total) * 100
    stats['neutral_percentage'] = (stats['sentiment_distribution'].get('neutral', 0) / total) * 100
    
    return stats


def get_mood_insights(history: List[Dict]) -> List[str]:
    """
    Generate insights from mood history
    
    Args:
        history: List of analysis records
    
    Returns:
        List of insight strings
    """
    if len(history) < 3:
        return ["Keep tracking your moods to unlock insights!"]
    
    df = pd.DataFrame(history)
    stats = calculate_mood_statistics(history)
    insights = []
    
    # Positive trend insight
    if stats['positive_percentage'] > 60:
        insights.append("🌟 You're maintaining a predominantly positive mood!")
    
    # Negative trend warning
    if stats['negative_percentage'] > 50:
        insights.append("💙 Consider reaching out to someone you trust or a professional for support.")
    
    # Variety insight
    unique_moods = df['mood'].nunique()
    if unique_moods > 5:
        insights.append(f"🎭 You've experienced {unique_moods} different moods - that's normal emotional variety!")
    
    # Recent trend
    if len(df) >= 5:
        recent_sentiment = df.tail(5)['sentiment'].value_counts()
        if recent_sentiment.index[0] == 'positive':
            insights.append("📈 Your recent entries show an upward trend!")
    
    return insights if insights else ["Continue tracking to see personalized insights!"]


def format_timestamp(timestamp: str) -> str:
    """
    Format timestamp for display
    
    Args:
        timestamp: ISO format timestamp string
    
    Returns:
        Formatted timestamp string
    """
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime('%B %d, %Y at %I:%M %p')
    except:
        return timestamp


def validate_api_key() -> bool:
    """
    Validate that Gemini API key is configured
    
    Returns:
        Boolean indicating if API key is valid
    """
    api_key = os.getenv("GEMINI_API_KEY")
    return api_key is not None and len(api_key) > 0


def get_confidence_badge_color(confidence: str) -> str:
    """
    Get color for confidence badge
    
    Args:
        confidence: Confidence level (High, Medium, Low)
    
    Returns:
        Hex color code
    """
    confidence = confidence.lower()
    
    color_map = {
        'high': '#10b981',
        'medium': '#f59e0b',
        'low': '#ef4444'
    }
    
    return color_map.get(confidence, '#6b7280')
