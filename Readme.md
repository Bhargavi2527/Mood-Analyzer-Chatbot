# 🧠 Mood Analyzer - AI-Powered Emotion & Behavior Detection

A professional, production-ready Streamlit application that uses Google's Gemini AI to analyze emotional states and behavioral patterns from text messages. Perfect for portfolio projects showcasing AI/ML, NLP, and data analysis skills.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### Core Functionality
- 🎯 **Real-time Mood Detection** - Analyze emotions from text messages instantly
- 📊 **Sentiment Analysis** - Classify sentiments as positive, negative, or neutral
- 🎭 **Behavior Pattern Recognition** - Identify behavioral types and patterns
- 💯 **Confidence Scoring** - Get confidence levels for each analysis
- 💡 **Smart Recommendations** - Receive personalized mood improvement suggestions

### Advanced Features
- 📈 **Mood Trend Visualization** - Interactive charts showing emotional trends over time
- 📜 **Analysis History** - Track all your analyses with persistent storage
- 📊 **Statistics Dashboard** - View comprehensive mood statistics
- 🎨 **Professional UI/UX** - Modern, clean, and responsive design
- ⚙️ **Customizable Analysis** - Three depth levels (Quick, Standard, Deep)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mood-analyzer.git
cd mood-analyzer
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API key**
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_actual_api_key_here
```

5. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
mood-analyzer/
│
├── app.py                      # Main Streamlit application
├── prompts.py                  # Prompt engineering for Gemini AI
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
│
├── static/
│   └── css/
│       └── style.css          # Professional CSS styling
│
├── utils/
│   ├── __init__.py
│   └── helpers.py             # Helper functions and utilities
│
└── data/                      # Created automatically
    └── analysis_history.json  # Persistent analysis storage
```

## 🎨 Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Gemini AI (gemini-pro)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Styling**: Custom CSS with modern design principles
- **Language**: Python 3.8+

## 📖 Usage Guide

### Basic Usage

1. **Enter Message**: Type or paste the text you want to analyze in the input area
2. **Adjust Settings** (Optional):
   - Choose analysis depth (Quick/Standard/Deep)
   - Enable/disable recommendations
3. **Analyze**: Click the "Analyze Mood" button
4. **View Results**: See detailed mood, sentiment, and behavior analysis

### Understanding Results

- **Mood**: Primary emotion detected (happy, sad, anxious, etc.)
- **Sentiment**: Overall tone (positive, negative, neutral)
- **Confidence**: How confident the AI is in its analysis
- **Behavior Type**: Observed behavioral patterns
- **Explanation**: Brief explanation of the analysis
- **Recommendations**: Actionable suggestions (when enabled)

### Viewing History

- All analyses are automatically saved
- View mood trends over time in interactive charts
- Access statistics in the sidebar
- Export history data for further analysis

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
ENVIRONMENT=development
DEBUG=False
```

### Customization

**Adjust Analysis Depth**: Modify prompts in `prompts.py`

**Change Styling**: Edit `static/css/style.css`

**Add Features**: Extend `utils/helpers.py` for new functionality

## 🎯 Use Cases

- **Personal Journaling** - Track emotional wellbeing over time
- **Customer Support** - Analyze customer sentiment in messages
- **Mental Health** - Monitor emotional patterns (not a replacement for professional help)
- **Research** - Study emotional expressions in text
- **Content Moderation** - Detect negative or harmful content
- **UX Research** - Analyze user feedback sentiment

## 🌟 Portfolio Highlights

This project demonstrates:

✅ **AI Integration** - Working with LLM APIs (Gemini)  
✅ **Prompt Engineering** - Optimized prompts for accurate results  
✅ **Data Analysis** - Processing and visualizing emotional data  
✅ **Full-Stack Development** - Complete frontend and backend  
✅ **Professional UI/UX** - Modern, responsive design  
✅ **Best Practices** - Proper code structure, documentation, and version control  

Perfect for:
- Data Analyst portfolios
- AI/ML Engineer applications
- Full-Stack Developer showcases
- NLP project demonstrations

## 📊 Sample Output

```json
{
  "mood": "anxious",
  "sentiment": "negative",
  "confidence": "High",
  "behaviour_type": "stressed",
  "explanation": "Message shows clear signs of anxiety with overwhelm about deadlines.",
  "recommendations": [
    "Break tasks into smaller, manageable chunks",
    "Practice deep breathing or meditation",
    "Consider talking to someone you trust"
  ]
}
```

## 🚀 Deployment

### Streamlit Cloud (Free)

1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add `GEMINI_API_KEY` in Secrets section
5. Deploy!

### Docker (Optional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Multi-language support
- [ ] Voice input capability
- [ ] Advanced analytics dashboard
- [ ] Email/SMS integration
- [ ] Mobile app version
- [ ] Export to PDF reports
- [ ] User authentication
- [ ] Team/group analysis
- [ ] AI model comparison (Claude, GPT, etc.)

## ⚠️ Disclaimer

This application is for informational and educational purposes only. It is not a substitute for professional mental health advice, diagnosis, or treatment. If you're experiencing mental health issues, please consult a qualified healthcare provider.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
- Portfolio: [yourwebsite.com](https://yourwebsite.com)

## 🙏 Acknowledgments

- Google Gemini AI for powerful language understanding
- Streamlit for the amazing web framework
- The open-source community for inspiration and support

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Email: your.email@example.com
- Twitter: [@yourhandle](https://twitter.com/yourhandle)

---

**⭐ If you found this project helpful, please consider giving it a star!**

Made with ❤️ and AI
