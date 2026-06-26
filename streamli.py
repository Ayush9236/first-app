import streamlit as st
st.title("My Streamlit App")
"""
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is some text")
st.write("This is a write statement")
yt=st.selectbox("Select a number", [1, 2, 3, 4, 5])
st.write(f"You selected: {yt}")
st.success("This is a success message")
if st.button("Click me"):
    st.success("Button clicked!")
ut=st.checkbox("Check me")
if ut:
    st.write("Checkbox is checked")
mt=st.radio("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {mt}")
"""
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    vote1= st.button("Vote for Option 1")
    if vote1:
        st.success("You voted for Option 1")
with col2:
    st.header("Column 2")   
    vote2= st.button("Vote for Option 2")
    if vote2:
        st.success("You voted for Option 2")

name=st.sidebar.text_input("Sidebar")
option=st.sidebar.selectbox("Select an option", ["Option A", "Option B", "Option C"])
st.sidebar.write(f"You selected: {option}")
