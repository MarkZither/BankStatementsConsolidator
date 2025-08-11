import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import streamlit as st
from bank_statements_consolidator.app import consolidate_statements

st.title('Bank Statements Consolidator')

st.write('Upload your bank statements to consolidate them into one format.')

uploaded_files = st.file_uploader('Choose bank statement files', accept_multiple_files=True)

if uploaded_files:
    st.write(f'You uploaded {len(uploaded_files)} files.')
    # Call CLI logic for consolidation
    consolidated = consolidate_statements(uploaded_files)
    st.write('Consolidated Data:')
    st.dataframe(consolidated)
else:
    st.info('Please upload bank statement files.')
