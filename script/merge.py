
name: Merge M3U Playlists

on:
  workflow_dispatch:
  schedule:
    - cron: '*/30 * * * *'

permissions:
  contents: write

jobs:
  merge:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Download and Merge M3U
        run: |
          set -e

          URL1="https://jiostbplus.saregojo99.workers.dev/m3u"
          URL2="https://raw.githubusercontent.com/sportlive18/Sonyliv-Playlist-Autoupdate/refs/heads/main/sonyliv.m3u"

          curl -fLsS "$URL1" -o jio.m3u
          curl -fLsS "$URL2" -o sony.m3u

          echo "#EXTM3U" > Combined.m3u

          for file in jio.m3u sony.m3u; do
            sed '1{/^#EXTM3U/d;}' "$file" >> Combined.m3u
          done

          rm jio.m3u sony.m3u

      - name: Commit Updated Playlist
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add Combined.m3u
          git diff --cached --quiet || git commit -m "Update Combined M3U"
          git push
