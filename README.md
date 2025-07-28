
# NeuroTwin: Multi-Agent AI for Personalized Learning 🧠🤖

**Status**: 🚧 *Under Active Development* 

---

## 📌 Overview
An adaptive AI tutor that uses **multi-agent systems** and **cognitive profiling** to tailor explanations to individual learning styles, mimicking how human teachers adjust for slower/faster learners.  

**Key Features**:
- � **Cognitive Profiling**: Classifies users via [MM-IQ dataset](https://huggingface.co/datasets/huanqia/MM-IQ) + real-time feedback.
- 🧩 **Multi-Agent Architecture**: Specialized agents for assessment, explanation, and retention.
- 🎯 **Dynamic Adaptation**: Shifts teaching strategies based on user comprehension.

---

## 🌟 Why This Project?
Most AI tutors treat all learners the same. **CogMind**:
- 🔍 Detects *how* you learn (visual/verbal/abstract).
- 📈 Evolves with your progress (like a human tutor).
- 💡 Explains *why*, not just *what*.

---

## 🛠️ Current Progress (Under Development)
| Component          | Status       | Next Steps                  |
|--------------------|--------------|-----------------------------|
| Cognitive Profiler | 🟡 Prototype | Integrate Bayesian updating |
| Explanation Agent  | 🟠 Planning  | Build knowledge graph       |
| Orchestrator       | 🔴 Research  | AutoGen/LangGraph setup     |

**Recent Updates**:  
- ✅ MM-IQ dataset analysis complete (June 2024)  
- ⚙️ Testing FastText for initial user classification  

---

## 🧩 Technical Stack (Planned)
| Area               | Tools/Libraries                          |
|--------------------|------------------------------------------|
| Multi-Agent System | AutoGen, LangChain                       |
| Cognitive Modeling | PyMC3 (Bayesian), XGBoost                |
| Explanations       | Mistral-7B, Neo4j (Knowledge Graph)      |
| Infrastructure     | FastAPI, Redis, Docker                   |

