import streamlit as st

# Function to calculate the convo score based on the post content
def calculate_convo_score(post):
    # Placeholder for your scoring algorithm
    # Replace this with your actual logic for calculating the convo score
    return len(post) % 11  # Simple placeholder for a score out of 10

# Function to create a circular progress bar
def circular_progress(score):
    # Adjust the progress bar color based on the score
    color = "#22C55E" if score > 5 else "#EF4444"
    # Custom HTML/CSS to create the circular progress bar
    progress = f"""
    <div class="circle-wrap">
        <div class="circle">
            <div class="mask full" style="transform: rotate({score * 3.6}deg);">
                <div class="fill" style="background: {color}; transform: rotate({score * 3.6}deg);"></div>
            </div>
            <div class="mask half">
                <div class="fill" style="background: {color}; transform: rotate({score * 3.6}deg);"></div>
            </div>
            <div class="inside-circle"> {score} </div>
        </div>
    </div>
    """
    return progress

# Custom CSS to style the circular progress bar and the page
def load_custom_css():
    st.markdown("""
    <style>
    .circle-wrap {
        margin: 50px auto;
        width: 150px;
        height: 150px;
        background: #e6e2e7;
        border-radius: 50%;
    }

    .circle .mask,
    .circle .fill {
        width: 150px;
        height: 150px;
        position: absolute;
        border-radius: 50%;
    }

    .circle .mask {
        clip: rect(0px, 150px, 150px, 75px);
    }

    .circle .mask .fill {
        clip: rect(0px, 75px, 150px, 0px);
        background: #22C55E;
    }

    .circle .mask.full,
    .circle .fill {
        animation: fill ease-in-out 3s;
        transform: rotate(126deg);
    }

    @keyframes fill {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(126deg);
        }
    }

    .inside-circle {
        width: 130px;
        height: 130px;
        background: white;
        line-height: 130px;
        text-align: center;
        margin-top: 10px;
        border-radius: 50%;
        position: absolute;
        z-index: 100;
        font-weight: bold;
        font-size: 2em;
    }

    .header {
        text-align: center;
        padding: 0;
        margin: 0;
    }
    
    .suggestion-box {
        border: 2px solid #22C55E;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Begin Streamlit app
st.set_page_config(page_title="Posts Score", layout="wide")
load_custom_css()

def main():
    st.markdown("<h1 class='header'>Convo Score</h1>", unsafe_allow_html=True)
    user_post = st.text_area("Your Post", height=200)

    if st.button("Calculate Score"):
        score = calculate_convo_score(user_post)
        progress_bar = circular_progress(score)
        st.markdown(progress_bar, unsafe_allow_html=True)
        st.markdown("""
            <div>
                <p>Your post contains most of the features of posts that lead to productive back and forth discussion online. There are a few things you can do to make it more discussable.</p>
                <div class="suggestion-box">
                    <p><strong>Suggested Post</strong></p>
                    <p>Based on what I've seen in my travels, it seems that the communities with the fewest financial resources have the most collaborative cultures. Have you seen the same thing?</p>
                    <button onclick="navigator.clipboard.writeText(this.previousElementSibling.innerText)">Copy</button>
                    <button>Re-roll</button>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()