import pandas as pd
import streamlit as st
from app_utils import (
    get_due_date_timeline,
    get_priority_counts,
    get_recent_tasks,
    get_task_summary,
    get_upcoming_tasks,
    loadTasks,
)

st.set_page_config(page_title="Dashboard", page_icon="🏠", layout="wide")
st.title("Dashboard")
st.write("A simple task overview for your To-Do Manager.")

tasks = loadTasks()
summary = get_task_summary(tasks)
priority_counts = get_priority_counts(tasks)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Tasks", summary["total"])
col2.metric("Completed", summary["completed"])
col3.metric("Pending", summary["pending"])
col4.metric("High Priority", summary["high_priority"])

st.markdown("---")
st.subheader("Recent Tasks")
recent_tasks = get_recent_tasks(tasks, limit=6)
if recent_tasks:
    recent_df = pd.DataFrame(
        [
            {
                "Task": name,
                "Priority": details["priority"],
                "Status": details["status"],
                "Due Date": details["due_date"],
            }
            for name, details in recent_tasks
        ]
    )
    st.dataframe(recent_df, use_container_width=True, hide_index=True)
else:
    st.write("No tasks have been created yet.")

st.markdown("---")
st.subheader("Upcoming Due Dates")
upcoming = get_upcoming_tasks(tasks, limit=6)
if upcoming:
    upcoming_df = pd.DataFrame(
        [
            {
                "Task": name,
                "Priority": details["priority"],
                "Status": details["status"],
                "Due Date": details["due_date"],
            }
            for name, details in upcoming
        ]
    )
    st.dataframe(upcoming_df, use_container_width=True, hide_index=True)
else:
    st.write("No upcoming tasks found.")

st.markdown("---")
st.subheader("Priority Distribution")
priority_df = pd.DataFrame(
    {"Priority": list(priority_counts.keys()), "Count": list(priority_counts.values())}
)
st.bar_chart(priority_df.set_index("Priority"))

st.markdown("---")
st.subheader("Timeline Overview")
line_data = get_due_date_timeline(tasks)
if line_data:
    timeline_df = pd.DataFrame(line_data)
    timeline_df["Start"] = pd.to_datetime(timeline_df["Start"])
    timeline_counts = timeline_df.groupby(timeline_df["Start"].dt.date).size()
    st.line_chart(timeline_counts)
else:
    st.write("Tasks will appear in the timeline once due dates are added.")
