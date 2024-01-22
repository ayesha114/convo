import streamlit as st
import base64


# Begin Streamlit app
st.set_page_config(page_title="Convo", layout="wide")

# Function to load and encode the logo image
def load_logo(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')



# Paths to your images - replace these with the actual file paths on your system
logo_path = r"C:\Users\LENOVO T480\Desktop\Convo\images\img.png"  # Replace with the path to your logo image

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

.header, .header h1,  {{
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
height: 766px;
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
    border-radius: 45%;
    margin-top: 2%;      
    width: 30%  
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
    width: 140px; /* Adjust as necessary */
    height: 140px; /* Adjust as necessary */
    border: 13px solid #D9D9D9;
    border-radius: 50%; /* Makes it circular */
    text-align: center;
    line-height: 150px; /* Adjust as necessary */
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


}}
            
            
/* Adjustments for Safari Browser (Apple Devices) */
@media not all and (min-resolution:.001dpcm) {{ 
    @supports (-webkit-appearance:none) {{
        .stTextArea, .stButton > button {{
            /* Safari-specific adjustments if needed */
        }}
    }}
}}

</style>
""", unsafe_allow_html=True)

# Inject the logo into the header
st.markdown(f"""
    <div class="header" style="text-align: center; color: #FFFFFF;">
        <img src="data:image/png;base64,{logo_encoded}" class="img-fluid" alt="Convo logo">
        <h1 style="text-align: center; color: #FFFFFF;">Analyzing post</h1>
    <div class="convo-score-container">
    <div class="convo-score-meter"></div>
    </div>
        <h5 class="convo-score-description" style="text-align: center; color: #FFFFFF;">
                We're evaluating how your post compares to those that have sparked productive conversations.    
                Let's amplify the impact of your posts and foster deeper discussions!
        </h5> 
        
    </div>
""", unsafe_allow_html=True)

