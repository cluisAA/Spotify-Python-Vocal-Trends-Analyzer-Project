# vocal_evolution_69.py - The forbidden vocal shift analyzer (2025 edition)

import pandas as pd
import matplotlib.pyplot as plt
from auth import create_spotify

sp = create_spotify()
data = []

print("VOCAL EVOLUTION 69 – Loading your listening history...\n")

# Recently Played - updates instantly
try:
    recent = sp.current_user_recently_played(limit=50)['items']
    for item in recent:
        track = item['track']
        data.append({
            'period': 'Recent Plays',
            'artist': track['artists'][0]['name'],
            'song': track['name'],
            'popularity': track['popularity'],
            'explicit': 1 if track['explicit'] else 0
        })
except:
    pass

# Top tracks over time
for timeframe, label in [("long_term", "All Time"), ("medium_term", "Last 6 Months"), ("short_term", "Recent Top")]:
    try:
        tracks = sp.current_user_top_tracks(limit=30, time_range=timeframe)['items']
        for track in tracks:
            data.append({
                'period': label,
                'artist': track['artists'][0]['name'],
                'song': track['name'],
                'popularity': track['popularity'],
                'explicit': 1 if track['explicit'] else 0
            })
    except:
        pass

df = pd.DataFrame(data)

if len(df) == 0:
    print("No tracks yet — play some music on Spotify, then run again in 5 minutes!")
else:
    # The 69 Proxy (works without audio features)
    df['falsetto_clean_score'] = df['popularity'] * (1 - df['explicit']) * 1.5
    df['growl_rap_score'] = (100 - df['popularity']) * df['explicit'] * 2

    avg = df.groupby('period')[['falsetto_clean_score', 'growl_rap_score']].mean().reset_index()

    plt.figure(figsize=(16, 10))
    plt.plot(avg['period'], avg['falsetto_clean_score'], 'o-', linewidth=8, markersize=20, color='#ff1493', label='High Falsetto / Clean Pop Trend')
    plt.plot(avg['period'], avg['growl_rap_score'], 's-', linewidth=8, markersize=20, color='#9400d3', label='Low Growl / Rap Trend')
    plt.title('VOCAL EVOLUTION 69 – Your Real Shift in 2025', fontsize=28, fontweight='bold')
    plt.ylabel('Dominance Score', fontsize=18)
    plt.xlabel('Listening Period', fontsize=18)
    plt.legend(fontsize=20)
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.savefig('VOCAL_EVOLUTION_69.png', dpi=400, bbox_inches='tight')
    print(f"\nCollected {len(df)} tracks – Graph saved as VOCAL_EVOLUTION_69.png")
    print("Welcome to 69. 💀🚀")
    plt.show()
