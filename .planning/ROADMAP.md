# Roadmap: Music Recommender Simulation

## Overview

A 3-phase journey to understand recommendation systems, build a weighted-score content-based recommender in Python, run tests and experiments, and write a detailed Model Card.

## Phases

- [x] **Phase 1: Conceptualization and README Explanation** - Research real-world recommenders and document the design overview in README.md.
- [x] **Phase 2: Dataset Expansion and Core Algorithm** - Expand the dataset in songs.csv and implement the functional and OOP recommendation engine logic.
- [x] **Phase 3: Profiling, Experiments, and Model Card** - Create user profiles, run recommendation simulations, evaluate performance, and write the model card.

## Phase Details

### Phase 1: Conceptualization and README Explanation
**Goal**: Explain recommendation systems and outline how our simulator works.
**Depends on**: Nothing
**Requirements**: DOC-01, DOC-02
**Success Criteria**:
  1. README.md contains accurate documentation of collaborative vs content-based filtering.
  2. "How The System Works" section details what attributes the Song and UserProfile will use and how the scoring will work.

### Phase 2: Dataset Expansion and Core Algorithm
**Goal**: Expand the song catalog and implement the recommender code.
**Depends on**: Phase 1
**Requirements**: DATA-01, DATA-02, CORE-01, CORE-02, CORE-03, CORE-04
**Success Criteria**:
  1. `data/songs.csv` contains at least 20 diverse tracks.
  2. Recommender functions/classes compile and satisfy tests in `tests/test_recommender.py` when run with pytest.

### Phase 3: Profiling, Experiments, and Model Card
**Goal**: Test with user profiles, document experiments, and complete the reflection.
**Depends on**: Phase 2
**Requirements**: DOC-03, PROF-01, PROF-02
**Success Criteria**:
  1. At least 3 distinct user profiles are defined and simulated.
  2. Output recommendations and explanations are printed, and the differences are analyzed.
  3. `model_card.md` sections 1 to 9 are fully completed.

## Progress

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Conceptualization | 1/1 | Complete | 2026-07-24 |
| 2. Core Algorithm | 1/1 | Complete | 2026-07-24 |
| 3. Reflection | 1/1 | Complete | 2026-07-24 |
