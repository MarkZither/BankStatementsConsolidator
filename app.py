import streamlit as st
import pandas as pd

st.title('Bank Statements Consolidator')

st.write('Upload your bank statements to consolidate them into one format.')

uploaded_files = st.file_uploader('Choose bank statement files', accept_multiple_files=True)

if uploaded_files:
    st.write(f'You uploaded {len(uploaded_files)} files.')
    # Placeholder for parsing and consolidation logic
    st.info('Parsing and consolidation logic will go here.')
else:
    st.info('Please upload bank statement files.')
