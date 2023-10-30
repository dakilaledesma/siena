import streamlit as st

st.title("Siena")

sirna_name = st.text_input("siRNA name")
seq = st.text_area("Sequence")

col1, col2 = st.columns(2)
with col1:
    st.text_input("Motif size:")

    restrict_region = st.slider(
        "Restrict the search to the region from position:",
        0, 9600, (0, 9600))

    gc_percent = st.slider(
        "siRNA target sequence GC% between:",
        0, 100, (33, 55))

with col2:
    fnts = st.selectbox("First nucleotide of the target sequence:", ["A or G", "A", "G"])
    c_quadruplet = st.checkbox("Enable C quadruplet")
    a_quadruplet = st.checkbox("Enable A quadruplet")
    g_quadruplet = st.checkbox("Enable G quadruplet")





