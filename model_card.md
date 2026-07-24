# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This recommender generates personalized song suggestions by scoring and ranking track attributes against a user's stated taste profile. 
- **Recommendations**: Generates a sorted list of the top `k` matching songs.
- **Assumptions**: Assumes users can accurately state their favorite genre, mood, target energy (on a 0.0 to 1.0 scale), and whether they prefer acoustic sounds.
- **Audience**: Designed for classroom exploration and basic algorithmic simulation.

---

## 3. How the Model Works  

VibeFinder uses a content-based filtering approach:
- **Song Features**: Genre, mood, energy level (0.0 to 1.0), and acousticness (0.0 to 1.0).
- **Taste Preferences**: Favorite genre, favorite mood, target energy, and a yes/no preference for acoustic music.
- **Scoring**: It computes a final score out of 8.0 max. Matching the genre exactly is worth 3.0 points. Matching the mood is worth 2.0 points. The energy score (up to 2.0 points) is calculated based on how close the song's energy is to the target. Acousticness matches are worth 1.0 point (adding acousticness for acoustic fans, and subtracting it for non-acoustic fans).
- **Starter Logic Changes**: We expanded the algorithm to support acousticness preferences and added structured text explanations explaining the exact points breakdown.

---

## 4. Data  

- **Catalog Size**: 20 songs.
- **Represented Genres & Moods**: Pop, lofi, rock, ambient, jazz, synthwave, hip-hop, and edm. Moods include happy, chill, intense, relaxed, moody, and focused.
- **Data Changes**: We expanded the starter CSV from 10 songs to 20 songs to test cross-genre matching and profile behaviors under a larger set.
- **Missing Elements**: Missing lyrics, sub-genres, release year, artist fame/reputation, and cultural context.

---

## 5. Strengths  

- **Capturing Niche Vibes**: Works really well for users with clear, high-contrast tastes, like a chill lofi fan or an intense EDM lover.
- **Intuitive Scoring**: The proximity calculation for energy works great, correctly ranking tracks that match the user's intensity levels even if the genre differs.

---

## 6. Limitations and Bias  

- **Missing Features**: Does not consider tempo, valence (happiness), or song length.
- **Underrepresented Categories**: Classical, metal, and country are completely missing from the dataset.
- **Genre Overfitting**: Because genre is weighted heavily (3.0 out of 8.0), a user is highly likely to only get songs of their favorite genre, forming a filter bubble.
- **Popularity/Feedback Loops**: Since there is no user feedback loop (e.g., skips or likes), the recommendations are completely static.

---

## 7. Evaluation  

We tested the recommender using three distinct user profiles:
1. **EDM Fan**: (edm, intense, 0.9 energy, non-acoustic) -> Recommended high-energy, low-acousticness EDM tracks (`Techno Pulse`, `Electric Horizon`).
2. **Chill Lofi Listener**: (lofi, chill, 0.35 energy, acoustic) -> Successfully recommended lofi, low-energy, acoustic-heavy tracks (`Library Rain`, `Midnight Coding`).
3. **Synthwave/Rock Enthusiast**: (synthwave, moody, 0.75 energy, non-acoustic) -> Correctly recommended synthwave tracks (`Night Drive Loop`, `Neon Samurai`).

The scoring matched our intuition, showing that high-energy preferences properly filtered out ambient tracks.

---

## 8. Future Work  

- **Tempo and Valence**: Incorporate tempo_bpm and valence into the weighted similarity score.
- **Diversity Penalty**: Introduce a penalty for returning too many songs from the same artist or genre, forcing the list to be more diverse.
- **Dynamic Feedback**: Keep track of user skips and adjust the profile weights over time.

---

## 9. Personal Reflection  

I learned that content-based recommenders are simple to build but suffer from lack of diversity. It was interesting to see how small tweaks in weights drastically change what gets suggested. This assignment changed how I think about apps like Spotify. I now see how easy it is to get trapped in a "filter bubble" if an algorithm focuses too heavily on matching metadata rather than exploring collaborative user behavior.
