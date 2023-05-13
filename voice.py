import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the engine
engine.setProperty('rate', 150)  # Speed in words per minute
engine.setProperty('volume', 0.7)  # Volume level

# Define the text to be spoken
text = "Hello, how are you doing today?"

# Convert text to speech
engine.say(text)

# Run the engine and wait for the speech to finish
engine.runAndWait()
