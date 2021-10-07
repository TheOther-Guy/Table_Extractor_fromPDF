# installing camelot-py should be done from terminal ONLY using the next 2 lines of code
# first -->  pip3 install camelot-py
# then pip install "camelot-py[base]"


# importing packages
import camelot as cm
import seaborn as sns


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
wesp_2019 = df.copy()


# getting the second dataframe from the second table
input_pdf[1].df


# loading the second table into DataFrame
df2 = input_pdf[1].df.loc[2:36, :]
df2


# getting a copy of the second DataFrame df2
gwog_2020 = df2.copy()












