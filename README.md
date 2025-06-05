<h1 align="center">FitAgent</h1>

FitAgent is an AI-powered fitness coaching platform that provides personalized workout recommendations through an interactive chat interface. The system combines conversational AI with fitness expertise to deliver tailored exercise programs based on user goals, fitness levels, and preferences.


## Key Features ✨
### 1. Interactive AI Fitness Coach 🤖💬
 - **Conversational Interface:** Chat naturally with your AI coach to discuss fitness goals, preferences, and limitations.

 - **Smart Recommendations:** The AI analyzes user inputs (age, weight, fitness level) to suggest personalized workouts.

 - **Real-Time Feedback:** Get instant advice on workout adjustments based on performance.

### 2. Personalized Workout Plans 🏋️‍♂️📅
 - Goal-Oriented Workouts: Custom plans for weight loss, muscle gain, endurance, or flexibility.

 - Adaptive Difficulty: AI adjusts workout intensity based on user progress and feedback.

 - Exercise Variety: Avoid plateaus with dynamically changing routines.

### 3. User Management & Progress Tracking 📊🔍
 - User Profiles: Save fitness levels, goals, and preferences.

 - Workout History: Track completed sessions with performance metrics (sets, reps, duration).

 - Progress Analytics: Visual charts show improvements over time (strength, endurance, consistency).

### 4. AI-Powered Workout Generation ⚙️🧠
 - Dynamic Exercise Selection: AI picks exercises based on available equipment (home/gym).

 - Form Tips: Basic guidance on proper exercise techniques (future: CV integration).

 - Rest Timer & Pacing: Smart rest intervals based on workout intensity.


### 5. Web-Based Dashboard 💻🖥️
 - Responsive Design: Works on desktop and mobile browsers.

 - Interactive UI:

   - Chat Interface (chat.html) – Talk to your AI coach.

   - Workout Display (workout.html) – View exercise details (demos, reps, sets).

   - Results Page (result.html) – Review completed workouts.

 - User Registration (register.html) – Secure sign-up/login system.

### 6. Backend & Data Management 🛠️🗃️
 - SQLite Database (fitness.db): Stores user profiles, workout history, and preferences.

 - Logging System (logger.py): Tracks app activity and errors for debugging.

 - API Endpoints (api.py): Handles data exchange between the frontend and AI logic.


## Technology Stack
### Backend
 - Python (with Flask framework)

 - SQLite (fitness.db for data storage)

 - Conda for environment management

 - Python Standard Library modules:

   - logging (`logger.py`)

   - sqlite3 (`database.py`)

### Frontend
 - **HTML5** (`templates/`)

 - CSS3

 - Jinja2 templating

### AI Components
 - Custom workout generation logic (`workout_generator.py`)

 - Chat agent implementation (`chat_agent.py`)

### Development Tools
 - .env for environment configuration

 - requirements.txt for dependency management

 - Comprehensive logging system (`logger.py`)

## Project Structure
    FitAgent/
    ├── _pysache/                       # Main application package
    │   ├── __pycache__/                # Python bytecode cache
    │   │   ├── api.cpython-312.pyc
    │   │   └── logger.cpython-312.pyc
    │   ├── templates/                  # Frontend templates
    │   │   ├── base.html               # Base template
    │   │   ├── chat.html               # Chat interface
    │   │   ├── home.html               # Home page
    │   │   ├── register.html           # User registration
    │   │   ├── result.html             # Workout results
    │   │   └── workout.html            # Workout display
    │   ├── .conda                      # Conda environment config
    │   ├── .env                        # Environment variables
    │   ├── api.py                      # API endpoints
    │   ├── app.log                     # Application log file
    │   ├── app.py                      # Main application entry point
    │   ├── chat_agent.py               # AI chat functionality
    │   ├── database.py                 # Database operations
    │   ├── fitness.db                  # SQLite database
    │   ├── logger.py                   # Logging configuration
    │   ├── README.md                   # Project documentation
    │   ├── requirements.txt            # Python dependencies
    │   └── workout_generator.py        # Workout generation logic


## Installation Guide
### Prerequisites
 - Python 3.12+

 - Conda (recommended)

 - pip

### Setup Instructions
1. Clone the repository:

```bash
git clone [repository-url]
cd ITAGENT/_pysache
```

2. Create and activate a Conda environment:

```bash
conda create --name itagent python=3.12
conda activate itagent
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:

```bash
python database.py
```

6. Run the application:

```bash
python app.py
```

## Usage
1. Access the web interface at http://localhost:5000

2. Register a new account or log in

3. Interact with the chat agent to:

    - Set fitness goals

    - Receive workout recommendations

    - Track progress

4. View generated workouts in the workout interface


## API Documentation
The application provides RESTful API endpoints (api.py) for:

 - User authentication

 - Workout generation

 - Chat interactions

 - Progress tracking

Access the API documentation at `http://localhost:5000/api/docs` after starting the application.




