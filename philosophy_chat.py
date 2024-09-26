from openai import OpenAI
import streamlit as st
from streamlit_option_menu import option_menu
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from PIL import Image
import os

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer() 

# Sidebar selection
with st.sidebar:
    selected_philosopher = option_menu("Choose your Philosopher", 
                        ["Socrates", "Diogenes", "Confucius", "Friedrich Nietzsche", 
                         "Immanuel Kant", "Simone de Beauvoir"], 
                        default_index=0)
    st.write("You selected: ", selected_philosopher)

    # Descriptions for each philosopher
    if selected_philosopher == "Socrates":
        st.write("Socrates was a classical Greek philosopher credited as one of the founders of Western philosophy. He is known for his Socratic method, a form of cooperative argumentative dialogue.")
    elif selected_philosopher == "Diogenes":
        st.write("Diogenes was a Greek philosopher and one of the most famous figures of Cynicism. He is best known for his ascetic lifestyle and his criticism of social norms and conventions.")
    elif selected_philosopher == "Confucius":
        st.write("Confucius was a Chinese philosopher and politician of the Spring and Autumn period. His teachings, preserved in the Analects, emphasize morality, social relationships, and justice.")
    elif selected_philosopher == "Friedrich Nietzsche":
        st.write("Friedrich Nietzsche was a German philosopher known for his critique of traditional morality and religion. He is famous for his concept of the Übermensch and the declaration that 'God is dead.'")
    elif selected_philosopher == "Immanuel Kant":
        st.write("Immanuel Kant was an 18th-century German philosopher whose work on epistemology and ethics had a profound influence on modern philosophy. He is best known for his theory of the categorical imperative.")
    elif selected_philosopher == "Simone de Beauvoir":
        st.write("Simone de Beauvoir was a French existentialist philosopher, writer, and feminist. She is best known for her work 'The Second Sex,' in which she analyzed women's oppression and the construction of gender roles.")

# Set up app title
st.title("💬 Philosophy Chat-o-Battle ⚔️")

# Function to generate response content
def generate_content(prompt):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'system',
                'content': f"You are roleplaying {selected_philosopher}, the philosopher, and you will be engaging in a debate. You have to express your answer with the personality, writing style, and knowledge of the philosopher. You can exaggerate your emotions based on these 4 (neutral, amused, curious, irritated), ask questions, defend your position or clarify jargon, etc."
            },
            {'role': 'user', 'content': prompt}
        ],
        n=1
    )
    return response.choices[0].message.content

# Function to analyze sentiment and determine the emotion
def get_emotion_from_response(response):
    sentiment_score = analyzer.polarity_scores(response)['compound']  # Get compound score from VADER

    if sentiment_score >= 0.5:
        return "amused"  # Strongly positive sentiment
    elif sentiment_score > 0:
        return "curious"  # Mildly positive sentiment
    elif sentiment_score == 0:
        return "neutral"  # Neutral sentiment
    else:
        return "irritated"  # Negative sentiment

# Initialize chat history for each philosopher
if "philosopher_chats" not in st.session_state:
    st.session_state.philosopher_chats = {
        "Socrates": [],
        "Diogenes": [],
        "Confucius": [],
        "Friedrich Nietzsche": [],
        "Immanuel Kant": [],
        "Simone de Beauvoir": []
    }


# Define the path for the neutral image based on the selected philosopher
neutral_image_path = f"./philosopher_images/{selected_philosopher.lower()}_neutral.png"
if os.path.exists(neutral_image_path):
        image = Image.open(neutral_image_path)
        st.image(image, caption=f"{selected_philosopher}", use_column_width=False, width=300)
        
# If there's no history for the selected philosopher, initialize it with a greeting
if not st.session_state.philosopher_chats[selected_philosopher]:
    st.session_state.philosopher_chats[selected_philosopher].append({
        'role': 'assistant',
        'content': f"I am {selected_philosopher}. How can I help you?"
    })

# Display chat messages from the current philosopher's history
for message in st.session_state.philosopher_chats[selected_philosopher]:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
# Function to process user input and get AI response
def ai_function(prompt):
    response = generate_content(prompt)
    emotion = get_emotion_from_response(response)

    # Display and store the user's message
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.philosopher_chats[selected_philosopher].append(
        {
            'role': 'user',
            'content': prompt
        }
    )

    image_filename = f"./philosopher_images/{selected_philosopher.lower()}_{emotion}.png"
        
    # Check if the file exists
    if os.path.exists(image_filename):
        # Load and display the image
        image = Image.open(image_filename)
        st.image(image, caption=f"{selected_philosopher} feeling {emotion}", use_column_width=False, width=256)
    else:
        st.write(f"No image found for {selected_philosopher} feeling {emotion}.")

    # Display and store the assistant's message
    with st.chat_message('assistant'):
        st.markdown(response)
    st.session_state.philosopher_chats[selected_philosopher].append(
        {
            'role': 'assistant',
            'content': response
        }
    )


# Accept user input
prompt = st.chat_input("Ask me anything in philosophy")

# If there's a prompt, process it
if prompt:
    ai_function(prompt)
