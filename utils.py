import streamlit as st 
import streamlit.components as stc

# Utils
import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")


class FileDownloader(object):
	
	def __init__(self, data,filename='myfile',file_ext='txt'):
		super(FileDownloader, self).__init__()
		self.data = data
		self.filename = filename
		self.file_ext = file_ext

	def download(self):
		b64 = base64.b64encode(self.data.encode()).decode()
		new_filename = "{}_{}_.{}".format(self.filename,timestr,self.file_ext)
		st.markdown("#### Download File ###")
		href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'
		st.markdown(href,unsafe_allow_html=True)








import streamlit as st
import pickle
import pandas as pd
import json
import base64
import uuid
import re

import importlib.util


def import_from_file(module_name: str, filepath: str):
    """
    Imports a module from file.
    Args:
        module_name (str): Assigned to the module's __name__ parameter (does not
            influence how the module is named outside of this function)
        filepath (str): Path to the .py file
    Returns:
        The module
    """
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def notebook_header(text):
    """
    Insert section header into a jinja file, formatted as notebook cell.
    Leave 2 blank lines before the header.
    """
    return f"""# # {text}
"""


def code_header(text):
    """
    Insert section header into a jinja file, formatted as Python comment.
    Leave 2 blank lines before the header.
    """
    seperator_len = (75 - len(text)) / 2
    seperator_len_left = math.floor(seperator_len)
    seperator_len_right = math.ceil(seperator_len)
    return f"# {'-' * seperator_len_left} {text} {'-' * seperator_len_right}"


def to_notebook(code):
    """Converts Python code to Jupyter notebook format."""
    notebook = jupytext.reads(code, fmt="py")
    return jupytext.writes(notebook, fmt="ipynb")


def open_link(url, new_tab=True):
    """Dirty hack to open a new web page with a streamlit button."""
    # From: https://discuss.streamlit.io/t/how-to-link-a-button-to-a-webpage/1661/3
    if new_tab:
        js = f"window.open('{url}')"  # New tab or window
    else:
        js = f"window.location.href = '{url}'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)


def download_button(object_to_download, download_filename, button_text):
    """
    Generates a link to download the given object_to_download.
    From: https://discuss.streamlit.io/t/a-download-button-with-custom-css/4220
    Params:
    ------
    object_to_download:  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv,
    some_txt_output.txt download_link_text (str): Text to display for download
    link.
    button_text (str): Text to display on download button (e.g. 'click here to download file')
    pickle_it (bool): If True, pickle file.
    Returns:
    -------
    (str): the anchor tag to download object_to_download
    Examples:
    --------
    download_link(your_df, 'YOUR_DF.csv', 'Click to download data!')
    download_link(your_str, 'YOUR_STRING.txt', 'Click to download text!')
    """
    # if pickle_it:
    #    try:
    #        object_to_download = pickle.dumps(object_to_download)
    #    except pickle.PicklingError as e:
    #        st.write(e)
    #        return None

    # if:
    if isinstance(object_to_download, bytes):
        pass

    elif isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)
    # Try JSON encode for everything else
    else:
        object_to_download = json.dumps(object_to_download)

    try:
        # some strings <-> bytes conversions necessary here
        b64 = base64.b64encode(object_to_download.encode()).decode()
    except AttributeError as e:
        b64 = base64.b64encode(object_to_download).decode()

    button_uuid = str(uuid.uuid4()).replace("-", "")
    button_id = re.sub("\d+", "", button_uuid)

    custom_css = f""" 
        <style>
            #{button_id} {{
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background-color: rgb(255, 255, 255);
                color: rgb(38, 39, 48);
                padding: .25rem .75rem;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;
            }} 
            #{button_id}:hover {{
                border-color: rgb(246, 51, 102);
                color: rgb(246, 51, 102);
            }}
            #{button_id}:active {{
                box-shadow: none;
                background-color: rgb(246, 51, 102);
                color: white;
                }}
        </style> """

    dl_link = (
        custom_css
        + f'<a download="{download_filename}" id="{button_id}" href="data:file/txt;base64,{b64}">{button_text}</a><br><br>'
    )
    # dl_link = f'<a download="{download_filename}" id="{button_id}" href="data:file/txt;base64,{b64}"><input type="button" kind="primary" value="{button_text}"></a><br></br>'

    st.markdown(dl_link, unsafe_allow_html=True)





def csvtovcf(input):
    #input=list(csv.reader(open(input,'r'))) 
	input = pd.read_csv("input") 
	#input = pd.read_csv("csv_practice.csv") 

    output = open('con_13.11.22.vcf','w') 

for row in input: 
    output.write("BEGIN:VCARD\n") 
    output.write("VERSION:3.0\n")
    output.write("FN:"+row[0]+'.'+row[1]+'.NECF '+ row[2]+"\n") 
    output.write("N:"+"NECF "+row[2]+";"+row[0]+'.'+row[1]+";;;\n") 
    output.write("TEL;TYPE=CELL:"+row[3]+"\n")
    output.write("CATEGORIES:"+'Imported on 30/10,myContacts'+"\n") 
    output.write("END:VCARD\n") 
    #output.close()
    return 'xyz'	


    generate_download_button(csv_data=data_path, filename="abc", file_label="mag")
    down = st.button("Download")
    #Saving upload

def download2(fn):
    print("Download request recieved")
    data_path = os.path.join(parent_path, "vcf_file.vcf")
    #st.download_button('Download CSV', text_contents, 'text/csv')
    #return (data_path, as_attachment=True, mimetype="csv")
    with open('vcf_file.vcf', 'rb') as f:
        st.download_button('Download vcc', f, file_name='vcf_file.vcf')


def generate_download_button(csv_data, filename, file_label):
    st.download_button(label=f"Download {file_label} as CSV",
                           data=csv_data,
                           file_name=f"{filename}.vcf")