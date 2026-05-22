import subprocess

# Install Streamlit and pyngrok if not already installed
# We use -q for quiet installation and check if already installed to avoid unnecessary output
!pip install -q streamlit pyngrok

# Run the Streamlit app 'clean_app.py'
# The `&>/dev/null&` runs the process in the background and suppresses output, so the cell can complete.
# You will typically see a public ngrok URL printed in the output, which you can click to open your app.
# It might take a moment for the URL to appear.

# Note: This method uses a public ngrok tunnel, which is temporary. For persistent deployment, consider other options.
print('Starting Streamlit app... Look for a public URL in the output.')
!streamlit run clean_app.py &>/dev/null&

# You can use the following command to stop the Streamlit app if needed:
# !pkill -f streamlit
