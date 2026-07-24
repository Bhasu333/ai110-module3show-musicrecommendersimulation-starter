from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic
        }
        res = []
        for s in self.songs:
            sd = {
                "id": s.id,
                "title": s.title,
                "artist": s.artist,
                "genre": s.genre,
                "mood": s.mood,
                "energy": s.energy,
                "tempo_bpm": s.tempo_bpm,
                "valence": s.valence,
                "danceability": s.danceability,
                "acousticness": s.acousticness
            }
            score, _ = score_song(prefs, sd)
            res.append((s, score))
        res.sort(key=lambda item: item[1], reverse=True)
        return [item[0] for item in res[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic
        }
        sd = {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "tempo_bpm": song.tempo_bpm,
            "valence": song.valence,
            "danceability": song.danceability,
            "acousticness": song.acousticness
        }
        val, reasons = score_song(prefs, sd)
        return f"Score: {val:.2f} because: " + (", ".join(reasons) if reasons else "general match")

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    songs = []
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                song = {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"])
                }
                songs.append(song)
    except Exception:
        pass
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    pts = 0.0
    reasons = []

    pref_genre = user_prefs.get("genre") or user_prefs.get("favorite_genre")
    if pref_genre is not None:
        if song.get("genre") == pref_genre:
            pts += 3.0
            reasons.append("matches favorite genre")

    pref_mood = user_prefs.get("mood") or user_prefs.get("favorite_mood")
    if pref_mood is not None:
        if song.get("mood") == pref_mood:
            pts += 2.0
            reasons.append("matches favorite mood")

    pref_energy = user_prefs.get("energy") or user_prefs.get("target_energy")
    if pref_energy is not None:
        diff = abs(song.get("energy") - float(pref_energy))
        energy_score = 2.0 * (1.0 - diff)
        pts += energy_score
        if diff < 0.15:
            reasons.append("energy is a close match")
        elif diff < 0.3:
            reasons.append("energy is a decent match")

    pref_acoustic = user_prefs.get("likes_acoustic")
    if pref_acoustic is not None:
        if pref_acoustic:
            pts += song.get("acousticness")
            if song.get("acousticness") > 0.6:
                reasons.append("high acousticness aligns with taste")
        else:
            pts += (1.0 - song.get("acousticness"))
            if song.get("acousticness") < 0.4:
                reasons.append("low acousticness aligns with taste")

    return pts, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored = []
    for s in songs:
        score, reasons = score_song(user_prefs, s)
        explanation = ", ".join(reasons) if reasons else "general recommendation"
        scored.append((s, score, explanation))
    
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
