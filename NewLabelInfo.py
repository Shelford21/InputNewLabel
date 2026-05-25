import streamlit as st
import pandas as pd
import os
import json
from streamlit_autorefresh import st_autorefresh
# AUTO REFRESH EVERY 30 SECOND
st_autorefresh(
    interval=5 * 1000,
    key="datarefresh"
)

st.set_page_config(
    page_title="Input New Label",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# =========================
# SIDEBAR TOGGLE
# =========================
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False

if st.button("Group Chat"):
    st.session_state.show_chat = not st.session_state.show_chat
    
CSV_FILE = "production_data.csv"
CHAT_FILE = "chat.json"

if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=[
        "Department & Factory",
        "LINE",
        "Article Name",
        "Destination",
        "Week",
        "Status",
        "Highlight"
    ])
    df_init.to_csv(CSV_FILE, index=False)

# =========================
# CREATE CHAT FILE
# =========================
if not os.path.exists(CHAT_FILE):
    with open(CHAT_FILE, "w") as f:
        json.dump([], f)


def load_data():
    return pd.read_csv(CSV_FILE)


def save_data(df):
    df.to_csv(CSV_FILE, index=False)
# =========================
# LOAD CHAT
# =========================
def load_chat():
    with open(CHAT_FILE, "r") as f:
        return json.load(f)

# =========================
# SAVE CHAT
# =========================
def save_chat(chat_data):
    with open(CHAT_FILE, "w") as f:
        json.dump(chat_data, f)
        
st.title("📋 Input New Label")

# =========================
# SIDEBAR CHAT
# =========================
if st.session_state.show_chat:

    st.sidebar.title("💬 Group Chat")

    chat_messages = load_chat()

    # CHAT DISPLAY
    for msg in chat_messages:

        st.sidebar.markdown(
            f"""
            <div style="
                background-color:#f1f1f1;
                padding:10px;
                border-radius:10px;
                margin-bottom:8px;
                color:black;
            ">
                <b>anonymous:</b><br>
                {msg}
            </div>
            """,
            unsafe_allow_html=True
        )

    # CHAT INPUT
    chat_input = st.sidebar.text_input(
        "Chat khusus QC + fauzan",
        key="chat_input"
    )

    # SEND BUTTON
    if st.sidebar.button("Kirim Pesan"):

        if chat_input.strip() != "":
    
            chat_messages.append(chat_input)
    
            save_chat(chat_messages)
    
            # RESET INPUT
            st.session_state.chat_input = ""
    
            st.rerun()
        
department_factory_options = [
    "Finishing - Quty 2",
    "Finishing - Quty 1",
    "Sewing - Quty 2",
    "Sewing - Quty 1"
    
    
    
]
line_options = [
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "A9",
    "A10",

    "B1",
    "B2",
    "B3",
    "B4",
    "B5",
    "B6",
    "B7",
    "B8",
    "B9",
    "B10",

    "C1",
    "C2",
    "C3",
    "C4",
    "C5",
    "C6",
    "C7",
    "C8",
    "C9",
    "C10",
]

article_names = [
"AFTONSPARV SOFT TOY W ASTRONAUT SUIT 28 CAT",
"ALPTALL CSH 47 PINK/FLOWER-SHAPED",
"ALPTALL SOFT TOY 27 ASIATIC BLACK BEAR CUB",
"ALPTALL SOFT TOY 36 RED PANDA",
"ALPTALL SOFT TOY 52 SNOW LEOPARD/PATTERNED WHITE",
"ALPTALL SOFT TOY 60 BENGAL TIGER/STRIPED LORANGE",
"ALPTALL SOFT TOY 9 LONG-EARED JERBOA/BEIGE",
"ALPTALL SOFT TOY 9 RED PANDA/MINI",
"BARNDROM CSH 36X45 WHITE/CLOUD-SHAPED",
"BARNDROM CSH 51X30 YELLOW/TAXI-SHAPED",
"BARTHOLOMEW BEAR MEDIUM",
"BLAHAJ N SOFT TOY 55 BABY SHARK",
"BLAHAJ NNN SOFT TOY 100 SHARK",
"BLAVINGAD CSH 40X32 PENGUIN-SHAPED BLACK/WHITE",
"BLAVINGAD SOFT TOY 100 BLUE WHALE",
"BLAVINGAD SOFT TOY 44 TURTLE/GREEN",
"CHEESE - LATSAS BASKET",
"CHILI - ACC DUKTIG PIZZA",
"DJUNGELSKOG GLOVE PUPPET SNAKE/BURMESE PYTHON",
"DJUNGELSKOG N SOFT TOY 11 MINI/PANDA",
"DJUNGELSKOG N SOFT TOY 20 MINI/ORANGUTAN",
"DJUNGELSKOG SOFT TOY 28 BROWN BEAR",
"DJUNGELSKOG SOFT TOY BROWN BEAR",
"DJUNGELSKOG SOFT TOY ORANGUTAN",
"DJUNGLESKOG SOFT TOY BEAR",
"DUKTIG ACC CHILI",
"DUKTIG PIZZA S24 PIZZA/MULTICOLOUR",
"FAMNIG HJARTA CUSHION 40X101 RED",
"FISH - ACC DUKTIG PIZZA",
"GOSIG GOLDEN SOFT TOY 40 DOG/GOLDEN RETRIEVER",
"GOSIG GOLDEN SOFT TOY 70 DOG/GOLDEN RETRIEVER",
"GOSIG RATTA SOFT TOY 23 GREY/BEIGE",
"GREENPAPER - LATSAS BASKET",
"GREJSIMOJS SOFT TOY 100 BEAR/BEIGE",
"GREJSIMOJS SOFT TOY 38 BEAR/OFF-WHITE",
"INNER N CUSH PAD 40X58 WHITE/FIRM ID",
"INNER N CUSH PAD 50X50 WHITE/FIRM ID",
"JATTESTOR NNN SOFT TOY ELEPHANT/GREY",
"KRAMIG SOFT TOY WHITE/BLACK",
"LATSAS SHOPPING BSKT S12",
"LIVLIG SOFT TOY 57 DOG/SIBERIAN HUSKY",
"LIVLIG SOFT TOY HUSKY",
"MUSHROOM - ACC DUKTIG PIZZA",
"ONION - ACC DUKTIG PIZZA",
"PASTA - LATSAS BASKET",
"PINNEAPLE - ACC DUKTIG PIZZA",
"PIZZA BREAD - ACC DUKTIG PIZZA",
"RUCOLLA - ACC DUKTIG PIZZA",
"SANDL?PARE 45 GIRAFFE CALF/BROWN",
"SANDL?PARE SOFT TOY 8 MEERKAT/MINI BEIGE",
"SANDLOPARE 45 GIRAFFE CALF/BROWN",
"SANDLOPARE SOFT TOY 45 GIRAFFE CALF/BROWN",
"SANDLOPARE SOFT TOY 8 MEERKAT/MINI BEIGE",
"SANDLOPARE SOFT TOY 20 MEERKAT/BEIGE",
"SANDLOPARE SOFT TOY 45 GIRAFFE CALF/BROWN",
"SANDLOPARE SOFT TOY 70 GIRAFFE/BROWN",
"SANDLOPARE SOFT TOY 8 MEERKAT/MINI BEIGE",
"SAUSAGE/SALAMI - ACC DUKTIG PIZZA",
"SKOGSDUVA CSH 47 FLOWER-SHAPED/WHITE",
"SKOGSDUVA CSH 47X8 FLOWER-SHAPED/WHITE",
"SKOGSDUVA CUSHION W POCKET 32X37 ACORN SHPD/BROWN",
"SKOGSDUVA SOFT TOY 63 LYNX/ORANGE BROWN",
"SKOGSDUVA STOOL CVR TOADSTOOL SHAPED/RED WHITE",
"SMASLUG SOFT TOY DOG/BROWN",
"SNUTTIG SFT TOY 29 POLAR BEAR/WHITE CUB",
"SNUTTIG SOFT TOY 29 WHITE POLAR BEAR",
"SNUTTIG SOFT TOY POLAR BEAR/WHITE",
"TITTA DJUR FINGER PUPPET MIXED COLOURS 10-P",
"TITTADJUR DEER",
"TITTADJUR LION",
"TITTADJUR PANDA",
"TITTADJUR TURTLE",
"TOMATO - ACC DUKTIG PIZZA",
"TREVNAD CSH 50X50 BLUE ID",
"TREVNAD CSH 50X50 GREEN ID",
"TREVNAD CSH 50X50 LIGHT BLUE ID",
"TREVNAD CSH 50X50 YELLOW ID",
"VINTERFINT 2025 DECO 74 SANTA CLAUS RED",
"VINTERFINT 2026 DECO 30 SANTA CLAUS RED",
"VINTERFINT 2026 DECO 30 SANTA CLAUS SITTING/RED",
"VINTERFINT 2026 DECO 65 SANTA CLAUS BROWN",
"VINTERFINT 2026 DECO 74 SANTA CLAUS RED",
    "test"
]

destinations = ["EU", "AP", "NA", "ME", "GB", "CA", "US"]

status_options = ["wait", "done"]

# =========================
# SPECIAL BUTTON
# =========================
if "show_fauzan_input" not in st.session_state:
    st.session_state.show_fauzan_input = False

if "fauzan_mode" not in st.session_state:
    st.session_state.fauzan_mode = False

top_left_col, _ = st.columns([1, 5])

# with top_left_col:

#     if st.button("Panggil FAUZAN"):

#         st.session_state.show_fauzan_input = True

# # =========================
# # FAUZAN INPUT
# # =========================
# if st.session_state.show_fauzan_input:

#     with st.form("fauzan_form"):

#         fauzan_text = st.text_input(
#             "Ketik pesan"
#         )

#         fauzan_submit = st.form_submit_button("Submit")

#         if fauzan_submit:

#             df = load_data()

            

#             new_row = {
#                 "Department": "-",
#                 "Factory": "-",
#                 "LINE": "-",
#                 "Line Number": "-",
#                 "Article Name": fauzan_text,
#                 "Destination": "-",
#                 "Week": "-",
#                 "Status": "wait",
#                 "Highlight": "YES"
#             }

#             df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

#             save_data(df)

#             st.success("FAUZAN has been called!")

#             st.session_state.show_fauzan_input = False

#             st.rerun()


with st.form("production_form"):

    col1, col2 = st.columns(2)

    with col1:

        department_factory = st.selectbox(
            "Pilih Departemen & Gedung",
            department_factory_options
        )
    
        line_combined = st.selectbox(
            "Pilih LINE",
            line_options
        )

    with col2:
        article_name = st.selectbox(
            "Pilih Nama Artikel",
            article_names
        )

        destination = st.selectbox(
            "Pilih Destinasi",
            destinations
        )

        week = st.text_input(
        "Ketik Week",
        placeholder="Contoh : 2552"
)

    submit_button = st.form_submit_button("Minta Label")


if submit_button:

    df = load_data()

  

    new_row = {
        "Department & Factory": department_factory,
        "LINE": line_combined,
        "Article Name": article_name,
        "Destination": destination,
        "Week": week,
        "Status": "wait",
        "Highlight": "NO"
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    save_data(df)

    st.success("Data added successfully!")


df = load_data()

STATUS_PASSWORD = "fauzann"


if "status_unlocked" not in st.session_state:
    st.session_state.status_unlocked = False

st.subheader("📄 List Minta Label ")

if df.empty:
    st.info("No data submitted yet.")

else:

    for index, row in df.iterrows():

        highlighted = str(row.get("Highlight", "NO")) == "YES"

        container_style = """
        <style>
        .red-glow {
            border: 2px solid red;
            padding: 15px;
            border-radius: 12px;
            background-color: rgba(255,0,0,0.08);
            box-shadow: 0 0 20px red;
            margin-bottom: 10px;
        }
        </style>
        """
        
        if highlighted:
            st.markdown(container_style, unsafe_allow_html=True)
            st.markdown('<div class="red-glow">', unsafe_allow_html=True)
        
        with st.container(border=False):

            cols = st.columns([2,1,2,1,1,1,1])

            cols[0].write(row["Department & Factory"])
            cols[1].write(row["LINE"])
            cols[2].write(row["Article Name"])
            cols[3].write(row["Destination"])
            cols[4].write(row["Week"])
            

            current_status = row["Status"]

            # =========================
            # STATUS DROPDOWN
            # =========================
            selected_status = cols[5].selectbox(
                "Status",
                status_options,
                index=status_options.index(current_status),
                key=f"status_{index}",
                label_visibility="collapsed",
                disabled=not st.session_state.status_unlocked
            )

            # UPDATE STATUS
            if (
                st.session_state.status_unlocked
                and selected_status != current_status
            ):
                df.at[index, "Status"] = selected_status
                save_data(df)
                st.rerun()

            # =========================
# DELETE BUTTON
# =========================
if f"confirm_delete_{index}" not in st.session_state:
    st.session_state[f"confirm_delete_{index}"] = False

delete_button = cols[6].button(
    "Delete",
    key=f"delete_{index}"
)

# Show confirmation
if delete_button:
    st.session_state[f"confirm_delete_{index}"] = True

# Confirmation UI
if st.session_state[f"confirm_delete_{index}"]:

    st.warning("Are you sure you want to delete this row?")

    confirm_col1, confirm_col2 = st.columns(2)

    with confirm_col1:
        yes_button = st.button(
            "Yes",
            key=f"yes_delete_{index}"
        )

    with confirm_col2:
        no_button = st.button(
            "No",
            key=f"no_delete_{index}"
        )

    # YES DELETE
    if yes_button:
        df = df.drop(index=index).reset_index(drop=True)
        save_data(df)

        st.session_state[f"confirm_delete_{index}"] = False

        st.rerun()

    # CANCEL DELETE
    if no_button:
        st.session_state[f"confirm_delete_{index}"] = False
        st.rerun()

# st.divider()

# st.subheader("📊 CSV Data Preview")

# csv_df = pd.read_csv(CSV_FILE)

# st.dataframe(
#     csv_df,
#     use_container_width=True
# )


# st.divider()
st.subheader("🔒 Unlock Status Editing")

password_input = st.text_input(
    "Enter Password",
    type="password"
)

if st.button("Unlock"):

    if password_input == STATUS_PASSWORD:
        st.session_state.status_unlocked = True
        st.success("Status editing unlocked!")

    else:
        st.error("Wrong password!")

# =========================
# CLEAR CACHE WITH PASSWORD
# =========================
CLEAR_PASSWORD = "fauzann"

st.divider()

st.subheader("⚠️ Clear Cache")

clear_password_input = st.text_input(
    "Enter Clear Cache Password",
    type="password",
    key="clear_cache_password"
)

if st.button("Clear Cache"):

    if clear_password_input == CLEAR_PASSWORD:

        # CLEAR SESSION
        st.session_state.clear()

        # CLEAR CHAT
        if os.path.exists(CHAT_FILE):
            with open(CHAT_FILE, "w") as f:
                json.dump([], f)

        st.success("Cache cleared!")

        st.rerun()

    else:
        st.error("Wrong password!")
