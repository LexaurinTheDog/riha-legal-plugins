"""Složí PNG snímky do MP4 (1920x1080, H.264, prolínačky).

python3 build_video.py                  -> frames/*.png -> promo.mp4 (karty 5 s, záběry 6,5 s)
build(frames, durations, out)           -> obecné použití z jiných skriptů
"""
import glob, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
XF = 0.6


def build(frames, dur, out):
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for f, d in zip(frames, dur):
        cmd += ["-loop", "1", "-t", str(d), "-i", f]
    filt, prev, offset = [], "[0:v]", 0.0
    for i in range(1, len(frames)):
        offset += dur[i - 1] - XF
        filt.append(f"{prev}[{i}:v]xfade=transition=fade:duration={XF}:offset={offset:.2f}[v{i}]")
        prev = f"[v{i}]"
    filt.append(f"{prev}format=yuv420p[out]")
    cmd += ["-filter_complex", ";".join(filt), "-map", "[out]", "-r", "30",
            "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    print(f"{os.path.basename(out)}: {len(frames)} snímků, {sum(dur) - XF * (len(frames) - 1):.1f} s")


if __name__ == "__main__":
    frames = sorted(glob.glob(os.path.join(HERE, "frames", "*.png")))
    # první tři a poslední dvě jsou titulkové karty
    dur = [5.0 if i < 3 or i >= len(frames) - 2 else 6.5 for i in range(len(frames))]
    build(frames, dur, os.path.join(HERE, "promo.mp4"))
