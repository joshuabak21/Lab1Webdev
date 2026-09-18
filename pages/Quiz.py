import streamlit as st

st.set_page_config(page_title="Soccer Quiz", page_icon="⚽", layout="centered")

st.title("⚽ Soccer Personality Quiz")
st.write("Answer the questions to discover what kind of soccer player you are!")
st.write("---")

# Question 1: Radio
positions = ["Goalkeeper 🧤", "Defender 🛡️", "Midfielder 🎯", "Forward ⚡"]
position = st.radio("1. What's your favorite position?", positions)  # NEW

# Question 2: Multiselect
skills = st.multiselect("2. What skills do you bring to the game?", 
                        ["Speed", "Strength", "Passing", "Leadership", "Dribbling"])  # NEW

# Question 3: Number input
goals = st.number_input("3. How many goals could you score in a season?", 
                        min_value=0, max_value=100, value=5)  # NEW

# Question 4: Slider
teamwork = st.slider("4. How much do you value teamwork? (0-10)", 0, 10, 5)

# Question 5: Images with buttons (no 'with')
st.subheader("5. Pick your favorite soccer moment:")
cols = st.columns(3)

choice = None
if cols[0].button("🏆 World Cup Trophy"):
    choice = "Winner"
cols[0].image("Images/worldcup.png", caption="Winning the World Cup", use_container_width=True)

if cols[1].button("⚡ Last-Minute Goal"):
    choice = "Clutch"
cols[1].image("Images/goal.png", caption="Scoring in the final minute", use_container_width=True)

if cols[2].button("🧤 Epic Save"):
    choice = "Hero"
cols[2].image("Images/save.png", caption="Making a crucial save", use_container_width=True)

st.write("---")

# Results
if st.button("See My Soccer Identity"):
    player = "All-Rounder 🌍"
    for skill in skills:
        if skill == "Speed" or choice == "Clutch":
            player = "Forward ⚡"
        elif skill == "Passing" or position.startswith("Midfielder"):
            player = "Midfielder 🎯"
        elif skill == "Strength" or position.startswith("Defender"):
            player = "Defender 🛡️"
        elif position.startswith("Goalkeeper") or choice == "Hero":
            player = "Goalkeeper 🧤"
    summary = f"Your soccer identity is: **{player.upper()}**"  

    st.success(summary)
    st.balloons()  # NEW
