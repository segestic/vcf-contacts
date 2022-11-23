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


def csvtovcf(input, filename):
    #csv_file.name
    #output=open('vcf_file.vcf','w')
    output=open(f'{filename}.vcf','w') #f'{fn}.jpg'
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
    return output



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
            CSV to VCF is an automated way to convert a csv file to a vcf file. Customized to meet NECF(https://necf.church) needs. The generated contact (vcf file) is then uploaded on contact. 
            """)
        '''
        ## How does it work ❓ 
        Upload csv file and click convert. File will be converted to vcf.
        '''


    with col2:
        st.subheader("Automate the Generation of VCf contacts from CSV file👨‍🌾")


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
            process = csvtovcf(df, csv_file.name)
            #process = csvtovcf(f'{df}.vcf')
            col1.write('''
		    ## Results 🔍 
		    ''')
            col1.success("sussucefully converted, You can click on download button to download ")
            
            if process:
                #data_path = os.path.join(parent_path, "vcf_file.vcf'")
                #with open('vcf_file.vcf', 'rb') as f:
                    #st.download_button('Download VCF', f, file_name='vcf_file.vcf')
                with open(f'{csv_file.name}.vcf', 'rb') as f:
                    st.download_button('Download VCF', f, file_name=f'{csv_file.name}.vcf') 

                    if st.download_button(...):
                        st.write('Thanks for downloading!')                             
 
                print ('Finished processng....')


      #code for html ☘️ 🌾 🌳 👨‍🌾  🍃

    st.warning("Note: This application is customized for NECF (https://necf.church) use for bulk conversion of members csv contacts file. ")
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