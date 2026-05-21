from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = {
    "alex-hormozi-video1": "MD5-HByRxoA",
    "alex-hormozi-video2": "qsXxckCbci0",
    "chris-walker-video1": "vIuuRMEPWL0",
    "chris-walker-video2": "JkXom1dC_20",
    "dan-koe-video1": "7HM-rptYdTs",
    "dan-koe-video2": "_VhxCfUb2Ys"
}

os.makedirs("transcripts", exist_ok=True)

ytt_api = YouTubeTranscriptApi()

for name, video_id in videos.items():
    try:
        transcript = ytt_api.fetch(video_id)

        with open(f"transcripts/{name}.txt", "w", encoding="utf-8") as f:
            for line in transcript:
                f.write(line.text + "\n")

        print(f"Saved transcript for {name}")

    except Exception as e:
        print(f"Error with {name}: {e}")