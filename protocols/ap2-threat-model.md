# AP2 Protocol Threat Modeling Reference Document

## Protocol Overview

The Agent Payments Protocol (AP2) is an open protocol that enables AI agents to perform financial transactions on behalf of users or other agents. AP2 operates as an extension layer on top of the Agent2Agent (A2A) protocol and Model Context Protocol (MCP), introducing payment-specific security mechanisms.

## Core Security Architecture

### Mandate System

AP2 implements a three-tier mandate system using cryptographically signed Verifiable Credentials (VCs):

#### 1. Intent Mandate
- **Purpose**: Grants agent authority for transactions in human-not-present scenarios
- **Security Properties**: 
  - Cryptographically signed by user's private key
  - Contains constraints: price ceilings, merchant allowlists, time windows, item categories
  - Includes TTL (Time To Live) for temporal restrictions
  - Contains NLP prompt playback for intent verification
  - Non-repudiable authorization record

#### 2. Cart Mandate  
- **Purpose**: Final authorization for specific transaction in human-present scenarios
- **Security Properties**:
  - References Intent Mandate via cryptographic linking
  - Contains exact transaction details (items, prices, quantities)
  - Includes payer/payee DIDs (Decentralized Identifiers)
  - Tokenized payment method (no raw payment data)
  - Risk signals: IMEI, location, device fingerprint
  - User's cryptographic signature provides non-repudiation

#### 3. Payment Mandate
- **Purpose**: Communication with payment networks and issuers
- **Security Properties**:
  - Derived from Cart/Intent Mandates
  - Signals human-present/not-present status
  - Contains agent identifier
  - Separate from user authentication credentials
  - Payment network specific formatting

### Cryptographic Specifications

- **Signature Algorithm**: ECDSA (Elliptic Curve Digital Signature Algorithm)
- **Data Format**: JSON-LD objects with embedded signatures
- **Key Management**: Hardware-backed key storage (e.g., Android DPC, hardware security modules)
- **Verification**: Public key chains with DID resolution
- **Mandate Chaining**: Each mandate cryptographically references previous mandates in chain

## Trust Boundaries

### Agent-to-User Boundary
- User signs mandates with private key
- Agent cannot modify signed mandates
- Agent operates within mandate constraints
- User retains revocation capability

### Agent-to-Merchant Boundary  
- Merchant verifies mandate signatures
- Merchant validates mandate constraints
- Agent identity included in all communications
- Merchant maintains audit logs

### Agent-to-Payment-Processor Boundary
- Payment processor receives Payment Mandate only
- No direct access to user payment credentials
- Processor validates agent authorization
- Risk scoring based on agent reputation

## Transaction Flows and Attack Surfaces

### Human-Present Flow
1. User initiates request → Agent creates Intent Mandate
2. Agent negotiates with merchant → Merchant provides cart
3. User reviews cart → User signs Cart Mandate
4. Agent submits to merchant → Merchant processes payment

**Attack Surface**: 
- Mandate modification between signing and submission
- Cart substitution attacks
- Session hijacking between mandate creation
- Man-in-the-middle on agent-merchant channel

### Human-Not-Present Flow  
1. User pre-signs Intent Mandate with constraints
2. Agent monitors for trigger conditions
3. Agent automatically generates Cart Mandate when conditions met
4. Agent executes transaction without user interaction

**Attack Surface**:
- Constraint bypass vulnerabilities
- Time-of-check to time-of-use (TOCTOU) attacks
- Agent compromise leading to mandate misuse
- Trigger condition manipulation

## Identified Threat Vectors

### Mandate-Related Threats
- **Mandate Spoofing**: Forging or cloning valid mandates
- **Mandate Replay**: Reusing expired or completed mandates  
- **Constraint Violation**: Bypassing price, merchant, or time restrictions
- **Signature Stripping**: Removing or corrupting cryptographic signatures
- **Reference Chain Breaking**: Disrupting mandate linkage

### Agent-Related Threats
- **Agent Impersonation**: Malicious agent claiming legitimate identity
- **Agent Compromise**: Hijacked agent with valid credentials
- **Prompt Injection**: Manipulating agent via crafted inputs to generate unauthorized mandates
- **Memory Poisoning**: Corrupting agent's context or embeddings to influence decisions
- **Model Poisoning**: Training data manipulation affecting agent behavior

### System-Level Threats
- **Double Spending**: Using same mandate for multiple transactions
- **Race Conditions**: Exploiting timing gaps in mandate validation
- **Delegation Chain Attacks**: Exploiting multi-level agent delegations
- **Cross-Protocol Attacks**: Exploiting AP2/A2A/MCP interaction points
- **Audit Trail Tampering**: Modifying or deleting transaction logs

## Payment Method Specifics

### Traditional Payment Rails (Cards, Bank Transfers)
- Tokenization required for card data
- PCI-DSS compliance boundaries
- Real-time authorization with existing networks
- Chargeback and dispute mechanisms

### Cryptocurrency/Stablecoin (x402 Extension)
- On-chain transaction finality
- Smart contract interactions
- Gas fee considerations
- Bridge protocol vulnerabilities
- Cross-chain transaction risks

## Security Controls and Mitigations

### Cryptographic Controls
- Hardware-backed key generation and storage
- Certificate pinning for agent communications
- Mandate expiration enforcement
- Signature verification at each hop
- Secure random number generation for nonces

### Operational Controls  
- Rate limiting per agent/user
- Anomaly detection on spending patterns
- Reputation scoring for agents
- Audit log immutability
- Incident response procedures

### Protocol-Level Controls
- Principle of least privilege in mandates
- Mandatory constraint validation
- Multi-party verification for high-value transactions
- Rollback mechanisms for disputed transactions
- Version control and backward compatibility

## Integration Points Requiring Security Review

### With Existing Payment Infrastructure
- API authentication mechanisms
- Network segmentation requirements  
- Compliance with regional regulations
- Legacy system compatibility
- Error handling and fallback procedures

### With Agent Frameworks
- Agent authentication and enrollment
- Secure credential storage
- Runtime security boundaries
- Resource consumption limits
- Sandboxing and isolation

## Compliance and Regulatory Considerations

### Financial Regulations
- PCI-DSS for card data handling
- PSD2 Strong Customer Authentication (SCA)
- AML/KYC requirements
- GDPR for personal data
- Regional payment regulations

### Agent-Specific Regulations
- Liability allocation frameworks
- Agent accountability standards
- Automated decision-making regulations
- Consumer protection requirements
- Cross-border transaction rules

## Known Implementation Vulnerabilities

### Reference Implementation Issues
- Python samples use JSON-RPC without authentication
- No rate limiting in example code
- Simplified key management in demos
- Missing input validation in some flows
- Insufficient error handling

### Production Considerations
- Scalability of signature verification
- Latency impact of mandate validation
- Storage requirements for audit trails
- Network partition handling
- Disaster recovery procedures

## Testing and Validation Requirements

### Security Testing
- Fuzzing mandate parsers
- Cryptographic implementation review
- Side-channel analysis
- Penetration testing of integration points
- Red team exercises on agent compromise scenarios

### Compliance Testing
- Payment card industry standards
- Regulatory requirement validation
- Privacy impact assessments
- Cross-border transaction testing
- Dispute resolution procedures

## Threat Modeling Inputs

### Assets to Protect
- User payment credentials
- Mandate signing keys
- Transaction integrity
- Audit trail completeness
- Agent reputation data

### Threat Actors
- Malicious agents
- Compromised merchants
- External attackers
- Insider threats
- Nation-state actors (for high-value targets)

### Attack Motivations
- Financial theft
- Service disruption  
- Data harvesting
- Reputation damage
- Regulatory non-compliance

## Risk Assessment Framework

### High-Risk Scenarios
- Autonomous high-value transactions
- Cross-border payments
- Multi-agent coordination
- Recurring payment authorizations
- Emergency transaction overrides

### Medium-Risk Scenarios
- Standard e-commerce purchases
- Service subscriptions
- Micropayments
- Agent-to-agent payments
- Loyalty program interactions

### Low-Risk Scenarios
- Information queries
- Price checking
- Cart abandonment
- Failed transaction retries
- Test transactions

## Monitoring and Detection Requirements

### Real-Time Monitoring
- Mandate validation failures
- Unusual spending patterns
- Agent behavior anomalies
- Network traffic patterns
- Cryptographic operation failures

### Post-Transaction Analysis
- Audit trail consistency
- Dispute patterns
- Agent reputation trends
- Merchant compliance
- Regulatory reporting

## Incident Response Considerations

### Immediate Response
- Mandate revocation mechanisms
- Agent suspension procedures
- Transaction rollback capabilities
- User notification systems
- Evidence preservation

### Investigation Requirements
- Cryptographic proof validation
- Audit trail reconstruction
- Agent behavior analysis
- Network forensics
- Third-party coordination

## Future Threat Considerations

### Emerging Threats
- Quantum computing impact on ECDSA
- Advanced AI manipulation techniques
- Coordinated multi-agent attacks
- Zero-day protocol vulnerabilities
- Social engineering via agents

### Protocol Evolution
- New mandate types
- Additional payment methods
- Enhanced privacy features
- Decentralized governance
- Cross-protocol standardization