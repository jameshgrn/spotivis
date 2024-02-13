def get_saved_tracks(spotify_client):
    results = spotify_client.current_user_saved_tracks()
    saved_tracks = []
    while results:
        for item in results['items']:
            track = item['track']
            saved_tracks.append({
                'id': track['id'],
                'name': track['name'],
                'artist': ', '.join([artist['name'] for artist in track['artists']]),
                'album': track['album']['name'],
                'release_date': track['album']['release_date'],
                'popularity': track['popularity']
            })
        if results['next']:
            results = spotify_client.next(results)
        else:
            break
    return saved_tracks
