import streamlit as st
import base64


# Begin Streamlit app
st.set_page_config(page_title="Convo", layout="wide")

# Function to load and encode the logo image
def load_logo(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def calculate_convo_score(post):
    score = 0
    score += min(len(post) / 100, 0)  # Up to 3 points for length
    score += post.count('?') * 2  # 2 points for each question
    score += post.count('!')  # 1 point for each exclamation mark
    score = min(score, 10)  # Cap the score at 10
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


# Paths to your images - replace these with the actual file paths on your system
logo_path = "images/img.png"  # Replace with the path to your logo image

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
position: relative;
width: 100%;
height: 700px;
left: 0%;
right: 0%;
top: 0%;
bottom: 0%;
background: linear-gradient(180deg, #0FEF34 -15.36%, #1DA6DB 42.43%, #022D60 100%);
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
    border-radius: 40%;
    margin-top: 2%;        
}}
            
.stTextArea {{
    margin-top: -23%; /* Pull the text area up into the header */
    width: 70% !important;
    margin-left: auto;
    margin-right: auto;
     border-radius: 0px;
    z-index: 3; /* Corrected property name for stacking order */
}}

.stTextArea>div>div>textarea {{
    background-color: #eff3f6;
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
    margin-top: -11%;/* Adjust this value to move the button up into the header */
    z-index: 5; /* Ensure the button is above other elements */
    background: #A8C4BA;
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
    margin-top: 20px; /* Adjust as necessary */
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

/* Style for custom file uploader button */
            
[data-testid='stFileUploader'] {{
          margin-top: -16.21%;
          margin-left: auto;
          margin-right: auto;
          width: max-content;
         
    }}
    [data-testid='stFileUploader'] section {{
        border: 2px solid #0068c9;
        padding: 8px 500px;
        background-color: #1da6db;
       
    }}
    [data-testid='stFileUploader'] section > input + div {{
        display: none;
        
    }}
    [data-testid='stFileUploader'] section + div {{
        float: right;
        padding-top: 0;
        
    }}

/* Style adjustments for upload button to align with the text area */

/* Media query for mobile devices to adjust the header, search bar, and button */
@media (max-width: 768px) {{
    .header {{
        padding: 0.5rem 0.5rem; /* Smaller padding on mobile */
        width: 100%;
        height: 600px;
    }}

    .img-fluid {{
        max-width: 150px; /* Smaller logo on mobile */
       
    }}

    /* Adjust the search bar position, width, and other properties for mobile */
    .stTextArea {{
        margin-top: -85% !important; /* Adjust this value to move the search bar up into the header */
        width: 85% !important; /* Adjust width as necessary */
        margin-left: auto;
        margin-right: auto;
        z-index: 3!important;
    }}

    .stTextArea>div>div>textarea {{
        background-color: #eff3f6;
        border-radius: 20px;
        border: 1px solid #ced4da;
        height: 120px; /* Adjust height for mobile */
    }}

    /* Hide the label of the text area on mobile */
    .stTextArea label {{
        display: none;
    }}

    /* Adjust the button position and size for mobile */
    .stButton > button {{
        font-size: 14px; /* Smaller font size on mobile */
        margin-top: -35% !important; /* Adjust this value to move the button up into the header */
        position: absolute;
        top: 55%; /* Adjust top position for mobile */
        left: 50%; /* Center the button horizontally */
        transform: translateX(-50%);
        width: 85%; /* Adjust button width as necessary */
        padding: 20px 20px !important; /* Adjust padding for mobile */
        font-family: 'Arvo';
        font-weight: 700;
        line-height: 15px;
        text-align: center;
        color: #FFFFFF;
        background: #A8C4BA;
        border-radius: 4px;
        z-index: 3;
    }}
            
.stButton > button:hover {{
          color: #FFFFFF;  
          background: #17ca88;
          border: #FFFFFF;
}}

.upload-btn-wrapper {{
  margin-top: -52%;
  z-index: 4;
}}
            
.btn{{
    padding: 8px 0px;
    width: 100%;
    margin-left: -9%;
}}


            
}}
</style>
""", unsafe_allow_html=True)

# Inject the logo into the header
st.markdown(f"""
    <div class="header" style="text-align: center; color: #FFFFFF;">
        <img src="data:image/png;base64,{logo_encoded}" class="img-fluid" alt="Convo logo">
        <h1>Let's get talking</h1>
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

# Button action
if analyze_button:
    if user_input:
        # Calculate the score
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

st.markdown(f"""
    <div class="Discourse" style="text-align: center; "> 
        <h1>Creating Healthy Discourse</h1>
        <h5>AI can be a powerful tool for modeling healthy conversations that promote understanding, empathy, and growth. Our models have analyzed hundreds of thousands of posts to learn what makes a post lead to productive discourse. When you share your post drafts with Convo, we rate it and offer suggestions for how it can be better. </h5>
    </div>
""", unsafe_allow_html=True)
