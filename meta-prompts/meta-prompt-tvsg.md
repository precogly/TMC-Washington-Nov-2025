# Meta-Prompt: Temporal Vulnerabilities Stories Generator (TVSG)

## Objective

Generate a comprehensive prompt (800-1200 words) for an AI agent that will analyze multi-agentic systems and create pre-mortem narrative stories about temporal emergent vulnerabilities - risks that arise from timing, sequencing, synchronization, or temporal coordination issues between agents.

## Target Prompt Structure

### 1. Role & Context (~75 words)

Establish that this agent is part of a 4-agent vulnerability analysis pipeline. Its specific role is to identify temporal vulnerabilities while three sibling agents handle resonant, behavioral, and dependency vulnerabilities. Emphasize that it's generating pre-mortem failure narratives for emergent risks arising from timing mismatches, coordination failures, phase relationships, and temporal dynamics between agents.

### 2. Definitions (~125 words)

Define "temporal vulnerabilities" in multi-agentic systems. These are emergent risks arising from:

- Timing mismatches between agents operating on different time scales
- Race conditions and synchronization failures at system level
- Cascade effects from sequential timing dependencies
- Clock skew or temporal coordination issues
- Phase-locking or oscillation problems
- Delayed feedback loops causing instability
- Time-of-check to time-of-use vulnerabilities at system scale
- Temporal ordering assumptions that break under load

Make clear these are NOT single-agent timing bugs, but emergent temporal patterns from agent interactions. Focus on coordination failures, timing conflicts, and temporal cascades that arise from multi-agent dynamics.

### 3. Success Criteria (~125 words)

Articulate what makes a temporal vulnerability story valuable:

- **Non-obvious**: Not immediately apparent from system design
- **Plausible**: Could realistically occur given agent architectures
- **Specific**: Tied to concrete temporal mechanisms, not generic
- **Emergent**: Arises from multi-agent interaction, not single-agent failure
- **Actionable**: Points to testable scenarios or design considerations
- **Narrative**: Tells a story of how the failure unfolds over time

### 4. Anti-patterns (~125 words)

Specify what to avoid:

- Generic "system was slow" narratives
- Single-agent timeout failures
- Simple latency issues without emergence
- Surface-level observations lacking temporal mechanism
- Vulnerabilities that would be caught by basic testing
- Stories that don't explain the temporal cascade
- Overuse of buzzwords without concrete sequences
- **Synchronized amplification**: When all agents act simultaneously causing overload (that's resonant domain) vs. timing coordination failures or mismatches (temporal domain)

### 5. Historical Examples (~250 words)

Provide 5-6 examples of temporal vulnerabilities from multiple disciplines:

**Ariane 5 Flight 501 (1996)**: Rocket exploded 37 seconds after launch due to timing issue. Inertial reference system reused from Ariane 4 couldn't process velocity data fast enough for faster Ariane 5. Software assumed it had time to complete conversion before next data arrived. Timing assumption broke, system crashed, rocket destroyed. Temporal mismatch between agent speeds ($370M loss).

**Mars Climate Orbiter (1999)**: Navigation team sent trajectory corrections in pound-seconds while spacecraft expected newton-seconds. Commands accumulated over 9 months. No single command was wrong, but temporal accumulation of unit mismatch caused spacecraft to enter atmosphere at wrong altitude and burn up ($327M loss). Slow temporal cascade from repeated small errors.

**Therac-25 Radiation Overdoses (1985-1987)**: Medical linear accelerator had race condition between operator interface and radiation control. Fast operators could change settings faster than safety interlocks updated. Timing window allowed lethal radiation doses. Six patients injured/killed. Temporal ordering vulnerability from different agent speeds (human vs. machine).

**Knight Capital Trading Glitch (2012)**: Old software activated by deployment timing error executed at market speed (milliseconds) while risk systems operated on minute-scale updates. Fast trading agent overwhelmed slow monitoring agent. Temporal mismatch between trading execution (microseconds) and risk detection (minutes) caused $440M loss in 45 minutes.

**Nest Thermostat "Cold Houses" (2016)**: Software update caused Wi-Fi reconnection issues. Battery drain faster than recharge rate during failed reconnections. Temporal feedback loop: disconnection → reconnection attempt → battery drain → system shutdown → restart → repeat. Thousands of homes lost heating. Different time scales (battery hours vs. reconnection seconds) created unstable oscillation.

**Air France 447 (2009)**: Pitot tube icing caused temporary airspeed sensor failure. Autopilot disengaged, control transferred to pilots. Pilots received conflicting speed readings from different sensors with different update rates. Temporal confusion from sensors operating on different time scales and pilots having seconds to interpret contradictory data streams. 228 deaths.

### 6. System Context (~75 words)

Provide a template for system input: "You will receive a description of a multi-agentic system including: agent types and roles, communication patterns, agent protocols, decision-making frequencies, feedback loops, temporal constraints, and coordination mechanisms. Analyze how temporal factors in THIS SPECIFIC SYSTEM could create emergent vulnerabilities."

### 7. Guiding Questions (~175 words)

Include questions that prompt deep temporal analysis:

**Time Scale Questions:**

- What happens when agents operate on different time scales? (microseconds vs. seconds vs. minutes)
- How do feedback loops interact across different temporal frequencies?
- What happens when fast agents overwhelm slow agents?
- Where do agents make assumptions about response times or latency?

**Synchronization Questions:**

- Where might race conditions occur at the system level (not code level)?
- What temporal coordination assumptions could break under load or stress?
- What happens if messages arrive out of expected order?
- Where do agents assume synchronous operations that are actually asynchronous?

**Ordering Questions:**

- What cascades occur if one agent's output arrives later than expected?
- What temporal ordering assumptions could break?
- Where might temporal ordering create unexpected dependencies?
- How do agents handle staleness or temporal uncertainty in information?

**Feedback Timing Questions:**

- What oscillations or resonances could emerge from timing patterns?
- Where might delayed feedback loops cause instability?
- What happens when correction mechanisms operate slower than problem evolution?
- Where do temporal mismatches between monitoring and action create blind spots?

### 8. Emergent Emphasis (~75 words)

Reinforce that temporal vulnerabilities must be emergent properties of the multi-agent system. A single agent being slow is not emergent. Multiple agents creating a temporal cascade, oscillation, or synchronization failure that wouldn't exist with any single agent IS emergent. The vulnerability should arise from the INTERACTION of temporal behaviors, not from individual timing failures. Focus on how different time scales, coordination requirements, and temporal dynamics interact across agents.

### 9. Output Format (~125 words)

Specify the output structure for each vulnerability story:

**Title**: Concise name for the vulnerability

**Temporal Pattern Type**: Classification [race_condition|phase_lock|oscillation|feedback_delay|synchronization_failure|timing_cascade]

**Temporal Mechanism**: 2-3 sentences on the specific timing/sequencing issue

**Narrative (200-300 words)**: Pre-mortem story describing how the failure unfolds, including:

- Initial conditions and temporal assumptions
- Temporal cascade sequence
- Agent interactions over time
- Tipping point or critical moment
- Final failure state

**Key Temporal Factors**: Bulleted list of specific timing elements and time scales involved

**Temporal Impact Analysis**: Quantify the temporal scope - critical time scales involved and their mismatches (microseconds to hours), cascade speed (how fast failure propagates), duration of instability or oscillation, number of agents operating on conflicting time scales, and coordination breakdown timeline

**Emergence Explanation**: Why this is emergent (couldn't occur with single agent)

Generate exactly 5 distinct temporal vulnerability stories.

## Instructions for Prompt Generation

Create a prompt that incorporates all nine sections above in a clear, actionable format. Use professional but direct language. Keep total length between 800-1200 words. Ensure the prompt will produce consistent, high-quality temporal vulnerability narratives for any multi-agentic system description provided.
