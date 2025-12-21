# Feedback Analysis

AI-powered feedback analysis system that processes customer feedback from multiple sources (app store reviews, support emails) and automatically generates structured tickets using LangGraph.

## Features
- Multi-source feedback processing (CSV files)
- AI-powered classification (Bug, Feature Request, Praise, Complaint, Spam)
- Automated priority analysis and ticket generation
- LangGraph workflow visualization

## Setup

Install dependencies:
```bash
uv sync
```

## Usage

### Generate workflow visualization:
```bash
uv run python -m graphs.feedback_graph
```
Result: `FeedbackAnalysis/results/feedback_graph.png`

### Process feedback and generate tickets:
```bash
uv run python -m app.main
```
Result: `FeedbackAnalysis/results/generated_tickets.csv`

## Data Sources
- `data/app_store_reviews.csv`
- `data/support_emails.csv`

