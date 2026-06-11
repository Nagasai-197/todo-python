import json
import os
from datetime import date, datetime, timedelta

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")
STATUS_OPTIONS = ["Incomplete", "Complete"]
PRIORITY_OPTIONS = ["High", "Medium", "Low"]
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def loadTasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def saveTasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def parse_due_date(due_date_str):
    return datetime.strptime(due_date_str, "%d-%m-%Y").date()


def format_due_date(due_date_str):
    return parse_due_date(due_date_str).strftime("%b %d, %Y")


def validate_task_input(task_name, priority, due_date, tasks, original_name=None):
    if not task_name.strip():
        return False, "Task name cannot be empty."

    if priority not in PRIORITY_OPTIONS:
        return False, "Priority must be High, Medium, or Low."

    if due_date < date.today():
        return False, "Due date cannot be in the past."

    if original_name and task_name == original_name:
        return True, ""

    if task_name in tasks and task_name != original_name:
        return False, "A task with that name already exists."

    return True, ""


def get_task_summary(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks.values() if task.get("status") == "Complete")
    pending = total - completed
    high_priority = sum(1 for task in tasks.values() if task.get("priority") == "High")
    progress = int((completed / total) * 100) if total else 0

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "high_priority": high_priority,
        "progress": progress,
    }


def get_task_rows(tasks, search_query="", status_filter="All", priority_filter="All", sort_by="Due Date", ascending=True):
    rows = []
    normalized_query = search_query.strip().lower()

    for task_name, details in tasks.items():
        if status_filter != "All" and details.get("status") != status_filter:
            continue
        if priority_filter != "All" and details.get("priority") != priority_filter:
            continue
        if normalized_query and normalized_query not in task_name.lower():
            continue

        due_date = parse_due_date(details["due_date"])
        days_left = (due_date - date.today()).days

        rows.append(
            {
                "Task": task_name,
                "Status": details["status"],
                "Priority": details["priority"],
                "Due Date": details["due_date"],
                "Days Left": days_left,
            }
        )

    if sort_by == "Due Date":
        rows.sort(key=lambda item: parse_due_date(item["Due Date"]), reverse=not ascending)
    elif sort_by == "Priority":
        rows.sort(key=lambda item: PRIORITY_ORDER.get(item["Priority"], 3), reverse=not ascending)
    else:
        rows.sort(key=lambda item: item["Task"].lower(), reverse=not ascending)

    return rows


def get_recent_tasks(tasks, limit=5):
    upcoming = sorted(tasks.items(), key=lambda item: parse_due_date(item[1]["due_date"]))
    return upcoming[:limit]


def get_upcoming_tasks(tasks, limit=5):
    future_tasks = [
        (name, details)
        for name, details in tasks.items()
        if parse_due_date(details["due_date"]) >= date.today()
    ]
    future_sorted = sorted(future_tasks, key=lambda item: parse_due_date(item[1]["due_date"]))
    return future_sorted[:limit]


def get_due_date_timeline(tasks):
    timeline = []
    for task_name, details in tasks.items():
        due_date = parse_due_date(details["due_date"])
        timeline.append(
            {
                "Task": task_name,
                "Start": due_date,
                "Finish": due_date + timedelta(days=1),
                "Priority": details["priority"],
                "Status": details["status"],
            }
        )
    return timeline


def get_priority_counts(tasks):
    counts = {"High": 0, "Medium": 0, "Low": 0}
    for details in tasks.values():
        priority = details.get("priority")
        if priority in counts:
            counts[priority] += 1
    return counts
