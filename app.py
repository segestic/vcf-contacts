import streamlit as st 
import os
import warnings
import csv


st.set_page_config(page_title="CSV to VCF", page_icon="🌿", layout='centered', initial_sidebar_state="collapsed")

def csvtovcf(input):
    input=list(csv.reader(open(input,'r'))) 
    output=open('vcf/con_13.11.22.vcf','w') 
    for row in input: 
        output.write("BEGIN:VCARD\n") 
        output.write("VERSION:3.0\n")
        output.write("FN:"+row[0]+'.'+row[1]+'.NECF '+ row[2]+"\n") 
        output.write("N:"+"NECF "+row[2]+";"+row[0]+'.'+row[1]+";;;\n") 
        output.write("TEL;TYPE=CELL:"+row[3]+"\n")
        output.write("CATEGORIES:"+'Imported on 30/10,myContacts'+"\n") 
        output.write("END:VCARD\n") 
    output.close()
    return 'xyz'


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


        csv_file = st.file_uploader("Upload Csv", type=["csv"])

    if csv_file is not None:
		# To See details
        file_details = {"filename":csv_file.name, "filetype":csv_file.type,
                              "filesize":csv_file.size}
        st.write(file_details)

        # To View Uploaded Image
        N = st.number_input("Nitrogen", 1,10000)
        P = st.number_input("Phosporus", 1,10000)
        K = st.number_input("Potassium", 1,10000)
        temp = st.number_input("Temperature",0.0,100000.0)
        humidity = st.number_input("Humidity in %", 0.0,100000.0)
        ph = st.number_input("Ph", 0.0,100000.0)
        rainfall = st.number_input("Rainfall in mm",0.0,100000.0)

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1,-1)
        
        if st.button('Predict'):

            loaded_model = load_model('model.pkl')
            prediction = loaded_model.predict(single_pred)
            col1.write('''
		    ## Results 🔍 
		    ''')
            col1.success(f"{prediction.item().title()} are recommended by the A.I for your farm.")
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