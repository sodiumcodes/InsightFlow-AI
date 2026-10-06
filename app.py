import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔬",
    layout="wide",
)

# ---------- Styling ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background: radial-gradient(circle at 15% 10%, #1b1f3b 0%, #0b0d1a 55%, #07080f 100%);
        color: #e8eaf6;
    }

    header[data-testid="stHeader"] { background: transparent; }

    .hero {
        text-align: center;
        padding: 2.2rem 1rem 1rem 1rem;
    }
    .hero h1 {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #7c4dff, #00e5ff, #69f0ae);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .hero p { color: #9fa8da; font-size: 1.1rem; }

    .steps {
        display: flex; flex-wrap: wrap; justify-content: center;
        gap: 0.7rem; margin: 1.2rem 0 2rem 0;
    }
    .step-chip {
        padding: 0.5rem 1.1rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(124,77,255,0.45);
        color: #c5cae9;
        font-size: 0.9rem;
        font-weight: 500;
        backdrop-filter: blur(6px);
        transition: all .25s ease;
    }
    .step-chip:hover {
        transform: translateY(-3px);
        border-color: #00e5ff;
        box-shadow: 0 6px 20px rgba(0,229,255,0.25);
    }

    .card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.09);
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        box-shadow: 0 10px 35px rgba(0,0,0,0.35);
        backdrop-filter: blur(10px);
        line-height: 1.7;
    }
    .card.report  { border-left: 5px solid #7c4dff; }
    .card.critic  { border-left: 5px solid #69f0ae; }
    .card.search  { border-left: 5px solid #00e5ff; }
    .card.scrape  { border-left: 5px solid #ffab40; }

    .topic-badge {
        display: inline-block;
        padding: 0.35rem 0.9rem;
        border-radius: 10px;
        background: linear-gradient(90deg, #7c4dff33, #00e5ff33);
        border: 1px solid #7c4dff88;
        color: #e8eaf6;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    div[data-testid="stTextInput"] input {
        background: rgba(255,255,255,0.06);
        color: #fff;
        border: 1px solid rgba(124,77,255,0.5);
        border-radius: 14px;
        padding: 0.9rem 1rem;
        font-size: 1.05rem;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #00e5ff;
        box-shadow: 0 0 0 2px rgba(0,229,255,0.25);
    }

    div.stButton > button {
        width: 100%;
        border: none;
        border-radius: 14px;
        padding: 0.85rem 1rem;
        font-size: 1.05rem;
        font-weight: 600;
        color: white;
        background: linear-gradient(90deg, #7c4dff, #00b0ff);
        transition: all .25s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 28px rgba(124,77,255,0.45);
        color: white;
    }

    button[data-baseweb="tab"] { font-weight: 600; color: #9fa8da; }
    button[aria-selected="true"] { color: #00e5ff !important; }

    section[data-testid="stSidebar"] {
        background: rgba(10,12,28,0.9);
        border-right: 1px solid rgba(255,255,255,0.07);
    }
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## 🔬 Research Agent")
    st.markdown("A multi-agent pipeline that researches any topic for you.")
    st.markdown("---")
    st.markdown(
        """
        **Pipeline**
        1. 🔎 Search Agent
        2. 📄 Reader Agent
        3. ✍️ Writer
        4. 🧐 Critic
        """
    )

# ---------- Hero ----------
st.markdown(
    """
    <div class="hero">
        <h1>AI Research Agent</h1>
        <p>Search · Scrape · Write · Review — all in one place</p>
    </div>
    <div class="steps">
        <div class="step-chip">🔎 Step 1 · Search</div>
        <div class="step-chip">📄 Step 2 · Read</div>
        <div class="step-chip">✍️ Step 3 · Write</div>
        <div class="step-chip">🧐 Step 4 · Critique</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Input ----------
_, mid, _ = st.columns([1, 3, 1])
with mid:
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Latest advances in quantum computing",
        label_visibility="collapsed",
    )
    run = st.button("🚀 Start Research")

# ---------- Run pipeline ----------
if run:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        with st.status("Agents are working on your topic...", expanded=True) as status:
            st.write("🔎 Search agent, reader agent, writer and critic are running...")
            try:
                state = run_research_pipeline(topic)
                status.update(label="Research complete ✅", state="complete", expanded=False)
                st.session_state["state"] = state
                st.session_state["topic"] = topic
            except Exception as e:
                status.update(label="Something went wrong", state="error")
                st.error(f"Error: {e}")

# ---------- Results ----------
if "state" in st.session_state:
    state = st.session_state["state"]

    st.markdown(
        f"<div style='text-align:center'><span class='topic-badge'>📌 {st.session_state['topic']}</span></div>",
        unsafe_allow_html=True,
    )

    tab_report, tab_feedback, tab_search, tab_scrape = st.tabs(
        ["📝 Final Report", "🧐 Critic Feedback", "🔎 Search Results"]
    )

    with tab_report:
        st.markdown('<div class="card report">', unsafe_allow_html=True)
        st.markdown(state["report"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_feedback:
        st.markdown('<div class="card critic">', unsafe_allow_html=True)
        st.markdown(state["feedback"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_search:
        st.markdown('<div class="card search">', unsafe_allow_html=True)
        st.markdown(state["search_results"])
        st.markdown("</div>", unsafe_allow_html=True)