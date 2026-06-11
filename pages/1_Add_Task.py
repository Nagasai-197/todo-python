import streamlit as st
from datetime import date
from app_utils import PRIORITY_OPTIONS, loadTasks, saveTasks, validate_task_input

st.set_page_config(page_title="Add Task", page_icon="📝", layout="wide")
st.title("Add Task")
st.write("Add a new task to your todo list.")

tasks = loadTasks()

with st.form(key="add_task_form"):
    task_name = st.text_input("Task Name")
    priority = st.selectbox("Priority", PRIORITY_OPTIONS)
    due_date = st.date_input("Due Date", min_value=date.today())
    submitted = st.form_submit_button("Add Task")

if submitted:
    valid, message = validate_task_input(task_name, priority, due_date, tasks)
    if not valid:
        st.error(message)
    else:
        tasks[task_name] = {
            "status": "Incomplete",
            "priority": priority,
            "due_date": due_date.strftime("%d-%m-%Y"),
        }
        saveTasks(tasks)
        st.success("Task added successfully!")
        st.experimental_rerun()

st.markdown("---")
st.write("Use the form above to add a new task. Tasks appear immediately in the View Tasks and Dashboard pages.")
