
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

"""
class MockAIMessage: 
    
    def __init__(self, content): 
        self.content = content
"""

"""
class ChatGroq:

    def __init__(self,model,temperature=0,max_retries=2):
        self.model=model
        self.temperature=temperature
        self.max_retries=max_retries
        self.valid_models=[
            "llama-3.1-8b-instant",
            "llama-3.3-70b-versatile",
        ]
        if model  not in self.valid_models:
            raise ValueError(f"Invalid model: {model}")

    def invoke(self, message):
        if not isinstance(message,list) or len(message)==0:
            raise ValueError("Message must be a non-empty list")

        if self.model== "llama-3.1-8b-instant":

            content=f"[Llama 3 Response] Machine learning is a subset of AI that enables computers to learn patterns from data without explicit programming."

        elif self.model== "llama-3.3-70b-versatile":

            if self.temperature>0.2:

                content =f"[Llama 3.3 Creative Response] Machine learning is like teaching a computer to recognize patterns in data, much like how humans learn from experience!"
            
            else:
                content=f"[Llama 3.3 Response] Machine learning allows computers to learn and improve from data without being explicitly programmed."
        else:
            content= f"[Mock Response] This is a simulated response from {self.model}"

        return MockAIMessage(content)
"""

def implement_set_api_key(api_key):
    os.environ["GROQ_API_KEY"]=api_key
    print("✓ API key has been set in environment variables!")

def check_api_key():
    if "GROQ_API_KEY" not in os.environ:
        raise exception ("GROQ_API_KEY environment variable is required")

def implement_llama_3_3_model():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_retries=2
    )

def implement_query_model(model,prompt):
    try:
        # Use LangChain message format
        messages = [("human", prompt)]
        response = model.invoke(messages)
        return response.content
    except Exception as e:
        raise Exception(f"Error querying model: {str(e)}")


print("🚀 Groq Model Switching Solution (LangChain Integration)")
print("=" * 55)
print("📝 Complete solution for langchain-groq integrationpatterns!")
print("🌐 Using exact model names from console.groq.com")
print()


try:
    # Demonstrate API key management
    #print("🔑 Setting API key...")
    #implement_set_api_key(api_key)
    
    # Verify API key was set correctly
    check_api_key()
    print("✓ API key validation working!")
    
    # Test prompt
    test_prompt = "Explain the concept of machine learning in one sentence."


    print(f"🤖 Testing Llama 3.3 (llama-3.3-70b-versatile):")
    llama33 = implement_llama_3_3_model()
    response33 = implement_query_model(llama33, test_prompt)
    print(f"Llama 3.3: {response33}\n")



    print("\n🎉 All langchain-groq integration functions workingcorrectly!")
    print("✅ Solution demonstrates:")
    print("  - Proper API key management with implement_set_api_ke()")
    print("  - Exact Groq model names from console.groq.com")
    print("  - Correct LangChain message formatting")
    print("  - Proper temperature configurations")
    print("  - Function composition and data structure handling")
    
    print("\n🚀 For real langchain-groq projects:")
    print("  1. Install: pip install langchain-groq")
    print("  2. Import: from langchain_groq import ChatGroq")
    print("  3. Get API key from console.groq.com")
    print("  4. Use exact model names from Groq documentation")
    print("  5. Follow the same integration patterns shown here")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("This shouldn't happen in the complete solution!")

