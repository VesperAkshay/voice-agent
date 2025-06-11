# Indian Grievance Resolver - Voice Assistant

A voice-enabled grievance resolution system that helps citizens register and track their complaints with government services. This application provides multi-language support and integrates with government grievance portals to streamline the complaint resolution process.

#### 🎥 Demo: Working Prototype in Action

Watch the full walkthrough of our AI-powered citizen grievance redressal system:

[![WhatsApp Image 2025-06-11 at 15 38 02_06bb7a2b](https://github.com/user-attachments/assets/4f910cfb-fe26-4e1b-9d38-f5fb938b6325)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)





## Features

- **Multi-language Support**: Interact in English, Hindi, and other regional languages
- **Voice-Enabled**: Use natural language to register and track grievances
- **Real-time Updates**: Get instant notifications about your complaint status
- **Government Scheme Information**: Access details about relevant government schemes
- **User-Friendly Interface**: Simple and intuitive web interface for all users

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- Node.js 14+ (for frontend assets)
- Google Cloud credentials for speech-to-text and text-to-speech

### 2. Install Dependencies

First, create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Or on macOS/Linux
# source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```
# Google Cloud Credentials
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json

# Application Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
HOST=0.0.0.0
PORT=8000

# Database Configuration
DATABASE_URL=sqlite:///grievance.db
```

### 4. Initialize Database

```bash
# Run database migrations
python manage.py db upgrade

# Create initial admin user
python manage.py create_admin
```

### 5. Start the Application

#### Development Mode

```bash
# Start the development server
python manage.py run

# The application will be available at http://localhost:8000
```

#### Production Mode

For production deployment, use a production WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

## Using the Grievance Resolver

### Voice Commands

You can interact with the system using natural language:

- "Register a new grievance"
- "Check my complaint status"
- "Update my contact information"
- "What government schemes am I eligible for?"
- "Explain the grievance resolution process"
- "I need help with a land dispute"
- "What documents do I need to submit?"
- "Track my application status"

### Web Interface

The web interface provides:

1. **Dashboard**: Overview of your grievances and their status
2. **New Grievance**: File a new complaint with voice or text input
3. **Track Status**: Check the current status of your complaints
4. **Profile**: Update your personal information and preferences
5. **Help Center**: Find answers to common questions

#### 💻 Web Application Screens (User Interface Overview)

![WhatsApp Image 2025-06-11 at 13 51 19_11633e74](https://github.com/user-attachments/assets/09b72b28-c6fc-4260-b79e-182cc557f95b)

#### 🖼️ Interface Walkthrough: Dashboard & Contact Us

![WhatsApp Image 2025-06-11 at 13 50 35_5740da8b](https://github.com/user-attachments/assets/980c4afd-1980-4969-8ba8-d4a63995e11d)

![WhatsApp Image 2025-06-11 at 13 50 31_8c36952f](https://github.com/user-attachments/assets/2b1da372-048e-4509-8b14-575800ee3c4e)


## API Documentation

The system provides RESTful APIs for integration with other services:

- `POST /api/grievances` - Register a new grievance
- `GET /api/grievances` - List all grievances
- `GET /api/grievances/<id>` - Get grievance details
- `PUT /api/grievances/<id>` - Update grievance status
- `GET /api/schemes` - List available government schemes

## Multi-language Support

The system supports multiple Indian languages. To change the language:

1. Click on the language selector in the top-right corner
2. Select your preferred language
3. The interface and voice assistant will switch to the selected language

Available languages:
- English (en)
- Hindi (hi)
- Bengali (bn)
- Tamil (ta)
- Telugu (te)
- Marathi (mr)
- Gujarati (gu)
- Kannada (kn)
- Malayalam (ml)
- Punjabi (pa) Cleaning'"

## Running the Application

After completing the setup, you can run the application using the following command:

```bash
# Start the ADK Voice Assistant with hot-reloading enabled
uvicorn main:app --reload
```

This will start the application server, and you can interact with your voice assistant through the provided interface.

## Troubleshooting

### Voice Recognition Issues

If the system has trouble understanding your voice:

1. Ensure you're in a quiet environment
2. Speak clearly and at a moderate pace
3. Check your microphone permissions in browser settings
4. Try using the text input method instead

### Grievance Submission Problems

If you encounter issues submitting a grievance:

1. Check your internet connection
2. Ensure all required fields are filled
3. Verify the file attachments (if any) meet the requirements
4. Try refreshing the page and submitting again

### Common Error Messages

- **"Unable to process request"**: Server might be down, try again later
- **"Authentication failed"**: Log out and log back in
- **"File size too large"**: Ensure attachments are under 5MB
- **"Invalid input"**: Check that all fields contain valid information

## Security and Privacy

- All communications are encrypted using HTTPS
- Personal information is stored securely and never shared without consent
- Regular security audits are conducted to protect user data
- Users can request data deletion at any time through their profile settings

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description of your changes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support or to report issues, please contact:
- Email: support@grievance-resolver.gov.in
- Helpline: 1800-XXX-XXXX (Toll-free)
- Visit your nearest Common Service Center (CSC)
