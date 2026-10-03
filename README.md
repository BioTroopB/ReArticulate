# 🦴 ReArticulate

**Prototype ML tool to predict whether two primate shoulder bones belong to the same individual**

ReArticulate is an experimental pair-matching classifier for reassociating commingled / disassociated primate shoulder elements (clavicle, scapula, humerus). It is a **demo / research prototype**, not a production same-individual matcher. For production landmark-based species/sex/side ID, see [PrimateOsteoID V3](https://github.com/BioTroopB/PrimateOsteoID).

---

## How to Use

1. Upload a landmark coordinate file (`.txt` or `.dta`) for **Bone 1**, or paste coordinates
2. Upload or paste landmarks for **Bone 2**
3. The app detects bone type from landmark count
4. Click **Predict Same Individual?**
5. Returns **SAME INDIVIDUAL** or **DIFFERENT INDIVIDUALS** with a model probability

**Supported bones**: Clavicle (7 landmarks), Humerus (16 landmarks), Scapula (13 landmarks)

**Supported taxa** (7 total):
- C = *Cercopithecus ascanius*
- H = *Hylobates lar*
- T = *Trachypithecus cristatus*
- G = *Gorilla gorilla*
- P = *Pan troglodytes*
- O = *Pongo pygmaeus*
- M = *Macaca mulatta*

---

## Important: what the shipped metrics mean

The live Space still loads **`bone_reassociation_xgboost_v2.pkl`**. Older banners quoted **91.3% accuracy** and **ROC-AUC 0.945**. Those figures come from a training/eval setup that mixes easy negatives (different taxon / sex) and is **not** a fair measure of “same animal” performance on realistic pairs.

An Oct 2026 audit with corrected specimen labels and an **individual-level holdout** found:

| Evaluation slice | What it tests | Takeaway |
|---|---|---|
| Full bone pairs | Includes easy different-taxon/sex negatives | Headline accuracy looks high but is dominated by easy “different” cases |
| Same species, different element | Realistic reassociation use case | Precision at 0.5 is low (~15–32% depending on model); not a reliable matcher |
| Same species + same sex, different element | Hardest / most relevant subset | Near chance for honest same-individual separation (AUC ~0.58–0.73); size ratio barely helps |

**Bottom line:** the five-feature XGBoost model mainly acts as a **same-taxon / same-sex compatibility filter**, not a trustworthy same-individual classifier. Treat scores as experimental.

### Features the model uses

| Feature | Meaning | At inference in this app |
|---|---|---|
| `same_species` | Same taxon label | **Hardcoded `1`** (app does not ask for species) |
| `same_element` | Same bone type | `1` if landmark counts match, else `0` |
| `same_side` | Same side | Match of selected sides; **Unknown → treated as same** (`1`) |
| `same_sex` | Same sex label | **Hardcoded `1`** (app does not ask for sex) |
| centroid-size ratio | `min(cs1,cs2)/max(cs1,cs2)` | From uploaded landmark coordinates |

`bone_reassociation_xgboost_prototype_v1.1.pkl` is unused legacy weights.

A corrected-label retrain (`v3`) was evaluated locally and **not shipped**, because it still fails the hard same-species/same-sex subset.

---

## Methodology

Technical write-up (centroid size, size ratio, XGBoost settings, original validation narrative):

→ [ReArticulate v1: Comprehensive Methodology (PDF)](ReArticulate_v1_Methodology_Overview.pdf)

Note: the PDF’s headline accuracy should be read with the caveats above.

---

## Live Demo

→ [ReArticulate v1 on Hugging Face](https://huggingface.co/spaces/BioTroopB/ReArticulate-v1) (private Space)

---

## Data Summary

- **158 complete individuals** with clavicle + humerus + scapula
- **7 nonhuman primate taxa**
- Anonymized internal IDs only (no museum numbers to the model)
- Trained on **landmark coordinate-derived features** only (no raw 3D scans)

### Lab data constraint (why landmark-in, not `.ply`-in)

Labeled 3D surface scans (`.ply`) exist for these specimens, but lab instruction **prohibits training AI models on that mesh / scan data** (and bars use of human data). For that reason:

- Models use only **coordinate / landmark-derived features** (match flags and centroid size)
- Raw scans are **not** training input
- A future “upload `.ply` → auto-landmarks → match” front-end would need a rule change or a landmarking tool **not** trained on those barred scans

This is a **data-use constraint**, not a claim that mesh landmarking is impossible in general.

---

## Credits

### Project Lead & Development
- **Kevin P. Klier**, M.A. Anthropology, University at Buffalo

### Scientific Oversight
- **Noreen von Cramon-Taubadel**, Ph.D.

### 3D Scan Collection
Scans performed by:
- Brittany Kenyon-Flatt
- Evan Simons
- Marianne Cooper
- Amandine Eriksen
- Kevin P. Klier (*Macaca mulatta*)

### Specimen Collections
- American Museum of Natural History (AMNH)
- Neil C. Tappen Collection, University of Minnesota (NCT)
- Field Museum of Natural History (FMNH)
- Harvard Museum of Comparative Zoology (MCZ)
- University at Buffalo Primate Skeletal Collection (UBPSC)
- Cleveland Museum of Natural History (CMNH)

### Funding & Support
Work conducted with support from the **National Science Foundation**.

---

## Development
- **Code & models**: Kevin P. Klier
- **AI pair programming assistance**: Grok (xAI), Claude (Anthropic)

---

## License

- **Code & Models**: MIT License
- **Documentation**: CC-BY 4.0 (cite Kevin P. Klier if reused)

---

*"Helping reassociate the disassociated — one bone at a time."*
— **Kevin P. Klier**, 2026
