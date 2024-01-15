import streamlit as st
import base64

# Function to load and encode the logo image
def load_logo(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Paths to your images - replace these with the actual file paths on your system
logo_path = r"C:\Users\LENOVO T480\Desktop\Convo\images\img.png"  # Replace with the path to your logo image

# Load and encode the logo
logo_encoded = load_logo(logo_path)

# Begin Streamlit app
st.set_page_config(page_title="Convo", layout="wide")


style = """
    display: flex;
    justify-content: center;
"""
# Custom CSS for styling
st.markdown(f"""
<style>
            
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
    z-index: 3; /* Corrected property name for stacking order */
}}

.stTextArea>div>div>textarea {{
    background-color: #eff3f6;
    border-radius: 20px;
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
    left: 70%; /* Center the button horizontally */
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
/* Base styles for the score boxes */
.score-box {{
    background-color: #F9F9F9; /* Light background color */
    border-radius: 15px;
    padding: 20px 20px;
    margin: 10px;
    color: #333; /* Dark text for contrast */
    display: flex;
    align-items: center;
    justify-content: start;
    height: 150px !important;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}}

.score-box:hover {{
    transform: translateY(-5px); /* Slight lift effect on hover */
}}

.score-icon {{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 60px; /* Width of the icon */
    height: 60px; /* Height of the icon */
    margin-right: 20px;
    border: 3px solid #AAAAAA; /* Grey border */
    border-radius: 50%; /* Circular border */
    font-size: 2em;
    color: #AAAAAA; /* Grey color */
}}

.score-title {{
    margin: 0;
    font-weight: 600; /* Slightly bolder font for the title */
    font-size: 1.2em; /* Larger font size for the title */
}}

.score-description {{
    margin: 5px 0 0;
    font-size: 0.9em; /* Standard font size for the description */
}}

/* Extra adjustments for alignment */
.row {{
    display: flex;
    flex-wrap: nowrap;
    gap: 10px;
}}

/* Ensure the content in the columns is centered */
.stColumn {{
    display: flex;
    justify-content: center;
}}    

.Discourse{{
position: relative;
width: 100%;
padding: 20px 20px;
text-align: center;
}}

/* Media query for mobile devices to adjust the header, search bar, and button */
@media (max-width: 768px) {{
    .header {{
        padding: 1rem 0.5rem; /* Smaller padding on mobile */
    }}

    .img-fluid {{
        max-width: 80px; /* Smaller logo on mobile */
    }}

    /* Adjust the search bar position, width, and other properties for mobile */
    .stTextArea {{
        margin-top: -22%; /* Adjust this value to move the search bar up into the header */
        width: 80%; /* Adjust width as necessary */
        margin-left: auto;
        margin-right: auto;
        z-index: 3;
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
        margin-top: -50px; /* Adjust this value to move the button up into the header */
        position: absolute;
        top: 55%; /* Adjust top position for mobile */
        left: 50%; /* Center the button horizontally */
        transform: translateX(-50%);
        width: 80%; /* Adjust button width as necessary */
        padding: 8px 16px; /* Adjust padding for mobile */
        font-family: 'Arvo';
        font-weight: 700;
        line-height: 15px;
        text-align: center;
        color: #FFFFFF;
        background: #A8C4BA;
        border-radius: 4px;
        z-index: 3;
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

# Text area for post input
user_input = st.text_area("Post Input", placeholder="Paste your post here, and we’ll tell you how likely it is to foster productive conversation", height=150, )



if st.button('Analyze Post'):
    st.success("The analysis of the post will be displayed here.")

# Column layout for score boxes (placeholders for now)
col1, col2, col3 = st.columns([1, 1, 1], gap="small")

with col1:
    st.markdown("""
    <div class="score-box">
        <div class="score-icon">0</div>
        <div>
            <div class="score-title">Discussability</div>
            <div class="score-description">How similar your post is to posts that have generated a lot of fruitful discussion</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="score-box">
        <div
class="score-icon">0</div>
<div>
<div class="score-title">Sentiment</div>
<div class="score-description">The positivity or negativity rating of your post</div>
</div>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class="score-box">
<div class="score-icon">0</div>
<div>
<div class="score-title">Comparison</div>
<div class="score-description">The number of percentage points above or below <br> the average post studied your post is in both <br>discussability and sentiment</div>
</div>
</div>
""", unsafe_allow_html=True)
    

st.markdown(f"""
    <div class="Discourse" style="text-align: center; "> 
        <h1>Creating Healthy Discourse</h1>
        <h5>AI can be a powerful tool for modeling healthy conversations that promote understanding, empathy, and growth. Our models have analyzed hundreds of thousands of posts to learn what makes a post lead to productive discourse. When you share your post drafts with Convo, we rate it and offer suggestions for how it can be better. </h5>
    </div>
""", unsafe_allow_html=True)
