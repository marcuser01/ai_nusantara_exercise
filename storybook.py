from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

def story_generator(prompt):
  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {'role': 'system',
           'content': """
          You are an accomplished storyteller. You have published short stories for 10 years.
          Given a topic, you can write quality fantasy stories with an interesting twist.
          The story is only about 100-150 words long.
          """},
          {'role': 'user', 'content': prompt}
      ],
      temperature = 1.3
  )
  return response.choices[0].message.content

def cover_prompt(prompt):
  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {'role': 'system',
           'content': """
          You are tasked with generating a prompt for an AI image generator.
          A fantasy story will be given and you have to analyse and digest the contents and extract the main element/essence of the story.

          Write a short prompt to produce an interesting and relevant cover art for the story.
          """},
          {'role': 'user', 'content': prompt}
      ],
      temperature = 1,
      max_tokens = 1000
  )
  return response.choices[0].message.content

def cover_art(prompt):
  response = client.images.generate(
      model = 'dall-e-3',
      prompt = prompt,
      size = '1024x1024',
      quality = 'standard',
      n= 1,
      style = 'vivid'
  )
  return response.data[0].url

def storybook(prompt):
  story = story_generator(prompt)
  cover = cover_prompt(story)
  image = cover_art(prompt)

  st.image(image)
  st.caption(cover)
  st.divider()
  st.write(story)

prompt = st.text_input("Give me a story topic")
if st.button("Generate story"):
  storybook(prompt)

