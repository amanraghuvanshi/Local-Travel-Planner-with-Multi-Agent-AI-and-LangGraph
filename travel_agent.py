import os
import json
import streamlit as st
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from langchain_community.chat_models import ChatOllama
from langchain_community.utilities import GoogleSerperAPIWrapper
from agents import generate_itinerary, recommend_activities, fetch_useful_links, weather_forecaster, packing_list_generator, food_culture_recommender, chat_agent