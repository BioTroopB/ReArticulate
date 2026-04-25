import streamlit as st
import numpy as np
import joblib
import base64
import io

st.set_page_config(page_title="ReArticulate", page_icon="🦴", layout="wide")

# ==================== CENTERED LOGO + TITLE ====================
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

try:
    img_b64 = get_base64_image("lab-logo.jpg")
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <img src='data:image/jpeg;base64,{img_b64}' width='220' style='display: block; margin: 0 auto 12px auto;'/>
            <h1 style='margin-top: 0;'>ReArticulate</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
except Exception:
    st.markdown("<h1 style='text-align: center;'>ReArticulate</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 18px;'>ML-powered tool — predicts whether two primate shoulder bones belong to the same individual</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #666;'>v1 • Trained on 158 complete individuals • XGBoost • 91.3% accuracy | 0.945 ROC-AUC</p>", unsafe_allow_html=True)

MODEL_PATH = "bone_reassociation_xgboost_v2.pkl"
model = joblib.load(MODEL_PATH)

def parse_landmarks(text):
    lines = [line.strip() for line in text.splitlines() if line.strip() and not line.startswith("#")]
    coords = []
    for line in lines:
        try:
            parts = line.split()
            if len(parts) >= 3:
                x, y, z = map(float, parts[:3])
                coords.append([x, y, z])
        except:
            pass
    return np.array(coords)

def get_centroid_size(coords):
    if len(coords) == 0:
        return 0.0
    return np.linalg.norm(coords - np.mean(coords, axis=0))

def detect_element(n):
    if n == 7:    return "clavicle"
    elif n == 16: return "humerus"
    elif n == 13: return "scapula"
    else:         return "unknown"

# ==================== RESET COUNTER ====================
if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

# ==================== RESET BUTTON ====================
if st.button("🔄 Restart / Clear All", type="secondary"):
    st.session_state.reset_counter += 1
    st.rerun()

st.markdown("---")

# ==================== LANDMARK INPUT ====================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🦴 Bone 1")
    uploaded1 = st.file_uploader(
        "Upload Bone 1 landmark file (.txt or .dta)", 
        type=["txt", "dta"], 
        key=f"upload1_{st.session_state.reset_counter}"
    )
    if uploaded1 is not None:
        text1 = io.StringIO(uploaded1.getvalue().decode("utf-8")).read()
    else:
        text1 = st.text_area("...or paste landmarks here", height=280, key=f"text1_{st.session_state.reset_counter}")
    c1 = parse_landmarks(text1)
    if len(c1) > 0:
        elem1 = detect_element(len(c1))
        st.success(f"✅ {len(c1)} landmarks → **{elem1}**")
    else:
        c1 = np.array([]); elem1 = "unknown"

    side1 = st.selectbox("Side (optional)", ["Unknown", "L", "R"], index=0, key=f"side1_{st.session_state.reset_counter}")

with col2:
    st.subheader("🦴 Bone 2")
    uploaded2 = st.file_uploader(
        "Upload Bone 2 landmark file (.txt or .dta)", 
        type=["txt", "dta"], 
        key=f"upload2_{st.session_state.reset_counter}"
    )
    if uploaded2 is not None:
        text2 = io.StringIO(uploaded2.getvalue().decode("utf-8")).read()
    else:
        text2 = st.text_area("...or paste landmarks here", height=280, key=f"text2_{st.session_state.reset_counter}")
    c2 = parse_landmarks(text2)
    if len(c2) > 0:
        elem2 = detect_element(len(c2))
        st.success(f"✅ {len(c2)} landmarks → **{elem2}**")
    else:
        c2 = np.array([]); elem2 = "unknown"

    side2 = st.selectbox("Side (optional)", ["Unknown", "L", "R"], index=0, key=f"side2_{st.session_state.reset_counter}")

st.markdown("---")

# ==================== PREDICTION ====================
if st.button("🔍 Predict Same Individual?", type="primary", use_container_width=True):
    if len(c1) == 0 or len(c2) == 0:
        st.error("Please upload or paste landmark data in both boxes.")
    elif elem1 == "unknown" or elem2 == "unknown":
        st.error("Unrecognised landmark count. Expected 7 (clavicle), 13 (scapula), or 16 (humerus).")
    else:
        same_element = 1 if elem1 == elem2 else 0

        if side1 == "Unknown" or side2 == "Unknown":
            same_side = 1
        else:
            same_side = 1 if side1 == side2 else 0

        cs1 = get_centroid_size(c1)
        cs2 = get_centroid_size(c2)
        size_ratio = min(cs1, cs2) / max(cs1, cs2) if max(cs1, cs2) > 0 else 0.0

        X = np.array([[1, same_element, same_side, 1, size_ratio]], dtype=np.float32)
        prob = model.predict_proba(X)[0][1]

        st.divider()
        if prob > 0.5:
            st.success(f"✅ **SAME INDIVIDUAL** — {prob:.1%}")
            st.balloons()
        else:
            st.error(f"❌ **DIFFERENT INDIVIDUALS** — {prob:.1%}")

        with st.expander("Model inputs"):
            st.write(f"same_element = {same_element} ({elem1} vs {elem2})")
            st.write(f"same_side   = {same_side} ({side1} vs {side2})")
            st.write(f"size_ratio   = {size_ratio:.4f}")
            st.write(f"Raw probability: {prob:.4f}")

st.caption("v1 • Upload .txt/.dta landmark files or paste coordinates above • Buffalo Human Evolutionary Morphology Lab")
