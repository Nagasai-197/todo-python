import pandas as pd
import streamlit as st
from app_utils import get_due_date_timeline, get_priority_counts, get_task_summary, loadTasks

st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")
st.title("Analytics")
st.write("View task performance and simple charts.")

tasks = loadTasks()
summary = get_task_summary(tasks)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Tasks", summary["total"])
col2.metric("Completed", summary["completed"])
col3.metric("Pending", summary["pending"])
col4.metric("High Priority", summary["high_priority"])

if not tasks:
    st.write("No tasks are available for analytics.")
else:
    st.markdown("---")
    st.subheader("Status Distribution")
    status_df = pd.DataFrame(
        {"Status": ["Complete", "Incomplete"], "Count": [summary["completed"], summary["pending"]]}
    )
    st.bar_chart(status_df.set_index("Status"))

    st.markdown("---")
    st.subheader("Priority Distribution")
    priority_counts = get_priority_counts(tasks)
    priority_df = pd.DataFrame(
        {"Priority": list(priority_counts.keys()), "Count": list(priority_counts.values())}
    )
    st.bar_chart(priority_df.set_index("Priority"))

    st.markdown("---")
    st.subheader("Tasks by Due Date")
    timeline_data = get_due_date_timeline(tasks)
    if timeline_data:
        timeline_df = pd.DataFrame(timeline_data)
        timeline_df["Start"] = pd.to_datetime(timeline_df["Start"])
        timeline_counts = timeline_df.groupby(timeline_df["Start"].dt.date).size()
        st.line_chart(timeline_counts)
    else:
        st.write("No due date data is available yet.")
