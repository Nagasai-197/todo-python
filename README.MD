# To-Do Manager

A Streamlit-based task manager with dedicated page modules for adding, viewing, editing, completing, deleting, and analyzing tasks.

## Run the app

1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Start the Streamlit app:
   ```powershell
   streamlit run app.py
   ```

## File structure

- `app.py` — root landing page
- `pages/1_Add_Task.py` — add a new task
- `pages/2_View_Tasks.py` — browse and filter tasks
- `pages/3_Edit_Task.py` — edit an existing task
- `pages/4_Complete_Task.py` — mark a task complete
- `pages/5_Delete_Task.py` — delete a task
- `pages/6_Analytics.py` — view analytics and charts
- `Main.py` — legacy CLI interface
- `tasks.json` — task storage
- `requirements.txt` — Python dependencies

## Notes

- `Main.py` is preserved as a console fallback.
- `tasks.json` is created automatically when tasks are added.
