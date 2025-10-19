# Meta-Prompt: Dependency Cascade Vulnerabilities Stories Generator (DCVSG)

## Objective

Generate a comprehensive prompt (800-1200 words) for an AI agent that will analyze multi-agentic systems and create pre-mortem narrative stories about dependency cascade emergent vulnerabilities - risks that arise when failures propagate sequentially through dependency relationships between agents, causing cascading failures across the system.

## Target Prompt Structure

### 1. Role & Context (~75 words)

Establish that this agent is part of a 4-agent vulnerability analysis pipeline. Its specific role is to identify dependency cascade vulnerabilities while three sibling agents handle temporal, resonant, and behavioral vulnerabilities. Emphasize that it's generating pre-mortem failure narratives for emergent risks where failures propagate through "depends on" relationships, often crossing organizational and technical boundaries. Focus on systemic vulnerabilities from dependency structures, not malicious exploitation scenarios.

### 2. Definitions (~125 words)

Define "dependency cascade vulnerabilities" in multi-agentic systems. These are emergent risks arising from:

- Sequential failure propagation along dependency chains (A→B→C)
- Single points of failure with high fan-out to multiple dependents
- Circular dependencies creating recovery deadlocks
- Transitive dependencies creating hidden risk chains
- Cross-boundary dependencies increasing coordination complexity
- Upstream failures cascading to downstream dependents
- Shared infrastructure dependencies creating correlated failures
- Trust chain failures invalidating downstream relationships

Make clear these involve SEQUENTIAL propagation (not simultaneous failure). The key question: "What do we depend on that can break us, and what depends on us that we can break?" Failures flow along explicit dependency arrows in the system architecture.

### 3. Success Criteria (~125 words)

Articulate what makes a dependency cascade vulnerability story valuable:

- **Non-obvious**: Hidden transitive dependencies or unexpected cascade paths
- **Plausible**: Could realistically propagate through the dependency chain
- **Specific**: Tied to concrete dependency relationships with clear arrows (A→B→C)
- **Emergent**: Cascade wouldn't occur with single agent; requires chain of dependencies
- **Actionable**: Points to specific dependency relationships to harden or eliminate
- **Narrative**: Tells a sequential story of how failure propagates hop-by-hop through the chain

### 4. Anti-patterns (~125 words)

Specify what to avoid:

- Simultaneous failures without clear dependency relationships
- Generic "service went down" without tracing propagation path
- Single-agent failures without downstream cascade
- Vague dependency relationships (be specific: "A depends on B for X")
- Ignoring recovery coordination complexity
- Missing the transitive dependencies (stopping at direct dependencies)
- Assuming failures are immediately detected (propagation often happens before detection)
- Forgetting cross-organizational boundary complexity
- Focusing on malicious exploitation rather than systemic vulnerability

### 5. Historical Examples (~250 words)

Provide 5-6 cross-disciplinary examples of dependency cascade vulnerabilities:

**AWS S3 Outage (2017)**: Single typo in command during debugging removed more S3 servers than intended. S3 status dashboard depended on S3 for storage, so status page couldn't report the outage. Billing system depended on S3, breaking cost tracking. Thousands of services depending on S3 failed sequentially: A (S3) → B (status page) → C (billing) → D-Z (customer services). Four-hour cascade affecting major internet services.

**2003 Northeast Blackout**: Ohio power line sagged into tree, triggering local failure. Monitoring system was down (unnoticed), preventing operators from seeing cascade forming. FirstEnergy's failure propagated to Michigan → Pennsylvania → New York → Ontario through grid dependencies. 50 million people, 8 states, cascade took 2 hours. Sequential propagation: local fault → regional grid → interconnect → eastern seaboard.

**Knight Capital Trading Loss (2012)**: Deployment of new software failed to complete on 8 servers. Old software on those servers executed test orders as live trades. Risk management system depended on correct order flagging (missing), allowing $7B in erroneous trades. Downstream: order execution → risk checks (failed) → market impact → liquidity crisis → $440M loss in 45 minutes. Chain of failed dependencies in trading infrastructure.

**Bangladesh Bank Heist (2016)**: Not an attack scenario but dependency cascade - printer failure prevented notification of fraudulent SWIFT transfers. Bank depended on printer alerts for transaction monitoring, monitoring depended on timely notification, recovery depended on quick detection. Printer failure (A) → alert system blind (B) → monitoring delayed (C) → $81M stolen before cascade detected. Infrastructure dependency created vulnerability window.

**Target Canada Supply Chain Collapse (2013-2015)**: ERP system had data quality issues. Inventory management depended on ERP accuracy. Store operations depended on inventory data. Customer experience depended on product availability. Cascade: bad data → inventory chaos → empty shelves → customer exodus → $2B loss and shutdown. Sequential dependency failure across retail operations.

**Let's Encrypt Certificate Revocation (2020)**: Bug in Let's Encrypt certificate authority affected 3 million certificates. Millions of websites depended on these certificates for HTTPS. User authentication depended on HTTPS. E-commerce depended on user trust. Could have cascaded: CA → certificates → websites → user access → business operations. Avoided through careful coordination, but showed transitive dependency risk.

### 6. System Context (~75 words)

Provide a template for system input: "You will receive a description of a multi-agentic system including: agent types and roles, dependencies between agents (what each agent requires from others), service levels and availability requirements, communication patterns, agent protocols, organizational ownership (which agents are internal vs. external), and coordination mechanisms. Analyze how dependency relationships in THIS SPECIFIC SYSTEM could create sequential cascade failures."

### 7. Guiding Questions (~175 words)

Include questions that prompt deep dependency cascade analysis:

**Direct Dependency Questions**:

- What does each agent depend on to function? (Map all dependencies as A→B arrows)
- What depends on each agent? (Identify downstream dependents and fan-out)
- What specific capabilities or data does each dependency provide?

**Transitive Dependency Questions**:

- What are the transitive dependencies? (A→B→C→D chains)
- Where are hidden dependencies you don't know you have?
- How deep are the longest dependency chains?

**Topology Questions**:

- Where are single points of failure with high fan-out?
- Where do circular dependencies exist? (A→B→C→A creating deadlock)
- What dependencies cross organizational boundaries? (Requiring external coordination for recovery)
- Which dependencies are on shared infrastructure? (Multiple agents depending on same provider)

**Recovery Coordination Questions**:

- How do failures propagate through the chain? (Sequential timing of cascade)
- What's the blast radius if each dependency fails? (How many downstream systems affected)
- What coordination is required to recover from cascades?
- Where do trust chains create vulnerability? (Certificate authorities, authentication systems)

### 8. Emergent Emphasis (~75 words)

Reinforce that dependency cascade vulnerabilities must be emergent properties of the multi-agent system. A single agent failing is not emergent. Multiple agents where failure propagates SEQUENTIALLY along dependency chains (A fails → then B fails because it depends on A → then C fails because it depends on B) IS emergent. The vulnerability arises from the CHAIN of dependencies, not individual dependencies. Focus on propagation paths, not individual failure points.

### 9. Output Format (~125 words)

Specify the output structure for each vulnerability story:

**Title**: Concise name for the vulnerability

**Cascade Topology**: Classification of dependency structure [linear_chain|fan_out|circular|transitive|hub_spoke]

**Dependency Chain**: 2-3 sentences mapping the specific dependency path (A→B→C→D)

**Narrative (200-300 words)**: Pre-mortem story describing how the cascade unfolds, including:

- Root cause failure (which system fails first)
- Sequential propagation (step-by-step cascade along dependency chain with timing)
- Cross-boundary moments (organizational/technical boundaries crossed)
- Coordination complexity (why recovery is hard)
- Final failure state and blast radius

**Key Dependency Factors**: Bulleted list of specific dependencies and their characteristics

**Cascade Impact Analysis**: Quantify the blast radius - number of systems/agents affected, propagation depth (how many hops in the dependency chain), number of users impacted, estimated downtime duration, and cross-boundary complexity (organizational/technical boundaries crossed)

**Emergence Explanation**: Why this is emergent (requires chain of dependencies)

Generate exactly 5 distinct dependency cascade vulnerability stories.

## Instructions for Prompt Generation

Create a prompt that incorporates all nine sections above in a clear, actionable format. Use professional but direct language. Keep total length between 800-1200 words. Ensure the prompt will produce consistent, high-quality dependency cascade vulnerability narratives that focus on SEQUENTIAL failure propagation along dependency chains for any multi-agentic system description provided. The key distinguishing characteristic: failures flow along "depends on" arrows in sequence, not occurring simultaneously. Focus on emergent systemic vulnerabilities from dependency structures, not malicious exploitation scenarios.
