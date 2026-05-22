# Install Streamlit and pyngrok if not already installed.
# These are shell commands that run directly in the Colab environment.
!pip install -q streamlit pyngrok

# Run the Streamlit app 'clean_app.py'.
# The `&>/dev/null&` runs the process in the background and suppresses output, so the cell can complete.
# You will typically see a public ngrok URL printed in the output, which you can click to open your app.
# It might take a moment for the URL to appear.
print('Starting Streamlit app... Look for a public URL in the output, it may take a few moments.')
!streamlit run clean_app.py &>/dev/null&

# You can use the following command to stop the Streamlit app if needed:
# !pkill -f streamlit
