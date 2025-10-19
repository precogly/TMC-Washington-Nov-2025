# EPIC: Book Travel to TMC Conference 2027

**Epic ID:** AGENT-2027  
**Reporter:** Sarah Chen (User)  
**Assignee:** PersonalAssistantAgent v3.2  
**Priority:** High  
**Status:** In Progress  
**Created:** 2027-03-15  
**Target Date:** 2027-04-10 (Conference dates: 2027-05-20 to 2027-05-23)

## Epic Description

**User Request (Simple):**
> "Hey, book me tickets for TMC 2027 in San Francisco. I need flights, hotel near the venue, and register me for the conference. Budget is flexible but keep it reasonable."

**What Actually Happens Behind the Scenes:**
A cascade of 15+ agent interactions across 8 different specialized agents using 4 protocols (ANS, A2A, MCP, AP2) to coordinate discovery, communication, data access, and payments.

---

## User Stories

### STORY 1: Intent Understanding & Agent Discovery
**Story ID:** AGENT-2027-1  
**Protocol(s):** MCP, ANS  
**Agent(s):** PersonalAssistantAgent → ANS Registry

**As a** Personal Assistant Agent  
**I want to** parse the user's request and discover specialized agents  
**So that** I can delegate tasks to the right services

**Acceptance Criteria:**
- [x] Parse natural language request using LLM via MCP
- [x] Extract entities: event="TMC 2027", location="San Francisco", tasks=["flights", "hotel", "registration"]
- [x] Query ANS Registry for agents with capabilities: `travel.booking`, `event.registration`, `payment.processing`
- [x] Verify agent certificates and DIDs
- [x] Retrieve Agent Cards for discovered agents

**Technical Implementation:**
```
1. MCP Connection to LLM Service:
   - Host: PersonalAssistantAgent
   - Server: AnthropicLLMService
   - Tool: natural_language_understanding
   
2. ANS Query:
   - Query: agents.capability.travel.booking
   - Returns: FlightBookingAgent (did:agent:flight-booking-global)
            HotelReservationAgent (did:agent:hotel-res-marriott)
            EventRegistrationAgent (did:agent:event-reg-tmc)
   
3. Certificate Verification via ANS CA
```

**Dependencies:** None  
**Estimate:** 2 story points

---

### STORY 2: Flight Search & Availability Check
**Story ID:** AGENT-2027-2  
**Protocol(s):** A2A, MCP  
**Agent(s):** PersonalAssistantAgent → FlightBookingAgent → AirlineAPIAgent

**As a** Personal Assistant Agent  
**I want to** request flight options from specialized flight agent  
**So that** I can present options to the user

**Acceptance Criteria:**
- [x] Establish A2A connection with FlightBookingAgent
- [x] Send task request with parameters (origin, destination, dates, preferences)
- [x] FlightBookingAgent queries multiple airline APIs via MCP
- [x] Receive streaming results via SSE
- [x] Filter results based on user preferences and budget
- [x] Present top 3 options to user

**Technical Implementation:**
```
A2A Task Flow:
├─ POST /a2a/tasks (PersonalAssistant → FlightBooking)
│  ├─ Task ID: task-flight-2027-abc123
│  ├─ State: PENDING → PROCESSING
│  ├─ Parameters:
│  │  ├─ origin: "SFO/OAK/SJC" (flexible)
│  │  ├─ destination: "SFO"
│  │  ├─ departure: "2027-05-19"
│  │  ├─ return: "2027-05-24"
│  │  └─ class: "economy-premium"
│  └─ Callback: https://personal-agent.internal/callbacks/flight-results

FlightBookingAgent → MCP Connections:
├─ Server: UnitedAirlinesAPI
├─ Server: DeltaAirlinesAPI
├─ Server: AmericanAirlinesAPI
└─ Tool calls: search_flights, get_availability

A2A Response (Streaming via SSE):
├─ Event: flight_found (United, $420)
├─ Event: flight_found (Delta, $385)
├─ Event: flight_found (American, $395)
└─ Event: task_completed
```

**Dependencies:** AGENT-2027-1  
**Estimate:** 5 story points

---

### STORY 3: Hotel Search with Venue Proximity
**Story ID:** AGENT-2027-3  
**Protocol(s):** A2A, MCP  
**Agent(s):** PersonalAssistantAgent → HotelReservationAgent → VenueInformationAgent

**As a** Personal Assistant Agent  
**I want to** find hotels near the conference venue  
**So that** the user has convenient accommodation

**Acceptance Criteria:**
- [x] Query VenueInformationAgent (A2A) for TMC 2027 venue location
- [x] HotelReservationAgent searches within 1-mile radius
- [x] Access hotel booking systems via MCP
- [x] Filter by amenities (wifi, gym, breakfast)
- [x] Check real-time availability
- [x] Return 5 options with ratings and prices

**Technical Implementation:**
```
A2A Chain:
PersonalAssistant → HotelReservationAgent → VenueInformationAgent

1. Get Venue Location:
   POST /a2a/tasks to VenueInformationAgent
   Response: Moscone Center, 747 Howard St, SF 94103
   Coordinates: 37.7842° N, 122.4016° W

2. Hotel Search via MCP:
   HotelReservationAgent → MCP Servers:
   ├─ MarriottBookingSystem
   ├─ HiltonReservationAPI
   └─ IndependentHotelsNetwork
   
   Tools: search_hotels, check_availability, get_amenities
   
3. A2A Results:
   Task State: COMPLETED
   Hotels Found: 5
   ├─ Marriott Marquis (0.2 mi, $289/night, 4.5★)
   ├─ Hilton Union Square (0.5 mi, $245/night, 4.3★)
   └─ Hyatt Regency (0.3 mi, $310/night, 4.6★)
```

**Dependencies:** AGENT-2027-1  
**Estimate:** 5 story points

---

### STORY 4: Conference Registration Check
**Story ID:** AGENT-2027-4  
**Protocol(s):** A2A, MCP  
**Agent(s):** PersonalAssistantAgent → EventRegistrationAgent → TMCRegistrationSystem

**As a** Personal Assistant Agent  
**I want to** check conference registration availability and requirements  
**So that** I can register the user correctly

**Acceptance Criteria:**
- [x] Contact EventRegistrationAgent via A2A
- [x] Query TMC registration system for availability
- [x] Retrieve ticket types and pricing
- [x] Check if user qualifies for discounts (speaker, early bird, etc.)
- [x] Verify registration prerequisites (membership, etc.)
- [x] Obtain registration form requirements

**Technical Implementation:**
```
A2A Communication:
POST /a2a/tasks to EventRegistrationAgent
├─ Event: "TMC 2027"
├─ Attendee: "Sarah Chen"
└─ Query: availability, pricing, requirements

EventRegistrationAgent → MCP:
├─ Server: TMCRegistrationSystem
├─ Tools: check_availability, get_ticket_types, verify_attendee
└─ Resources: registration_form_schema

Response via A2A:
├─ Available: Yes
├─ Ticket Types:
│  ├─ General Admission: $799
│  ├─ Premium Pass: $1,299
│  └─ Speaker/Sponsor: Complimentary
├─ User Status: Regular attendee
└─ Required Info: Full name, Email, Company, Dietary restrictions
```

**Dependencies:** AGENT-2027-1  
**Estimate:** 3 story points

---

### STORY 5: User Preference Confirmation
**Story ID:** AGENT-2027-5  
**Protocol(s):** MCP  
**Agent(s):** PersonalAssistantAgent → UserProfileAgent

**As a** Personal Assistant Agent  
**I want to** retrieve user's travel preferences and history  
**So that** I can make personalized recommendations

**Acceptance Criteria:**
- [x] Access UserProfileAgent via MCP
- [x] Retrieve travel preferences (seat type, hotel star rating, dietary restrictions)
- [x] Check past booking patterns
- [x] Get loyalty program memberships
- [x] Present curated options to user
- [x] Await user confirmation on selections

**Technical Implementation:**
```
MCP Connection:
├─ Host: PersonalAssistantAgent
├─ Client: MCP Client (OAuth 2.1)
├─ Server: UserProfileAgent
└─ Scoped Permissions: profile:read, preferences:read, history:read

Tools Called:
├─ get_travel_preferences()
│  Returns: 
│  ├─ flight_seat: "aisle, premium economy"
│  ├─ hotel_stars: "4+"
│  ├─ dietary: "vegetarian"
│  └─ accessibility: "none"
│
├─ get_loyalty_programs()
│  Returns:
│  ├─ United MileagePlus: #AA123456
│  ├─ Marriott Bonvoy: #987654321
│  └─ Delta SkyMiles: #DL789012
│
└─ get_booking_history()
   Returns: Last 5 trips for pattern analysis

Human-in-the-Loop:
Present to user → Await confirmation → Capture selection
Selected: Delta flight ($385), Marriott ($289), General Pass ($799)
```

**Dependencies:** AGENT-2027-2, AGENT-2027-3, AGENT-2027-4  
**Estimate:** 3 story points

---

### STORY 6: Payment Intent & Mandate Creation
**Story ID:** AGENT-2027-6  
**Protocol(s):** AP2  
**Agent(s):** PersonalAssistantAgent → PaymentCoordinatorAgent

**As a** Personal Assistant Agent  
**I want to** initiate payment process with proper authorization  
**So that** bookings can be secured

**Acceptance Criteria:**
- [x] Create Payment Intent Mandate (signed by user)
- [x] Define payment scope and limits
- [x] Establish authorization chain
- [x] Generate mandate signatures
- [x] Store mandate for audit trail
- [x] Pass to PaymentCoordinatorAgent

**Technical Implementation:**
```
AP2 Mandate Chain:

1. Intent Mandate (IM-2027-abc):
   ├─ Issuer: Sarah Chen (DID: did:user:sarah-chen-2027)
   ├─ Recipient: PersonalAssistantAgent
   ├─ Purpose: "TMC 2027 Travel Booking"
   ├─ Max Amount: $2,500 USD
   ├─ Validity: 2027-03-15 to 2027-03-20
   ├─ Signature: [Ed25519 signature by user]
   └─ Chain: Root mandate

2. Breakdown:
   ├─ Flight: ~$400
   ├─ Hotel (5 nights): ~$1,450
   ├─ Conference: ~$800
   └─ Buffer: ~$150

A2A Handoff to PaymentCoordinatorAgent:
├─ Mandate attached
├─ Booking details included
└─ Callback endpoint for payment status
```

**Dependencies:** AGENT-2027-5  
**Estimate:** 5 story points

---

### STORY 7: Flight Booking & Payment
**Story ID:** AGENT-2027-7  
**Protocol(s):** A2A, AP2, MCP  
**Agent(s):** PaymentCoordinatorAgent → FlightBookingAgent → AirlinePaymentGateway

**As a** Payment Coordinator Agent  
**I want to** execute flight booking with authorized payment  
**So that** the flight reservation is confirmed

**Acceptance Criteria:**
- [x] Create Cart Mandate for flight booking
- [x] Send booking request to FlightBookingAgent via A2A
- [x] FlightBookingAgent reserves seat with airline
- [x] Generate Payment Mandate
- [x] Process payment via AP2-compatible gateway
- [x] Receive confirmation and ticket number
- [x] Update user and store receipt

**Technical Implementation:**
```
AP2 Cart Mandate (CM-flight-xyz):
├─ Derived from: IM-2027-abc
├─ Merchant: Delta Airlines
├─ Items: [Flight DL1234, 2027-05-19, SFO-SFO RT]
├─ Amount: $385.00 USD
├─ Signature: [Signed by PaymentCoordinatorAgent]
└─ Chain: IM-2027-abc → CM-flight-xyz

A2A Task to FlightBookingAgent:
├─ Action: hold_booking
├─ Flight: Delta DL1234
├─ Passenger: Sarah Chen
├─ Payment Mandate: CM-flight-xyz attached
└─ State: PENDING

FlightBookingAgent → MCP → DeltaBookingAPI:
├─ Tool: reserve_seat
├─ Response: Reservation #DL20270519ABC, hold for 15 min
└─ Payment required

AP2 Payment Mandate (PM-flight-final):
├─ Derived from: CM-flight-xyz
├─ Amount: $385.00 (exact match to cart)
├─ Payment Method: Credit Card (Visa ****1234)
├─ Processor: StripePaymentAgent
├─ Signature: [Multi-sig: PaymentCoordinator + StripeAgent]
├─ Verification: DID-based credential check
└─ Chain: IM-2027-abc → CM-flight-xyz → PM-flight-final

Payment Processing:
├─ AP2 → Traditional Payment Network Bridge
├─ Authorization: Approved
├─ Transaction ID: TXN-stripe-20270315-98765
└─ Audit Log: Stored with full mandate chain

A2A Callback:
├─ Task State: COMPLETED
├─ Confirmation: Flight booked
├─ Ticket Number: DL-0123456789
├─ Receipt: Attached (PDF, blockchain hash)
└─ Loyalty Points: +1,540 miles added
```

**Dependencies:** AGENT-2027-6  
**Estimate:** 8 story points

---

### STORY 8: Hotel Reservation & Payment
**Story ID:** AGENT-2027-8  
**Protocol(s):** A2A, AP2, MCP  
**Agent(s):** PaymentCoordinatorAgent → HotelReservationAgent → MarriottBookingSystem

**As a** Payment Coordinator Agent  
**I want to** complete hotel booking with secured payment  
**So that** accommodation is guaranteed

**Acceptance Criteria:**
- [x] Create Cart Mandate for hotel reservation
- [x] Book 5 nights at Marriott Marquis via A2A
- [x] Generate Payment Mandate
- [x] Process payment via AP2
- [x] Receive confirmation number
- [x] Handle loyalty program integration

**Technical Implementation:**
```
AP2 Cart Mandate (CM-hotel-xyz):
├─ Derived from: IM-2027-abc
├─ Merchant: Marriott International
├─ Items: [5 nights, King room, Marriott Marquis SF]
├─ Dates: 2027-05-19 to 2027-05-24
├─ Amount: $1,445.00 USD (incl. taxes)
└─ Signature: [Signed by PaymentCoordinatorAgent]

A2A Task Flow:
PaymentCoordinator → HotelReservationAgent
├─ Action: create_reservation
├─ Hotel: Marriott Marquis (property_id: mar_sf_marquis)
├─ Guest: Sarah Chen
├─ Room Type: King, Non-smoking
├─ Special Requests: High floor, vegetarian breakfast options
├─ Loyalty: Marriott Bonvoy #987654321
└─ Payment Mandate: CM-hotel-xyz

HotelReservationAgent → MCP → MarriottBookingSystem:
├─ Tool: create_booking
├─ Pre-authorization: $1,445.00
├─ Hold: 30 minutes
└─ Loyalty Applied: 7,225 points earned

AP2 Payment Mandate (PM-hotel-final):
├─ Amount: $1,445.00
├─ Payment Method: Credit Card (Visa ****1234)
├─ Processor: StripePaymentAgent
├─ Hotel Guarantee: Deposit charged, refundable until 2027-05-17
├─ Signature: [Multi-sig chain verified]
└─ Mandate Chain: IM → CM-hotel-xyz → PM-hotel-final

Payment Execution:
├─ Authorization: Approved
├─ Transaction: TXN-stripe-20270315-98766
├─ Receipt: Generated with blockchain verification
└─ Audit Trail: Complete mandate chain logged

A2A Response:
├─ State: COMPLETED
├─ Confirmation: Hotel reserved
├─ Confirmation Number: M-87654321-SF
├─ Check-in: 2027-05-19, 4:00 PM
├─ Check-out: 2027-05-24, 11:00 AM
└─ Mobile Key: Will be available 24h before arrival
```

**Dependencies:** AGENT-2027-6  
**Estimate:** 8 story points

---

### STORY 9: Conference Registration & Payment
**Story ID:** AGENT-2027-9  
**Protocol(s):** A2A, AP2, MCP  
**Agent(s):** PaymentCoordinatorAgent → EventRegistrationAgent → TMCRegistrationSystem

**As a** Payment Coordinator Agent  
**I want to** register user for conference with payment  
**So that** conference access is secured

**Acceptance Criteria:**
- [x] Create Cart Mandate for conference ticket
- [x] Submit registration form via A2A
- [x] Process ticket payment via AP2
- [x] Receive conference badge details
- [x] Add event to user's calendar
- [x] Download conference materials access

**Technical Implementation:**
```
AP2 Cart Mandate (CM-conf-xyz):
├─ Derived from: IM-2027-abc
├─ Merchant: TMC Conference Organization
├─ Items: [General Admission Pass, TMC 2027]
├─ Amount: $799.00 USD
└─ Signature: [Signed by PaymentCoordinatorAgent]

A2A Registration Flow:
PaymentCoordinator → EventRegistrationAgent
├─ Event: TMC 2027
├─ Ticket Type: General Admission
├─ Attendee Info:
│  ├─ Name: Sarah Chen
│  ├─ Email: sarah.chen@email.com
│  ├─ Company: Tech Innovations Inc.
│  ├─ Dietary: Vegetarian
│  └─ T-shirt: Medium
└─ Payment Mandate: CM-conf-xyz

EventRegistrationAgent → MCP → TMCRegistrationSystem:
├─ Tool: register_attendee
├─ Form Submission: Complete
├─ Ticket Allocation: Confirmed
└─ Badge Printing: Queued

AP2 Payment Mandate (PM-conf-final):
├─ Amount: $799.00
├─ Payment Method: Credit Card (Visa ****1234)
├─ Processor: StripePaymentAgent
├─ Receipt: Digital ticket + tax receipt
├─ Signature: [Multi-sig verified]
└─ Mandate Chain: IM → CM-conf-xyz → PM-conf-final

Payment & Fulfillment:
├─ Transaction: TXN-stripe-20270315-98767
├─ Status: Completed
├─ Ticket Issued: #TMC2027-A-12345
├─ QR Code: Generated for mobile check-in
└─ Welcome Email: Triggered

A2A Response:
├─ State: COMPLETED
├─ Registration: Confirmed
├─ Badge Name: Sarah Chen
├─ Access Level: General (all sessions, expo, meals)
├─ Materials: App download link, schedule PDF
└─ Calendar Event: ICS file generated
```

**Dependencies:** AGENT-2027-6  
**Estimate:** 5 story points

---

### STORY 10: Calendar Integration & Itinerary Creation
**Story ID:** AGENT-2027-10  
**Protocol(s):** MCP, A2A  
**Agent(s):** PersonalAssistantAgent → CalendarAgent → ItineraryGeneratorAgent

**As a** Personal Assistant Agent  
**I want to** add all bookings to user's calendar  
**So that** user has complete trip visibility

**Acceptance Criteria:**
- [x] Connect to CalendarAgent via MCP
- [x] Create calendar events for flights, hotel, conference
- [x] Add reminders and notifications
- [x] Generate comprehensive itinerary document
- [x] Include all confirmation numbers and contacts
- [x] Share itinerary with user

**Technical Implementation:**
```
MCP Connection to CalendarAgent:
├─ Server: GoogleCalendarAPI
├─ OAuth 2.1: User-authorized access
├─ Scoped Permission: calendar:write

Calendar Events Created:
1. Flight Outbound (2027-05-19)
   ├─ Time: 6:45 AM - 9:30 AM
   ├─ Location: SFO Airport, Terminal 2
   ├─ Confirmation: DL-0123456789
   ├─ Reminder: 24h before, 3h before
   └─ Notes: Mobile boarding pass, TSA PreCheck lane

2. Hotel Check-in (2027-05-19)
   ├─ Time: 4:00 PM
   ├─ Location: Marriott Marquis, 780 Mission St
   ├─ Confirmation: M-87654321-SF
   └─ Reminder: Check-in available via app

3. Conference Day 1 (2027-05-20)
   ├─ Time: 8:00 AM - 6:00 PM
   ├─ Location: Moscone Center
   ├─ Badge: #TMC2027-A-12345
   └─ Notes: Vegetarian meal selections marked

4-6. Conference Days 2-3 (2027-05-21 to 2027-05-23)
   [Similar entries]

7. Hotel Check-out (2027-05-24)
   ├─ Time: 11:00 AM
   └─ Reminder: 1 day before

8. Flight Return (2027-05-24)
   ├─ Time: 2:15 PM - 4:55 PM
   ├─ Confirmation: DL-0123456789
   └─ Reminder: 3h before

A2A Call to ItineraryGeneratorAgent:
├─ Input: All booking confirmations
├─ Format: PDF + Interactive web page
└─ Content: 
   ├─ Timeline view
   ├─ Confirmation numbers
   ├─ Emergency contacts
   ├─ Local information (weather, transit, restaurants)
   └─ Packing checklist

Generated Itinerary Delivered via:
├─ Email (PDF attachment)
├─ Mobile app notification
└─ Cloud storage (Google Drive)
```

**Dependencies:** AGENT-2027-7, AGENT-2027-8, AGENT-2027-9  
**Estimate:** 5 story points

---

### STORY 11: Payment Reconciliation & Receipt Generation
**Story ID:** AGENT-2027-11  
**Protocol(s):** AP2, MCP  
**Agent(s):** PaymentCoordinatorAgent → AccountingAgent → ReceiptGeneratorAgent

**As a** Payment Coordinator Agent  
**I want to** consolidate all payments and generate receipts  
**So that** user has complete financial records

**Acceptance Criteria:**
- [x] Aggregate all AP2 payment mandates
- [x] Verify mandate chain integrity
- [x] Generate itemized receipt
- [x] Store blockchain-verified records
- [x] Prepare expense report format
- [x] Send to user and accounting system

**Technical Implementation:**
```
AP2 Mandate Chain Verification:
Root: IM-2027-abc (Intent Mandate)
├── CM-flight-xyz → PM-flight-final ($385.00)
├── CM-hotel-xyz → PM-hotel-final ($1,445.00)
└── CM-conf-xyz → PM-conf-final ($799.00)

Total: $2,629.00 (under $2,500 limit? OVER by $129)
Resolution: User pre-approved overage via confirmation in STORY 5

Audit Trail:
├─ All mandates signed and verified
├─ DID credentials validated
├─ Transaction IDs cross-referenced
├─ Blockchain hashes: 
│  ├─ Flight: 0x7a9f...3b2e
│  ├─ Hotel: 0x4c1d...8f9a
│  └─ Conference: 0x2e8b...5c7f
└─ Compliance: SOC 2, PCI DSS compliant

MCP Connection to AccountingAgent:
├─ Tool: create_expense_report
├─ Category: Business Travel
├─ Project: TMC 2027 Conference
├─ Tax deductible: Yes (conference + travel)
└─ Receipt format: PDF + CSV export

Generated Documents:
1. Consolidated Receipt (PDF)
   ├─ Itemized breakdown
   ├─ Payment method
   ├─ Transaction IDs
   ├─ Tax information
   └─ QR code linking to blockchain records

2. Expense Report (CSV)
   For import into accounting software

3. Tax Documentation
   Itemized for deduction purposes

A2A to ReceiptGeneratorAgent:
├─ All transaction data
├─ Branding: User's company logo
├─ Delivery: Email + Cloud storage
└─ Retention: 7 years for audit
```

**Dependencies:** AGENT-2027-7, AGENT-2027-8, AGENT-2027-9  
**Estimate:** 5 story points

---

### STORY 12: Notification & Confirmation to User
**Story ID:** AGENT-2027-12  
**Protocol(s):** MCP  
**Agent(s):** PersonalAssistantAgent → NotificationAgent

**As a** Personal Assistant Agent  
**I want to** notify user of completed booking  
**So that** user is informed and can review details

**Acceptance Criteria:**
- [x] Compile booking summary
- [x] Send multi-channel notifications (push, email, SMS)
- [x] Include links to itinerary and receipts
- [x] Provide options to modify or cancel
- [x] Log completion status
- [x] Request user feedback

**Technical Implementation:**
```
MCP to NotificationAgent:
├─ Channels: Push notification, Email, SMS
├─ Priority: High
└─ Content template: "Booking Confirmation"

Notification Content:
━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ TMC 2027 Trip Booked!

Hi Sarah, your trip is confirmed:

✈️ Flight: Delta DL1234
   May 19, 6:45 AM → May 24, 2:15 PM
   Confirmation: DL-0123456789

🏨 Hotel: Marriott Marquis SF
   May 19-24 (5 nights)
   Confirmation: M-87654321-SF

🎫 Conference: TMC 2027
   May 20-23, General Admission
   Badge: #TMC2027-A-12345

💰 Total: $2,629.00
   Flight: $385 | Hotel: $1,445 | Conf: $799

📄 Full itinerary: [Link]
📊 Receipts: [Link]
📅 Added to calendar: [View]

Need changes? Reply or ask me!
━━━━━━━━━━━━━━━━━━━━━━━━━

Actions Available:
├─ View detailed itinerary
├─ Download receipts
├─ Modify reservations
├─ Add to Wallet (boarding pass)
└─ Share with colleagues

Feedback Request:
"Was this booking experience helpful?"
[👍 Yes] [👎 No] [💬 Comment]
```

**Dependencies:** AGENT-2027-10, AGENT-2027-11  
**Estimate:** 3 story points

---

### STORY 13: Continuous Monitoring & Updates
**Story ID:** AGENT-2027-13  
**Protocol(s):** A2A, MCP  
**Agent(s):** PersonalAssistantAgent → TravelMonitoringAgent → Multiple External Agents

**As a** Personal Assistant Agent  
**I want to** monitor trip details for changes  
**So that** user is informed of updates proactively

**Acceptance Criteria:**
- [x] Subscribe to flight status updates via A2A
- [x] Monitor hotel reservation status
- [x] Track conference schedule changes
- [x] Set up weather alerts
- [x] Enable real-time notifications
- [x] Suggest alternatives if issues arise

**Technical Implementation:**
```
A2A Asynchronous Subscriptions:

1. Flight Status Monitoring:
   ├─ Subscribe: FlightStatusAgent (A2A async callback)
   ├─ Flight: DL1234
   ├─ Events: Gate changes, delays, cancellations
   ├─ Callback: https://personal-agent/callbacks/flight-status
   └─ Active: Until 2027-05-24

2. Hotel Monitoring:
   ├─ Subscribe: HotelReservationAgent
   ├─ Events: Reservation changes, room upgrades
   └─ Active: Until 2027-05-24

3. Conference Updates:
   ├─ Subscribe: EventRegistrationAgent
   ├─ Events: Schedule changes, session updates
   └─ Active: Until 2027-05-23

MCP Services:
├─ WeatherAPI: Daily forecast for SF
├─ TransitAPI: Traffic and public transport alerts
└─ LocalEventsAPI: Related activities

Proactive Actions:
├─ Flight delayed → Notify + adjust hotel check-in
├─ Weather alert → Suggest packing rain gear
├─ Conference session canceled → Suggest alternatives
└─ Nearby networking event → Recommend attendance
```

**Dependencies:** AGENT-2027-12  
**Estimate:** 8 story points

---

## Agent Interaction Map

```
User (Sarah Chen)
    ↓ [Natural Language Request]
    ↓
PersonalAssistantAgent (Orchestrator)
    ↓
    ├─→ [ANS] Discover agents
    │   └─→ ANS Registry
    │       └─→ Returns: Agent Cards + DIDs
    │
    ├─→ [MCP] Natural Language Understanding
    │   └─→ AnthropicLLMService
    │
    ├─→ [MCP] User Profile & Preferences
    │   └─→ UserProfileAgent
    │
    ├─→ [A2A] Flight Search
    │   └─→ FlightBookingAgent
    │       └─→ [MCP] Multiple airline APIs
    │
    ├─→ [A2A] Hotel Search
    │   └─→ HotelReservationAgent
    │       ├─→ [A2A] Venue location
    │       │   └─→ VenueInformationAgent
    │       └─→ [MCP] Hotel booking systems
    │
    ├─→ [A2A] Conference Registration
    │   └─→ EventRegistrationAgent
    │       └─→ [MCP] TMC Registration System
    │
    └─→ [A2A] Payment Coordination
        └─→ PaymentCoordinatorAgent
            ├─→ [AP2] Flight payment
            │   └─→ FlightBookingAgent
            │       └─→ [AP2→Traditional] Airline gateway
            │
            ├─→ [AP2] Hotel payment
            │   └─→ HotelReservationAgent
            │       └─→ [AP2→Traditional] Hotel gateway
            │
            ├─→ [AP2] Conference payment
            │   └─→ EventRegistrationAgent
            │       └─→ [AP2→Traditional] Event gateway
            │
            └─→ [MCP] Accounting
                └─→ AccountingAgent

Post-Booking:
    ├─→ [MCP] Calendar updates
    │   └─→ CalendarAgent
    │
    ├─→ [A2A] Itinerary generation
    │   └─→ ItineraryGeneratorAgent
    │
    ├─→ [MCP] Notifications
    │   └─→ NotificationAgent
    │
    └─→ [A2A] Monitoring subscriptions
        └─→ TravelMonitoringAgent
            ├─→ FlightStatusAgent
            ├─→ WeatherAgent
            └─→ EventUpdateAgent
```

---

## Protocol Usage Summary

| Protocol | Primary Use Case | Stories |
|----------|------------------|---------|
| **ANS** | Agent discovery, identity verification, capability lookup | 1 |
| **A2A** | Inter-agent communication, task delegation, async callbacks | 2, 3, 4, 5, 7, 8, 9, 10, 13 |
| **MCP** | LLM integration, external system access, OAuth authentication | 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13 |
| **AP2** | Payment authorization, mandate chain, transaction verification | 6, 7, 8, 9, 11 |

---

## Total Complexity Behind Simple Request

**What User Said:**
> "Book me tickets for TMC 2027"

**What Actually Happened:**
- **13 User Stories** across multiple sprint cycles
- **15+ Agent Interactions** across 8 specialized agents
- **4 Protocol Types** (ANS, A2A, MCP, AP2)
- **25+ Individual API Calls** to external systems
- **3 Payment Transactions** with full audit trail
- **8 Calendar Events** created
- **5 Document Artifacts** generated (tickets, receipts, itinerary)
- **3 Async Monitoring** subscriptions active until trip completion

**Total Story Points:** 71 points  
**Estimated Dev Time:** ~3 sprint cycles (if building from scratch)  
**Actual User Wait Time:** ~45 seconds (all agents working in parallel)

---

## Epic Success Criteria

- [x] Flight booked and confirmed
- [x] Hotel reserved with preferences met
- [x] Conference registration complete
- [x] All payments processed with full audit trail
- [x] Calendar updated with all events
- [x] Itinerary and receipts delivered
- [x] User notified and satisfied
- [x] Continuous monitoring active
- [x] All protocol standards followed (ANS, A2A, MCP, AP2)
- [x] Security and compliance requirements met

---

## Epic Retrospective Notes

**What Went Well:**
- Agent discovery via ANS was seamless
- A2A protocol enabled efficient parallel processing
- AP2 mandate chain provided complete payment traceability
- MCP integrations with external systems were robust
- User received booking confirmation in under 1 minute

**Challenges:**
- Budget slightly exceeded due to hotel pricing (+$129)
- Multiple async callbacks required careful state management
- Different hotel/airline APIs had varying response formats (solved via MCP abstraction)

**Lessons Learned:**
- Always query user preferences early (STORY 5) to avoid rework
- Payment mandate chains (AP2) add overhead but provide essential audit trail
- ANS agent discovery should cache results for frequently-used agents
- Consider implementing retry logic for external API timeouts

---

*End of Epic*