import pandas as pd
import streamlit as st
from app_utils import PRIORITY_OPTIONS, STATUS_OPTIONS, get_task_rows, loadTasks

st.set_page_config(page_title="View Tasks", page_icon="📋", layout="wide")
st.title("View Tasks")
st.write("Search and filter your tasks.")

tasks = loadTasks()
search_query = st.text_input("Search tasks", "")
status_filter = st.selectbox("Status", ["All"] + STATUS_OPTIONS)
priority_filter = st.selectbox("Priority", ["All"] + PRIORITY_OPTIONS)
sort_by = st.selectbox("Sort by", ["Due Date", "Priority", "Task Name"])
ascending = st.radio("Order", ["Ascending", "Descending"]) == "Ascending"

rows = get_task_rows(
    tasks,
    search_query=search_query,
    status_filter=status_filter,
    priority_filter=priority_filter,
    sort_by=sort_by,
    ascending=ascending,
)

st.write(f"{len(rows)} task(s) found")

if rows:
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.write("No tasks match the active filters.")
