import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Insurance Risk Analytics",
    page_icon="📊",
    layout="wide"
)


# Title
st.title("📊 Insurance Risk Analytics Dashboard")


st.markdown(
    """
    ## Business Objective

    This dashboard helps insurance stakeholders:

    - Explore customer risk patterns
    - Analyze claim behavior
    - Understand important risk factors
    - Support data-driven underwriting decisions

    """
)


# Dashboard summary cards

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        label="Total Policies",
        value="50,000"
    )


with col2:
    st.metric(
        label="Average Claim Amount",
        value="$12,500"
    )


with col3:
    st.metric(
        label="High Risk Customers",
        value="8,200"
    )


st.divider()


st.subheader("Project Overview")


st.write(
    """
    The system uses machine learning models to predict insurance risk
    and provide transparent explanations for predictions.
    """
)