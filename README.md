# 🦴 ReArticulate

**ML-powered tool to predict whether two primate shoulder bones belong to the same individual**

ReArticulate is a prototype AI classifier built to help reassociate commingled and disassociated primate skeletal elements — directly addressing the needs of skeletal biologists working with mixed bone assemblages.

---

## How to Use

1. Upload a landmark coordinate file (`.txt` or `.dta`) for **Bone 1** using the file uploader, or paste coordinates directly into the text box
2. Upload a landmark coordinate file (`.txt` or `.dta`) for **Bone 2** using the file uploader, or paste coordinates directly into the text box
3. The app will automatically detect the bone type from the number of landmarks
4. Click **🔍 Predict Same Individual?**
5. The app instantly returns:
   - **SAME INDIVIDUAL** (with probability) + balloon animation 🎈
   - or **DIFFERENT INDIVIDUALS** (with probability)

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

## Model Performance

| Metric              | Value    |
|---------------------|----------|
| **Accuracy**        | **91.3%** |
| **ROC-AUC**         | **0.945** |
| Training individuals| 158      |
| Total bones         | 474      |

The model uses 5 biologically meaningful features:
- Same element type
- Centroid size ratio
- Same taxon (assumed in this prototype)
- Same side (assumed)
- Same sex (assumed)

---

## Live Demo

→ [ReArticulate v1 on Hugging Face](https://huggingface.co/spaces/BioTroopB/ReArticulate-v1)

---

## Data Summary

- **158 complete individuals** with all three shoulder bones (clavicle + humerus + scapula)
- **7 nonhuman primate taxa**
- All data fully anonymized (internal IDs only — no museum numbers visible to the model)
- Trained exclusively on **landmark coordinate data** (no raw 3D scans)

---

## Credits

### Project Lead & Development
- **Kevin P. Klier**, M.A. Anthropology, University at Buffalo

### Scientific Oversight
- **Noreen von Cramon-Taubadel**, Ph.D.  
  (Buffalo Human Evolutionary Morphology Lab)

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
Conducted at the **Buffalo Human Evolutionary Morphology Lab (BHEML)**, supported by the **National Science Foundation**.

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
— **Kevin P. Klier**, Buffalo Human Evolutionary Morphology Lab, 2026
