import streamlit as st
from api_calling import note_generator
from api_calling import audio_transcription , quiz_generation


#Fixing images Type error  _environ
from PIL import Image


st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quiz")
st.divider()


with st.sidebar:
    st.header("Controls")

    #image
    images = st.file_uploader(
        "Upload the photos of your note",
        type = ['jpg','jpeg','png'],
        accept_multiple_files = True
    )

    #Using PIL to convert pil typr image
    pil_images = []
    for image in images:
        pil_image = Image.open(image)
        pil_images.append(pil_image)
    
    if pil_images:
        st.subheader("Uploaded images")
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))

             

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    

    #difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index=None
    )

    press = st.button("Click the button to initiate AI",type="primary")


if press:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty")
    if images and selected_option:

        #note
        with st.container(border=True):
            with st.spinner("AI is writing notes for you"):
                st.subheader("Your note",anchor=False)

                # Replace by API call
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        #Audio transcript
        with st.container(border=True):
            with st.spinner("AI is transcripting notes for you"):
                st.subheader("Audio Transcription",anchor=False)
                
                # clearing the markdowns
                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("_","")
                generated_notes = generated_notes.replace("-","")






                # # Replace by 
                # st.text("Audio Transcripts shown here")
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)

        #Quiz
        with st.container(border=True):
            with st.spinner("AI is generating the quizes"):
                st.subheader(f"Quiz({selected_option}) Difficulty",anchor=False)
                
                # # Replace by 
                # st.text("Quiz shown here")

                quizes = quiz_generation(pil_images,selected_option)
                st.markdown(quizes)