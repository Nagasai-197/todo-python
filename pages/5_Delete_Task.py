import streamlit as st
from app_utils import loadTasks, saveTasks

st.set_page_config(page_title="Delete Task", page_icon="🗑️", layout="wide")
st.title("Delete Task")
st.write("Delete a task carefully.")

tasks = loadTasks()

if not tasks:
    st.write("No tasks are available to delete.")
else:
    with st.form(key="delete_task_form"):
        selected_task = st.selectbox("Task to Delete", sorted(tasks.keys()))
        confirm = st.checkbox("I understand this action cannot be undone.")
        submitted = st.form_submit_button("Delete Task")

    if submitted:
        if not confirm:
            st.warning("Please confirm deletion before proceeding.")
        else:
            del tasks[selected_task]
            saveTasks(tasks)
            st.success(f"Task '{selected_task}' has been deleted.")
            st.experimental_rerun()

st.markdown("---")
st.write("Deleting a task removes it from the dashboard permanently.")
