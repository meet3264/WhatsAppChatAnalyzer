# WhatsApp Chat Analyzer

## Overview

The WhatsApp Chat Analyzer is a Python application that allows users to analyze their WhatsApp chat data. It provides insights such as the total number of messages, words count, media shared, links shared, and a visual representation of chat activity over time. The application utilizes the Streamlit library for an interactive user interface, along with data processing libraries like pandas and matplotlib.

## Features

- Upload a WhatsApp chat file in `.txt` format.
- View overall and user-specific statistics:
  - Total Messages
  - Total Words
  - Shared Media
  - Shared Links
- Visualize monthly and daily chat timelines.
- Identify the most active users in group chats.
- Generate word clouds and analyze common words used in chats.
- Emoji usage analysis.


## Setup Instructions

### Step 1: Clone the Repository

Clone the repository or download the files to your local machine.

```bash
git clone https://github.com/meet3264/WhatsAppChatAnalyzer.git
cd WhatsAppChatAnalyzer
```

### Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage your project dependencies. You can do this using `venv`.

**Using venv:**

```bash
python -m venv VE
```

### Step 3: Activate the Virtual Environment

After creating the virtual environment, you need to activate it.

- **On Windows:**

```bash
.\VE\Scripts\activate
```
- **On macOS and Linux:**

```bash
source VE/bin/activate
```

### Step 4: Install the required dependencies
```bash
pip install -r requirements.txt
```

## File Structure

```
/WhatsAppChatAnalyzer
├── app.py             # Main application file
├── helper.py          # Helper functions for data analysis
├── preprocessor.py    # Data preprocessing functions
├── stop_hinglish.txt  # File containing stop words for filtering
└── README.md          # Project documentation
```

## How to Use

1. Place your WhatsApp chat `.txt` file in the project directory.

2. Run the Streamlit application:

   ```bash
   streamlit run app.py

3. Open the URL provided in your terminal in your web browser.
4. Use the sidebar to upload your WhatsApp chat file and start analyzing!

## Input Format

The application expects the WhatsApp chat to be in the following format:

[Date, Time] - User: Message

For example:
```
12/01/20, 10:30 AM - John: Hey! How are you? 
12/01/20, 10:31 AM - Jane: I'm good, thanks!
```
