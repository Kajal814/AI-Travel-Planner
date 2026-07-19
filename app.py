import streamlit as st

from chains import (
    generate_itinerary,
    recommend_hotels,
    estimate_budget
)

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ----------------------------------------------------------------------------
# STYLING — dark design system with motion
# ----------------------------------------------------------------------------
def inject_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');


header[data-testid="stHeader"]{
    display:none;
}

div[data-testid="stToolbar"]{
    display:none;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

.block-container{
    padding-top:0.5rem;
    padding-bottom:2rem;
    max-width:1200px;
}


    :root{
        --primary:#4F8CFF;
        --primary-deep:#2F63D9;
        --secondary:#8B5CF6;
        --accent:#22D3EE;
        --success:#34D399;
        --warning:#FBBF24;
        --bg:#0A0E17;
        --bg-alt:#0F1524;
        --card:rgba(30,41,59,0.55);
        --card-solid:#111827;
        --border:rgba(148,163,184,0.16);
        --text-primary:#F1F5F9;
        --text-secondary:#94A3B8;
        --radius:16px;
        --shadow-sm:0 2px 12px rgba(0,0,0,0.35);
        --shadow-md:0 10px 30px rgba(0,0,0,0.45);
        --shadow-lg:0 18px 44px rgba(0,0,0,0.55);
        --glow-primary:0 0 0 rgba(79,140,255,0);
    }

    html, body, [class*="css"]{
        font-family:'Inter', sans-serif;
        color:var(--text-primary);
    }

    .stApp{
        background:
            radial-gradient(circle at 15% 0%, rgba(79,140,255,0.10) 0%, rgba(10,14,23,0) 45%),
            radial-gradient(circle at 85% 20%, rgba(139,92,246,0.10) 0%, rgba(10,14,23,0) 45%),
            var(--bg);
    }

    section[data-testid="stSidebar"]{ display:none; }
    div[data-testid="collapsedControl"]{ display:none; }

    .block-container{
        padding-top:2rem;
        padding-bottom:3rem;
        max-width:980px;
        margin:0 auto;
    }

    .section-block{ margin-top:32px; }

    /* Scrollbar */
    ::-webkit-scrollbar{ width:8px; height:8px; }
    ::-webkit-scrollbar-track{ background:transparent; }
    ::-webkit-scrollbar-thumb{ background:#334155; border-radius:8px; }
    ::-webkit-scrollbar-thumb:hover{ background:#475569; }

    /* -------- KEYFRAMES -------- */
    @keyframes fadeInUp{
        from{ opacity:0; transform:translateY(14px); }
        to{ opacity:1; transform:translateY(0); }
    }
    @keyframes gradientShift{
        0%{ background-position:0% 50%; }
        50%{ background-position:100% 50%; }
        100%{ background-position:0% 50%; }
    }
    @keyframes floatOrb{
        0%, 100%{ transform:translate(0,0); }
        50%{ transform:translate(14px,-14px); }
    }
    @keyframes pulseDot{
        0%{ box-shadow:0 0 0 0 rgba(79,140,255,0.55); }
        70%{ box-shadow:0 0 0 9px rgba(79,140,255,0); }
        100%{ box-shadow:0 0 0 0 rgba(79,140,255,0); }
    }
    @keyframes shimmer{
        0%{ background-position:-200% 0; }
        100%{ background-position:200% 0; }
    }

    /* -------- HERO -------- */
    .hero{
        background:linear-gradient(120deg, #0F1E4D 0%, #1D3E9E 35%, #4C1D95 70%, #0F1E4D 100%);
        background-size:220% 220%;
        animation:gradientShift 12s ease infinite;
        border-radius:var(--radius);
        padding:52px 48px;
        box-shadow:var(--shadow-lg), 0 0 60px rgba(79,140,255,0.15);
        position:relative;
        overflow:hidden;
        border:1px solid rgba(148,163,184,0.12);
        animation:fadeInUp 0.6s ease both, gradientShift 12s ease infinite;
    }
    .hero::before{
        content:"";
        position:absolute;
        top:-70px; right:-40px;
        width:260px; height:260px;
        border-radius:50%;
        background:radial-gradient(circle, rgba(34,211,238,0.22) 0%, rgba(34,211,238,0) 70%);
        animation:floatOrb 7s ease-in-out infinite;
    }
    .hero::after{
        content:"";
        position:absolute;
        bottom:-90px; left:-30px;
        width:220px; height:220px;
        border-radius:50%;
        background:radial-gradient(circle, rgba(139,92,246,0.20) 0%, rgba(139,92,246,0) 70%);
        animation:floatOrb 9s ease-in-out infinite reverse;
    }
    .hero-title{
        color:#F8FAFC;
        font-size:2.4rem;
        font-weight:800;
        letter-spacing:-0.8px;
        line-height:1.2;
        margin:0 0 10px 0;
        position:relative;
    }
    .hero-subtitle{
        color:#CBD5E1;
        font-size:1rem;
        max-width:560px;
        line-height:1.6;
        margin:0;
        position:relative;
    }
    .hero-divider{
        height:1px;
        background:linear-gradient(90deg, var(--border), transparent);
        margin:28px 0 0 0;
    }

    /* -------- SECTION LABELS -------- */
    .section-eyebrow{
        color:var(--accent);
        font-size:0.74rem;
        font-weight:700;
        letter-spacing:1.6px;
        text-transform:uppercase;
        margin-bottom:4px;
    }
    .section-title{
        color:var(--text-primary);
        font-size:1.3rem;
        font-weight:800;
        letter-spacing:-0.3px;
        margin:0 0 18px 0;
    }

    /* -------- CARDS -------- */
    div[data-testid="stVerticalBlockBorderWrapper"]{
        border-radius:var(--radius) !important;
        border:1px solid var(--border) !important;
        background:var(--card) !important;
        backdrop-filter:blur(16px);
        -webkit-backdrop-filter:blur(16px);
        box-shadow:var(--shadow-sm);
        transition:box-shadow 0.3s ease, transform 0.3s ease, border-color 0.3s ease;
        animation:fadeInUp 0.5s ease both;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover{
        box-shadow:var(--shadow-md), 0 0 0 1px rgba(79,140,255,0.25);
        border-color:rgba(79,140,255,0.35) !important;
        transform:translateY(-2px);
    }

    /* -------- INPUTS -------- */
    .stTextInput input,
    .stNumberInput input{
        border-radius:12px !important;
        border:1px solid var(--border) !important;
        height:2.9rem !important;
        background:linear-gradient(180deg, rgba(15,20,32,0.85), rgba(10,14,23,0.85)) !important;
        color:var(--text-primary) !important;
        box-shadow:inset 0 1px 3px rgba(0,0,0,0.4) !important;
        transition:border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
    }
    .stTextInput input:hover,
    .stNumberInput input:hover{
        border-color:rgba(148,163,184,0.32) !important;
    }
    .stTextInput input:focus,
    .stNumberInput input:focus{
        border-color:var(--primary) !important;
        background:rgba(15,20,32,0.95) !important;
        box-shadow:inset 0 1px 3px rgba(0,0,0,0.4), 0 0 0 3px rgba(79,140,255,0.28), 0 0 16px rgba(79,140,255,0.18) !important;
    }
    .stSelectbox > div{
        border-radius:12px !important;
        background:linear-gradient(180deg, rgba(15,20,32,0.85), rgba(10,14,23,0.85)) !important;
        box-shadow:inset 0 1px 3px rgba(0,0,0,0.4) !important;
        transition:box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .stSelectbox > div:hover{
        border-color:rgba(148,163,184,0.32) !important;
    }
    .stSelectbox > div:focus-within{
        border-color:var(--primary) !important;
        box-shadow:inset 0 1px 3px rgba(0,0,0,0.4), 0 0 0 3px rgba(79,140,255,0.28), 0 0 16px rgba(79,140,255,0.18) !important;
    }
    label{
        font-weight:600 !important;
        color:var(--text-primary) !important;
        font-size:0.85rem !important;
        margin-bottom:4px !important;
    }
    ::placeholder{ color:#64748B !important; }

    /* -------- BUTTONS -------- */
    .stButton > button{
        width:100%;
        height:3.1rem;
        border-radius:var(--radius);
        font-weight:700;
        font-size:0.98rem;
        letter-spacing:0.2px;
        border:1px solid var(--border);
        transition:all 0.25s cubic-bezier(0.4,0,0.2,1);
        color:var(--text-primary);
        background:linear-gradient(180deg, rgba(51,65,85,0.55), rgba(30,41,59,0.55));
    }
    .stButton > button:hover{
        border-color:rgba(148,163,184,0.35);
    }
    .stButton > button[kind="primary"]{
        background:
            linear-gradient(180deg, rgba(255,255,255,0.16) 0%, rgba(255,255,255,0) 45%),
            linear-gradient(135deg, var(--primary) 0%, var(--primary-deep) 55%, var(--secondary) 100%);
        background-size:100% 100%, 200% 200%;
        border:1px solid rgba(148,197,255,0.4);
        color:#FFFFFF;
        box-shadow:var(--shadow-md), 0 0 24px rgba(79,140,255,0.30);
    }
    .stButton > button[kind="primary"]:hover{
        transform:translateY(-2px) scale(1.005);
        box-shadow:var(--shadow-lg), 0 0 38px rgba(79,140,255,0.48);
        background-position:0% 0%, 100% 0%;
        border-color:rgba(148,197,255,0.65);
    }
    .stButton > button[kind="primary"]:active{
        transform:translateY(0) scale(0.995);
    }
    .stDownloadButton > button{
        border-radius:var(--radius);
        font-weight:700;
        border:1.5px solid var(--primary);
        color:var(--primary);
        background:rgba(79,140,255,0.06);
        box-shadow:var(--shadow-sm);
        transition:all 0.25s ease;
    }
    .stDownloadButton > button:hover{
        background:rgba(79,140,255,0.14);
        border-color:var(--accent);
        color:var(--accent);
        transform:translateY(-2px);
        box-shadow:var(--shadow-md), 0 0 20px rgba(34,211,238,0.25);
    }

    /* -------- METRIC CARDS -------- */
    .metric-card{
        border:1px solid var(--border);
        border-radius:var(--radius);
        background:var(--card);
        backdrop-filter:blur(16px);
        padding:22px;
        box-shadow:var(--shadow-sm);
        height:100%;
        transition:transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        position:relative;
        overflow:hidden;
        animation:fadeInUp 0.5s ease both;
    }
    .metric-card:hover{
        transform:translateY(-4px);
        box-shadow:var(--shadow-md), 0 0 22px rgba(79,140,255,0.20);
        border-color:rgba(79,140,255,0.35);
    }
    .metric-card::before{
        content:"";
        position:absolute;
        top:0; left:0; right:0;
        height:4px;
        background:linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
        background-size:200% 100%;
        animation:shimmer 5s linear infinite;
    }
    .metric-label{
        color:var(--text-secondary);
        font-size:0.75rem;
        font-weight:700;
        letter-spacing:1px;
        text-transform:uppercase;
        margin-bottom:8px;
    }
    .metric-value{
        color:var(--text-primary);
        font-size:1.6rem;
        font-weight:800;
        letter-spacing:-0.4px;
    }

    /* -------- TABS -------- */
    div[data-baseweb="tab-list"]{
        gap:8px;
        border-bottom:1px solid var(--border);
    }
    button[data-baseweb="tab"]{
        font-size:15px;
        font-weight:700;
        color:var(--text-secondary);
        padding:12px 20px;
        transition:color 0.25s ease;
    }
    button[data-baseweb="tab"]:hover{
        color:var(--accent);
    }
    button[data-baseweb="tab"][aria-selected="true"]{
        color:#FFFFFF;
        border-bottom:3px solid var(--primary);
    }

    /* -------- OUTPUT CARDS -------- */
    .output-card-header{
        color:var(--text-primary);
        font-size:1.05rem;
        font-weight:800;
        letter-spacing:-0.2px;
        margin-bottom:0;
    }
    .output-divider{
        height:1px;
        background:var(--border);
        margin:12px 0 16px 0;
    }
    .output-scroll{
        max-height:460px;
        overflow-y:auto;
        padding-right:8px;
        line-height:1.7;
        font-size:0.96rem;
        color:#E2E8F0;
    }

    /* -------- STATUS / ALERTS -------- */
    div[data-testid="stStatusWidget"]{
        border-radius:var(--radius) !important;
        border:1px solid var(--border) !important;
        background:var(--card) !important;
        backdrop-filter:blur(16px);
        box-shadow:var(--shadow-sm);
    }
    div[data-testid="stStatusWidget"] svg{
        filter:drop-shadow(0 0 6px rgba(79,140,255,0.6));
    }
    div[data-testid="stAlert"]{
        border-radius:var(--radius) !important;
        box-shadow:var(--shadow-sm);
        animation:fadeInUp 0.4s ease both;
    }

    /* Live pulse dot next to status text, purely decorative motion cue */
    .live-dot{
        display:inline-block;
        width:8px; height:8px;
        border-radius:50%;
        background:var(--primary);
        margin-right:8px;
        animation:pulseDot 1.8s infinite;
        vertical-align:middle;
    }

    /* -------- FOOTER -------- */
    .app-footer{
        text-align:center;
        color:var(--text-secondary);
        font-size:0.84rem;
        padding-top:22px;
        border-top:1px solid var(--border);
        margin-top:8px;
    }

    /* -------- GENERIC TEXT -------- */
    p, span, div, li{
        color:var(--text-primary);
    }
    .stCaption, .stMarkdown p{
        color:var(--text-secondary);
    }

    /* -------- RESPONSIVE -------- */
    @media (max-width: 992px){
        .hero{ padding:40px 32px; }
        .hero-title{ font-size:2rem; }
    }
    @media (max-width: 768px){
        .hero{ padding:30px 22px; }
        .hero-title{ font-size:1.65rem; }
        .hero-subtitle{ font-size:0.9rem; }
        .metric-value{ font-size:1.3rem; }
    }

    </style>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# REUSABLE RENDER HELPERS
# ----------------------------------------------------------------------------
def render_hero(title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-title">{title}</div>
            <p class="hero-subtitle">{subtitle}</p>
        </div>
        <div class="hero-divider"></div>
        """,
        unsafe_allow_html=True
    )


def render_section_header(eyebrow, title):
    st.markdown(f'<div class="section-eyebrow">{eyebrow}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def render_metric_card(column, label, value):
    with column:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


def render_output_card(header, content):
    with st.container(border=True):
        st.markdown(f'<div class="output-card-header">{header}</div>', unsafe_allow_html=True)
        st.markdown('<div class="output-divider"></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="output-scroll">{content}</div>', unsafe_allow_html=True)


def build_downloadable_plan(destination, days, budget, travel_style, itinerary, hotels, budget_plan):
    return (
        f"AI TRAVEL PLANNER\n"
        f"Destination: {destination}\n"
        f"Duration: {days} Days\n"
        f"Budget: Rs. {budget:,}\n"
        f"Travel Style: {travel_style}\n"
        f"{'-'*60}\n\n"
        f"ITINERARY\n{'-'*60}\n{itinerary}\n\n"
        f"HOTELS\n{'-'*60}\n{hotels}\n\n"
        f"BUDGET ESTIMATE\n{'-'*60}\n{budget_plan}\n"
    )


# ----------------------------------------------------------------------------
# APP
# ----------------------------------------------------------------------------
inject_css()

render_hero(
    "Plan your next trip in seconds",
    "Generate a complete, personalized travel plan — itinerary, hotel recommendations, "
    "and a full budget breakdown — tailored to your destination, duration, and style."
)

# -------------------- INPUT CARD --------------------
st.markdown('<div class="section-block"></div>', unsafe_allow_html=True)
with st.container(border=True):
    render_section_header("Step 1", "Trip Details")

    col1, col2 = st.columns(2)
    with col1:
        source = st.text_input("Source", placeholder="Enter your starting location")
    with col2:
        destination = st.text_input("Destination", placeholder="Enter your destination")

    col3, col4, col5 = st.columns(3)
    with col3:
        days = st.number_input("Duration (Days)", min_value=1, max_value=30, value=3)
    with col4:
        budget = st.number_input("Budget", min_value=1000, value=20000, step=1000)
    with col5:
        travel_style = st.selectbox("Travel Style", ["Budget", "Standard", "Luxury"])

    st.write("")
    generate = st.button("Generate Travel Plan", use_container_width=True, type="primary")

# -------------------- RESULTS --------------------
if generate:

    if destination == "":
        st.warning("Please enter a destination.")
    else:
        with st.status("Initializing planner...", expanded=True) as status:

            st.write("Generating itinerary...")
            itinerary = generate_itinerary(
                source,
                destination,
                str(days)
            )

            st.write("Searching hotels...")
            hotels = recommend_hotels(
                destination,
                str(budget),
                itinerary
            )

            st.write("Estimating budget...")
            budget_plan = estimate_budget(
                source,
                destination,
                str(days),
                str(budget),
                hotels
            )

            st.write("Preparing results...")

            status.update(label="Completed", state="complete", expanded=False)

        st.success("Travel plan generated successfully.")

        st.markdown('<div class="section-block"></div>', unsafe_allow_html=True)
        render_section_header("Overview", "Trip Summary")

        col1, col2, col3 = st.columns(3)
        render_metric_card(col1, "Destination", destination)
        render_metric_card(col2, "Duration", f"{days} Days")
        render_metric_card(col3, "Budget", f"₹{budget:,}")

        st.markdown('<div class="section-block"></div>', unsafe_allow_html=True)
        render_section_header("Step 2", "Your Travel Plan")

        tab1, tab2, tab3 = st.tabs(["Itinerary", "Hotels", "Budget Analysis"])

        with tab1:
            render_output_card("Travel Itinerary", itinerary)
        with tab2:
            render_output_card("Recommended Hotels", hotels)
        with tab3:
            render_output_card("Budget Estimation", budget_plan)

        st.markdown('<div class="section-block"></div>', unsafe_allow_html=True)
        full_plan_text = build_downloadable_plan(
            destination, days, budget, travel_style, itinerary, hotels, budget_plan
        )
        st.download_button(
            label="Download Travel Plan",
            data=full_plan_text,
            file_name=f"travel_plan_{destination.strip().replace(' ', '_') or 'trip'}.txt",
            mime="text/plain",
            use_container_width=True
        )

# -------------------- FOOTER --------------------
st.markdown('<div class="section-block"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-footer">AI Travel Planner &middot; Built with Streamlit</div>',
    unsafe_allow_html=True
)