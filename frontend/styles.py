import streamlit as st

# ================== 🎨 Finalized Theme ==================
theme = {
    "primary_bg": "#121212",
    "text_color": "#F5F5F5",
    "input_bg": "#1E1E1E",
    "accent_color": "#E91E63",
    "accent_soft": "#9C27B0",
    "shadow": "rgba(0,0,0,0.6)",
    "sidebar_bg": "#1A1A1A",
    "header_gradient": "#ff69b4, #9b59b6"
}

# ================== 💅 Theme Styler ==================
def apply_theme_styles():
    st.markdown(f"""
        <style>
        html, body, .stApp {{
            background-color: {theme['primary_bg']};
            color: {theme['text_color']};
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        }}

        .block-container {{
            padding-top: 1rem !important;
        }}

        h1, h2, h3, h4, h5 {{
            margin-top: 0.2rem !important;
            margin-bottom: 0.2rem !important;
            color: {theme['accent_color']} !important;
        }}

        section[data-testid="stSidebar"] {{
            background-color: {theme['sidebar_bg']};
            color: {theme['text_color']};
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }}

        input, textarea, select, .stTextInput>div>div>input {{
            background-color: {theme['input_bg']} !important;
            color: {theme['text_color']} !important;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}

        .stButton>button {{
            background-color: {theme['accent_color']} !important;
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-weight: 500;
            box-shadow: 0 4px 16px {theme['shadow']};
            transition: 0.3s ease;
        }}

        .stButton>button:hover {{
            background-color: {theme['accent_soft']} !important;
            transform: translateY(-1px);
        }}

        .stFileUploader>div>div {{
            background-color: {theme['input_bg']} !important;
            color: {theme['text_color']} !important;
            border-radius: 10px;
            border: 1px dashed {theme['accent_color']};
            padding: 1rem;
        }}

        .streamlit-expanderHeader {{
            color: {theme['text_color']} !important;
            font-weight: 600;
        }}

        .stMarkdown, .stText, .stCodeBlock, code {{
            color: {theme['text_color']} !important;
        }}

        .mermaid {{
            color: {theme['text_color']} !important;
        }}

        .main-header {{
            font-size: 40px;
            font-weight: 800;
            text-align: center;
            letter-spacing: 1px;
            font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
            background: linear-gradient(to right, {theme['header_gradient']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
            
        }}

        .pipeline-img {{
            width: 100px;
            height: 100px;
            object-fit: cover;
            border-radius: 16px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: block;
            margin: 1.5rem auto;
        }}

        .pipeline-img:hover {{
            transform: scale(1.05);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
        }}

        @media (max-width: 768px) {{
            .pipeline-img {{
                width: 220px;
                height: 220px;
            }}
        }}

        .stImage + div {{
            text-align: center;
            font-size: 0.9rem;
            color: {theme['text_color']};
            margin-top: -0.5rem;
        }}

        a {{
            color: {theme['accent_color']} !important;
            text-decoration: none;
        }}
        a:hover {{
            color: {theme['accent_soft']} !important;
        }}

        .stRadio > div {{
            background-color: {theme['input_bg']} !important;
            border-radius: 10px;
            padding: 0.5rem;
        }}

        .stRadio label, .stRadio div[data-testid="stMarkdownContainer"] p {{
            color: {theme['text_color']} !important;
            font-weight: 500;
        }}

        label[data-testid="stFileUploaderLabel"],
        label, .stTextInput label {{
            color: {theme['text_color']} !important;
            font-weight: 500;
        }}
        </style>
    """, unsafe_allow_html=True)

    return theme  # No dark_mode toggle anymore
