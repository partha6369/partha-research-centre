import gradio as gr
import os

APP_TITLE = "🧪 Dr. Partha Majumdar’s Research Centre"
APP_DESCRIPTION = (
    "Welcome to a suite of AI-powered tools developed and maintained by Dr. Partha Majumdar. "
    "These applications explore Natural Language Processing, document summarisation, sentiment analysis, and more. "
    "Use the interactive modules below to access each application in its dedicated workspace. "
    "All the code and artefacts are available for studying, researching, and enhancing."
)

# Try to load the PayPal URL from the environment; if missing, use a placeholder
paypal_url = os.getenv("PAYPAL_URL", "https://www.paypal.com/donate/dummy-link")

with gr.Blocks(title=APP_TITLE) as app:
    gr.HTML(f"""
        <div style='text-align: center; margin-bottom: 30px;'>
            <p style='font-size: 40px; font-weight: bold;'>{APP_TITLE}</p>
            <p style='font-size: 16px; line-height: 1.6; max-width: 900px; margin: auto;'>
                {APP_DESCRIPTION}
            </p>
        </div>
    """)

    with gr.Tabs():
        with gr.TabItem("Natural Language Processing (NLP)"):

            with gr.Tabs():
                with gr.TabItem("Transformers"):

                    with gr.Tabs():
                        with gr.TabItem("Gemini"):
        
                            with gr.Tabs():
                                with gr.TabItem("🧘 ManoVākya (मनॊवाक्य) - Sentiment & Summary"):
                                    gr.HTML("""
                                    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 40px; margin-top: 20px;">
                                        
                                        <!-- LEFT: App Description -->
                                        <div style="flex: 1; min-width: 300px; max-width: 600px; font-size: 15px; line-height: 1.6;">
                                            <h3>🧘 ManoVākya (मनॊवाक्य)</h3>
                                            <p>
                                            ManoVākya is your intelligent AI companion for understanding and interpreting language with clarity and insight.
                                            Whether you're journaling, reflecting, managing team communication, or reviewing documents, ManoVākya reveals tone,
                                            structure, and the distilled essence of your writing.
                                            </p>
                                            <p>
                                            It offers sentiment classification, document summarisation (PDF or plain text), and meaning extraction
                                            — all in one app.
                                            </p>
                                            <p>
                                            💡 <strong>Technology Used:</strong><br>
                                            • <code>Google Generative AI (Gemini)</code> for Sentiment Analysis, Text Summarisation and Document Summarisation<br>
                                            </p>
                                            <p>
                                            Developed with researchers, professionals, and reflective individuals in mind, ManoVākya helps you not just write better, but think deeper.
                                            </p>
                                            <a href="https://huggingface.co/spaces/partha6369/manovakya" target="_blank">
                                                <button style="background-color:#4CAF50;color:white;padding:10px 20px;
                                                font-size:16px;border:none;border-radius:5px;cursor:pointer;margin-top:10px;">
                                                    🚀 Open ManoVākya App
                                                </button>
                                            </a>
                                        </div>
                                    
                                        <!-- RIGHT: App Image -->
                                        <div style="flex: 1; min-width: 300px; text-align: center;">
                                            <img src="https://huggingface.co/spaces/partha6369/partha-research-centre-preprod/resolve/main/AppImage-manovakya.png" 
                                                 alt="Application Screenshot"
                                                 style="pointer-events: none; 
                                                        user-select: none; 
                                                        -webkit-user-drag: none; 
                                                        width: 100%; 
                                                        max-width: 600px; 
                                                        border-radius: 10px; 
                                                        box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
                                        </div>
                                    </div>
                                    """)

                                with gr.TabItem("🩺 NidanaMap"):
                                    gr.HTML("""
                                    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 40px; margin-top: 20px;">
                                        
                                        <!-- LEFT: App Description -->
                                        <div style="flex: 1; min-width: 300px; max-width: 600px; font-size: 15px; line-height: 1.6;">
                                            <h3>🩺 NidanaMap</h3>
                                            <p>
                                            NidanaMap is an AI-powered ICD-10 diagnosis mapper designed to support healthcare professionals, medical coders, and researchers in linking free-text diagnoses to standardised ICD-10 codes. With a combination of fuzzy matching and vector embeddings trained on the official ICD-10 hierarchy, NidanaMap brings accuracy, relevance, and interpretability to the task of medical code prediction.
                                            </p>
                                            <p>
                                            Users can enter any diagnosis, such as “chronic kidney disease” or “type 2 diabetes” — and receive top ICD-10 code matches, each justified using a blend of textual similarity and ICD vector proximity. The system also enables user feedback via suggestions, helping the model grow organically.
                                            </p>
                                            <p>
                                            💡 <strong>Technology Used:</strong><br>
                                            • <code>ICDCodex</code> for ICD-10 hierarchy and embeddings<br>
                                            • <code>RapidFuzz</code> for fast fuzzy string matching<br>
                                            • <code>NLTK</code> for intelligent text preprocessing and lemmatisation<br>
                                            • <code>Pandas</code> and <code>Gradio</code> for interface and interaction
                                            </p>
                                            <p>
                                            NidanaMap helps bridge the gap between human-readable clinical notes and machine-readable diagnostic standards — essential for hospital workflows, claims processing, epidemiological research, and AI-driven health applications.
                                            </p>
                                            <a href="https://huggingface.co/spaces/partha6369/NidanaMap" target="_blank">
                                                <button style="background-color:#4CAF50;color:white;padding:10px 20px;
                                                font-size:16px;border:none;border-radius:5px;cursor:pointer;margin-top:10px;">
                                                    🚀 Open NidanaMap App
                                                </button>
                                            </a>
                                        </div>
                                    
                                        <!-- RIGHT: App Image -->
                                        <div style="flex: 1; min-width: 300px; text-align: center;">
                                            <img src="https://huggingface.co/spaces/partha6369/partha-research-centre-preprod/resolve/main/AppImage-nidanamap.png" 
                                                 alt="Application Screenshot"
                                                 style="pointer-events: none; 
                                                        user-select: none; 
                                                        -webkit-user-drag: none; 
                                                        width: 100%; 
                                                        max-width: 600px; 
                                                        border-radius: 10px; 
                                                        box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
                                        </div>
                                    </div>
                                    """)
                        
                        with gr.TabItem("BART"):
        
                            with gr.Tabs():
                                with gr.TabItem("🪷 Saarika (सारिका) – Essence Extractor for Text using Transformers"):
                                    gr.HTML("""
                                    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 40px; margin-top: 20px;">
                                        
                                        <!-- LEFT: App Description -->
                                        <div style="flex: 1; min-width: 300px; max-width: 600px; font-size: 15px; line-height: 1.6;">
                                            <h3>🪷 Saarika (सारिका)</h3>
                                            <p>
                                            Saarika is your AI-powered essence extractor designed to distil lengthy texts into clear, concise summaries. Whether you're dealing with movie reviews, research articles, policy documents, or user-submitted content, Saarika captures the core message and reduces reading time, without losing meaning.
                                            </p>
                                            <p>
                                            This application is especially useful for researchers, educators, professionals, and developers who need to process large volumes of information and extract key ideas efficiently. Saarika can generate summaries for both real-world datasets and user-submitted content.
                                            </p>
                                            <p>
                                            💡 <strong>Technology Used:</strong><br>
                                            • <code>Transformers (facebook/bart-large-cnn)</code> for abstractive text summarisation<br>
                                            • <code>Datasets (Hugging Face)</code> for sourcing authentic training/test data like IMDB reviews<br>
                                            • <code>NLTK</code> for intelligent post-processing of summaries
                                            </p>
                                            <p>
                                            Unlike basic extractive summarizers, Saarika relies on deep learning transformers to rephrase, compress, and clarify the meaning of text, making it ideal for use in NLP research, educational tools, and editorial workflows.
                                            </p>
                                            <a href="https://huggingface.co/spaces/partha6369/saarika" target="_blank">
                                                <button style="background-color:#4CAF50;color:white;padding:10px 20px;
                                                font-size:16px;border:none;border-radius:5px;cursor:pointer;margin-top:10px;">
                                                    🚀 Open Saarika App
                                                </button>
                                            </a>
                                        </div>
                                    
                                        <!-- RIGHT: App Image -->
                                        <div style="flex: 1; min-width: 300px; text-align: center;">
                                            <img src="https://huggingface.co/spaces/partha6369/partha-research-centre-preprod/resolve/main/AppImage-saarika.png" 
                                                 alt="Application Screenshot"
                                                 style="pointer-events: none; 
                                                        user-select: none; 
                                                        -webkit-user-drag: none; 
                                                        width: 100%; 
                                                        max-width: 600px; 
                                                        border-radius: 10px; 
                                                        box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
                                        </div>
                                    </div>
                                    """)
        
                with gr.TabItem("Machine Learning / Deep Learning"):

                    with gr.Tabs():
                        with gr.TabItem("🧠 भावविवेक (BhāvaViveka)"):
                            gr.HTML("""
                                <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 40px; margin-top: 20px;">
                                    
                                    <!-- LEFT: App Description -->
                                    <div style="flex: 1; min-width: 300px; max-width: 600px; font-size: 15px; line-height: 1.6;">
                                        <h3>🧠 भावविवेक (BhāvaViveka)</h3>
                                        <p>
                                        BhāvaViveka is your AI-powered sentiment interpreter, designed to assess and classify the emotional tone embedded in written language. Whether you’re drafting emails, analysing reviews, interpreting social media posts, or curating feedback, BhāvaViveka provides a mindful lens into how your words may be perceived.
                                        </p>
                                        <p>
                                        This tool is ideal for communication professionals, educators, researchers, and anyone seeking to refine their emotional intelligence in digital writing. It allows both random sampling from the IMDB dataset and real-time analysis of custom text, making it suitable for both academic evaluation and everyday use.
                                        </p>
                                        <p>
                                        💡 <strong>Technology Used:</strong><br>
                                        • <code>TensorFlow</code> for deep neural network–based binary sentiment classification<br>
                                        • <code>IMDB Dataset</code> from <code>tf.keras.datasets</code> for training and benchmarking<br>
                                        • <code>textcleaner-partha</code> for robust preprocessing (HTML removal, EMOJI removal, lemmatisation, contraction expansion, abbreviation expansion, etc.)<br>
                                        </p>
                                        <p>
                                        Unlike generic sentiment checkers, BhāvaViveka uses a pre-trained neural network enhanced with high-quality text cleaning to offer consistent, reproducible, and intelligent sentiment evaluation, supporting mindful writing and emotionally aware interactions.
                                        </p>
                                        <a href="https://huggingface.co/spaces/partha6369/bhavaviveka" target="_blank">
                                            <button style="background-color:#4CAF50;color:white;padding:10px 20px;
                                            font-size:16px;border:none;border-radius:5px;cursor:pointer;margin-top:10px;">
                                                🚀 Open BhāvaViveka App
                                            </button>
                                        </a>
                                    </div>
                                
                                    <!-- RIGHT: App Image -->
                                    <div style="flex: 1; min-width: 300px; text-align: center;">
                                        <img src="https://huggingface.co/spaces/partha6369/partha-research-centre-preprod/resolve/main/AppImage-bhavaviveka.png" 
                                             alt="Application Screenshot"
                                             style="pointer-events: none; 
                                                    user-select: none; 
                                                    -webkit-user-drag: none; 
                                                    width: 100%; 
                                                    max-width: 600px; 
                                                    border-radius: 10px; 
                                                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
                                    </div>
                                </div>
                            """)

        with gr.TabItem("Reinforcement Learning"):

            with gr.Tabs():
        
                with gr.TabItem("🎯 Play Tic Tac Toe Against a TD-Learning Agent"):
                    gr.HTML("""
                        <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 40px; margin-top: 20px;">
                            
                            <!-- LEFT: App Description -->
                            <div style="flex: 1; min-width: 300px; max-width: 600px; font-size: 15px; line-height: 1.6;">
                                <h3>🎯 Play Tic Tac Toe Against a TD-Learning Agent</h3>
                                <p>
                                This interactive application lets you challenge a reinforcement learning agent trained using Temporal Difference (TD) learning, one of the foundational algorithms in reinforcement learning. Every game you play becomes part of the agent's learning journey, helping it improve over time without ever needing a predefined strategy.
                                </p>
                                <p>
                                Ideal for students, educators, and AI enthusiasts, this app demonstrates how machines can learn game strategies through exploration and feedback. It uses real-time state-value updates to make increasingly optimal decisions, providing both fun and educational insights into machine learning.
                                </p>
                                <p>
                                💡 <strong>Technology Used:</strong><br>
                                • <code>Python</code> for logic and simulation<br>
                                • <code>Numpy</code> and <code>Pandas</code> for game state representation and display<br>
                                • <code>Gradio</code> for creating an interactive web-based game interface<br>
                                • A custom-built <code>TD(0)</code> learning agent that updates its state values using rewards from human–agent gameplay
                                </p>
                                <p>
                                The agent improves as it plays more games, adapting its moves based on past outcomes. The interface shows the game board, allows human input (positions 0–8), and keeps daily statistics of matches and agent victories. A great hands-on experience to witness how reinforcement learning unfolds in practice.
                                </p>
                                <a href="https://huggingface.co/spaces/partha6369/TicTacToe" target="_blank">
                                    <button style="background-color:#4CAF50;color:white;padding:10px 20px;
                                    font-size:16px;border:none;border-radius:5px;cursor:pointer;margin-top:10px;">
                                        🚀 Open Tic Tac Toe App
                                    </button>
                                </a>
                            </div>
                        
                            <!-- RIGHT: App Image -->
                            <div style="flex: 1; min-width: 300px; text-align: center;">
                                <img src="https://huggingface.co/spaces/partha6369/partha-research-centre-preprod/resolve/main/AppImage-tictactoe.png" 
                                     alt="Application Screenshot"
                                     style="pointer-events: none; 
                                            user-select: none; 
                                            -webkit-user-drag: none; 
                                            width: 100%; 
                                            max-width: 600px; 
                                            border-radius: 10px; 
                                            box-shadow: 0 4px 8px rgba(0,0,0,0.2);" />
                            </div>
                        </div>
                    """)

    gr.HTML(f"""
        <a href="{paypal_url}" target="_blank">
            <button style="background-color:#0070ba;color:white;border:none;padding:10px 20px;
            font-size:16px;border-radius:5px;cursor:pointer;margin-top:10px;">
                ❤️ Support Research via PayPal
            </button>
        </a>
        """)

if __name__ == "__main__":
    # Determine if running on Hugging Face Spaces
    on_spaces = os.environ.get("SPACE_ID") is not None
    
    # Launch the app conditionally
    app.launch(share=not on_spaces)