
import urllib.request
from urllib.parse import urlparse, parse_qs

PLAYLISTS = [
    (
        "SonyLIV",
        "https://raw.githubusercontent.com/sportlive18/Sonyliv-Playlist-Autoupdate/refs/heads/main/sonyliv.m3u"
    ),

    (
        "JioSTB Plus",
        "https://jiostbplus.saregojo99.workers.dev/m3u"
    ),
(
        "Fancode",
        "https://premiumplugx.top/mylive/playlist.php"
),
    (
        "Star TV",
        "https://mainplaylist.poonamchouhan076.workers.dev/"
    ),

    (
        "Fancode",
        "https://raw.githubusercontent.com/doctor-8trange/zyphx8/refs/heads/main/data/fancode.m3u"
    )
]

combined = ["#EXTM3U"]
total_channels = 0

for name, url in PLAYLISTS:

    print(f"\nDownloading: {name}")

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=120) as response:
            content = response.read().decode("utf-8-sig")

        lines = content.splitlines()
        channel_count = 0

        for line in lines:

            line = line.strip()

            if not line or line == "#EXTM3U":
                continue

            # Remove proxy wrapper, preserve original MPD URL
            if line.startswith("http") and "/proxy?url=" in line:

                parsed = urlparse(line)

                original_url = parse_qs(
                    parsed.query
                ).get("url", [])

                if original_url:
                    line = original_url[0]

            combined.append(line)

            if line.startswith("#EXTINF:"):
                channel_count += 1

        total_channels += channel_count

        print(f"{name}: {channel_count} channels")

    except Exception as error:
        print(f"ERROR downloading {name}: {error}")
        raise

with open("Combined.m3u", "w", encoding="utf-8") as file:
    file.write("\n".join(combined) + "\n")

print("\n==========================")
print("MERGE SUCCESSFUL")
print("Total channels:", total_channels)
print("Output: Combined.m3u")
print("==========================")
