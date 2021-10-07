# installing camelot-py should be done from terminal ONLY using the next 2 lines of code
# first -->  pip3 install camelot-py
# then pip install "camelot-py[base]"


# importing packages
import pandas as pd
import camelot as cm
import seaborn as sns
import numpy as np


# getting the file link and choose arguments as stream and the pages i needed
input_pdf = cm.read_pdf("https://www.un.org/development/desa/dpad/wp-content/uploads/sites/45/WESP2020_FullReport.pdf", \
                       flavor= 'stream',pages='24,25') # use this for pdfs from online sources


input_pdf # confirmation for data and it will give back the number of tables created as N


# getting the shape of each extracted table
for n in input_pdf:
    print(n)


# checking the first table with index zero
input_pdf[0].df


# assigning the result to a DataFrame --> df
df = input_pdf[0].df.loc[2:38, :]


# getting a copy of the DataFrame to do operations on it, so when i need to revert back i just run the previous cell
wesp_2020 = df.copy()


# making the first row is the columns names
wesp_2020.columns = wesp_2020.iloc[0]
#reseting the index of the dataframe
wesp_2020.reset_index(drop=True)
# dropping the first row as it is now columns and has no meanning in the dataframe
wesp_2020 = wesp_2020.iloc[1:,:]
wesp_2020


# getting the second dataframe from the second table
input_pdf[1].df


# loading the second table into DataFrame
df2 = input_pdf[1].df.loc[2:36, :]


# getting a copy of the second DataFrame df2
gwog_2020 = df2.copy()


# making the first row is the columns names 
gwog_2020.columns = gwog_2020.iloc[0]
# reseting the index of the dataframe to be able to drop the duplicated first row 
gwog_2020.reset_index(drop=True)
# dropping the first raw as it has no meaning in dataframe now
gwog_2020 = gwog_2020.iloc[1:,:]
gwog_2020


# reaplacing the empty values with np.nan to drop them
wesp_2020 = wesp_2020.replace("", np.nan)
wesp_2020 = wesp_2020.dropna() # drop na values
wesp_2020


# converting numeric columns to float instead of object
wesp_2020.loc[:,['2017', '2018', '2019a', '2020b', '2021b',
       '2019', '2020']] = wesp_2020.loc[:,['2017', '2018', '2019a', '2020b', '2021b',
       '2019', '2020']].apply(pd.to_numeric)


wesp_2020["value"] = wesp_2020['value'].astype(float)
wesp_2020.info()


# converting wesp_2020 to excel
wesp_2020.to_excel("wesp_excel.xlsx",  sheet_name='Sheet_name_2')


with pd.ExcelWriter('wesp_excel.xlsx') as writer:  
    wesp_2019.to_excel(writer, sheet_name='Sheet_name_1')
    wesp_2020.to_excel(writer, sheet_name='Sheet_name_2')


# changing the data from wide to long format using melt
wesp_2020 = wesp_2020.melt(id_vars='Annual percentage change', var_name='year')


import PyPDF2


#creating a pdf object and open it in binary mode
pdfobj = open("Weratedogs Analysis report.pdf", 'rb')
#create a reader object
filereader = PyPDF2.PdfFileReader(pdfobj)
#print number of pages
print(filereader.numPages)


for page in range(filereader.numPages):
    page = filereader.getPage(page)
    print(page.extractText())


# closing the pdf file object 
pdfobj.close() 


# getting each page in a seperate file
with open('Weratedogs Analysis report.pdf','rb') as pdf_file, open('sample.txt', 'w') as text_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages):   # use xrange in Py2
        page = read_pdf.getPage(page_number)
        page_content = page.extractText()
        text_file.write(page_content)


# STEP 1
# import libraries
import fitz
import io
from PIL import Image


# STEP 2
# file path you want to extract images from
file = "Weratedogs Analysis report.pdf"

# open the file
pdf_file = fitz.open(file)

# STEP 3
# iterate over PDF pages
for page_index in range(len(pdf_file)):
	
	# get the page itself
	page = pdf_file[page_index]
	image_list = page.getImageList()
	
	# printing number of images found in this page
	if image_list:
		print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
	else:
		print("[get_ipython().getoutput("] No images found on page", page_index)")
	for image_index, img in enumerate(page.getImageList(), start=1):
		
		# get the XREF of the image
		xref = img[0]
		
		# extract the image bytes
		base_image = pdf_file.extractImage(xref)
		image_bytes = base_image["image"]
		
		# get the image extension
		image_ext = base_image["ext"]
        



