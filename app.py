from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title='My Webpage', page_icon=":tada:",layout="wide")

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  

#------Load Assets----
lottie_coding = load_lottieur("https://assets10.lottiefiles.com/packages/lf20_zrqthn6o.json")       
img_contact_form = Image.open("images/Cover.jpg")
img_lottie_animation = Image.open("images\Cover.jpg")

#----HEADER SECTION------

st.subheader("Hi,Iam AswinJoseph :wave:")
st.title("A Data Scientist From India")
st.write("Iam passionate about finding ways to use Python and VBA to be more efficient and efective in business settings.")
st.write("[Learn More >](https://www.youtube.com/channel/UC37vyFV_XjFwou4oX5F3sFA)")

#--------What I Do-----------
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my Youtube channel Iam creating tutorials for people who:
            - are lookin for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive task in Excel and are looking for a way to use Python
            - want to learn Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way.
            
            If this sounds intresting to you, consider subscribing and turning on the notifications
            """
        ) 
        st.write("[You Tube Channel >](https://www.youtube.com/channel/UC37vyFV_XjFwou4oX5F3sFA)")
        
    with right_column:
        st_lottie(lottie_coding,height=300, key='codings')

# ---------Projects----------

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader('INtegrate Lottie Animations Inside your Streamlit App')
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animation make your web app more engagging and fun, and Lttie Files are the easiest way to do it
            In  this turorial, I'll show you exactly how to do it
            """
        )    
        st.markdown("[Watch Video...](https://youtu.be/Wtmmv7Q0LcQ)")    

# #--------Contact------ "https://formsubmit.co"
# with st.container():
#     st.write('---')
#     st.header("Get In Touch with Me!")
#     st.write("##")

#     contact_form = """
#     <form action="https://formsubmit.co/aswin.joseph2011@email.com" method="POST">
#         <input type= "hidden" name="_captcha" value="false">
#         <input type="text" name="name" placeholder= "Your name" required>
#         <input type="email" name="email" placeholder= "Your email" required>
#         <textarea name = "message" placeholder= "Your message here" required></textarea>
#         <button type="submit">Send</button>
#         </form>
#     """
#     left_column,right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()    
