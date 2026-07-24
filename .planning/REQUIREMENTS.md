# Requirements: Music Recommender Simulation

**Defined:** 2026-07-24
**Core Value:** Accurately simulate recommendations using student-level modular Python code while meeting all course rubric criteria.

## v1 Requirements

### Documentation & Concept

- [ ] **DOC-01**: Clear explanation of real-world recommendation systems (collaborative vs content-based) in README.md.
- [ ] **DOC-02**: Identify main data types involved in recommendation systems in README.md.
- [ ] **DOC-03**: Complete Model Card (`model_card.md`) covering all 9 sections including biases, limitations, evaluation, and future work.

### Song Dataset

- [ ] **DATA-01**: Expand `data/songs.csv` to contain at least 20 songs.
- [ ] **DATA-02**: Ensure each song has at least 3 attributes (genre, mood, energy, tempo_bpm, valence, danceability, acousticness).

### Recommendation Core Logic

- [ ] **CORE-01**: Implement `load_songs(csv_path)` to load and parse CSV data into a list of dictionaries.
- [ ] **CORE-02**: Implement `score_song(user_prefs, song)` weighting genre, mood, energy difference, and acousticness.
- [ ] **CORE-03**: Implement `recommend_songs(user_prefs, songs, k)` ranking/sorting songs descending by score.
- [ ] **CORE-04**: Implement dataclasses `Song` and `UserProfile`, and OOP wrapper class `Recommender` with `recommend` and `explain_recommendation` matching requirements of `tests/test_recommender.py`.

### Profiling & Evaluation

- [ ] **PROF-01**: Define at least 3 distinct user profiles.
- [ ] **PROF-02**: Perform and document experiments with these 3 user profiles, presenting outputs and reflections on their differences in README.md and model_card.md.

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| DOC-01 | Phase 1 | Pending |
| DOC-02 | Phase 1 | Pending |
| DOC-03 | Phase 3 | Pending |
| DATA-01 | Phase 2 | Pending |
| DATA-02 | Phase 2 | Pending |
| CORE-01 | Phase 2 | Pending |
| CORE-02 | Phase 2 | Pending |
| CORE-03 | Phase 2 | Pending |
| CORE-04 | Phase 2 | Pending |
| PROF-01 | Phase 3 | Pending |
| PROF-02 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 11 total
- Mapped to phases: 11
- Unmapped: 0 ✓

---
*Last updated: 2026-07-24 after initial definition*
