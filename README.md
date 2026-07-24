# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This is a Python-based content-based music recommender simulator. It takes a user taste profile (favorite genre, favorite mood, target energy, and acoustic preference) and ranks songs from a CSV file using a weighted scoring formula. The system outputs the top recommended tracks along with a plain-text explanation of why they were suggested.

---

## How The System Works

Our recommendation system uses a content-based filtering approach, matching song features directly with user preferences:

- **Song Attributes**:
  - `genre` (e.g., pop, rock, lofi)
  - `mood` (e.g., happy, chill, intense)
  - `energy` (continuous float value from 0.0 to 1.0)
  - `acousticness` (continuous float value from 0.0 to 1.0 representing how acoustic the song is)
- **UserProfile Taste Info**:
  - `favorite_genre`: Preferred music genre.
  - `favorite_mood`: Preferred emotional vibe.
  - `target_energy`: Ideal energy level (float 0.0 to 1.0).
  - `likes_acoustic`: Boolean flag indicating if the user prefers acoustic sounds.
- **Scoring Rule**:
  - **Genre Match** (Weight = 3.0): If `song.genre` matches `user.favorite_genre`, add 3.0 points.
  - **Mood Match** (Weight = 2.0): If `song.mood` matches `user.favorite_mood`, add 2.0 points.
  - **Energy Similarity** (Weight = 2.0): Calculate as `2.0 * (1.0 - abs(song.energy - user.target_energy))`. Songs closer to the target energy receive higher points.
  - **Acousticness Match** (Weight = 1.0): If `user.likes_acoustic` is True, add `1.0 * song.acousticness`. If False, add `1.0 * (1.0 - song.acousticness)`.
- **Ranking Rule**:
  - The system scores all songs, sorts them in descending order of score, and selects the top `k` highest-scoring songs to recommend. Ties are resolved by the song's position in the dataset.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Here is the simulation output from the command line run showing recommendations for different user profiles:

```
Top recommendations:

Sunrise City - Score: 7.78
Because: matches favorite genre, matches favorite mood, energy is a close match, low acousticness aligns with taste

Gym Hero - Score: 5.69
Because: matches favorite genre, energy is a close match, low acousticness aligns with taste

Golden Gate Groove - Score: 4.81
Because: matches favorite mood, energy is a close match, low acousticness aligns with taste

Electric Horizon - Score: 4.80
Because: matches favorite mood, energy is a close match, low acousticness aligns with taste

Rooftop Lights - Score: 4.57
Because: matches favorite mood, energy is a close match, low acousticness aligns with taste

--- Recommendations for EDM Fan ---
Techno Pulse (edm) - Score: 7.92
Because: matches favorite genre, matches favorite mood, energy is a close match, low acousticness aligns with taste

Electric Horizon (edm) - Score: 5.96
Because: matches favorite genre, energy is a close match, low acousticness aligns with taste

Raging Thunder (rock) - Score: 4.89
Because: matches favorite mood, energy is a close match, low acousticness aligns with taste

--- Recommendations for Chill Lofi Listener ---
Library Rain (lofi) - Score: 7.86
Because: matches favorite genre, matches favorite mood, energy is a close match, high acousticness aligns with taste

Midnight Coding (lofi) - Score: 7.57
Because: matches favorite genre, matches favorite mood, energy is a close match, high acousticness aligns with taste

Focus Flow (lofi) - Score: 5.68
Because: matches favorite genre, energy is a close match, high acousticness aligns with taste

--- Recommendations for Synthwave/Rock Enthusiast ---
Night Drive Loop (synthwave) - Score: 7.78
Because: matches favorite genre, matches favorite mood, energy is a close match, low acousticness aligns with taste

Neon Samurai (synthwave) - Score: 5.66
Because: matches favorite genre, energy is a close match, low acousticness aligns with taste

Chillwave Coast (synthwave) - Score: 5.36
Because: matches favorite genre, energy is a decent match, low acousticness aligns with taste
```

---

## Experiments You Tried

We ran a few testing scenarios to see how recommendations shifted:
- **Genre Dominance**: Keeping the genre weight at 3.0 makes sure that songs of the same genre are always pushed to the top, even if their energy or acousticness isn't a perfect match. When we temporarily set the genre weight to 0.5, cross-genre recommendations started appearing because the score relied more heavily on energy and mood alignment.
- **Valence and Tempo**: We experimented with adding tempo to the scoring. We found that without normalization, tempo (with values around 60-150 BPM) completely dominates the score. We had to exclude it or scale it down.
- **Acousticness weight**: Adjusting the acousticness weight to 1.0 worked well for differentiating lofi/acoustic lovers from EDM fans who hate acoustic sounds.

---

## Limitations and Risks

- **Tiny Catalog**: We are only querying a dataset of 20 songs, which limits the diversity and availability of matches.
- **Filter Bubbles**: Because we use static content features, a user who likes "lofi" will only ever receive lofi songs. They will never discover new genres since there is no collaborative discovery mechanism.
- **Hard-coded weights**: The weights on features (genre: 3.0, mood: 2.0, etc.) are fixed and might not represent how an individual actually values music (e.g. some people care way more about tempo than genre).

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

I learned how content-based recommender systems rely on matching item metadata with user tastes through simple distance and similarity calculations. It was interesting to see how changing weights immediately alters what a user gets recommended. For instance, putting a high weight on genre locks users into a specific genre loop, creating a strong filter bubble.

In real-world apps like Spotify, this bias is handled by combining content-based algorithms with collaborative filtering (what similar users listen to) and session history. Doing this prevents users from getting stuck in repetitive recommendation loops. Overall, this project helped me understand the mathematical backing behind everyday recommender features and the trade-offs involved in tuning them.




