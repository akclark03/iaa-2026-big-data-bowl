# NFL Big Data Bowl 2026 - Analytics

### Institute for Advanced Analytics — University Track Submission

Explore the 2026 NFL Big Data Bowl, the league’s premier analytics competition powered by AWS and hosted on Kaggle:  
[Big Data Bowl Overview](https://operations.nfl.com/gameday/analytics/big-data-bowl/)  

The Big Data Bowl is an annual crowd-sourced data science competition that leverages **NFL Next Gen Stats (NGS)** and traditional play data to drive innovation in football strategy, safety, and performance.
This year’s challenge invites participants to **predict player movement after the football is thrown**, using pre-throw data from the 2023–2024 NFL seasons. Models will be evaluated on how accurately they forecast player positions during the ball’s flight.

Our team — composed of graduate students at the **Institute for Advanced Analytics** — is competing in the **University Track**, which is open exclusively to undergraduate and graduate students.

---

## Data

Official competition data is hosted on Kaggle:  
[NFL Big Data Bowl 2026 - Analytics](https://www.kaggle.com/c/nfl-big-data-bowl-2026-analytics)

The dataset includes:

- Player tracking data from the 2023–2024 NFL seasons (Weeks 14–18)
- Pre- and post-snap positioning data
- Play-level contextual and metadata information
- Target labels for player movement trajectories

---

## Project Structure

```
iaa-2026-big-data-bowl/
│
├── data/                     # Raw and processed datasets
├── notebooks/                # Jupyter notebooks
├── src/                      # Source code root
│   └── nfl_competition_analytics/  # Python scripts
├── tests/                    # Unit and integration tests
├── environment.yml           # Conda environment specification
├── requirements.txt          # List of dependencies
├── README.md                 # Project overview, setup, and team info
├── LICENSE                   # License file
└── .gitignore                # Exclude data, cache, and environment files from Git
```

---

## Environment Setup (Using Conda)

To set up and reproduce our environment:

1. **Install Conda**
   - [Miniconda Installation Guide](https://docs.conda.io/en/latest/miniconda.html)

2. **Create a new environment**

```bash
conda create -n bigdatabowl python=3.11
conda activate bigdatabowl
```

3. **Install dependencies from requirements.txt**

```bash
conda install --file requirements.txt
```

If some packages are unavailable via conda, install them via pip:

```bash
pip install -r requirements.txt
```

4. **Launch JupyterLab**

```bash
jupyter lab
```

5. **(Optional) Add environment to Jupyter kernels**

```bash
conda install ipykernel
python -m ipykernel install --user --name=bigdatabowl
```

To ensure reproducibility, environment specifications can be exported:

```bash
conda env export > environment.yml
```

---

## Team Members

This submission represents work completed by graduate students at the Institute for Advanced Analytics
for the University Track of the NFL Big Data Bowl 2026 competition.

| Name | Role | Contact / Profile |
|------|------|------------------|
| Andrew Clark | TBD| TBA |
| Troy Hall | TBD | TBA |
| Tavis Propst | TBD | TBA |
| Zachary Richardson | TBD | TBA |

---

© 2025 Andrew Clark, Troy Hall, Travis Propst, Zachary Richardson
