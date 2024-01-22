import streamlit as st
import base64
from random import choice
import models

suggested_posts = ["hello world"]
# Begin Streamlit app
st.set_page_config(page_title="Convo", layout="wide")

# Function to load and encode the logo image
def load_logo(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
def calculate_convo_score(post):

    a,b = models.sentimentAnalyser(post) # type, score
    global suggested_posts
    suggested_posts.append(models.convertor(post))
    # st.session_state["current_post"] = models.convertor(post)
    models.convertor(post)
    score = b
    # score += min(len(post) / 100, 0)  # Up to 3 points for length
    # score += post.count('?') * 2  # 2 points for each question
    # score += post.count('!')  # 1 point for each exclamation mark
    # score = min(score, 10)  # Cap the score at 10
    return score


def get_score_style(score):
    if score == 10:
        color = "#0FEF34"  # Green
        message = "Great post!"
    elif score >= 7:
        color = "#FFEB3B"  # Yellow
        message = "Pretty good post"
    elif score >= 5:
        color = "#FF9800"  # Orange
        message = "Could be better"
    else:
        color = "#f44336"  # Red
        message = "Needs work"
    return color, message




# Function to get a random post from the list of suggested posts
def get_random_post():
    st.session_state['current_post'] = choice(suggested_posts)

# Initialize the current post in session state if not already done
if 'current_post' not in st.session_state:
    st.session_state['current_post'] = models.convertor("Hello world")

# Paths to your images - replace these with the actual file paths on your system
logo_path = "images/img.jpg"  # Replace with the path to your logo image

# Load and encode the logo
logo_encoded = load_logo(logo_path)

# Custom CSS for styling
st.markdown(f"""
<style>

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}
div.block-container {{
    max-width: calc(100% - 2rem);
}}

.header, .header h1, .header h2 {{
    color: #FFFFFF;
}}
            
/* Remove the padding and margin from the specific Streamlit layout divs */
div.streamlit-container {{
    padding: 0px 0px !important;
    margin: 0px 0px !important;
}}
div.block-container {{
    padding: 0px 0px !important;
    margin: 0px 0px !important;
}}
/* Main app background color */
body, .main {{
    padding: 0 !important;
    margin: 0 !important;
}}
/* Hide the entire header section */
[data-testid="stHeader"] {{
    display: none !important;
}}

/* Adjust the top margin/padding of the main content if necessary */
.main .block-container {{
    margin-top: 0 !important;
    padding-top: 0 !important;
}}

/* Ensure the top-level elements stretch to full width after removing the hamburger menu */
div.block-container {{
    max-width: 100%;
}}

/* Header with gradient background and white text */
.header {{
position: relative;
width: 100%;
height: 400px;
left: 0%;
right: 0%;
top: 0%;
bottom: 0%;
background: linear-gradient(180deg, #0FEF34 -15.36%, #1DA6DB 42.43%, #022D60 120%);
color: #FFFFFF;
padding: 10px 10px;
text-align: center;
margin-top: -17px;
padding: 4rem 1rem;  /* Adjust the padding to fit your search bar */  
}}
            

/* Logo with white background and circular border */
.img-fluid {{
    background-color: white;
    padding: 10px;
    border-radius: 20%;
    margin-top: 2%;      
    width: 20%  
}}
            
.stTextArea {{
    margin-top: 2%; /* Pull the text area up into the header */
    width: 70% !important;
    margin-left: auto;
    margin-right: auto;
     border-radius: 0px;
    z-index: 3; /* Corrected property name for stacking order */
}}

.stTextArea>div>div>textarea {{
    background-color: #b7bbbc;
    border: 1px solid #ced4da;
    height: 100px; /* Adjust height as necessary */
}}

/* Hide the label of the text area */
.stTextArea label {{
    display: none;
}}

            
/* Custom button styling */
.stButton > button {{
    font-size: 18px;  
    margin-top: 0%;/* Adjust this value to move the button up into the header */
    # z-index: 5; /* Ensure the button is above other elements */
    background: #adc9c6;
    border-radius: 4px;
    position: absolute;
    left: 29.5%;
    right: 30.5%;
    font-family: 'Arvo';
    font-style: normal;
    font-weight: 700;
    font-size: 12px;
    line-height: 15px;
    text-align: center;
    color: #FFFFFF;
}}
            
.stButton > button:hover {{
          color: #FFFFFF;  
          background: #17ca88;
          border: #FFFFFF;
}}
            

/* Base styles for the score boxes */
.convo-score-container {{
    position: relative;
    width: 100%;
    text-align: center;
    margin-top: 3%; /* Adjust as necessary */
}}

.convo-score-meter {{
    position: relative;
    display: inline-block;
    width: 150px; /* Adjust as necessary */
    height: 150px; /* Adjust as necessary */
    border: 13px solid #D9D9D9;
    border-radius: 50%; /* Makes it circular */
    text-align: center;
    line-height: 120px; /* Adjust as necessary */
}}

.convo-score-value {{
    font-family: 'Barlow', sans-serif;
    font-weight: 500;
    font-size: 1.75rem; /* Adjust as necessary */
    color: #A7A7A7;
    vertical-align: middle;
}}

.convo-score-label {{
    font-family: 'BR Candor', sans-serif;
    font-weight: 700;
    font-size: 2.5em;/* Adjust as necessary */
    color: #022D60;
    margin-top: 20px; /* Adjust as necessary */
}}

.convo-score-description {{
    font-size: 1.4em; /* Adjust as necessary */
    color: #333;
    margin-top: 2% !important; /* Adjust as necessary */
    width: 80%; /* Adjust as necessary */
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}}
            
.Discourse{{
    position: relative;
    width: 100%;
    padding: 20px 20px;
    text-align: center;
}}        

.Suggested{{
    font-family: 'BR Candor', sans-serif;
    font-weight: 700;
    font-size: 2em;/* Adjust as necessary */
    color: #022D60;
    margin-top: 20px; /* Adjust as necessary */
    padding-left: 15%;
    margin-bottom: 10px;
}}    

button {{
    display: inline-block;
    padding: 0.5em 1.5em;
    margin: 0.5em;
    font-size: 16px; /* Adjust the font size as needed for mobile view */
}}
.copy-button{{
    display: inline-block;
    padding: 0.5em 5em;
    font-size: 1em;
    font-family: 'Arvo', sans-serif;
    font-weight: 700;
    color: #FFFFFF;
    background-color: #1da6db; /* Your desired button color */
    border: none;
     border-radius: 10px;
    cursor: pointer;
    text-align: center;
    margin-left: 30.5%;
    margin-top: -5% !important;
    border: 3.5px solid #1da6db;
            
}}
            
.reroll-button{{
   
    padding: 0.5em 5em;
    font-size: 1em;
    font-family: 'Arvo', sans-serif;
    font-weight: 700;
    color: #1da6db;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    text-align: center;
    margin-left: 42%;
    margin-top: -50% !important;  
    border: 3.5px solid #1da6db;
}}            

.copy-button:hover  {{
    background-color: white;
    color: #1da6db;
    border: 3.5px solid #1da6db;    
}}
            
.reroll-button:hover{{
    background-color: #1da6db;
    color: #FFFFFF;
}}
        
.original{{
    font-family: 'BR Candor', sans-serif;
    font-weight: 700;
    font-size: 2em;/* Adjust as necessary */
    color: #022D60;
    margin-top: 20px; /* Adjust as necessary */
    padding-left: 15%;
    margin-bottom: 10px;     
}}

.frames{{
   display: flex; 
   align-items: center; 
   gap: 10px; 
   padding-left: 15%;
   padding-top: 2%; 
   padding-bottom: 1%;         

}}
            

.circle{{
            width: 70px; 
            height: 70px; 
            border-radius: 50%; 
            border: 10px solid #65C466; 
            display: flex;
}}
.convo-score-description {{
    font-size: 1.4em; /* Adjust as necessary */
    color: #333;
    margin-top: 20px; /* Adjust as necessary */
    width: 80%; /* Adjust as necessary */
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}}
            
.Discourse{{

   font-size: 1.4em; /* Adjust as necessary */
    color: #333;
    width: 80%; /* Adjust as necessary */
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}}           

/* Media query for mobile devices to adjust the header, search bar, and button */
@media (max-width: 768px) {{
    .header {{
      margin-top: -4%;
    }}

    .img-fluid {{
          background: #FFFFFF;
          border-radius: 25px;
          width: 40%;   
       
    }}
            
.stTextArea {{
    width: 80% !important;
    border: 4px solid #1da6db;
    border-radius: 10px

}}
/* Hide the label of the text area */
.stTextArea label {{
    display: none;
}}
            
.Suggested{{
    padding-left: 11%;
    font-size: 1.5em;/* Adjust as necessary */
}}    

            
.copy-button, .reroll-button {{
        cursor: pointer;
        width: 80%; 
        margin-top: 0px; 
        margin-bottom: 8px; 
        margin-left: 10%; 
        padding: 7px 0; 
        font-size: 14px; /* Adjust font size for mobile if needed */
}}

.copy-button {{
        order: 1; /* Ensure 'Copy' is on top */
}}
    
.reroll-button {{
         margin-top: -10px; 
        order: 2; /* Ensure 'Reroll' is below 'Copy' */

}}

.copy-button:hover  {{
    background-color: white;
    color: #,1da6db;
    border: 3.5px solid #1da6db;    
}}
            
.reroll-button:hover{{
    background-color: #1da6db;
    color: #FFFFFF;
}}
            

        
.frames{{
   display: flex; 
   align-items: center; 
   gap: 5px; 
   padding-left: 5%; 
   padding-bottom: 1%;         

}}
            
.circle{{
        width: 130px; 
        height: 60px; 
        border-radius: 50%; 
        border: 7px solid #65C466; 
            
}}
        
            
.stButton > button {{
    background: #adc9c6;
    border-radius: 4px;
    position: absolute;
    left: 11%;
    right: 11%;
}}
            
.convo-score-container {{
    margin-top: 10%; /* Adjust as necessary */
}}

}}

@media (min-width: 300px) and (max-width: 550px) {{
    .stTextArea>div>div>textarea {{
        background-color: #eff3f6;
        border-radius: 20px;
        height: 120px; /* Adjust height for mobile */
    }}

    /* Hide the label of the text area on mobile */
    .stTextArea label {{
        display: none;
    }}
 .img-fluid {{
          background: #FFFFFF;
          border-radius: 25px;
          width: 40%;   
       
    }}
    .convo-score-container {{
    margin-top: 10%; /* Adjust as necessary */
}}

    
}}


@media (min-width: 550px) and (max-width: 750px) {{
   .convo-score-container {{
    margin-top: 10%; /* Adjust as necessary */
}}
            

}}

@media (min-width: 750px) and (max-width: 1000px) {{
   .convo-score-container {{
    margin-top: 5%; /* Adjust as necessary */
}}
            
}}
    

</style>
""", unsafe_allow_html=True)

# Inject the logo into the header
st.markdown(f"""
    <div class="header" style="text-align: center; color: #FFFFFF;">
        <img src="data:image/png;base64,{logo_encoded}" class="img-fluid" alt="Convo logo">
        <h1>Get people talking</h1>
        <h2>Power up your posts to foster meaningful conversation</h2>
    </div>
""", unsafe_allow_html=True)

# Container for the input field and custom upload button
user_input = st.text_area("Post Input", height=150, placeholder="Paste your post here, and we’ll tell you how likely it is to foster productive conversation")


# Custom file uploader button
# st.file_uploader(f"", type=['png', 'jpg', 'jpeg'])


# Button for analyzing post
analyze_button = st.button('Analyze Post')

# Container to hold the success message, placed above the score circle
success_message_container = st.empty()

# Container to hold the score circle
score_container = st.empty()

# Show initial score circle with score 0
score_container.markdown(f"""
<div class="convo-score-container">
    <div class="convo-score-meter">
        <span class="convo-score-value"> <strong>0</strong>/10</span>
    </div>
    <div class="convo-score-label">convo score</div>
</div>
""", unsafe_allow_html=True)
# Button action
if analyze_button:
    if user_input:
        # Calculate the score
        global x 
        x = user_input
        score = calculate_convo_score(user_input)
        
        # Get the color and message based on the score
        color, message = get_score_style(score)
        
        
        # Update the score circle with dynamic border color and update the score value inside the circle
        score_container.markdown(f"""
        <div class="convo-score-container">
            <div style="color: {color}; font-size: 2em; font-weight: bold; margin-bottom: 10px;">{message}</div>
            <div class="convo-score-meter" style="border: 13px solid {color};">
                <span class="convo-score-value">{score}/10</span>
            </div>
            <div class="convo-score-label">convo score</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        success_message_container.error("Please enter a post to analyze.")

st.markdown("""
<h5 class="convo-score-description">
    We've studied thousands of conversations to identify the elements of posts that lead to the most discussions online, the higher your post's convo score, the more your post contains the elements that lead to discussion.
</h5>
""", unsafe_allow_html=True)

st.markdown("""
  <div class="frames" >
    <div class="circle">
    </div>
    <div class="content" style="padding-top: 15px;"><h5>
            This suggested post frames the content in a more conversational manner, and includes a question.</h5></div>
  </div>
""", unsafe_allow_html=True)


st.markdown("""
  <div class="Suggested"> Suggested Post</div>
""", unsafe_allow_html=True)
suggested_post_area = st.empty()
suggested_post_area.text_area("Suggested Post",height=150, help="This is your suggested post. Feel free to edit!")
txt = models.convertor(user_input)

if user_input:
    txt = models.convertor(user_input)
    # logtxtbox.text_area("Logging: ",txt, height = 500)
# Suggested Post section with buttons
    suggested_post_area.empty()
    suggested_post_area.text_area("Suggested Post", txt ,height=150, key="post_area", help="This is your suggested post. Feel free to edit!")


reroll_button = st.button("Reroll")

if reroll_button:
    pass
# # Placing the buttons in the same row
# col1, col2 = st.columns([1, 1], gap="small")
# reroll_button = st.button("Reroll")
# with col1:
#     # Custom 'Copy' button
#     reroll_button.markdown(f"""
#     <button class="copy-button" onclick="navigator.clipboard.writeText(`{st.session_state['current_post']}`)">Copy</button>
#     """, unsafe_allow_html=True)

# with col2:
#     # Custom 'Reroll' button
#     reroll_button = st.markdown("""
#     <button class="reroll-button" onclick="models.convertor()">Reroll</button>
#     """, unsafe_allow_html=True)
# # if reroll_button:
# #     print("reroll pressed")


st.markdown(f"""
    <div class="Discourse" style="text-align: center; "> 
        <h1>Creating Healthy Discourse</h1>
        <h5>AI can be a powerful tool for modeling healthy conversations that promote understanding, empathy, and growth. Our models have analyzed hundreds of thousands of posts to learn what makes a post lead to productive discourse. When you share your post drafts with Convo, we rate it and offer suggestions for how it can be better. </h5>
    </div>
""", unsafe_allow_html=True)
