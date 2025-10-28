
import streamlit as st

# Assuming business_features and get_chatbot_response are defined elsewhere or imported
# For this example, we'll include simple definitions to make the file runnable

business_features = {
    "Customer Support": {
        "description": "Our customer support is available 24/7 via chat, email, and phone to assist you with any issues or questions you may have.",
        "details": "We offer multi-language support and dedicated account managers for enterprise clients."
    },
    "Billing": {
        "description": "Our billing system is flexible and allows for various payment methods, including credit cards, bank transfers, and popular online payment platforms.",
        "details": "You can view your invoices and payment history directly within your account dashboard."
    },
    "Product Features": {
        "description": "We offer a wide range of product features designed to streamline your workflow and boost productivity.",
        "details": "Specific features include task management, project collaboration tools, and integrated analytics."
    }
}

def get_chatbot_response(query):
    """
    Processes user query and returns information about business features.

    Args:
        query: The user's input string.

    Returns:
        A string containing the relevant feature information or a default message.
    """
    query_lower = query.lower()
    for feature_name, feature_info in business_features.items():
        if feature_name.lower() in query_lower or feature_name.lower().replace(" ", "") in query_lower.replace(" ", ""):
            response = f"**{feature_name}:**\n\n"
            response += f"**Description:** {feature_info['description']}\n\n"
            response += f"**Details:** {feature_info['details']}"
            return response

    return "I'm sorry, I couldn't find information on that topic. Please ask about Customer Support, Billing, or Product Features."


st.title("Business Features Chatbot")

user_query = st.text_input("Ask me about our business features:")

if user_query:
    st.write("You asked:", user_query)
    # Call the chatbot logic function
    chatbot_response = get_chatbot_response(user_query)
    # Display the chatbot response
    st.info(chatbot_response)
else:
    st.info("Enter your query above to start the conversation.")
