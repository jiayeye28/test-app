import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly_express as px
import streamlit.components.v1 as components

def stats(dataframe):
    st.header('Binding Constraint')
    st.write(dataframe.head())

def data_header(dataframe):
    st.header('Data Header')
    st.write(df.describe())

def scatter(dataframe):
    st.header('Scatter Plot')
    st.markdown('#### This is  **markdown** ')

    fig, ax = plt.subplots(1,1)
    ax.scatter (x=df['date'], y = df['Constraint Exposure_base'])
    ax.set_xlabel('date')
    ax.set_ylabel('Constraint Exposure_base')
    st.pyplot(fig)

def interact_plot(df):
    x_axis_val = st.selectbox('Select X asix value', options = df.columns)
    y_axis_val = st.selectbox('Select Y asix value', options = df.columns)
    col = st.color_picker('Select a colr')

    plot = px.scatter(df, x = x_axis_val, y= y_axis_val)
    plot.update_traces(marker = dict(color = col))

    st.plotly_chart(plot)

def line_chart(df):
    # Add a slider for selecting the number of data points to display
    num_points = st.slider('Select number of data points to display', 10, len(df), 50)


    # Create a Plotly line chart with selected number of points
    fig = px.line(df.head(num_points), 
                  x=df.index[:num_points], 
                  y=['A', 'B', 'C'], 
                  labels={'x': 'Index', 'value': 'Values'},
                  title='Random Data Plot with Plotly')
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)

st.title('Vanessa Trial Blog')

st.text('This is a web app to explore')

st.markdown('## This is  **markdown** ')

st.sidebar.title('Navigation')

upload_file = st.sidebar.file_uploader('Upload your file here')

options = st.sidebar.radio('Pages', options = ['Home','Binding Constraint','Data Header','Scatter Plot','Interactive Plot','Line Chart'])

# if upload_file:
    
#     df = pd.read_excel(upload_file)
 
df=pd.read_excel(r"X:\Market Analysis\Departmental\DAYZER\PJM\Trading\Spec\Output\bcr_sort.xlsx")

np.random.seed(42)
data = np.random.randn(100, 3)
    # Create a DataFrame
df_line = pd.DataFrame(data, columns=['A', 'B', 'C'])

if options == 'Binding Constraint':
    stats(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Scatter Plot':
    scatter(df)
elif options == 'Interactive Plot':
    interact_plot(df)
elif options == 'Line Chart':
    line_chart(df_line)

# # show_print_button ="""
# #     <script>
# #         function print_page(obj) {
# #             obj.style.display = "none";
# #             parent.window.print();
# #         }
# #     </script>
# #     <button onclick="print_page(this)">
# #         Print page (choose 'Save as PDF' in print dialogue)
# #     </button>
# #     """
# # components.html(show_print_button)
# # Function to generate PDF
# def generate_pdf(tables_and_charts):
#     pdf = PDF()
    
#     for title, content in tables_and_charts:
#         pdf.add_page()
#         pdf.chapter_title(title)

#         if isinstance(content, str):
#             pdf.chapter_body(content)
#         else:
#             chart_path = f"{title}.png"
#             content.savefig(chart_path)
#             pdf.image(chart_path, x=10, w=190)
#             plt.close(content)  # Close the figure to free up memory

#     pdf_file_path = "performance_report.pdf"
#     pdf.output(pdf_file_path)
#     return pdf_file_path

# # Streamlit app layout
# st.title('Vanessa Trial Blog')
# st.text('This is a web app to explore')
# st.markdown('## This is  **markdown** ')

# st.sidebar.title('Navigation')
# upload_file = st.sidebar.file_uploader('Upload your file here')
# options = st.sidebar.radio('Pages', options=['Home', 'Binding Constraint', 'Data Header', 'Scatter Plot', 'Interactive Plot', 'Line Chart', 'Download PDF'])

# # Load DataFrame
# df = pd.read_excel(r"X:\Market Analysis\Departmental\DAYZER\PJM\Trading\Spec\Output\bcr_sort.xlsx")

# # Generate random data for line chart
# np.random.seed(42)
# data = np.random.randn(100, 3)
# df_line = pd.DataFrame(data, columns=['A', 'B', 'C'])

# # Store content for PDF
# tables_and_charts = []

# if options == 'Binding Constraint':
#     stats(df)
#     tables_and_charts.append(('Binding Constraint', df.head().to_string()))
# elif options == 'Data Header':
#     data_header(df)
#     tables_and_charts.append(('Data Header', df.describe().to_string()))
# elif options == 'Scatter Plot':
#     fig = scatter(df)
#     tables_and_charts.append(('Scatter Plot', fig))
# elif options == 'Interactive Plot':
#     fig = interact_plot(df)
#     tables_and_charts.append(('Interactive Plot', fig))
# elif options == 'Line Chart':
#     fig = line_chart(df_line)
#     tables_and_charts.append(('Line Chart', fig))
# elif options == 'Download PDF':
#     pdf_file_path = generate_pdf(tables_and_charts)
#     with open(pdf_file_path, 'rb') as f:
#         st.download_button("Download Performance Report", f.read(), file_name="performance_report.pdf")

# # Print button
# show_print_button = """
#     <script>
#         function print_page(obj) {
#             obj.style.display = "none";
#             parent.window.print();
#         }
#     </script>
#     <button onclick="print_page(this)">
#         Print page (choose 'Save as PDF' in print dialogue)
#     </button>
# """
# components.html(show_print_button)

# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# from fpdf import FPDF

# # Create a PDF class
# class PDF(FPDF):
#     def header(self):
#         self.set_font('Arial', 'B', 12)
#         self.cell(0, 10, 'Dayzer Performance Report', 0, 1, 'C')

#     def chapter_title(self, title):
#         self.set_font('Arial', 'B', 12)
#         self.cell(0, 10, title, 0, 1, 'L')
#         self.ln(2)

#     def chapter_body(self, body):
#         self.set_font('Arial', '', 12)
#         self.multi_cell(0, 10, body)
#         self.ln()

# # Function to generate PDF
# def generate_pdf(charts):
#     pdf = PDF()
    
#     for i, chart in enumerate(charts):
#         pdf.add_page()
#         pdf.chapter_title(f"Page {i + 1}: Chart")
        
#         # Save each chart to a file
#         chart_path = f"chart_{i + 1}.png"
#         plt.figure(figsize=(8, 4))
#         plt.plot(chart)
#         plt.title(f"Chart {i + 1}")
#         plt.savefig(chart_path)
#         plt.close()  # Close the plot to free up memory
        
#         pdf.image(chart_path, x=10, w=190)
#         pdf.ln(10)

#     pdf_output = "performance_report.pdf"
#     pdf.output(pdf_output)
#     return pdf_output

# # Streamlit layout
# st.title('Dayzer Performance Report')

# # Generate some sample data
# charts_data = [np.random.randn(100).cumsum() for _ in range(3)]

# if st.button("Download PDF"):
#     pdf_file_path = generate_pdf(charts_data)
#     with open(pdf_file_path, 'rb') as f:
#         st.download_button("Download Performance Report", f.read(), file_name="performance_report.pdf")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from fpdf import FPDF

# PDF class definition
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Dayzer Performance Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def stats(dataframe):
    st.header('Binding Constraint')
    st.write(dataframe.head())
    return dataframe.head().to_string()

def data_header(dataframe):
    st.header('Data Header')
    st.write(dataframe.describe())
    return dataframe.describe().to_string()

def scatter(dataframe):
    st.header('Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(x=dataframe['date'], y=dataframe['Constraint Exposure_base'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Constraint Exposure Base')
    st.pyplot(fig)
    return fig

def interact_plot(dataframe):
    x_axis_val = st.selectbox('Select X axis value', options=dataframe.columns)
    y_axis_val = st.selectbox('Select Y axis value', options=dataframe.columns)
    col = st.color_picker('Select a color')
    
    plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=col))
    
    st.plotly_chart(plot)
    return plot

def line_chart(dataframe):
    num_points = st.slider('Select number of data points to display', 10, len(dataframe), 50)
    fig = px.line(dataframe.head(num_points), x=dataframe.index[:num_points], y=['A', 'B', 'C'], 
                  labels={'x': 'Index', 'value': 'Values'}, title='Random Data Plot with Plotly')
    st.plotly_chart(fig)
    return fig

# Function to generate PDF
def generate_pdf(tables_and_charts):
    pdf = PDF()
    
    for title, content in tables_and_charts:
        pdf.add_page()
        pdf.chapter_title(title)

        if isinstance(content, str):
            pdf.chapter_body(content)
        else:
            chart_path = f"{title}.png"
            content.savefig(chart_path)
            pdf.image(chart_path, x=10, w=190)
            plt.close(content)  # Close the figure to free up memory

    pdf_file_path = "performance_report.pdf"
    pdf.output(pdf_file_path)
    return pdf_file_path

# Streamlit app layout
st.title('Vanessa Trial Blog')
st.text('This is a web app to explore')
st.markdown('## This is  **markdown** ')

st.sidebar.title('Navigation')
upload_file = st.sidebar.file_uploader('Upload your file here', key='file_uploader_1')
options = st.sidebar.radio('Pages', options=['Home', 'Binding Constraint', 'Data Header', 'Scatter Plot', 'Interactive Plot', 'Line Chart', 'Download PDF'])

# Load DataFrame
df = pd.read_excel(r"X:\Market Analysis\Departmental\DAYZER\PJM\Trading\Spec\Output\bcr_sort.xlsx")

# Generate random data for line chart
np.random.seed(42)
data = np.random.randn(100, 3)
df_line = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Store content for PDF
tables_and_charts = []

if options == 'Binding Constraint':
    content = stats(df)
    tables_and_charts.append(('Binding Constraint', content))
elif options == 'Data Header':
    content = data_header(df)
    tables_and_charts.append(('Data Header', content))
elif options == 'Scatter Plot':
    fig = scatter(df)
    tables_and_charts.append(('Scatter Plot', fig))
elif options == 'Interactive Plot':
    fig = interact_plot(df)
    tables_and_charts.append(('Interactive Plot', fig))
elif options == 'Line Chart':
    fig = line_chart(df_line)
    tables_and_charts.append(('Line Chart', fig))
elif options == 'Download PDF':
    if tables_and_charts:  # Only generate if there is content
        pdf_file_path = generate_pdf(tables_and_charts)
        with open(pdf_file_path, 'rb') as f:
            st.download_button("Download Performance Report", f.read(), file_name="performance_report.pdf")
    else:
        st.warning("No content to include in the PDF.")

# Print button
show_print_button = """
    <script>
        function print_page(obj) {
            obj.style.display = "none";
            parent.window.print();
        }
    </script>
    <button onclick="print_page(this)">
        Print page (choose 'Save as PDF' in print dialogue)
    </button>
"""
st.components.v1.html(show_print_button)
