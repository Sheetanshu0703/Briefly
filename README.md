# Briefly - AI Text Summarizer 🚀

A beautiful, modern AI-powered text summarization application built with FastAPI and Transformers.

## ✨ Features

- **Modern UI**: Beautiful, responsive design with animations and interactive elements
- **AI-Powered**: Uses state-of-the-art transformer models for text summarization
- **Real-time Processing**: Instant summarization with progress indicators
- **Statistics**: Shows compression ratio and word count statistics
- **API Support**: RESTful API endpoints for integration
- **Responsive Design**: Works perfectly on desktop and mobile devices

## 🎨 UI Features

- **Gradient Background**: Eye-catching purple gradient design
- **Animated Elements**: Smooth animations and transitions
- **Interactive Feedback**: Real-time character counting and validation
- **Loading Animations**: Beautiful spinners and progress indicators
- **Success Animations**: Bounce effects for successful operations
- **Particle Effects**: Floating particles in the background
- **Dark Mode Support**: Automatic dark mode detection

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Open in Browser**:
   Navigate to `http://localhost:8000`

## 📱 Usage

1. **Enter Text**: Paste or type your text in the input area (minimum 50 characters)
2. **Generate Summary**: Click the "Generate Summary" button
3. **View Results**: See your summary with statistics and compression ratio

## 🔧 API Endpoints

- `GET /` - Main application interface
- `POST /predict` - Generate text summary
- `GET /train` - Train the model
- `GET /health` - Health check
- `GET /api-docs` - API documentation

## 🛠️ Technical Stack

- **Backend**: FastAPI, Python
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Model**: Transformers (Hugging Face)
- **Styling**: Custom CSS with animations
- **Icons**: Font Awesome

## 📁 Project Structure

```
Briefly/
├── app.py                 # Main FastAPI application
├── templates/
│   └── index.html        # Beautiful UI template
├── static/
│   ├── style.css         # Additional styles
│   └── script.js         # Enhanced interactions
├── src/
│   └── Briefly/          # Core AI components
└── requirements.txt      # Python dependencies
```

## 🎯 Features in Detail

### Interactive UI Elements
- Real-time character counter
- Dynamic border colors based on input length
- Smooth hover effects and transitions
- Loading spinners with custom animations

### Statistics Dashboard
- Original text word count
- Summary word count
- Compression ratio percentage
- Visual progress indicators

### Error Handling
- User-friendly error messages
- Input validation with helpful feedback
- Graceful error recovery

## 🌟 Why Choose Briefly?

- **Beautiful Design**: Modern, tech-inspired interface
- **Fast Performance**: Optimized for speed and responsiveness
- **User-Friendly**: Intuitive interface with helpful feedback
- **Professional**: Production-ready with proper error handling
- **Extensible**: Easy to customize and extend

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Made with ❤️ and AI** 🚀


