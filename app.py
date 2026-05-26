import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Zebricorn // Financial IT & Data",
    page_icon="zebricorn_logo.png",
    layout="wide"
)

# --- 2. ZEBRICORN RED GITHUB CSS ---
st.markdown("""
    <style>
    /* Sidebar setup */
    [data-testid="stSidebar"] {
        min-width: 260px !important;
        max-width: 260px !important;
        width: 240px !important;
        border-right: 1px solid rgba(208, 215, 222, 0.5) !important;
    }
    [data-testid="stSidebar"] [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        padding-top: 20px;
        padding-bottom: 10px;
    }
    
    /* Headers */
    h1, h2 {
        border-bottom: 1px solid rgba(208, 215, 222, 0.3);
        padding-bottom: 0.3em;
        font-weight: 600;
        margin-top: 24px;
    }

    /* Den Röda "Git-boxen" */
    .zeb-box {
        padding: 16px;
        background-color: rgba(128, 128, 128, 0.07);
        border: 1px solid rgba(208, 215, 222, 0.5);
        border-radius: 6px;
        border-left: 4px solid #E30613; 
        margin-bottom: 20px;
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
    }
    
    .zeb-box a {
        color: #E30613 !important;
        text-decoration: none;
        font-weight: 600;
    }
    .zeb-box a:hover {
        text-decoration: underline;
    }

    /* Folder structure styling */
    .file-tree {
        font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
        font-size: 14px;
        background-color: #0d1117;
        color: #c9d1d9;
        padding: 15px;
        border-radius: 6px;
        margin-top: 10px;
    }

    code {
        background-color: rgba(175,184,193,0.2) !important;
        padding: 0.2em 0.4em !important;
        border-radius: 6px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TRANSLATIONS ---
t = {
    "English": {
        "nav_header": "Navigation",
        "nav_core": "consulting-core",
        "nav_github": "github-repository",
        "nav_slides": "architecture-decks",
        "nav_contact": "contact-info",
        "status_label": "Status",
        "status_text": "Available for Projects",
        "hero_h": "Financial IT & Data Architecture",
        "gh_note": "Zebricorn Consulting AB is available for assignments, bridging the gap between <strong>Financial Logic</strong> and <strong>Technical Implementation</strong>.",
        "services_h": "Expertise & Services",
        "serv_reg_h": "Regulatory Reporting",
        "serv_reg_d": "Specialist in implementation of **Basel II/III** and **AnaCredit**. Experience in mapping complex credit risk data to regulatory directives.",
        "serv_sql_h": "SQL & ETL Architecture",
        "serv_sql_d": "Expert in large-scale data migrations and optimization of T-SQL flows in strictly regulated environments (Banking/Finance).",
        "serv_sol_h": "Solution Architecture",
        "serv_sol_d": "The link between business and IT. Experience in modernizing legacy landscapes and establishing stable data flows in Azure DevOps.",
        "serv_ai_h": "AI-Integrated Dev",
        "serv_ai_d": "Utilizes GitHub Copilot and advanced prompting to accelerate documentation, code quality, and traceability.",
        "gh_h": "Open Source & Repository",
        "gh_d": "The Zebricorn repository is designed for cloud-native deployment and containerized development. Here is the current architecture of the main project:",
        "repo_h": "Repository Structure (zebricorn / main)",
        "gh_btn": "View on GitHub",
        "slides_h": "Interactive Architecture Specifications",
        "slides_d": "Select an architectural deck below to explore enterprise system maps and evolution metrics generated via tokenized prompt flows.",
        "slides_select": "Choose Presentation Deck",
        "deck_evolution": "🔄 Coach Engine: Project Deep Dive & Evolution",
        "deck_v47": "🧠 Coach Engine: v4.7 Technical Architecture Specification",
        "contact_info_h": "Contact Info",
        "contact_intro": "Zebricorn Consulting AB is available for specialist assignments in Financial IT and Data Architecture.",
        "contact_det": "Contact Details",
        "biz_info": "Business Information",
        "loc": "Rönninge, Sweden",
        "bv_label": "Brainville Profile"
    },
    "Svenska": {
        "nav_header": "Navigation",
        "nav_core": "konsult-profil",
        "nav_github": "github-repository",
        "nav_slides": "arkitektur-decks",
        "nav_contact": "kontakt-info",
        "status_label": "Status",
        "status_text": "Tillgänglig för uppdrag",
        "hero_h": "Finansiell IT & Dataarkitektur",
        "gh_note": "Zebricorn Consulting AB är tillgänglig för specialistuppdrag, bryggar gapet mellan <strong>Finansiell Logik</strong> och <strong>Teknisk Implementation</strong>.",
        "services_h": "Expertis & Tjänster",
        "serv_reg_h": "Regulatory Reporting",
        "serv_reg_d": "Specialist på implementation av **Basel II/III** och **AnaCredit**. Erfarenhet av att mappa komplexa kreditriskdata mot myndighetsdirektiv.",
        "serv_sql_h": "SQL & ETL Arkitektur",
        "serv_sql_d": "Expert på storskaliga datamigreringar och optimering av T-SQL-flöden i strikt reglerade miljöer (Banking/Finance).",
        "serv_sol_h": "Lösningsarkitektur",
        "serv_sol_d": "Länken mellan verksamhet och IT. Erfarenhet av att modernisera legacy-landskap och etablera stabila dataflöden i Azure DevOps.",
        "serv_ai_h": "AI-Integrerad Utveckling",
        "serv_ai_d": "Använder GitHub Copilot och avancerad prompting för att accelerera dokumentation, kodkvalitet och spårbarhet.",
        "gh_h": "Open Source & Repository",
        "gh_d": "Zebricorn-repositoryt är byggt för cloud-native driftsättning och containeriserad utveckling. Här är den nuvarande arkitekturen för huvudprojektet:",
        "repo_h": "Repository-struktur (zebricorn / main)",
        "gh_btn": "Se på GitHub",
        "slides_h": "Interaktiva Arkitekturspecifikationer",
        "slides_d": "Välj en presentation nedan för att utforska systemkartor och tekniska evolutionära milstolpar genererade via AI-arkitekturflöden.",
        "slides_select": "Välj presentationsmaterial",
        "deck_evolution": "🔄 Coach Engine: Projekt-evolution & Tidslinje",
        "deck_v47": "🧠 Coach Engine: v4.7 Teknisk Arkitekturspecifikation",
        "contact_info_h": "Kontaktinformation",
        "contact_intro": "Zebricorn Consulting AB är tillgänglig för specialistuppdrag inom Finansiell IT och Dataarkitektur.",
        "contact_det": "Kontaktuppgifter",
        "biz_info": "Företagsinformation",
        "loc": "Rönninge, Sverige",
        "bv_label": "Brainville-profil"
    }
}

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("zebricorn_logo.png", width=140)
    lang = st.selectbox("Select Language", ["English", "Svenska"], label_visibility="collapsed")
    st.divider()
    
    st.markdown(f"### {t[lang]['nav_header']}")
    menu = st.radio(
        "Navigation Menu",
        [t[lang]["nav_core"], t[lang]["nav_github"], t[lang]["nav_slides"], t[lang]["nav_contact"]],
        label_visibility="collapsed"
    )
    
    st.divider()
    st.markdown(f"**{t[lang]['status_label']}:** <span style='color: #1a7f37;'>● {t[lang]['status_text']}</span>", unsafe_allow_html=True)
    st.caption("v2.6.0 // Specification Architecture")

# --- 5. MAIN CONTENT ---

# SECTION 1: CORE
if menu == t[lang]["nav_core"]:
    st.markdown(f"<h1>{t[lang]['hero_h']}</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="zeb-box">
        📫 zebricornconsulting@gmail.com &nbsp; | &nbsp; 
        🔗 <a href="https://linkedin.com/in/robertsandstrom18439731/" target="_blank">LinkedIn</a> &nbsp; | &nbsp; 
        ⚡ <a href="https://www.brainville.com/p/robertsandstrom" target="_blank">Brainville</a> &nbsp; | &nbsp; 
        📍 {t[lang]['loc']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="zeb-box">
        {t[lang]['gh_note']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"## {t[lang]['services_h']}")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader(f"📊 {t[lang]['serv_reg_h']}")
        st.markdown(t[lang]['serv_reg_d'])
        st.subheader(f"💾 {t[lang]['serv_sql_h']}")
        st.markdown(t[lang]['serv_sql_d'])
    with c2:
        st.subheader(f"🏗️ {t[lang]['serv_sol_h']}")
        st.markdown(t[lang]['serv_sol_d'])
        st.subheader(f"🤖 {t[lang]['serv_ai_h']}")
        st.markdown(t[lang]['serv_ai_d'])

# SECTION 2: GITHUB
elif menu == t[lang]["nav_github"]:
    st.markdown(f"<h1>{t[lang]['gh_h']}</h1>", unsafe_allow_html=True)
    st.write(t[lang]['gh_d'])
    
    st.markdown(f"### {t[lang]['repo_h']}")
    st.markdown("""
    <div class="file-tree">
        📁 .devcontainer/<br>
        &nbsp;&nbsp;&nbsp;&nbsp;📄 devcontainer.json<br>
        📁 slides/<br>
        &nbsp;&nbsp;&nbsp;&nbsp;📄 coach_engine_deep_dive.html<br>
        &nbsp;&nbsp;&nbsp;&nbsp;📄 coach_engine_v4_7_architecture.html<br>
        📄 app.py<br>
        📄 requirements.txt<br>
        📄 zebricorn_logo.png<br>
        📄 README.md
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.link_button(t[lang]['gh_btn'], "https://github.com/Besserschmitt/zebricorn", type="primary")

# SECTION 3: INTERACTIVE SLIDES DECKS (FUTURE-PROOFED VIA ST.IFRAME)
elif menu == t[lang]["nav_slides"]:
    st.markdown(f"<h1>{t[lang]['slides_h']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p>{t[lang]['slides_d']}</p>", unsafe_allow_html=True)
    
    # Valbox för att byta mellan dina två olika HTML-decks
    selected_deck = st.selectbox(
        t[lang]["slides_select"],
        [t[lang]["deck_evolution"], t[lang]["deck_v47"]]
    )
    
    # Mappa valet till rätt lokal HTML-fil
    if selected_deck == t[lang]["deck_evolution"]:
        target_file = "slides/coach_engine_deep_dive.html"
    else:
        target_file = "slides/coach_engine_v4_7_architecture.html"
        
    # Säkerhetskontroll: Kolla att filen existerar innan vi renderar
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # KORREKT SYNTAX: Helt ren import av base64-biblioteket
        import base64
        b64_html = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")
        data_url = f"data:text/html;base64,{b64_html}"
        
        # MIGRATION: Ersatt st.components.v1.html med st.iframe för framtidssäkring efter 1 juni
        st.iframe(src=data_url, height=740, scrolling=True)
    else:
        st.error(f"Could not locate the architectural source file at `{target_file}`. Please check directory path alignment.")
        
# SECTION 4: CONTACT
elif menu == t[lang]["nav_contact"]:
    st.markdown(f"<h1>{t[lang]['contact_info_h']}</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="zeb-box">
        {t[lang]['contact_intro']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### {t[lang]['contact_det']}")
    st.markdown(f"""
- **Email:** zebricornconsulting@gmail.com
- **LinkedIn:** [linkedin.com/in/robertsandstrom18439731/](https://linkedin.com/in/robertsandstrom18439731/)
- **{t[lang]['bv_label']}:** [brainville.com/p/robertsandstrom](https://www.brainville.com/p/robertsandstrom)
- **Location:** {t[lang]['loc']}""")
    
    st.markdown(f"### {t[lang]['biz_info']}")
    st.markdown(f"""
- **Company:** Zebricorn Consulting AB
- **Org.nr:** 559553-6060""")

# --- 6. FOOTER ---
st.divider()
st.markdown(f"""
<div style='display: flex; justify-content: space-between; align-items: center; opacity: 0.6; font-size: 12px;'>
    <div>© 2026 Zebricorn Consulting AB | Org.nr: 559553-6060</div>
    <div>Built with Python & Streamlit // Cloud-Native Architecture</div>
</div>
""", unsafe_allow_html=True)
