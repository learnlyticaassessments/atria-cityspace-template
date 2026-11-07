# Atria CityPulse Engineering Stack — Your Lab Repo

This is **your** repository for the CityPulse Engineering Stack course. You own it, and it stays
yours after the course ends. All your lab work lives here.

## How to work on a lab

1. Open the lab in the Learnlytica platform. The right-hand panel shows the task and the current
   status of this repo.
2. Click **Open in Codespaces**. A free Linux container boots in a new browser tab with everything
   pre-installed (Python 3.11, pandas, scikit-learn, FastAPI, Streamlit, SQLite, …).
3. Write your solution in that day's folder (e.g. `day01/`). Follow the `TASK.md` in the folder.
4. **Commit and push.** Your push triggers a quick check (GitHub Actions) and updates the status
   panel back in the platform.
5. Click **Run Test** in the platform to get your official, graded result.

## How grading works

- Your repo is **public** so the platform can read it and so GitHub Actions minutes are free.
- When you click **Run Test**, the platform clones your repo at your latest commit, runs the
  official hidden tests for that day against your code, and records your result.
- The hidden tests are **not** in this repo — don't look for them. Commit your solution to the
  right file for the day and run the test.

## Environment

The container is defined by [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json)
and [`requirements.txt`](requirements.txt). If you work locally instead of Codespaces, create a
Python 3.11 virtualenv and `pip install -r requirements.txt`.

## Honor code

This repo is public so your instructors can grade it. Do your own work. Copying another learner's
solution is an integrity violation. You are responsible for what you commit here.
