#!/usr/bin/env python3
"""Download the original course-project datasets for local research use."""
from hashlib import sha1
from pathlib import Path
from urllib.request import urlopen

SOURCE = "https://raw.githubusercontent.com/M1sh13l/AI-Tutor-Recommendation-System/main/data"
FILES = {
    "StudentProfile.csv": "a8981c189232ec04dff11315a2ae57b9ff902adc",
    "TutorCourse.csv": "7f1e1d1d0d4b353893914b1df2cb23c62e5ad365",
    "InteractionDataset.csv": "a7804e0ccef7a3485ab52087d19495306e8584c2",
}
DEST = Path(__file__).resolve().parents[1] / "data"

def git_blob_sha(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    for name, expected in FILES.items():
        target = DEST / name
        if target.exists():
            existing = target.read_bytes()
            if git_blob_sha(existing) == expected:
                print(f"Verified: {name}")
                continue
            raise SystemExit(f"Existing {name} differs from the original. Review it before replacing.")
        with urlopen(f"{SOURCE}/{name}", timeout=90) as response:
            data = response.read(12_000_000)
        actual = git_blob_sha(data)
        if actual != expected:
            raise SystemExit(f"Checksum mismatch for {name}: {actual}")
        target.write_bytes(data)
        print(f"Downloaded and verified: {name}")
    print("Data files are ready for local use; they are ignored by Git.")

if __name__ == "__main__":
    main()
