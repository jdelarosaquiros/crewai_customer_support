import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool

@CrewBase
class CrewAICustomerSupport:
    """Crew for handling CrewAI customer support inquiries"""

    # Reference the YAML configurations
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def crewai_research_agent(self) -> Agent:
        """Creates the CrewAI Research Agent"""
        return Agent(
            config=self.agents_config['crewai_research_agent'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def crewai_customer_support_agent(self) -> Agent:
        """Creates the CrewAI Customer Support Agent"""
        return Agent(
            config=self.agents_config['crewai_customer_support_agent'],
            verbose=True
        )

    @task
    def extract_questions_research_task(self) -> Task:
        """Extracts questions from user input and researches them"""
        return Task(
            config=self.tasks_config['extract_questions_research_task']
        )

    @task
    def answer_formulation_task(self) -> Task:
        """Formulates well-structured responses from the research findings"""
        return Task(
            config=self.tasks_config['answer_formulation_task']
        )

    @task
    def email_response_task(self) -> Task:
        """Formats the final responses into a professional email"""
        return Task(
            config=self.tasks_config['email_response_task']
        )

    @before_kickoff
    def before_kickoff_hook(self, inputs):
        print(f"🚀 Preparing to process customer inquiries with inputs: {inputs}")
        return inputs

    @after_kickoff
    def after_kickoff_hook(self, result):
        print(f"✅ Customer support response generated successfully:\n{result}")
        return result

    @crew
    def crew(self) -> Crew:
        """Assembles the CrewAI Customer Support team"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorators
            tasks=self.tasks,  # Automatically created by the @task decorators
            process=Process.sequential,
            verbose=True
        )
