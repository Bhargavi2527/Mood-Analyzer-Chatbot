"""
Mood Analyzer - AI-Powered Emotion & Behavior Detection
A professional Streamlit application for analyzing emotional states and behaviors
"""

import streamlit as st
import google.generativeai as genai
import os
import json
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
from prompts import get_analysis_prompt
from utils.helpers import (
    load_custom_css,
    get_mood_emoji,
    get_sentiment_color,
    save_to_history,
    load_history,
    create_mood_chart
)

# Page Configuration
st.set_page_config(
    page_title="Mood Analyzer | AI Emotion Detection",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Custom CSS
load_custom_css()

# Initialize Gemini API
@st.cache_resource
def initialize_gemini():
    """Initialize Gemini API with error handling"""
    # Try Streamlit secrets first (for Streamlit Cloud), then environment variable
    try:
        api_key = st.secrets.get("GEMINI_API_KEY")
    except:
        api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        st.error("⚠️ GEMINI_API_KEY not found. Please configure it in Streamlit secrets or .env file")
        st.info("Get your API key from: https://makersuite.google.com/app/apikey")
        st.stop()
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-pro")

model = initialize_gemini()

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = load_history()

# Header Section
st.markdown("""
    <div class="header-container">
        <div class="header-content">
            <h1 class="main-title">🧠 Mood Analyzer</h1>
            <p class="subtitle">AI-Powered Emotion & Behavior Detection System</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <h2>📊 Analysis Dashboard</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Settings
    st.markdown("### ⚙️ Settings")
    analysis_depth = st.select_slider(
        "Analysis Depth",
        options=["Quick", "Standard", "Deep"],
        value="Standard",
        help="Depth of emotional analysis"
    )
    
    include_recommendations = st.checkbox(
        "Include Recommendations",
        value=True,
        help="Get personalized mood improvement suggestions"
    )
    
    st.markdown("---")
    
    # History Stats
    if st.session_state.history:
        st.markdown("### 📈 Your Stats")
        df_history = pd.DataFrame(st.session_state.history)
        
        total_analyses = len(df_history)
        st.metric("Total Analyses", total_analyses)
        
        if 'sentiment' in df_history.columns:
            positive_count = len(df_history[df_history['sentiment'] == 'positive'])
            positive_pct = (positive_count / total_analyses) * 100 if total_analyses > 0 else 0
            st.metric("Positive Mood %", f"{positive_pct:.1f}%")
    
    st.markdown("---")
    
    # Clear History
    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.history = []
        save_to_history([])
        st.rerun()

# Main Content Area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        <div class="input-section">
            <h3 class="section-title">💬 Enter Your Message</h3>
            <p class="section-description">Type or paste a message to analyze emotional tone and behavior patterns</p>
        </div>
    """, unsafe_allow_html=True)
    
    user_text = st.text_area(
        "Message Input",
        placeholder="Example: I'm feeling overwhelmed with all the deadlines this week...",
        height=150,
        label_visibility="collapsed",
        key="message_input"
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    
    with col_btn1:
        analyze_button = st.button("🔍 Analyze Mood", use_container_width=True, type="primary")
    
    with col_btn2:
        clear_button = st.button("🔄 Clear", use_container_width=True)
    
    if clear_button:
        st.rerun()

with col2:
    st.markdown("""
        <div class="info-card">
            <h4>ℹ️ How It Works</h4>
            <ol>
                <li>Enter your message or text</li>
                <li>Click "Analyze Mood"</li>
                <li>Get instant AI-powered insights</li>
                <li>View mood trends over time</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

# Analysis Section
if analyze_button and user_text.strip():
    with st.spinner("🤖 Analyzing emotional patterns..."):
        try:
            # Generate prompt
            prompt = get_analysis_prompt(
                user_text, 
                depth=analysis_depth,
                include_recommendations=include_recommendations
            )
            
            # Call Gemini API
            response = model.generate_content(prompt)
            
            # Parse response
            response_text = response.text.strip()
            
            # Extract JSON from markdown code blocks if present
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            data = json.loads(response_text)
            
            # Display Results
            st.markdown("---")
            st.markdown("""
                <div class="results-header">
                    <h2>📊 Analysis Results</h2>
                </div>
            """, unsafe_allow_html=True)
            
            # Main Results Cards
            result_col1, result_col2, result_col3 = st.columns(3)
            
            with result_col1:
                mood_emoji = get_mood_emoji(data.get('mood', 'neutral'))
                st.markdown(f"""
                    <div class="result-card mood-card">
                        <div class="card-icon">{mood_emoji}</div>
                        <div class="card-label">Detected Mood</div>
                        <div class="card-value">{data.get('mood', 'Unknown').title()}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with result_col2:
                sentiment = data.get('sentiment', 'neutral')
                sentiment_color = get_sentiment_color(sentiment)
                st.markdown(f"""
                    <div class="result-card sentiment-card" style="border-color: {sentiment_color};">
                        <div class="card-icon">{'😊' if sentiment == 'positive' else '😐' if sentiment == 'neutral' else '😔'}</div>
                        <div class="card-label">Sentiment</div>
                        <div class="card-value" style="color: {sentiment_color};">{sentiment.title()}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with result_col3:
                confidence = data.get('confidence', 'Medium')
                st.markdown(f"""
                    <div class="result-card confidence-card">
                        <div class="card-icon">📊</div>
                        <div class="card-label">Confidence</div>
                        <div class="card-value">{confidence}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Detailed Analysis
            st.markdown("<br>", unsafe_allow_html=True)
            
            detail_col1, detail_col2 = st.columns(2)
            
            with detail_col1:
                st.markdown(f"""
                    <div class="detail-card">
                        <h4>🎭 Behavior Type</h4>
                        <p class="behavior-text">{data.get('behaviour_type', 'Not detected').title()}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            with detail_col2:
                st.markdown(f"""
                    <div class="detail-card">
                        <h4>💡 Explanation</h4>
                        <p class="explanation-text">{data.get('explanation', 'No explanation available.')}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            # Recommendations (if enabled)
            if include_recommendations and 'recommendations' in data:
                st.markdown("""
                    <div class="recommendations-section">
                        <h4>✨ Personalized Recommendations</h4>
                    </div>
                """, unsafe_allow_html=True)
                
                for idx, rec in enumerate(data['recommendations'], 1):
                    st.markdown(f"""
                        <div class="recommendation-item">
                            <span class="rec-number">{idx}</span>
                            <span class="rec-text">{rec}</span>
                        </div>
                    """, unsafe_allow_html=True)
            
            # Save to history
            history_entry = {
                'timestamp': datetime.now().isoformat(),
                'text': user_text[:100] + "..." if len(user_text) > 100 else user_text,
                'mood': data.get('mood', 'unknown'),
                'sentiment': data.get('sentiment', 'neutral'),
                'behaviour': data.get('behaviour_type', 'unknown'),
                'confidence': data.get('confidence', 'Medium')
            }
            
            st.session_state.history.append(history_entry)
            save_to_history(st.session_state.history)
            
        except json.JSONDecodeError as e:
            st.error(f"❌ Error parsing AI response: {str(e)}")
            st.code(response_text)
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

elif analyze_button and not user_text.strip():
    st.warning("⚠️ Please enter a message to analyze")

# History Section
if st.session_state.history:
    st.markdown("---")
    st.markdown("""
        <div class="history-header">
            <h2>📜 Analysis History</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Mood Trend Chart
    if len(st.session_state.history) >= 2:
        fig = create_mood_chart(st.session_state.history)
        st.plotly_chart(fig, use_container_width=True)
    
    # History Table
    df_display = pd.DataFrame(st.session_state.history)
    
    # Rename columns for display
    display_columns = {
        'timestamp': 'Date & Time',
        'text': 'Message Preview',
        'mood': 'Mood',
        'sentiment': 'Sentiment',
        'behaviour': 'Behavior',
        'confidence': 'Confidence'
    }
    
    df_display = df_display.rename(columns=display_columns)
    
    # Format timestamp
    if 'Date & Time' in df_display.columns:
        df_display['Date & Time'] = pd.to_datetime(df_display['Date & Time']).dt.strftime('%Y-%m-%d %H:%M')
    
    st.dataframe(
        df_display[list(display_columns.values())].tail(10),
        use_container_width=True,
        hide_index=True
    )

# Footer
st.markdown("""
    <div class="footer">
        <p>Built with ❤️ using Streamlit & Google Gemini AI | © 2026 Mood Analyzer</p>
    </div>
""", unsafe_allow_html=True)
