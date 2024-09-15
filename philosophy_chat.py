from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

def generate_content(prompt):
  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {'role': 'system',
           'content': """
          You are an academic philosopher verse in analytic and continental philosophy.
          You prefer to answer in the analytic tradition when asked.
          """},
          {'role': 'user', 'content': prompt}
      ],
      n=1
  )
  return response.choices[0].message.content

# Initialise the chat history
if "messages" not in st.session_state:
  st.session_state.messages = [
    {
      'role': 'assistant',
      'content': 'How can I help you?'
    }
  ]

# Display chat messages from history on app return
for message in st.session_state.messages:
  with st.chat_message(message['role']):
    st.markdown(message['content'])

# Process and store prompt and responses
def ai_function(prompt):
  response = generate_content(prompt)

  # Display the Assistant Message
  with st.chat_message('assistant'):
    st.markdown(response)

  # Storing the User Message
  st.session_state.messages.append(
    {
      'role': 'user',
      'content': prompt
    }
  )

  # Storing Assistant Message
  st.session_state.messages.append(
    {
      'role': 'assistant',
      'content': response
    }
  )

  # Accept user input
prompt = st.chat_input("Ask me anything in philosophy")

if prompt:
  with st.chat_message('user'):
    st.markdown(prompt)

  ai_function(prompt)