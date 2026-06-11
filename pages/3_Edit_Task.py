import streamlit as st
from datetime import datetime, date
from app_utils import (
    PRIORITY_OPTIONS,
    STATUS_OPTIONS,
    loadTasks,
    saveTasks,
    validate_task_input,
)

st.set_page_config(page_title="Edit Task", page_icon="✏️", layout="wide")
st.title("Edit Task")
st.write("Select a task to modify its details.")

tasks = loadTasks()

if not tasks:
    st.write("No tasks are available to edit.")
else:
    task_names = sorted(tasks.keys())
    edit_task = st.selectbox("Task To Edit", task_names)
    current = tasks[edit_task]
    current_date = datetime.strptime(current["due_date"], "%d-%m-%Y").date()

    with st.form(key="edit_task_form"):
        new_name = st.text_input("Task Name", value=edit_task)
        new_priority = st.selectbox("Priority", PRIORITY_OPTIONS, index=PRIORITY_OPTIONS.index(current["priority"]))
        new_status = st.selectbox("Status", STATUS_OPTIONS, index=STATUS_OPTIONS.index(current["status"]))
        new_due_date = st.date_input("Due Date", value=current_date, min_value=date.today())
        submitted = st.form_submit_button("Save Changes")

    if submitted:
        valid, message = validate_task_input(new_name, new_priority, new_due_date, tasks, original_name=edit_task)
        if not valid:
            st.error(message)
        else:
            tasks[new_name] = {
                "status": new_status,
                "priority": new_priority,
                "due_date": new_due_date.strftime("%d-%m-%Y"),
            }
            if new_name != edit_task:
                del tasks[edit_task]
            saveTasks(tasks)
            st.success("Task updated successfully.")
            st.experimental_rerun()

st.markdown("---")
st.write("Editing a task keeps your task list up to date.")
