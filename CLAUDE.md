# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard (auto-reloads on file save)
streamlit run app.py
```

The app runs at http://localhost:8501 by default.

## Architecture

Single-file Streamlit dashboard (`app.py`). Data is loaded into a Pandas DataFrame and rendered via Streamlit's built-in chart/table components and Plotly Express. The app is designed as a template — the inline sample data is meant to be swapped out for a CSV or API source.

**Key dependencies**: Streamlit, Pandas, Plotly Express, Altair, PyDeck (all in `requirements.txt`).

No build step, no test suite, no linter configured.
