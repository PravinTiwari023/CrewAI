from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
import streamlit as st

from task import MeetingPrepTasks
from agents import MeetingPrepAgents

tasks = MeetingPrepTasks()
agents = MeetingPrepAgents()

st.title("Welcome to the Meeting Prep Crew")
participants = st.text_input("What are the names of the participants in the meeting?\n")
meeting_context = st.text_area("What is the context of the meeting?\n")
objective = st.text_area("What is your objective for this meeting?\n")

if st.button('Crew KickOff!!'):
	# Create Agents
	researcher_agent = agents.research_agent()
	industry_analyst_agent = agents.industry_analysis_agent()
	meeting_strategy_agent = agents.meeting_strategy_agent()
	summary_and_briefing_agent = agents.summary_and_briefing_agent()

	# Create Tasks
	research = tasks.research_task(researcher_agent, participants, meeting_context)
	industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, participants, meeting_context)
	meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, meeting_context, objective)
	summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, meeting_context, objective)

	meeting_strategy.context = [research, industry_analysis]
	summary_and_briefing.context = [research, industry_analysis, meeting_strategy]

	# Create Crew responsible for Copy
	crew = Crew(
		agents=[
			researcher_agent,
			industry_analyst_agent,
			meeting_strategy_agent,
			summary_and_briefing_agent
		],
		tasks=[
			research,
			industry_analysis,
			meeting_strategy,
			summary_and_briefing
		]
	)

	result = crew.kickoff()


	# Print results
	st.write("## Here is the result")
	st.write(result)
