# Philosophy Chat-o-Battle ⚔️

Philosophy Chat-o-Battle is an AI-powered app where users can engage in debates with historical philosophers, each exhibiting different emotions (amused, curious, irritated, neutral). This app uses OpenAI's GPT-4o-mini model for generating the philosophical dialogues and DALL·E 2 images to depict emotional expressions of each philosopher.

## Features

- **Choose Your Philosopher**: Engage with one of the following philosophers:
  - Socrates
  - Diogenes
  - Confucius
  - Friedrich Nietzsche
  - Immanuel Kant
  - Simone de Beauvoir
  
- **Philosophers' Emotions**: Each philosopher responds with a unique emotion (amused, curious, irritated, or neutral) based on the tone of the conversation, and corresponding AI-generated portraits are displayed.
  
- **AI Debates**: Generate responses based on a selected philosopher’s style and knowledge through GPT-4o-mini.
  
- **Sentiment-Based Emotion Detection**: Emotions are determined based on sentiment analysis of the AI's responses.

## Problem Statement

The challenge is to create an engaging educational app that makes learning philosophy fun by simulating debates with historical philosophers, while keeping the costs of AI image and text generation manageable.

## App Architecture

- **OpenAI GPT-4o-mini** is used to generate text responses mimicking each philosopher's personality.
- **DALL·E 2** is used to generate portraits of philosophers displaying different emotions. These images are pre-generated to cut down on API usage and stored locally for quick access.
- The **Streamlit** app manages user interaction and displays the corresponding dialogue and philosopher images.

## Prerequisites

- **Python 3.8+**
- **Streamlit**
- **OpenAI API key**
- **VADER Sentiment Analysis**

### Installation

1. Clone the repository and navigate into the project directory:
    ```bash
    git clone https://github.com/marcuser01/ai_nusantara_exercise
    cd philosophy-chat
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your OpenAI API key to the `secrets.toml` file (for Streamlit):
    ```toml
    [openai]
    api_key = "your_openai_api_key_here"
    ```

4. Pre-generate the philosopher emotion images using the DALL·E 2 API by running the `image_generator.py` script:
    ```bash
    python image_generator.py
    ```

   Ensure the images are saved in the `philosopher_images/` folder.

### Running the App

To start the app locally:

```bash
streamlit run app.py
```

## Contributing

Feel free to submit issues or pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License.

