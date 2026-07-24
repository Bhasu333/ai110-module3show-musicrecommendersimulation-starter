"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    profiles = [
        {"name": "EDM Fan", "genre": "edm", "mood": "intense", "energy": 0.9, "likes_acoustic": False},
        {"name": "Chill Lofi Listener", "genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True},
        {"name": "Synthwave/Rock Enthusiast", "genre": "synthwave", "mood": "moody", "energy": 0.75, "likes_acoustic": False}
    ]

    for p in profiles:
        print(f"--- Recommendations for {p['name']} ---")
        recs = recommend_songs(p, songs, k=3)
        for rec in recs:
            song, score, explanation = rec
            print(f"{song['title']} ({song['genre']}) - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
