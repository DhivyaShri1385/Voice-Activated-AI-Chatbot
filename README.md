# Voice-Activated-AI-Chatbot

Objective:

The purpose of this project is to develop a voice-activated AI chatbot using Python that can understand voice commands, respond through speech, and perform a range of useful tasks. The chatbot serves as a personal virtual assistant, capable of accessing online information, automating basic system functions, and interacting with the user in natural language.

Key Features:

1. Speech Recognition:
Utilizes the user's microphone to capture voice input.
Converts speech to text using the SpeechRecognition library.

2.  Text-to-Speech Response:
The chatbot replies using audible speech.
Implemented using the pyttsx3 library for offline voice output.

3. Smart Greeting System:
Greets the user appropriately based on the current time (e.g., Good morning/afternoon/evening).
Enhances personalization and user experience.

4. Web Automation:
Opens commonly used websites through voice commands.

Example: “Open Google” → launches the Google homepage.
Uses Python’s built-in webbrowser module.

5. Wikipedia Integration:
Can search Wikipedia and summarize results out loud.
Supports queries like “Wikipedia Python programming”.

6. Time and System Control:
Announces the current system time.
Can perform system operations like:
Shutdown
Restart
Lock the computer

7. Note Taking:
Voice-based note creation and reading.

Commands:
“Write a note” → records a voice note into a text file.
“Read note” → reads the saved note out loud.

8. Exit Command:
Listens for “exit” or “stop” to gracefully close the chatbot.

Technologies Used:

Component	Tool/Library
Programming Language	Python 3.8+
Speech Recognition	speechrecognition
Text-to-Speech	pyttsx3
Wikipedia Access	wikipedia-api
Web Automation	webbrowser (built-in)
System Functions	os, ctypes (built-in)

How It Works:

When the script is run, the chatbot:
Greets the user.
Enters a loop, continuously listening for voice input.
The user gives a voice command:
The chatbot converts the voice to text.
The text is matched against predefined commands.
The chatbot executes the matching command:
Speaks the result back to the user.
Performs the action (e.g., opens a website, tells the time, saves a note).
The loop continues until the user says “exit” or “stop”.

Learning Outcomes:

By building this project, you gain hands-on experience with:
Voice-based input and output in Python
Natural Language Processing fundamentals
Python automation and scripting
File handling and basic system control
Real-world use of third-party libraries
