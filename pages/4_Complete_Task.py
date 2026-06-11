import streamlit as st
from app_utils import loadTasks, saveTasks

st.set_page_config(page_title="Complete Task", page_icon="✅", layout="wide")
st.title("Complete Task")
st.write("Mark an incomplete task as complete.")

tasks = loadTasks()
incomplete_tasks = [name for name, details in tasks.items() if details.get("status") == "Incomplete"]

if not incomplete_tasks:
    st.write("All tasks are complete.")
else:
    with st.form(key="complete_task_form"):
        selected_task = st.selectbox("Incomplete Task", incomplete_tasks)
        submitted = st.form_submit_button("Mark Complete")

    if submitted:
        tasks[selected_task]["status"] = "Complete"
        saveTasks(tasks)
        st.success(f"{selected_task} has been marked complete.")
        st.experimental_rerun()

st.markdown("---")
st.write("Completed tasks will update your dashboard automatically.")
