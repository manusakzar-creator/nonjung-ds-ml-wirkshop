import subprocess

# Install Streamlit and pyngrok
subprocess.run(["pip", "install", "-q", "streamlit", "pyngrok"])

# Run the Streamlit app. This will provide a public URL to access the app.
# The `&` at the end runs the process in the background, allowing the notebook cell to complete.
# You will see a ngrok URL in the output that you can click to open your app.
!streamlit run clean_app.py &>/dev/null& # Running in background to avoid blocking the cell

# If you need to stop the Streamlit app, you can use:
# !pkill -f streamlit
