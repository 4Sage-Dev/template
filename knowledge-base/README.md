# 4SAGE Knowledge Base

This directory contains reference material, genre conventions, platform
constraints, and design patterns.

## Why This Exists

LLMs are excellent at reasoning, but their internal knowledge can be
generalized or occasionally hallucinate specifics. The documents in this
directory serve as **mandatory reference material** that the LLM must
consult when conducting a Key Design Decision dialogue.

By keeping genre conventions, platform constraints, and proven design
patterns explicit in this folder, we ensure that the AI consultant's
recommendations are grounded in reality.

## How to Use This

When acting as the consultant guiding the 4SAGE design process, you
(the LLM) should:
1. Search this directory for topics relevant to the current KDD.
2. Read the appropriate reference material.
3. Formulate your follow-on questions based on the constraints found.

## Structure (Planned)

- `genres/` — Genre conventions, player expectations, common mechanics
- `platforms/` — Platform capabilities, constraints, certification requirements
- `patterns/` — Proven game design patterns and anti-patterns
- `monetization/` — Business model conventions and trade-offs
