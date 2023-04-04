import streamlit as st
import Backend as b
import Db as db

st.set_page_config(layout="wide", page_title="BizCardX")
st.sidebar.success("Select a option from below.")
# st.title(':violet[BIZCARDX]')
st.markdown("<h1 style='text-align: center; color: violet;'>BIZCARDX</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 30px;'>Extracting Business Card Data with OCR</h1>", unsafe_allow_html=True)
# st.subheader('_Extracting Business Card Data with OCR_')
def handleClick(file):
    b.fetch_all(file)

def handleDelete(id):
    db.delete_record(id)



def show_table():
    df = db.getData()
    colms = st.columns((1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2))
    fields = ["id", "name", "mobile", "email", "url", "area",
              "city", "state", "pin", "company", "designation", "action"]
    for col, field_name in zip(colms, fields):
        col.write(field_name)
    for data in df:
        # print(data)
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(
            (1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2))
        col1.write(data[0])  # index
        col2.write(data[1])  # email
        col3.write(data[2])  # unique ID
        col4.write(data[3])
        col5.write(data[4])
        col6.write(data[5])
        col7.write(data[6])
        col8.write(data[7])
        col9.write(data[8])
        col10.write(data[9])
        col11.write(data[10])
        button_phold = col12.empty()  # create a placeholder
        button_phold.button("Edit", key=data[0], on_click=show_form, args=[data])


def show_uploader():
    file = st.file_uploader("Upload visiting card", accept_multiple_files=True)
    st.button("Upload", key=None, help="Click to upload and extract information",
              on_click=handleClick, args=file, type="primary")


def check_value():
    id = st.session_state.id
    name = st.session_state.name
    mobno = st.session_state.mobno
    email = st.session_state.email
    url = st.session_state.url
    address = st.session_state.address 
    city = st.session_state.city
    state = st.session_state.state
    pincode = st.session_state.pincode
    company = st.session_state.company
    desig = st.session_state.desig
    db.update_data(id, name, mobno, email, url, address, city, state, pincode, company, desig)

def check_id():
    id = st.session_state.id
    handleDelete(id)

def show_form(data):
    details = {}
    with st.form("my_form"):
        details['id'] = st.text_input("id", data[0], disabled=True, key="id")
        details["name"] = st.text_input('Movie title', value=f"{data[1]}", key="name")
        details["mobno"] = st.text_input(label="mobile", value = data[2], key="mobno")
        details["email"] = st.text_input(label="email", value = data[3], key="email")
        details["url"] = st.text_input(label="url", value = data[4], key="url")
        details['address'] = st.text_input(label="area", value = data[5], key="address")
        details['city'] = st.text_input(label="city", value = data[6], key="city")
        details['state'] = st.text_input(label="state", value = data[7], key="state")
        details['pincode'] = st.text_input(label="pincode", value = data[8], key="pincode")
        details['company'] = st.text_input(label="company name", value = data[9], key="company")
        details['desig'] = st.text_input(label="designation", value = data[10], key="desig")
        st.form_submit_button("Submit", on_click=check_value)
        st.form_submit_button("Delete", on_click=check_id)


page_names_to_funcs = {
    "Upload Card": show_uploader,
    "Display Data": show_table,
}

st.sidebar.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 20% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 20% !important;
      }
    </style>""", unsafe_allow_html=True)
demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

