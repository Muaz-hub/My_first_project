from google import genai
from dotenv import load_dotenv
import os , io
from gtts import gTTS



#Loading the environment variable
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#initialzing a client
client = genai.Client(api_key = my_api_key)



# not generator
def note_generator(images):
    prompt = """Summarize the picture in note format at max 100 words,
     make sure to add neccessary markdown to differentiate different secton"""


    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,prompt]
    )

    return response.text


def audio_transcription(text):
    speech = gTTS(text,lang='en',slow=False )

    # it will be saved in local memory it's not efficient way
    # speech.save("welcome.mp3")

    audio_buffer = io.BytesIO()

    #This line creates a places in RAM 
    # and written to the speech ,
    # Now it will not be stored in local memory
    speech.write_to_fp(audio_buffer)

    return audio_buffer


def quiz_generation(images,difficulty):

    prompt = f"Generate 3 quizes based on the {difficulty} . Make sure to add markdown to differentiate the options. Add correct answers after the quizes too"
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,prompt]
    )

    return response.text