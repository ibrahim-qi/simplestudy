# 📚 SimpleStudy

A modern, intuitive flashcard web application built with Flask that enables users to create, share, and study flashcard sets through interactive quizzes and collaborative learning.

## ✨ Features

### 🔐 Authentication System
- **Secure User Registration & Login**: Password hashing with Werkzeug security
- **Session Management**: Flask-Login integration for secure user sessions
- **User-specific Content**: Personal dashboards and flashcard management

### 📖 Flashcard Management
- **Create Custom Sets**: Organize flashcards by topic and subject
- **Rich Text Support**: Markdown support with Flask-PageDown for formatted content
- **Edit & Update**: Full CRUD operations for flashcards and sets
- **Personal Dashboard**: View and manage all your created flashcard sets

### 🧠 Interactive Learning
- **Multiple Quiz Types**:
  - **Self Quiz**: Traditional flashcard study with flip-to-reveal answers
  - **Multiple Choice Quiz**: Algorithmic quiz generation with randomized questions
- **Intelligent Question Generation**: Dynamic multiple choice questions from flashcard content
- **Performance Tracking**: Score tracking and quiz history

### 🌍 Social Learning
- **Browse Public Sets**: Discover flashcard sets created by other users
- **Search Functionality**: Find sets by name, topic, or subject
- **Rating System**: Rate and review flashcard sets to help others find quality content
- **Community-Driven**: Share your knowledge and learn from others

### 📱 Modern UI/UX
- **Responsive Design**: Mobile-first approach ensuring great experience on all devices
- **Bootstrap Integration**: Clean, professional interface with Flask-Bootstrap
- **Intuitive Navigation**: Easy-to-use interface for seamless studying

## 🛠️ Tech Stack

- **Backend**: Python 3.9+ with Flask Web Framework
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript with Bootstrap 3
- **Authentication**: Flask-Login with Werkzeug password hashing
- **Forms**: Flask-WTF with WTForms validation
- **Rich Text**: Flask-PageDown for Markdown support

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/SimpleStudy.git
   cd SimpleStudy
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python app/__init__.py
   ```
   The SQLite database will be automatically created on first run.

5. **Run the application**
   ```bash
   python app/__init__.py
   ```
   
6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### Development Setup with PyCharm

1. Open PyCharm IDE
2. Open the project directory
3. Configure Python interpreter:
   - Go to Settings → Project → Python Interpreter
   - Select the `venv/Scripts/python.exe` as your interpreter
4. Set run configuration:
   - Use `app/__init__.py` as the script file
   - Set working directory to project root

## 📖 Usage

### Getting Started
1. **Register an Account**: Create your account on the registration page
2. **Login**: Access your personal dashboard
3. **Create Your First Set**: Click "Create Set" and add a topic and subject
4. **Add Flashcards**: Add questions and answers to your set
5. **Start Studying**: Use either Self Quiz or Multiple Choice modes

### Study Modes

#### Self Quiz
- Traditional flashcard experience
- Click to reveal answers
- Perfect for memorization and recall practice

#### Multiple Choice Quiz
- Algorithmically generated questions
- Multiple answer options
- Immediate feedback and scoring
- Great for testing knowledge retention

### Social Features
- **Browse Sets**: Explore public flashcard sets from the community
- **Search**: Find specific topics using the search functionality
- **Rate Sets**: Help others discover quality content by rating sets
- **Share Knowledge**: Make your sets public for others to study

## 🗄️ Database Schema

The application uses SQLite with the following main entities:

- **Users**: Authentication and user management
- **Sets**: Flashcard set organization (topic, subject, creator)
- **Flashcards**: Individual question-answer pairs
- **Ratings**: User ratings for sets
- **Tests**: Quiz session tracking and scoring
- **Questions/Options**: Multiple choice quiz data

## 📱 Screenshots

### Dashboard
![Dashboard](https://github.com/ibbyq12/SimpleStudy/assets/100475296/6613a758-194a-461e-9f39-24029cc8ad90)

### Flashcard Set Example
![Flashcard Set](https://github.com/ibbyq12/SimpleStudy/assets/100475296/07bf6d47-374d-4656-966c-77df369bcc0a)

### Multiple Choice Quiz
![Multiple Choice Quiz](https://github.com/ibbyq12/SimpleStudy/assets/100475296/38e0a273-fd88-4201-9658-d7e9e2b621e2)

### Quiz Results
![Quiz Results](https://github.com/ibbyq12/SimpleStudy/assets/100475296/639ec59a-b36b-45f4-a9bc-50e8c1fb4b95)

### Secure Password Storage
![Password Security](https://github.com/ibbyq12/SimpleStudy/assets/100475296/522750c5-9155-474e-89a9-229e519f1ed6)

### Login Interface
![Login Page](https://github.com/ibbyq12/SimpleStudy/assets/100475296/75ea940b-2d8d-4a59-8fca-37416eed5929)

### Set Creation
![Create Set](https://github.com/ibbyq12/SimpleStudy/assets/100475296/a1e178a7-8a05-422d-9741-64a8a3fa4efa)

## 🏗️ Project Structure

```
SimpleStudy/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── forms.py                 # WTForms form definitions
│   ├── auth/
│   │   └── routes.py           # Authentication routes
│   ├── main/
│   │   └── routes.py           # Main application routes
│   ├── models/                 # Database models
│   │   ├── users.py
│   │   ├── sets.py
│   │   ├── flashcards.py
│   │   ├── ratings.py
│   │   ├── selftests.py
│   │   ├── multiplechoicetests.py
│   │   └── multiplechoicequestions.py
│   ├── static/                 # CSS and JavaScript files
│   │   ├── style.css
│   │   └── quiz.js
│   └── templates/              # HTML templates
│       ├── base.html
│       ├── dashboard.html
│       ├── browse.html
│       └── ...
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## 🔧 Configuration

The application uses the following default configuration:
- **Database**: SQLite (`NEA.sqlite3`)
- **Secret Key**: Configured in `app/__init__.py`
- **Debug Mode**: Enabled by default (disable in production)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] Add spaced repetition algorithm
- [ ] Implement flashcard statistics and analytics
- [ ] Add image support for flashcards
- [ ] Create mobile app version
- [ ] Add collaborative study groups
- [ ] Implement dark mode theme

## 🐛 Known Issues

- Ensure all Flask extensions are properly installed
- Some deployment configurations may require additional setup
- Mobile optimization is ongoing (responsive design implemented)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Ibrahim** - [GitHub Profile](https://github.com/ibbyq12)

## 🙏 Acknowledgments

- Flask community for excellent documentation
- Bootstrap for responsive design components
- SQLAlchemy for robust database management
- Contributors and users who help improve SimpleStudy

---

**Happy Studying! 📚✨**

*SimpleStudy - Making learning efficient and collaborative*
