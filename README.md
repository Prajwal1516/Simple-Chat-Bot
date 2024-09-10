Project Overview:
The chatbot was built by defining pairs and reflections, which are used to match the user's input to predefined responses. Here’s a brief breakdown of the process:

	Pairs: These are pattern-response pairs. For instance, if the user says "hello", the bot responds with a friendly greeting like "Hi there!".
	Reflections: These help the chatbot dynamically adjust responses by mapping certain words like "I" to "you", ensuring a more natural conversation flow.
	Interactive Frontend: I also developed a simple yet engaging frontend to make the bot easily accessible to users. This interface allows users to interact with the chatbot smoothly and efficiently.

Tech Stack:
	Python: The backbone of the project, handling the chatbot logic and backend operations.
	Flask: A lightweight web framework used to create the server and manage routes.
	NLTK (Natural Language Toolkit): Utilized for natural language processing, enabling the chatbot to understand and respond to user inputs.
	HTML/CSS/JavaScript: Developed a simple and interactive frontend for seamless user interaction.

Key Features:
	Natural Language Processing with NLTK:

		Pattern-Response Pairs: Defined specific patterns using regular expressions to match user inputs and provide appropriate responses.
		Reflections: Leveraged NLTK’s reflections to handle conversational nuances, making interactions feel more natural and engaging.
	Flask Backend:

		Routes: Created routes to serve the frontend and handle chat requests.
		Chat History Management: Implemented a mechanism to store and manage the conversation history, enhancing the continuity of interactions.
	Interactive Frontend:

		User Interface: Designed a clean and intuitive interface where users can easily type their messages and receive responses.
		Real-Time Interaction: Enabled real-time communication between the user and the chatbot using AJAX for smooth and dynamic updates.
	Smart Fallback Mechanism:

		Default Responses: When the chatbot doesn’t recognize a user input, it responds with “Let me search that for you.”
		ChatGPT Integration: Redirects users to ChatGPT for more complex queries, ensuring that users always get the information they need.

Technical Highlights:
	NLTK Integration: Utilized NLTK’s Chat class for creating the conversational structure.
	Custom Chatbot Logic: I defined custom chat patterns like greetings, farewells, and questions such as "What’s your name?" or "Who created you?"
	Dynamic Search Handling: In cases where the chatbot doesn't have a predefined answer, it offers users a link to search for more information dynamically.

