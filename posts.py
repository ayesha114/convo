import streamlit as st
import base64
from random import choice


# Begin Streamlit app
st.set_page_config(page_title="Convo", layout="wide")

# Function to load and encode the logo image
def load_logo(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

suggested_posts = [
    "Based on what I've seen in my travels, it seems that the communities with the fewest financial resources have the most collaborative cultures. Have you seen the same thing?",
     "This suggested post frames the content in a more conversational manner, and includes a question."
     "Part of the reason some cultures rely more on family relationships is due to lack of resources. This is what I keep seeing."
    # ... add more suggested posts as needed
]

# Function to get a random post from the list of suggested posts
def get_random_post():
    st.session_state['current_post'] = choice(suggested_posts)

# Initialize the current post in session state if not already done
if 'current_post' not in st.session_state:
    st.session_state['current_post'] = "Part of the reason some cultures rely more on family relationships is due to lack of resources. This is what I keep seeing."

# Paths to your images - replace these with the actual file paths on your system
logo_path = "images/img2.jpg"  # Replace with the path to your logo image

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

.header, .header h1, .header h2, .header .stTextArea, .header .stButton > button {{
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
left: 0%;
right: 0%;
top: 0%;
bottom: 0%;
margin-top: -2%;
}}
            

/* Logo with white background and circular border */
.img-fluid {{
    height: 600px;
    width: 100%;   
}}
            
.stTextArea {{
    width: 70% !important;
    margin-left: auto;
    margin-right: auto;
    border-radius: 10px;
    border: 5px solid #1da6db;

}}
/* Hide the label of the text area */
.stTextArea label {{
    display: none;
}}

            

/* Base styles for the score boxes */
.convo-score-container {{
    position: relative;
    width: 100%;
    text-align: center;
    margin-top: -10%; /* Adjust as necessary */
}}

.convo-score-meter {{
    position: relative;
    display: inline-block;
    width: 170px; /* Adjust as necessary */
    height: 170px; /* Adjust as necessary */
    border: 13px solid #D9D9D9;
    border-radius: 50%; /* Makes it circular */
    text-align: center;
    line-height: 150px; /* Adjust as necessary */
}}

.convo-score-value {{
    font-family: 'Barlow', sans-serif;
    font-weight: 500;
    font-size: 48px; /* Adjust as necessary */
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
    margin-top: 20px; /* Adjust as necessary */
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

/* Media query for mobile devices to adjust the header, search bar, and button */
@media (max-width: 768px) {{
    .header {{
      margin-top: -4%;
    }}

    .img-fluid {{
          height: 300px;
          width: 100%;   
       
    }}
            
.stTextArea {{
    width: 80% !important;
    border: 4px solid #1da6db;

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
            

.original{{
    padding-left: 11%;
    font-size: 1.5em;/* Adjust as necessary */
}}
        
.frames{{
   display: flex; 
   align-items: center; 
   gap: 5px; 
   padding-left: 10%; 
   padding-bottom: 1%;         

}}
            
.circle{{
        width: 130px; 
        height: 60px; 
        border-radius: 50%; 
        border: 7px solid #65C466; 
            
}}
        

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class="header">
        <img src="data:image/png;base64,{logo_encoded}" class="img-fluid" alt="Convo logo">

    </div>
""", unsafe_allow_html=True)

# Container to hold the success message, placed above the score circle
success_message_container = st.empty()

# Container to hold the score circle
score_container = st.empty()

# Show initial score circle with score 0
score_container.markdown(f"""
<div class="convo-score-container">
    <div class="convo-score-meter">
        <span class="convo-score-value">0/10</span>
    </div>
    <div class="convo-score-label">convo score</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h5 class="convo-score-description">
    We've studied thousands of conversations to identify the elements of posts that lead to the most discussions online, the higher your post's convo score, the more your post contains the elements that lead to discussion.
</h5>
""", unsafe_allow_html=True)


st.markdown("""
  <div class="Suggested"> Suggested Post</div>
""", unsafe_allow_html=True)

# Suggested Post section with buttons
suggested_post_area = st.text_area("Suggested Post", st.session_state["current_post"], height=150, key="post_area", help="This is your suggested post. Feel free to edit!")

# Placing the buttons in the same row
col1, col2 = st.columns([1, 1], gap="small")
with col1:
    # Custom 'Copy' button
    copy_button = st.markdown(f"""
    <button class="copy-button" onclick="navigator.clipboard.writeText(`{st.session_state['current_post']}`)">Copy</button>
    """, unsafe_allow_html=True)

with col2:
    # Custom 'Reroll' button
    reroll_button = st.markdown("""
    <button class="reroll-button" onclick="window.location.reload()">Reroll</button>
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
<div class="original">Original Post</div>
""", unsafe_allow_html=True)

# Changed the label of the input field here
original_post_area = st.text_area("Your Post Title Here",  # You can change "Your Post Title Here" to whatever you want
                                  st.session_state["current_post"],
                                  height=150,
                                  key="original_post_area",
                                  help="This is the original post content.")

# Layout for buttons using columns
col1, col2 = st.columns([2, 2])

with col1:
    # Custom 'Copy' button
    st.markdown(f"""
    <button class="copy-button" onclick="navigator.clipboard.writeText(`{st.session_state['current_post']}`)">
    Copy
    </button>
    """, unsafe_allow_html=True)