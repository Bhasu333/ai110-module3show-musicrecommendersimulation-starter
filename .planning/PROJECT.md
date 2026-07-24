# Music Recommender Simulation

## What This Is

A python-based music recommender simulator designed to demonstrate content-based filtering algorithms using attributes like genre, mood, and energy, and to explore algorithmic bias. It is built for CSE coursework to explore recommendation concepts.

## Core Value

Accurately simulate recommendations using student-level modular Python code while meeting all course rubric criteria.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] REQ-01: Clear explanation of how music recommendation systems work in README.
- [ ] REQ-02: Structured song dataset containing at least 20 songs in data/songs.csv.
- [ ] REQ-03: Scoring function that reflects user preferences in recommender.py.
- [ ] REQ-04: Recommendation function that ranks songs and returns top recommendations.
- [ ] REQ-05: Detailed explanation generator explaining why a song was recommended.
- [ ] REQ-06: Experiments with 3 distinct user profiles documented in README and model_card.md.
- [ ] REQ-07: Completed Model Card detailing dataset, approach, limitations/bias, and future improvements.

### Out of Scope

- Collaborative filtering system — excluded because we lack multi-user listening history datasets.
- Real-time API integrations — excluded as this is a command line simulation.

## Context

- Technical environment: Python 3 with standard library. pytest for verification.
- Purpose: Showcase content-based recommendation matching, weighting, and basic similarity calculations.

## Constraints

- **Tech stack**: Python 3 standard library only (no external machine learning frameworks).
- **Testing**: Must pass existing tests in tests/test_recommender.py.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Content-Based Filtering | Simulates recommendations using metadata matching, aligned with the scope | — Pending |

---
*Last updated: 2026-07-24 after initialization*
