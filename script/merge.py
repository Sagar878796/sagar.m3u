
import urllib.request
import os

PLAYLISTS = [
    {
        "name": "JioSTB Plus",
        "url": "https://jiostbplus.saregojo99.workers.dev/m3u"
    },
    {
        "name": "SonyLIV",
        "url": "https://raw.githubusercontent.com/sportlive18/Sonyliv-Playlist-Autoupdate/refs/heads/main/sonyliv.m3u"
    }
]

output = ["#EXTM3U"]

for playlist in PLAYLISTS:
    print("Downloading:", playlist["name"])

    request = urllib.request.Request(
        playlist["url"],
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(request, timeout=90) as response:
        content = response.read().decode("utf-8-sig")

    lines = content.splitlines()

    for line in lines:
        line = line.strip()

        if line and line != "#EXTM3U":
            output.append(line)

output_file = "Combined.m3u"

with open(output_file, "w", encoding="utf-8") as file:
    file.write("\n".join(output) + "\n")

print("Merge completed successfully!")
print("Total lines:", len(output))
print("Output:", output_file)
