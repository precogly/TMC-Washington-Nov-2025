# Meta-Prompt: Resonant Vulnerabilities Stories Generator (RVSG)

## Objective

Generate a comprehensive prompt (800-1200 words) for an AI agent that will analyze multi-agentic systems and create pre-mortem narrative stories about resonant emergent vulnerabilities - risks that arise when agents fail together rather than sequentially because they share critical properties: identical components (monoculture), synchronized timing, common thresholds, or coordinated behaviors. These shared properties, when triggered by internal conditions or environmental factors, create amplification that causes simultaneous or cascading failures.

## Target Prompt Structure

### 1. Role & Context (~75 words)

Establish that this agent is part of a 4-agent vulnerability analysis pipeline. Its specific role is to identify resonant vulnerabilities while three sibling agents handle dependency cascade, temporal, and behavioral vulnerabilities. Emphasize that it's generating pre-mortem failure narratives for emergent risks where failures AMPLIFY through alignment - whether structural (monoculture), temporal (synchronization), or behavioral (feedback loops). These vulnerabilities can occur within single systems OR across independent systems.

### 2. Definitions (~125 words)

Define "resonant vulnerabilities" in multi-agentic systems using the physics metaphor of resonance. These are emergent risks arising from:

- **Structural alignment (monoculture)**: Identical components/technologies deployed everywhere failing simultaneously
- **Temporal alignment (synchronization)**: All agents hitting thresholds or triggering events at the same moment
- **Behavioral alignment (feedback loops)**: Responses to problems making problems worse through positive feedback
- **Threshold effects**: Non-linear failures at specific boundaries (buffer limits, rate limits, capacity)
- **Amplification mechanisms**: Small inputs creating disproportionately large outputs through system structure

Make clear these involve AMPLIFICATION and ALIGNMENT (not sequential dependency propagation). The key question: "What structural, temporal, or behavioral properties create amplification when conditions align?" Failures occur simultaneously or cascade through amplification, not dependency chains.

### 3. Success Criteria (~125 words)

Articulate what makes a resonant vulnerability story valuable:

- **Non-obvious**: Hidden amplification mechanisms or surprising alignment conditions
- **Plausible**: Could realistically amplify given the system's structure
- **Scale-dependent**: Harmless at small scale but catastrophic at large scale (or vice versa with threshold effects)
- **Emergent**: Amplification wouldn't occur with isolated components; requires alignment across multiple agents
- **Actionable**: Points to specific architectural features to redesign or diversity to introduce
- **Narrative**: Tells a compelling story of how alignment conditions create amplification
- **Pattern-matched**: Clearly maps to established resonance patterns (monoculture, feedback loop, threshold, synchronization)

### 4. Anti-patterns (~125 words)

Specify what to avoid:

- **Dependency cascades**: Sequential A→B→C propagation (that's the other agent's domain)
- **Single-point failures**: One component breaking without amplification mechanism
- **Vague "at scale" claims**: Be specific about what scale property creates amplification
- **Missing amplification mechanism**: Must explain HOW small becomes large
- **Only monoculture examples**: Include feedback loops, thresholds, synchronization patterns
- **Ignoring intra-system scenarios**: Resonance works both within systems AND across independent systems
- **Linear scaling assumptions**: Resonant vulnerabilities are about NON-LINEAR effects
- **No physics grounding**: Should feel like actual resonance (frequency matching, amplitude amplification)
- **Temporal coordination failures**: When agents fail to synchronize properly (that's temporal domain) vs. successful synchronization creating amplification (resonant domain)

### 5. Historical Examples (~250 words)

Provide 5-6 cross-disciplinary examples of resonant vulnerabilities, ensuring coverage across ALL pattern types:

**Monoculture Pattern:**

**Y2K (2000)**: Two-digit date fields in millions of independent systems worldwide failing simultaneously on January 1, 2000. No dependencies between systems, but identical design flaw created synchronized global failure.

**Heartbleed (2014)**: OpenSSL vulnerability affecting 17% of all HTTPS servers globally at the same instant. Monoculture in cryptographic libraries amplified single bug into global crisis.

**Log4j (2021)**: Single logging library vulnerability in millions of applications across thousands of organizations. Structural alignment through shared component.

**Feedback Loop Pattern:**

**Bank Runs (recurring)**: Withdrawals trigger panic causing more withdrawals in positive feedback loop. Individual rational behavior amplifies into systemic crisis.

**Flash Crash (2010)**: Algorithmic selling triggered more selling, cascading through markets in 36 minutes, wiping $1 trillion in value before rebounding.

**LTCM Collapse (1998)**: Forced liquidation moved markets causing more losses requiring more liquidation. Feedback amplification destroyed a $4.6B fund.

**Threshold Effect Pattern:**

**Tacoma Narrows Bridge (1940)**: Wind oscillations hit resonant frequency causing catastrophic structural failure. Threshold crossing from stable to destructive.

**2003 Northeast Blackout**: Power grid exceeded threshold causing protective systems to cascade non-linearly, affecting 50 million people.

**I-35W Bridge Collapse (2007)**: Decades of load accumulation crossed failure threshold suddenly without warning.

**Synchronization Pattern:**

**Thundering Herd**: All clients reconnecting simultaneously after network partition overwhelming servers.

**Cache Stampede**: All application instances invalidating cache at once creating origin server overload.

**Certificate Expiration Waves**: Multiple certificates expiring on same date causing synchronized service failures.

### 6. System Context (~75 words)

Provide a template for system input: "You will receive a description of a multi-agentic system including: agent types and capabilities, architectural patterns (shared components, protocols, libraries), scale parameters (number of agents, request rates, data volumes), synchronization points (shared clocks, coordinated events), feedback mechanisms (retry logic, auto-scaling, circuit breakers), and threshold configurations (rate limits, buffer sizes, capacity limits). Analyze how ALIGNMENT PROPERTIES in THIS SPECIFIC SYSTEM could create amplification when conditions converge."

### 7. Guiding Questions (~175 words)

Include questions that prompt deep resonance analysis across all pattern types:

**Monoculture Questions:**

- What identical components/technologies are deployed across multiple/all agents?
- What single library, protocol, or standard does everything rely on?
- Where is there zero diversity in implementation?

**Feedback Loop Questions:**

- What responses to problems could make problems worse?
- Where do retry mechanisms, auto-scaling, or circuit breakers create positive feedback?
- What protective measures could themselves become attack vectors?

**Threshold Questions:**

- What numeric limits exist (buffer sizes, rate limits, connection pools)?
- What happens at exactly 100% capacity vs 99%?
- Where do gradual increases suddenly become catastrophic?

**Synchronization Questions:**

- What causes all agents to act at the same moment (time-based triggers, shared events)?
- Where could temporal alignment create simultaneous failures?
- What operations are synchronized across agents?

**Amplification Questions:**

- Where does 1 become N (fan-out patterns)?
- What architectural features amplify small failures into large ones?
- What's the amplification multiplier (2x, 10x, 100x, exponential)?

### 8. Emergent Emphasis (~75 words)

Reinforce that resonant vulnerabilities must be emergent properties of the multi-agent system arising from AMPLIFICATION THROUGH ALIGNMENT. A single agent failing is not emergent. Multiple agents failing SIMULTANEOUSLY due to shared properties (monoculture), CASCADING through feedback loops, SYNCHRONIZED by temporal alignment, or EXPLODING at thresholds IS emergent. The vulnerability arises from ALIGNMENT creating AMPLIFICATION, whether structural, temporal, or behavioral. Focus on how conditions align to amplify failures non-linearly.

### 9. Output Format (~125 words)

Specify the output structure for each vulnerability story:

**Title**: Concise name capturing the resonance pattern

**Pattern Classification**: Primary pattern type [monoculture|feedback_loop|threshold|synchronization] and secondary if applicable

**Amplification Mechanism**: 2-3 sentences explaining HOW alignment creates amplification (include estimated multiplier)

**Narrative (200-300 words)**: Pre-mortem story describing how resonance unfolds, including:

- Initial conditions and alignment properties
- Trigger event (what activates the resonance)
- Amplification cascade (how small becomes large)
- Feedback loops or threshold crossings
- Final failure state and blast radius

**Key Resonance Factors**: Bulleted list of specific alignment properties and amplification mechanisms

**Amplification Impact Analysis**: Quantify the amplification effects - threshold scale where vulnerability becomes critical (X agents, Y requests/sec, Z% capacity), amplification multiplier (1 failure → N failures), total systems affected when resonance occurs, and non-linear scaling characteristics

**Emergence Explanation**: Why this is emergent (requires alignment across multiple agents)

Generate exactly 5 distinct resonant vulnerability stories covering diverse pattern types.

## Instructions for Prompt Generation

Create a prompt that incorporates all nine sections above in a clear, actionable format. Use professional but direct language. Keep total length between 800-1200 words. Ensure the prompt will produce consistent, high-quality resonant vulnerability narratives that focus on AMPLIFICATION THROUGH ALIGNMENT for any multi-agentic system description provided. The key distinguishing characteristic: failures amplify through structural, temporal, or behavioral alignment - NOT through sequential dependency chains. Balance examples across monoculture, feedback loops, thresholds, and synchronization patterns.
