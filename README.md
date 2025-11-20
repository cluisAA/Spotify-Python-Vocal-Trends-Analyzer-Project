# Vocal Evolution 🚀

2025-proof Spotify vocal shift analyzer.

Spotify killed open access to audio features (energy, speechiness, valence, etc.) for normal developer apps in late 2024 → every old script dies with 403 Forbidden.

This is the **only version that still works** in 2025 without paying Spotify for enterprise access.

### What it proves
Pop vocals shifted dramatically:
- 2010s → mid-2010s: low growls, rap delivery, explicit lyrics
- Late 2010s → 2025: high falsettos, clean/smooth vocals, emotional pop

### How it works now (the 69 proxy)
Since we can't get real audio features, we use the only free data Spotify still gives:
- Track popularity (0–100)
- Explicit tag

→ High popularity + clean lyrics = **Falsetto / Clean Pop** score  
→ Low popularity + explicit = **Growl / Rap** score

Surprisingly accurate in 2025 pop.

### Features
- Pulls Recently Played (updates instantly) + Top Tracks over time
- No 403 errors, no broken playlist IDs, no paid dev account needed
- Fully commented, safe credentials handling
- Automatically saves your graph as `VOCAL_EVOLUTION_69.png`

### Setup (one-time)
1. Get your Spotify Client ID & Secret from https://developer.spotify.com/dashboard
2. Put them in `auth.py` (never commit real keys!)
3. Play some music on Spotify
4. Run `python3 vocal_evolution_69.py`

The more you listen, the better the graph gets.

### Requirements
- Python 3
- `spotipy`, `pandas`, `matplotlib` (install with `pip install spotipy pandas matplotlib`)

Created by LuisBoss – the guy who refused to lose to Spotify's API lockdown.
