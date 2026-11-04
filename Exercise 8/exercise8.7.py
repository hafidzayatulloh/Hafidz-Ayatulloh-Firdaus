def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


print(make_album('Sheila on 7', 'Kisah Klasik'))
print(make_album('Tulus', 'Monokrom'))
print(make_album('Dewa 19', 'Pandawa Lima'))
print(make_album('Raisa', 'Heart to Heart', tracks=10))