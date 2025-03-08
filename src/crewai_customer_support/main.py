#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai_customer_support.crew import CrewaiCustomerSupport

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    title = "Customer Inquiry: CrewAI Features"
    user_content = """
    Hi CrewAI Team,

    How does CrewAI handle memory?

    Thanks,
    Javier
    """
    inputs = {"title": title, "user_content": user_content}
    
    try:
        CrewaiCustomerSupport().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    title = "Customer Inquiry: CrewAI Features"
    user_content = """
    Hi CrewAI Team,
    
    I've been exploring CrewAI for a while and have a few questions:
    
    1. How does CrewAI handle memory between tasks?
    2. Can I integrate custom tools with CrewAI?
    3. What's the best way to debug agent outputs?
    
    Thanks!
    Manuel
    """
    inputs = {"title": title, "user_content": user_content}
    try:
        CrewaiCustomerSupport().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewaiCustomerSupport().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    title = "Customer Inquiry: CrewAI Features"
    user_content = """
    Hi CrewAI Team,
    
    I've been exploring CrewAI for a while and have a few questions:
    
    1. How does CrewAI handle memory between tasks?
    2. Can I integrate custom tools with CrewAI?
    3. What's the best way to debug agent outputs?
    
    Thanks!
    Manuel
    """
    inputs = {"title": title, "user_content": user_content.replace("**", "")}
    try:
        CrewaiCustomerSupport().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")