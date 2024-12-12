import streamlit as st
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults

llm = ChatGroq(api_key=st.secrets.get("GROQ_API_KEY"))
search = TavilySearchResults(max_results=2)
parser = StrOutputParser()

"# Wave The Magic Wand"
"## ...Gandalf Awaits..."
st.divider()

st.sidebar.title("Wizardry AI")
st.sidebar.markdown("Sales Assistant Enchanted By") 

st.sidebar.write("GroQ...  OpenAI...  StreamLit... ")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.page_link("app.py", label="Home", icon="🏠")
st.sidebar.page_link("http://www.google.com", label="Google", icon="🌎")
st.sidebar.page_link("https://github.com/karufy/My_Portfolio.github.io", label="GitHub", icon="👷‍♂️")
st.sidebar.write("")
st.sidebar.write("")

st.sidebar.subheader('Select Temperature')
Temperature = st.sidebar.select_slider(
   "Verbosity of Response",
     options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],value=0.5)
st.sidebar.write("")

st.sidebar.subheader('Select Top P')
Top_p = st.sidebar.select_slider(
   "Randomness of Response",
     options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],value=0.5)
temperature = 0.5
top_p = 0.3

st.sidebar.write("")
st.sidebar.feedback("stars")


with st.form("company_info", clear_on_submit=True):

    brand_name = st.text_input("**Brand Name**:")
    company_url = st.text_input("**Company URL**:")
    industry = st.text_input("**Industry**:")
    product_category = st.text_input("**Product Category**:")
    competitors = st.text_input("**Competitors**:")
    demographic = st.text_input("**Demographic**:")
    silver_bullet = st.text_input("**Silver Bullet**(Unique Selling Proposition):")
    target_investor = st.text_input("**Target Investor**:")
    Upload = st.file_uploader("**Upload a File**:")
    
    company_insights = ""
    
    if st.form_submit_button("Abracadabra"):
      if brand_name and company_url:
       with st.spinner("...brewing..."):
         company_information = search.invoke(company_url)
       print(company_information)
       
       prompt = """
You are an AI critical thinker, research assistant and expert sales and marketing guru. Perform these tasks:
      
    1. Your sole purpose is to write well written, critically acclaimed, sales pitch.
    2. Use the provided company data and industry, product category, competitors, demographic, silver bullet, and target investor to create a sales pitch.
    3. Create a one page marketing pitch in the style of David Ogilvy, complete with a catchy headline and graphics
    4. Create a Company Strategy: Insights into the companys activities and priorities.
    4. Create Competitor Mentions and analysis with a bar chart: Mentions of competitors from input URLs or scraped data.
    5. Leadership Information citing Ugo Bozz as the CEO: Relevant leaders and their roles.
    6. Product/Strategy Summary: Insights from public documents or reports.
    7. References: Links to articles, press releases, or other sources.
    8. Create a feasibility study and estimated revenue Line chart of predictive profits and competition analysis.

  Input Variables:
  - Brand Name: {brand_name}
  - Company URL: {company_url}      
  - Industry: {industry}
  - Product Category: {product_category}        
  - Competitors: {competitors}
  - Demographic: {demographic}
  - Silver Bullet: {silver_bullet}
  - Target Investor: {target_investor}
      
      """
       Prompt_Template = ChatPromptTemplate([("system", prompt)])
       chain = Prompt_Template | llm | parser 
       company_insights = chain.invoke({ 
         "brand_name": brand_name, 
         "company_url": company_url,
         "industry": industry,
         "product_category": product_category,
         "competitors": competitors,
         "demographic": demographic,
         "silver_bullet": silver_bullet,
         "target_investor": target_investor})

st.markdown(company_insights)




