# A2A Protocol Threat Modeling Reference Document

## Protocol Overview

The Agent-to-Agent (A2A) Communication Protocol is an open standard enabling AI agents to communicate and collaborate across different platforms and frameworks. Released by Google in April 2025, it is now maintained by the Linux Foundation. The protocol enables autonomous agents built on diverse frameworks by different vendors to interact as peer entities rather than as simple tools.

## Architecture Components

### Core Entities

1. **A2A Client (Client Agent)**
   - Initiates requests to remote agents
   - Can be an application, service, or another AI agent
   - Maintains task state and handles responses
   - Responsible for agent discovery via Agent Cards

2. **A2A Server (Remote Agent)**
   - Exposes HTTP/HTTPS endpoints implementing the A2A protocol
   - Processes incoming tasks and returns results
   - Publishes Agent Card for capability advertisement
   - May support push notifications for long-running tasks

3. **Agent Cards**
   - JSON metadata files typically served at `/.well-known/agent.json`
   - Contains: agent identity, capabilities, endpoint URLs, authentication requirements, supported modalities
   - Publicly accessible for discovery purposes
   - May support authenticated extended cards with additional capabilities

## Transport Layer Specifications

### Supported Protocols

1. **Primary: JSON-RPC 2.0 over HTTP(S)**
   - Content-Type: `application/json`
   - Standard JSON-RPC request/response format
   - Synchronous request-response pattern
   - HTTP status codes for transport-level errors

2. **Streaming: Server-Sent Events (SSE)**
   - Content-Type: `text/event-stream`
   - Used for long-running tasks and real-time updates
   - Unidirectional server-to-client communication
   - Each SSE data field contains complete JSON-RPC Response objects

3. **Asynchronous: Push Notifications**
   - Webhook-based callbacks to client-supplied endpoints
   - Optional capability (not all agents support)
   - Used for very long-running tasks or disconnection scenarios

### Message Structure

**JSON-RPC Request Components:**
- `jsonrpc`: Must be exactly "2.0"
- `method`: Method name (e.g., "message/send", "tasks/get")
- `params`: Structured parameters (typically objects)
- `id`: Correlation identifier for matching responses

**JSON-RPC Response Components:**
- `jsonrpc`: Version identifier "2.0"
- `id`: Must match request ID
- `result` OR `error`: Mutually exclusive success/failure indicators

## Authentication and Authorization

### Supported Mechanisms
- HTTP Basic Authentication
- Bearer Token (OAuth 2.0)
- API Keys (via headers or query parameters)
- Custom authentication schemes via HTTP headers
- No authentication (for public agents)

### Security Considerations
- Authentication handled at HTTP transport layer, not within JSON-RPC payloads
- Agent Cards may expose authentication requirements
- Extended Agent Cards may require authentication to access
- No built-in encryption beyond HTTPS transport security
- No standardized authorization model for task-level permissions

## Task Lifecycle and State Management

### Task States
- `pending`: Initial state after creation
- `processing`: Agent actively working on task
- `completed`: Task successfully finished with artifacts
- `failed`: Task encountered unrecoverable error
- `canceled`: Task terminated by client request
- `rejected`: Task refused by agent

### Task Management Operations
- Create new tasks with unique task IDs
- Query task status and retrieve results
- Cancel running tasks
- Subscribe to task updates via streaming
- Configure push notifications for task events

### Long-Running Task Considerations
- Tasks may run for hours or days
- Support for human-in-the-loop interactions
- State persistence requirements on both client and server
- Disconnection/reconnection handling via task IDs

## Data Exchange Patterns

### Message Parts
- Messages contain "parts" with specified content types
- Support for multimodal content (text, images, audio, video)
- File references rather than inline data for large content
- Negotiation of supported formats between agents

### Artifacts
- Output products of completed tasks
- Can include generated content, analysis results, or processed data
- May contain references to external resources
- Persistence and cleanup policies undefined by protocol

## Attack Surface Analysis

### Network Layer
- **Agent Discovery**
  - Agent Cards served over HTTP(S) - potential for spoofing
  - No built-in verification of Agent Card authenticity
  - DNS hijacking could redirect to malicious agents

- **Transport Security**
  - Relies entirely on HTTPS for confidentiality and integrity
  - No additional message-level encryption or signing
  - Vulnerable to MitM if TLS improperly configured

### Application Layer
- **JSON-RPC Parsing**
  - Standard JSON parsing vulnerabilities
  - Large payload DoS potential
  - Malformed JSON-RPC structure handling

- **Task Management**
  - Task ID prediction/enumeration possibilities
  - No rate limiting specified in protocol
  - Resource exhaustion through multiple long-running tasks

### Trust Boundaries
- **Agent-to-Agent Trust**
  - No built-in agent identity verification beyond transport auth
  - Opaque execution model prevents inspection of agent logic
  - No mechanism for capability verification beyond self-declaration

- **Data Handling**
  - No data classification or sensitivity labeling
  - Artifacts may contain sensitive information
  - No specified data retention or deletion policies

## Integration Points

### External Dependencies
- HTTP/HTTPS infrastructure
- DNS for agent discovery
- External authentication providers (OAuth, etc.)
- Webhook endpoints for push notifications
- File storage systems for large artifacts

### Multi-Agent Scenarios
- Potential for cascading agent calls
- No built-in loop detection or depth limiting
- Trust propagation across agent chains undefined
- Shared state management across multiple agents

## Protocol-Specific Risks

### Availability Risks
- No specified timeout values for operations
- Long-running tasks may consume resources indefinitely
- SSE connections may be held open indefinitely
- No built-in circuit breaker patterns

### Integrity Risks
- No message signing or verification
- Replay attack potential without nonce/timestamp validation
- No audit trail requirements
- Task results may be modified in transit (if not using HTTPS)

### Confidentiality Risks
- Agent Cards expose capability information publicly
- No field-level encryption for sensitive parameters
- Artifacts may leak through improper access controls
- Cross-agent information disclosure through error messages

## Error Handling

### Standard Error Codes
- JSON-RPC standard errors (-32700 to -32603)
- A2A custom errors (-32000 to -32099)
- Implementation-specific error codes permitted
- Error data field may contain sensitive information

### Error Response Considerations
- Detailed error messages may reveal system internals
- Stack traces or debug information in error responses
- No standardized error sanitization requirements

## Compliance and Governance Considerations

### Data Privacy
- No built-in GDPR/privacy compliance mechanisms
- Cross-border data transfer implications
- No data residency controls
- User consent management undefined

### Audit and Monitoring
- No standardized logging format
- No mandatory audit trail generation
- Tracing context propagation optional
- No built-in anomaly detection mechanisms

## Implementation Recommendations for Threat Mitigation

1. **Always use HTTPS with proper TLS configuration**
2. **Implement robust authentication and validate Agent Cards independently**
3. **Apply rate limiting and resource quotas for task creation**
4. **Validate and sanitize all JSON-RPC inputs and outputs**
5. **Implement timeout mechanisms for all operations**
6. **Monitor for unusual patterns in agent-to-agent communications**
7. **Establish trust relationships and agent allowlists**
8. **Implement circuit breakers for cascading agent calls**
9. **Sanitize error messages to prevent information disclosure**
10. **Log all agent interactions for security monitoring**

## Version and Update Considerations

- Protocol version: Currently draft/v0.2.6 (as of October 2025)
- No automatic version negotiation mechanism
- Backward compatibility not guaranteed across versions
- No standardized deprecation or migration patterns