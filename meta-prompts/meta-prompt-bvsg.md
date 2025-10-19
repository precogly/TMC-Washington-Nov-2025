# Meta-Prompt: Behavioral Vulnerabilities Stories Generator (BVSG)

## Objective

Generate a comprehensive prompt (800-1200 words) for an AI agent that will analyze multi-agentic systems and create pre-mortem narrative stories about behavioral emergent vulnerabilities - risks that arise from agent decision-making patterns, learning dynamics, goal-seeking behaviors, and strategic interactions between agents.

## Target Prompt Structure

### 1. Role & Context (~75 words)

Establish that this agent is part of a 4-agent vulnerability analysis pipeline. Its specific role is to identify behavioral vulnerabilities while three sibling agents handle temporal, resonant, and dependency vulnerabilities. Emphasize that it's generating pre-mortem failure narratives for emergent risks arising from how agents behave, adapt, and interact strategically.

### 2. Definitions (~125 words)

Define "behavioral vulnerabilities" in multi-agentic systems. These are emergent risks arising from:

- Conflicting optimization goals between agents
- Adversarial or game-theoretic dynamics
- Learned behaviors that create unintended system-level patterns
- Herding, mimicry, or coordination behaviors
- Incentive misalignment leading to collective failure
- Emergent strategies not designed into individual agents
- Adaptive behaviors that destabilize the system
- Goal-seeking that produces perverse outcomes
- Moral hazards and adverse selections

Make clear these are NOT individual agent bugs or single-agent misbehavior, but emergent behavioral patterns from agent interactions and strategic dynamics.

### 3. Success Criteria (~125 words)

Articulate what makes a behavioral vulnerability story valuable:

- **Non-obvious**: Not immediately apparent from individual agent designs
- **Plausible**: Could realistically emerge from agent incentives/goals
- **Specific**: Tied to concrete behavioral mechanisms, not generic
- **Emergent**: Arises from multi-agent strategic interaction, not single-agent failure
- **Actionable**: Points to testable scenarios or design considerations
- **Narrative**: Tells a story of how behavioral patterns evolve into failure

### 4. Anti-patterns (~125 words)

Specify what to avoid:

- Generic "agent made bad decision" narratives
- Single-agent misbehavior without emergence
- Bugs or errors rather than behavioral dynamics
- Surface-level observations lacking behavioral mechanism
- Vulnerabilities that could be fixed by changing one agent
- Stories that don't explain the strategic or adaptive dynamics
- Anthropomorphizing without grounding in actual agent logic
- Moral judgments about agent behavior rather than analytical description

### 5. Historical Examples (~250 words)

Provide 5-6 cross-disciplinary examples of behavioral vulnerabilities:

**Tragedy of the Commons (recurring)**: Individual farmers rationally overgraze shared pasture, each gaining benefit while externalizing costs. Collectively rational individual decisions destroy the shared resource. Classic game-theoretic failure where local optimization creates global collapse.

**2008 Financial Crisis**: Banks individually optimized for short-term profits through subprime lending, each assuming others would be conservative. Herding behavior and misaligned incentives (bonuses for volume, not quality) created systemic risk. No single bank caused the crisis, but collective behavior patterns amplified into global collapse.

**Traffic Congestion Paradox (Braess's Paradox)**: Individual drivers choosing optimal routes create worse outcomes for everyone. Adding roads can increase congestion because individual route optimization doesn't account for collective effects. Emerged from non-cooperative game dynamics.

**Cobra Effect (British India, 1900s)**: British government offered bounty for dead cobras to reduce snake population. People began breeding cobras for income. When program ended, breeders released snakes, worsening problem. Incentive created perverse goal-seeking behavior.

**Flash Crash Arms Race (2010s)**: High-frequency trading algorithms competing for speed advantage, each optimizing latency. Collective behavior created market instability through feedback loops and adversarial dynamics none were designed for. Arms race emergent from individual optimization.

**Goodhart's Law in Soviet Manufacturing**: Factories optimized for metrics (nail production by weight) rather than true objectives (useful nails). Produced heavy, useless nails. Individual agents gaming metrics created system-level dysfunction through goal misalignment.

### 6. System Context (~75 words)

Provide a template for system input: "You will receive a description of a multi-agentic system including: agent types and roles, objectives and reward functions, learning/adaptation mechanisms, information available to each agent, strategic constraints, and interaction patterns. Analyze how behavioral dynamics in THIS SPECIFIC SYSTEM could create emergent vulnerabilities."

### 7. Guiding Questions (~175 words)

Include questions that prompt deep behavioral analysis:

**Game-Theoretic Questions**:

- What are each agent's optimization goals and how might they conflict?
- What game-theoretic dynamics exist between agents? (cooperation, competition, adversarial)
- Where might individually rational behaviors create collectively irrational outcomes?
- What Nash equilibria exist, and are they socially optimal?

**Incentive Questions**:

- How do agents respond to incentive structures, and where might this create perverse outcomes?
- Where might agents optimize for proxies rather than true objectives?
- What moral hazards or adverse selections could emerge?
- Where do reward functions misalign with system objectives?

**Adaptation Questions**:

- How do agents adapt or learn from each other's behaviors?
- What strategies might agents evolve that weren't designed into them?
- Where might agents "game" the system in unexpected ways?
- What herding or mimicry behaviors could emerge?

**Emergent Strategy Questions**:

- Where do agents make assumptions about other agents' behaviors?
- How might goal-seeking behavior create unintended side effects?
- What behavioral feedback loops could amplify small differences?
- What happens when agents compete for scarce resources?

### 8. Emergent Emphasis (~75 words)

Reinforce that behavioral vulnerabilities must be emergent properties of the multi-agent system. A single agent making poor decisions is not emergent. Multiple agents whose behavioral interactions create collective patterns, strategic dynamics, or adaptive feedback loops that wouldn't exist with any single agent IS emergent. The vulnerability should arise from the INTERACTION of agent behaviors, goals, and adaptations, not from individual agent failures.

### 9. Output Format (~125 words)

Specify the output structure for each vulnerability story:

**Title**: Concise name for the vulnerability

**Behavioral Pattern Type**: Primary classification [game_theoretic|incentive_misalignment|adaptive_learning|herding|adversarial]

**Behavioral Mechanism**: 2-3 sentences on the specific agent behaviors and strategic dynamics

**Narrative (200-300 words)**: Pre-mortem story describing how the failure unfolds, including:

- Initial agent behaviors and goals
- Strategic interactions and adaptations
- Behavioral feedback loops or escalations
- Tipping point where collective behavior becomes problematic
- Final failure state

**Key Behavioral Factors**: Bulleted list of specific agent behaviors and incentives

**Behavioral Impact Analysis**: Quantify the scope and consequences - how many agents affected, strategic implications for system objectives, estimated degradation in system performance or outcomes, and which stakeholder groups bear the consequences

**Emergence Explanation**: Why this is emergent (couldn't occur with single agent)

Generate exactly 5 distinct behavioral vulnerability stories.

## Instructions for Prompt Generation

Create a prompt that incorporates all nine sections above in a clear, actionable format. Use professional but direct language. Keep total length between 800-1200 words. Ensure the prompt will produce consistent, high-quality behavioral vulnerability narratives for any multi-agentic system description provided.
