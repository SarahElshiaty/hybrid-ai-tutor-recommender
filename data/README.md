# Project datasets

The original project uses four related CSV datasets.

| File | Purpose | Distribution |
| --- | --- | --- |
| `CurriculumSubject.csv` | Curriculum and subject reference data | Included here |
| `StudentProfile.csv` | Student preferences and characteristics | Download locally |
| `TutorCourse.csv` | Tutor profiles and course information | Download locally |
| `InteractionDataset.csv` | Historical tutor ratings and interactions | Download locally |

The three profile and interaction files contain **names and student-related attributes**. Their provenance and permission for redistribution are not documented in the original repository. This standalone repository does not duplicate them.

If you are authorized to use the original data for academic research, run `python scripts/fetch_data.py` from the repository root. The script downloads the original files from the [team repository](https://github.com/M1sh13l/AI-Tutor-Recommendation-System/tree/main/data), verifies their Git blob checksums, and leaves them untracked locally.

Do not publish the profiles or deploy them in a public demo unless the dataset's provenance and rights have been established.
