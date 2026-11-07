# Hybrid Tutor Recommendation System

**Python · pandas · Surprise SVD · Gradio**  
Computer Science team project, Effat University

A tutor recommendation prototype that combines profile-based matching rules with collaborative filtering. The project considers subjects, curriculum, grade, location and session preferences when ranking tutors, then uses historical ratings to estimate student–tutor preferences.

## How it works

1. Standardizes student, tutor, curriculum and interaction data.
2. Groups education types into five broad categories for matching.
3. Uses soft matching rules to identify and score tutor candidates.
4. Trains a matrix-factorization model (Surprise SVD) on student–tutor ratings.
5. Combines candidate scores and predicted ratings to rank recommendations.
6. Examines top-five recommendation metrics, catalog coverage and exposure by tutor popularity.

The interface is a **Gradio prototype**, not a deployed tutoring marketplace.

## Results

The original project reports the following figures from its strict evaluation:

| Metric | Reported result |
| --- | ---: |
| Precision@5 | 0.8920 |
| Recall@5 | 0.9957 |
| NDCG@5 | 0.9538 |
| Catalog coverage | 85.35% |
| Exposure to less-popular tutors | 63.84% |

These are results **reported by the project**, not independently reproduced benchmarks. Exposure by popularity is a descriptive distribution measure; it does not establish demographic fairness or unbiased recommendations. The datasets and experimental evaluation setup should be reviewed before comparing these figures with other recommenders.

## Repository contents

| Path | Description |
| --- | --- |
| [src/recommender.py](src/recommender.py) | Adapted local-path version of the academic experiment |
| [research/ai_student_tutor_colab_export.py](research/ai_student_tutor_colab_export.py) | Original Colab-exported source preserved for reference |
| [data/](data/) | Four original datasets and their source information |
| [requirements.txt](requirements.txt) | Python dependencies |
| [CONTRIBUTORS.md](CONTRIBUTORS.md) | Team and original repository attribution |

## Running locally

The project was originally developed in Google Colab. A separate script under `src/` replaces the Drive mount and notebook package-install commands with local paths.

1. Install Python and create a virtual environment.
2. Install the [requirements](requirements.txt): `python -m pip install -r requirements.txt`.
3. Ensure these files are present in `data/`: `StudentProfile.csv`, `TutorCourse.csv`, `InteractionDataset.csv` and `CurriculumSubject.csv`. See [data instructions](data/README.md).
4. Run `python src/recommender.py` to execute the experiment and launch the Gradio interface.

Some combinations of Python, NumPy, Surprise and Gradio may require compatible package versions. **The full training and interface flow has not been independently rerun in a clean environment**, so these are setup instructions rather than a passing end-to-end test.

## Contributors

**Sarah Elshiaty · Mashael Saeed · Seifeldin Elshiaty**

Built as a collaborative university project. The [original team repository](https://github.com/M1sh13l/AI-Tutor-Recommendation-System) retains the development history. Sarah's [existing fork](https://github.com/SarahElshiaty/AI-Tutor-Recommendation-System) also remains available.

This is an academic prototype. It does not claim deployment, prospective evaluation, or proven fairness across student or tutor groups.
