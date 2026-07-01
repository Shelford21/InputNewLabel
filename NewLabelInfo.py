import streamlit as st
import pandas as pd
import os
import json
from streamlit_local_storage import LocalStorage
localS = LocalStorage()
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    prefix="labelapp_",
    password="fauzann"
)

if not cookies.ready():
    st.stop()

if "admin_unlocked" not in st.session_state:
    st.session_state.admin_unlocked = False
    
department_factory_options = [
        "Finishing - Quty 2",
        "Finishing - Quty 1",
        "Sewing - Quty 2",
        "Sewing - Quty 1",
        "Adm",
        "Lean Staff"
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
    "Fanny",
    "Anggih",
    "Indah",
    "fauzan"
]
    
if "user_registered" not in st.session_state:
    st.session_state.user_registered = False

if "user_department_factory" not in st.session_state:
    st.session_state.user_department_factory = department_factory_options[0]

if "user_line" not in st.session_state:
    st.session_state.user_line = line_options[0]
    
from streamlit_autorefresh import st_autorefresh
# AUTO REFRESH EVERY 30 SECOND

saved_department = localS.getItem("department_factory")
saved_line = localS.getItem("user_line")

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

# CREATE CHAT FILE
if not os.path.exists(CHAT_FILE):
    with open(CHAT_FILE, "w") as f:
        json.dump([], f)


def load_data():
    return pd.read_csv(CSV_FILE)


def save_data(df):
    df.to_csv(CSV_FILE, index=False)

#load chat
def load_chat():
    with open(CHAT_FILE, "r") as f:
        return json.load(f)

# =========================
# SAVE CHAT
# =========================
def save_chat(chat_data):
    with open(CHAT_FILE, "w") as f:
        json.dump(chat_data, f)
        
        
saved_department = cookies.get("department_factory")
saved_line = cookies.get("user_line")
if (
    saved_department in department_factory_options
    and
    saved_line in line_options
):

    st.session_state.user_department_factory = saved_department
    st.session_state.user_line = saved_line
    st.session_state.user_registered = True

if not st.session_state.user_registered:

    st.title("Identifikasi Pengguna")

    default_department_index = 0
        
    if saved_department in department_factory_options:
            default_department_index = department_factory_options.index(
                saved_department
            )

    department_factory = st.selectbox(
        "Pilih Departemen & Gedung",
        department_factory_options,
         index=default_department_index,
        filter_mode=None 
    )

    default_line_index = 0

    if saved_line in line_options:
        default_line_index = line_options.index(
            saved_line
    )

    line_selected = st.selectbox(
        "Pilih LINE",
        line_options,
         index=default_line_index,
        filter_mode=None 
    )

    if st.button("Masuk"):
        cookies["department_factory"] = department_factory
        cookies["user_line"] = line_selected
        cookies.save()
        st.session_state.user_department_factory = department_factory
        st.session_state.user_line = line_selected
        st.session_state.user_registered = True

        st.rerun()

    st.stop()
    
# =========================
# SIDEBAR TOGGLE
# =========================
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False

if st.button("Group Chat"):
    st.session_state.show_chat = not st.session_state.show_chat

if st.button("Ganti Identitas"):
            cookies["department_factory"] = ""
            cookies["user_line"] = ""
        
            cookies.save()
        
            st.session_state.user_registered = False
            st.session_state.user_department_factory = ""
            st.session_state.user_line = ""
        
            st.rerun()
        
st.title("📋 Input New Label")
st.success(
    f"Login sebagai: {st.session_state.user_department_factory} | {st.session_state.user_line}"
)
# =========================
# SIDEBAR CHAT
# =========================
if st.session_state.show_chat:
    department_factory_options = [
        "Finishing - Quty 2",
        "Finishing - Quty 1",
        "Sewing - Quty 2",
        "Sewing - Quty 1",
        "Lean Staff"
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
    "fauzan"
]
    
    
    st.sidebar.title("💬 Group Chat")
    # =========================
    # CHAT IDENTIFIER
    # =========================
    chat_department_factory = st.session_state.user_department_factory
    
    chat_line = st.session_state.user_line
    chat_messages = load_chat()

    # CHAT DISPLAY
    for msg in chat_messages:

        if isinstance(msg, str):
    
            sender = "Unknown"
            message = msg
    
        else:
    
            sender = f"{msg['department_factory']} | {msg['line']}"
            message = msg['message']
    
        st.sidebar.markdown(
            f"""
            <div style="
                background-color:#f1f1f1;
                padding:10px;
                border-radius:10px;
                margin-bottom:8px;
                color:black;
            ">
                <b>{sender}</b><br>
                {message}
            </div>
            """,
            unsafe_allow_html=True
        )
   
    
    # =========================
    # CHAT FORM
    # =========================
    with st.sidebar.form("chat_form", clear_on_submit=True):
    
        chat_input = st.text_input(
            "Chat khusus QC + Adm + Fauzan"
        )
    
        send_button = st.form_submit_button("Kirim Pesan")
    
        if send_button:
    
            if chat_input.strip() != "":
    
                chat_messages.append({
                "department_factory": chat_department_factory,
                "line": st.session_state.user_line,
                "message": chat_input
            })
    
                save_chat(chat_messages)
    
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
"ACORN SHPD/BROWN",
"ASKEPASK YELLOW",
"ASKEPASK GREEN",
"BARTHOLOMEW BEAR MEDIUM",
"BENGAL TIGER/STRIPED LORANGE",
"BLACK BEAR CUB",
"BLAHAJ N SOFT TOY 55 BABY SHARK",
"BLAHAJ NNN SOFT TOY 100 SHARK",
"BLAVINGAD TURTLE",
"BLUE WHALE",
"DJUNGELSKOG SOFT TOY 28 BROWN BEAR",
"DJUNGELSKOG SOFT TOY BROWN BEAR",
"FAMNIG HJARTA CUSHION 40X101 RED",
"FLOWER-SHAPED/WHITE",
"GOSIG GOLDEN SOFT TOY 40 DOG/GOLDEN RETRIEVER",
"GOSIG GOLDEN SOFT TOY 70 DOG/GOLDEN RETRIEVER",
"GOSIG RATTA SOFT TOY 23 GREY/BEIGE",
"GREJSIMOJS SOFT TOY 100 BEAR/BEIGE",
"GREJSIMOJS SOFT TOY 38 BEAR/OFF-WHITE",
"JATTESTOR NNN SOFT TOY ELEPHANT/GREY",
"JERBOA/BEIGE",
"KRAMIG PANDA",
"LEOPARD/PATTERNED WHITE",
"LIVLIG HUSKY",
"LYNX/ORANGE BROWN",
"MINI/ORANGUTAN",
"MINI/PANDA",
"ORANGUTAN",
"PENGUIN-SHAPED BLACK/WHITE",
"PINK/FLOWER-SHAPED",
"RED PANDA",
"RED PANDA/MINI",
"SANDLOPARE SOFT TOY 20 MEERKAT/BEIGE",
"SANDLOPARE SOFT TOY 45 GIRAFFE CALF/BROWN",
"SANDLOPARE SOFT TOY 70 GIRAFFE/BROWN",
"SANDLOPARE SOFT TOY 8 MEERKAT/MINI BEIGE",
"SMASLUG SOFT TOY DOG/BROWN",
"SNAKE/BURMESE PYTHON",
"SNUTTIG SOFT TOY 29 WHITE POLAR BEAR",
"SNUTTIG SOFT TOY POLAR BEAR/WHITE",
"TITTA DJUR FINGER PUPPET MIXED COLOURS 10-P",
"TITTADJUR DEER",
"TITTADJUR LION",
"TITTADJUR PANDA",
"TITTADJUR TURTLE",
"TOADSTOOL SHAPED/RED WHITE",
"TURTLE/GREEN",
"VINTERFINT 2025 DECO 74 SANTA CLAUS RED",
"VINTERFINT 2026 DECO 30 SANTA CLAUS RED",
"VINTERFINT 2026 DECO 30 SANTA CLAUS SITTING/RED",
"VINTERFINT 2026 DECO 65 SANTA CLAUS BROWN",
"WHITE/CLOUD-SHAPED",
"YELLOW/TAXI-SHAPED",
    "test"
]

destinations = ["EU", "AP", "NA-", "ME", "GB", "CA", "US"]

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
    
    col1, col2,col3 = st.columns(3)

    # with col1:

    #     department_factory = st.session_state.user_department_factory
    #     line_combined = st.session_state.user_line
    

    with col2:
        department_factory = st.session_state.user_department_factory
        line_combined = st.session_state.user_line
        
        article_name = st.selectbox(
            "Pilih Nama Artikel",
            article_names,
                filter_mode=None
        )

        destination = st.selectbox(
            "Pilih Destinasi",
            destinations,
                filter_mode=None
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
                disabled=not st.session_state.status_unlocked,
                    filter_mode=None
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
st.divider()

if "show_admin_login" not in st.session_state:
    st.session_state.show_admin_login = False

if st.button("🔧 Fitur Admin"):

    st.session_state.show_admin_login = (
        not st.session_state.show_admin_login
    )
    
ADMIN_PASSWORD = "1945"

if st.session_state.show_admin_login:

    admin_password = st.text_input(
        "Password Admin",
        type="password"
    )

    if st.button("Login Admin"):

        if admin_password == ADMIN_PASSWORD:

            st.session_state.admin_unlocked = True

            st.success("Admin mode unlocked!")

        else:

            st.error("Wrong password!")
            
if st.session_state.admin_unlocked:

    st.divider()

    st.subheader("🔒 Status Editing")

    if st.button("Unlock Status Editing"):

        st.session_state.status_unlocked = True

        st.success("Status editing unlocked!")

    st.divider()

    st.subheader("⚠️ Clear Messages")

    # clear_password_input = st.text_input(
    #     "Enter Clear Cache Password",
    #     type="password",
    #     key="clear_cache_password"
    # )

    if st.button("Clear Messages"):

        # if clear_password_input == ADMIN_PASSWORD:

            st.session_state.clear()

            if os.path.exists(CHAT_FILE):
                with open(CHAT_FILE, "w") as f:
                    json.dump([], f)

            st.success("Cache cleared!")

            st.rerun()

        # else:

            st.error("Wrong password!")
