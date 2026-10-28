# Agentic AI Pipeline

This repository is a hands-on collection of notebooks and examples for building agentic AI applications with Python, LangChain, LangGraph, and related tools. It explores the path from connecting to language models to creating tool-using agents, adding safety controls, retrieving information from documents, and evaluating application quality.

## Activate the environment (PowerShell)

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Project pipeline

The examples cover these stages:

1. **Connect to language models** — work with providers such as OpenAI, Google Gemini, and Groq, and explore streaming and batched responses.
2. **Build agent workflows** — use LangChain and LangGraph to compose prompts, messages, structured outputs, tools, state, memory, and streaming into interactive chatbot flows.
3. **Connect external tools** — expose functions through the Model Context Protocol (MCP) and let an agent select and call them. The `mcp/` example connects a math server over standard input/output and a weather server over Streamable HTTP.
4. **Add reliability and safety** — explore LLM gateways for provider routing, fallbacks, caching, and observability, along with guardrails such as input/output checks, PII handling, and human approval.
5. **Retrieve and evaluate knowledge** — build a document question-answering flow with PageIndex's tree-based retrieval approach, then evaluate chatbot and RAG responses with datasets and metrics using LangSmith.

These stages are demonstrated in separate notebooks and examples.

## Repository map

- `langchain/` — model integrations, messages, tools, middleware, and structured output.
- `langgraph/` — chatbot and agent workflows with tools, memory, and streaming.
- `mcp/` — math and weather MCP servers and a client that invokes their tools through an agent.
- `LLM-gateway/` — LiteLLM gateway patterns, including routing and fallbacks.
- `guardrails/` — safety and human-in-the-loop patterns for agents.
- `vectorless-RAG/` — document retrieval using PageIndex without conventional vector chunk search.
- `LLM-evaluation/` — chatbot and RAG evaluation examples.
- `deep-agents/` — examples of agents designed for multi-step tasks.
- `resources/` — supporting reference material.

