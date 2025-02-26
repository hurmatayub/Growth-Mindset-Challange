
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Growth Mindset App", layout="wide")

st.markdown(
    """
    <style>
        .main {
            background-color: #121212;  
        }
        .block-container {
            padding: 3rem 2rem; 
            border-radius: 12px;  
            background-color: #1e1e1e; 
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);  
        }
        h1, h2, h3, h4, h5, h6 {
            color: #66c2ff; 
        }
        .stButton>button {
            border: none;
            border-radius: 8px;  
            background-color: black !important; 
            color: white; 
            padding: 0.75rem 1.5rem;  
            font-size: 1rem;  
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4); 
        }
        .stButton>button:hover {
            background-color: #333333 !important;  
            cursor: pointer;
        }
        .stDataFrame, .stTable {
            border-radius: 10px;  
            overflow: hidden;  
        }
        .css-1aumxhk, .css-18e3th9 {
            text-align: left;
            color: white;  
        }
        .stRadio>label {
            font-weight: bold;
            color: white;
        }
        .stCheckbox>label {
            color: white;
        }
        .stDownloadButton>button {
            background-color: black !important;  
            color: white;
        }
        .stDownloadButton>button:hover {
            background-color: #333333 !important;  
        }
    </style>
    """,
    unsafe_allow_html=True  
)

if "goals" not in st.session_state:
    st.session_state.goals = []
if "reflections" not in st.session_state:
    st.session_state.reflections = []
if "achievements" not in st.session_state:
    st.session_state.achievements = []
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "moods" not in st.session_state:
    st.session_state.moods = []


st.sidebar.title("Navigation")
selection = st.sidebar.radio(
    "Go to", 
    ["Home", "Set Personal Goals", "Progress Tracking", "Reflective", 
     "Achievement Recognition", "Mood Tracker", "Data Sweeper", "Task Manager"]
)


if selection == "Home":
    st.title("Welcome to the Growth Mindset App")
    st.write("Explore the features through the sidebar.")

elif selection == "Set Personal Goals":
    st.title("Set Personal Goals")
    goal = st.text_input("Enter your goal:")
    if st.button("Save Goal"):
        if goal:
            st.session_state.goals.append(goal)
            st.success("Goal added successfully!")
        else:
            st.warning("Please enter a valid goal.")
    st.write("### Your Goals:")
    for g in st.session_state.goals:
        st.write(f"- {g}")

elif selection == "Progress Tracking":
    st.title("Progress Tracking")
    st.subheader("Track Your Progress Over Time")
    
    progress = st.slider("Select Progress Level:", 0, 100, 50)
    st.progress(progress / 100)
    
    st.subheader("Progress Trend")
    df = pd.DataFrame({
        'Day': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        'Progress': [10, 30, 50, 70, 90]
    })
    st.line_chart(df.set_index('Day'))

elif selection == "Task Manager":
    st.title("Task Manager")
    st.subheader("Manage Your Tasks Effectively")
    
    task = st.text_input("Enter a new task:")
    if st.button("Add Task"):
        if task:
            st.session_state.tasks.append(task)
            st.success("Task added successfully!")
        else:
            st.warning("Please enter a valid task.")
    st.write("### Your Tasks:")
    for t in st.session_state.tasks:
        st.write(f"✅ {t}")

elif selection == "Reflective":
    st.title("Reflective")
    reflection = st.text_area("Write your reflection:")
    if st.button("Save Reflection"):
        if reflection:
            st.session_state.reflections.append(reflection)
            st.success("Reflection saved successfully!")
        else:
            st.warning("Please write something before saving.")
    st.write("### Your Reflections:")
    for r in st.session_state.reflections:
        st.write(f"- {r}")

elif selection == "Achievement Recognition":
    st.title("Achievement Recognition")
    achievement = st.text_input("Enter your achievement:")
    if st.button("Save Achievement"):
        if achievement:
            st.session_state.achievements.append(achievement)
            st.success("Achievement added successfully!")
        else:
            st.warning("Please enter a valid achievement.")
    st.write("### Your Achievements:")
    for a in st.session_state.achievements:
        st.write(f"🏆 {a}")

elif selection == "Mood Tracker":
    st.title("Mood Tracker")
    mood = st.selectbox("Select your mood:", ["Happy", "Sad", "Neutral"])
    if st.button("Save Mood"):
        st.session_state.moods.append(mood)
        st.success("Mood saved successfully!")
    st.write("### Your Mood History:")
    for m in st.session_state.moods:
        st.write(f"🙂 {m}")

elif selection == "Data Sweeper":
    st.title("Data Sweeper")
    st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")
    uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            file_extension = os.path.splitext(file.name)[-1].lower()
            if file_extension == ".csv":
                df = pd.read_csv(file) 
            elif file_extension == ".xlsx":
                df = pd.read_excel(file)  
            else:
                st.error(f"Unsupported file type: {file_extension}")
                continue
            
            st.write(f"**📄 File Name:** {file.name}")
            st.write(f"**📏 File Size:** {file.size / 1024:.2f} KB")  
            st.write("🔍 Preview of the Uploaded File:")
            st.dataframe(df.head())  
            
            st.subheader("🛠️ Data Cleaning Options")
            if st.checkbox(f"Clean Data for {file.name}"):
                if st.button(f"Apply All Cleaning Steps for {file.name}"):
                    df.drop_duplicates(inplace=True)
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Data cleaned successfully!")
            
            st.subheader("📊 Data Visualization")
            if st.checkbox(f"Show Visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])  
