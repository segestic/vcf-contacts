import streamlit as st 
import os
import warnings
import csv
import pandas as pd
import pathlib
import io
parent_path = pathlib.Path(__file__).parent.parent.resolve()

st.set_page_config(page_title="CSV to VCF", page_icon="🌿", layout='centered', initial_sidebar_state="collapsed")



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


def csvtovcf(input):
    #input=list(input) 
    #input=list(csv.reader(open(input,'r'))) 
    #input = csv.reader(input)
    
    #input1 = io.BytesIO(input.content)
    #zz = pd.read_csv(input)
    #for index, row in df.iterrows():

    output=open('vcf_file.vcf','w')
    #my_text = st.text_area("Your Message") 
    #with io.BytesIO() as output:
    for index, row in input.iterrows():
        #print (row)
        output.write("BEGIN:VCARD\n") 
        output.write("VERSION:3.0\n")
        output.write("FN:"+str(row[0])+'.'+str(row[1])+'.NECF '+ str(row[2])+"\n") 
        output.write("N:"+"NECF "+str(row[2])+";"+str(row[0])+'.'+str(row[1])+";;;\n") 
        output.write("TEL;TYPE=CELL:"+str(row[3])+"\n")
        output.write("CATEGORIES:"+'Imported on 30/10,myContacts'+"\n") 
        output.write("END:VCARD\n")
    output.close() 
    #print (output)
    return output


def generate_download_button(csv_data, filename, file_label):
    st.download_button(label=f"Download {file_label} as CSV",
                           data=csv_data,
                           file_name=f"{filename}.vcf")

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> CSV to VCF  🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1,col2  = st.columns([2,2])
    
    with col1: 
        with st.expander(" ℹ️ Information", expanded=True):
            st.write("""
            CSV to VCF is one of the most important aspects of precision agriculture. Crop recommendations are based on a number of factors. Precision agriculture seeks to define these criteria on a site-by-site basis in order to address crop selection issues. While the "site-specific" methodology has improved performance, there is still a need to monitor the systems' outcomes.Precision agriculture systems aren't all created equal. 
            However, in agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.

            """)
        '''
        ## How does it work ❓ 
        Complete all the parameters and the machine learning model will predict the most suitable crops to grow in a particular farm based on various parameters
        '''


    with col2:
        st.subheader(" Find out the most suitable crop to grow in your farm 👨‍🌾")


        csv_file = st.file_uploader("Upload CSV", type=["csv"])

    if csv_file is not None:
		# To See details
        file_details = {"filename":csv_file.name, "filetype":csv_file.type,
                              "filesize":csv_file.size}
        st.write(file_details)
        file_container = st.expander("Check your uploaded .csv")
        df = pd.read_csv(csv_file)
        csv_file.seek(0)
        file_container.write(df)

        #Read CSV FIle...
        if st.button('Convert'):
            process = False
            process = csvtovcf(df)
            col1.write('''
		    ## Results 🔍 
		    ''')
            col1.success("sussucefully converted, You can click on download button to download ")
            
            if process:
                data_path = os.path.join(parent_path, "vcf_file.vcf'")
                #with open('vcf_file.vcf', 'w') as f:
                generate_download_button(csv_data=data_path, filename="abc", file_label="mag")
                down = st.button("Download")
                			  #Saving upload
                with open('vcf_file.vcf') as f:
                    #f.write((image_file)
                    f.download()
                    #st.write(process)
                #st.download_button('Download 4vcf', process) 
                print ('Finished processng....')
                # if down:
                #     download = FileDownloader(process).download()
                #     #st.download_button('Download vcf', download) 
                # #df = pd.read_csv("iris.csv")
                #st.dataframe(df)
                    #download = FileDownloader(process.to_csv(),file_ext='vcf').download()
                    #st.write(process)

                    #download = FileDownloader(process).download()

      #code for html ☘️ 🌾 🌳 👨‍🌾  🍃

    st.warning("Note: This A.I application is for educational/demo purposes only and cannot be relied upon. Check the source code [here](https://github.com/gabbygab1233/Crop-Recommendation)")
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()