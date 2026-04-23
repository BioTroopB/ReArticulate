# 🦴 ReArticulate

**ML-powered tool to predict whether two primate shoulder bones belong to the same individual**

ReArticulate is a prototype AI classifier built to help reassociate commingled and disassociated primate skeletal elements — directly addressing the needs of skeletal biologists working with mixed bone assemblages.

---

## How to Use

1. Paste the landmark coordinate data (`.txt` format) into **Bone 1** and **Bone 2**
2. Select the **Side** for each bone (L / R / Unknown)
3. Click **🔍 Predict Same Individual?**
4. The app returns:
   - **SAME INDIVIDUAL** (with probability + balloon animation)  
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
- Same side (now user-selectable)
- Same taxon (assumed in prototype)
- Same sex (assumed in prototype)

---

## Live Demo

→ [ReArticulate v1 on Hugging Face](https://huggingface.co/spaces/BioTroopB/ReArticulate-v1)

---

## GitHub Repository

https://github.com/BioTroopB/ReArticulate

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
Conducted for the **Buffalo Human Evolutionary Morphology Lab (BHEML)**, supported by the **National Science Foundation**.

### Development
- **Code & models**: Kevin P. Klier
- **AI assistance**: Grok (xAI)

---

## License

- **Code & Models**: MIT License
- **Documentation**: CC-BY 4.0 (cite Kevin P. Klier if reused)

---

*"Helping reassociate the disassociated — one bone at a time."*  
— **Kevin P. Klier**, Buffalo Human Evolutionary Morphology Lab, 2026# ReArticulate
ML-powered tool to predict whether two primate shoulder bones belong to the same individual
