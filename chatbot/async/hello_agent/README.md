# Gemini AI Chat Assistant

A conversational AI assistant built with Chainlit and Google's Gemini AI model. This application provides a chat interface where users can interact with a helpful AI assistant powered by Gemini-2.0-flash.

## Features

- Interactive chat interface using Chainlit
- Powered by Google's Gemini AI model
- Conversation history management
- Environment variable configuration
- Asynchronous request handling

## Installation

This project uses UV as the package manager. To get started:

1. Install UV if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:
```bash
git clone https://github.com/yourusername/gemini-chat-assistant.git
cd gemini-chat-assistant
```

3. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Gemini API key:
```env
GEMINI_API_KEY=your_api_key_here
```

## Dependencies

The main dependencies for this project are:
- chainlit
- python-dotenv
- agents (custom package for AI agent management)

To install dependencies:
```bash
uv add chainlit python-dotenv
```

## Usage

To run the chat application:

```bash
chainlit run main.py
```

The application will start a local server, and you can access the chat interface through your web browser.

## Project Structure

```
project/
├── main.py              # Main application file
├── agents/              # Agent management module
├── .env                 # Environment variables
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Development

To set up the development environment:

1. Install development dependencies:
```bash
uv pip install -r requirements-dev.txt
```

2. Lint code:
```bash
ruff check .
ruff format .
```

## How It Works

The application:
1. Initializes a chat interface using Chainlit
2. Connects to the Gemini AI model through the OpenAI-compatible API
3. Maintains conversation history for context
4. Processes user messages asynchronously
5. Returns AI-generated responses in real-time

## Environment Variables

Required environment variables:
- `GEMINI_API_KEY`: Your Google Gemini API key

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)
Project Link: [https://github.com/yourusername/gemini-chat-assistant](https://github.com/yourusername/gemini-chat-assistant)
