#!/usr/bin/env python3
"""
TMC 2027 Vulnerability Analysis Pipeline - Complete Visual Diagram
Generates a Graphviz diagram showing all 7 stages of the pipeline
"""

from graphviz import Digraph

# Create main diagram
dot = Digraph(comment='TMC 2027 Vulnerability Analysis Pipeline', format='png')
dot.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='1.2')
dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='11')
dot.attr('edge', fontname='Arial', fontsize='9', color='#333333')

# Define color scheme
COLOR_VSG = '#E3F2FD'          # Light blue - VSG generation
COLOR_FILTER = '#FFF3E0'       # Light orange - Filtering/processing
COLOR_JURY_VULN = '#F3E5F5'    # Light purple - Vulnerability jury
COLOR_ATTACK_GEN = '#E8F5E9'   # Light green - Attack generation
COLOR_JURY_ATTACK = '#FCE4EC'  # Light pink - Attack jury
COLOR_REPORT = '#FFF9C4'       # Light yellow - Reporting
COLOR_ARTIFACT = '#F5F5F5'     # Light grey - Artifacts

# Stage 1: VSG Generation
with dot.subgraph(name='cluster_stage1') as c:
    c.attr(label='Stage 1: VSG Generation', style='filled', color='#BBDEFB', fontsize='12', fontname='Arial Bold')
    c.node('bvsg', 'BVSG\n(Behavioral)', fillcolor=COLOR_VSG)
    c.node('dcvsg', 'DCVSG\n(Dependency Cascade)', fillcolor=COLOR_VSG)
    c.node('rvsg', 'RVSG\n(Resonant)', fillcolor=COLOR_VSG)
    c.node('tvsg', 'TVSG\n(Temporal)', fillcolor=COLOR_VSG)

dot.node('vsg_output', '8 Vulnerability Stories\n(2 per VSG)', shape='cylinder', fillcolor=COLOR_ARTIFACT)

# Stage 2: Deduplication
dot.node('stage2', 'Stage 2:\nDeduplication\n\n• Remove duplicates\n• Similarity analysis\n• Keep unique stories', fillcolor=COLOR_FILTER, width='2.5')
dot.node('dedup_output', '~6-7 Unique Stories', shape='cylinder', fillcolor=COLOR_ARTIFACT)

# Stage 3: Plausibility Check
dot.node('stage3', 'Stage 3:\nPlausibility Check\n\n• Technical Feasibility\n• Emergence Validity\n• Impact Severity\n• Detection Difficulty\n• Exploit Complexity', fillcolor=COLOR_FILTER, width='2.5')
dot.node('plaus_output', 'Scored & Filtered\nVulnerabilities', shape='cylinder', fillcolor=COLOR_ARTIFACT)

# Stage 4: Vulnerability Jury (NEW)
with dot.subgraph(name='cluster_stage4') as c:
    c.attr(label='Stage 4: Vulnerability Jury Evaluation ⭐ NEW', style='filled', color='#E1BEE7', fontsize='12', fontname='Arial Bold')
    c.node('vuln_sec', 'Security Researcher\n• Technical Depth\n• Emergence Validity\n• Research Novelty', fillcolor=COLOR_JURY_VULN, width='2.2')
    c.node('vuln_arch', 'System Architect\n• System Impact\n• Architectural Implications\n• Fix Feasibility', fillcolor=COLOR_JURY_VULN, width='2.2')
    c.node('vuln_biz', 'Business Risk Analyst\n• Business Impact\n• Stakeholder Costs\n• Strategic Priority', fillcolor=COLOR_JURY_VULN, width='2.2')
    c.node('vuln_ir', 'Incident Responder\n• Detection Potential\n• Response Complexity\n• Real-World Likelihood', fillcolor=COLOR_JURY_VULN, width='2.2')
    c.node('vuln_red', 'Red Team Lead\n• Exploitability\n• Threat Actor Appeal\n• Attack Surface', fillcolor=COLOR_JURY_VULN, width='2.2')

dot.node('vuln_jury_output', 'Vulnerability Scores\n& Recommendations\n(CRITICAL/HIGH/MEDIUM/LOW)', shape='cylinder', fillcolor=COLOR_ARTIFACT)

# Stage 5: Attack Generation
dot.node('stage5', 'Stage 5:\nAttack Scenario Generation\n\n• SCAMPER Framework\n• Creative exploitation techniques\n• Multiple attack vectors per vulnerability', fillcolor=COLOR_ATTACK_GEN, width='2.5')
dot.node('attack_output', 'Attack Scenarios\n(~8-16 scenarios)', shape='cylinder', fillcolor=COLOR_ARTIFACT)

# Stage 6: Attack Jury
with dot.subgraph(name='cluster_stage6') as c:
    c.attr(label='Stage 6: Attack Jury Evaluation ⭐ REFACTORED', style='filled', color='#F8BBD0', fontsize='12', fontname='Arial Bold')
    c.node('attack_sec', 'Security Researcher\n• Attack Technical Soundness\n• Exploit Realism\n• Attack Novelty', fillcolor=COLOR_JURY_ATTACK, width='2.2')
    c.node('attack_arch', 'System Architect\n• Attack Systemic Impact\n• Defense Feasibility\n• Cascading Effects', fillcolor=COLOR_JURY_ATTACK, width='2.2')
    c.node('attack_biz', 'Business Risk Analyst\n• Attack-Specific Impact\n• Attacker ROI\n• Defender Cost', fillcolor=COLOR_JURY_ATTACK, width='2.2')
    c.node('attack_ir', 'Incident Responder\n• Detection Difficulty\n• Response Complexity\n• Forensic Clarity', fillcolor=COLOR_JURY_ATTACK, width='2.2')
    c.node('attack_red', 'Red Team Lead\n• Attack Creativity\n• Threat Actor Motivation\n• Exploit Chain Validity', fillcolor=COLOR_JURY_ATTACK, width='2.2')

dot.node('attack_jury_output', 'Attack Scores\n& Recommendations\n(CRITICAL/HIGH/MEDIUM/LOW)', shape='cylinder', fillcolor=COLOR_ARTIFACT)

# Stage 7: Report Generation
with dot.subgraph(name='cluster_stage7') as c:
    c.attr(label='Stage 7: Final Report Generation ⭐ NEW', style='filled', color='#FFF59D', fontsize='12', fontname='Arial Bold')
    c.node('report_exec', 'Executive Summary\n(2-3 pages)\n• Business language\n• Financial impact\n• Strategic recommendations', fillcolor=COLOR_REPORT, width='2.2')
    c.node('report_tech', 'Technical Report\n(10-15 pages)\n• Detailed analysis\n• Defensive measures\n• Cross-cutting patterns', fillcolor=COLOR_REPORT, width='2.2')

dot.node('final_output', 'Complete Analysis\n• Vulnerability Rankings\n• Attack Scenarios\n• Actionable Recommendations', shape='doubleoctagon', fillcolor='#4CAF50', fontcolor='white', style='filled', width='2.5')

# Edges - Main pipeline flow
dot.edge('bvsg', 'vsg_output', label='2 stories')
dot.edge('dcvsg', 'vsg_output', label='2 stories')
dot.edge('rvsg', 'vsg_output', label='2 stories')
dot.edge('tvsg', 'vsg_output', label='2 stories')

dot.edge('vsg_output', 'stage2', label='8 stories')
dot.edge('stage2', 'dedup_output', label='~6-7 unique')
dot.edge('dedup_output', 'stage3', label='filtered')
dot.edge('stage3', 'plaus_output', label='scored ≥7.0')

# Stage 4 connections
dot.edge('plaus_output', 'vuln_sec', style='dashed', color='#9C27B0')
dot.edge('plaus_output', 'vuln_arch', style='dashed', color='#9C27B0')
dot.edge('plaus_output', 'vuln_biz', style='dashed', color='#9C27B0')
dot.edge('plaus_output', 'vuln_ir', style='dashed', color='#9C27B0')
dot.edge('plaus_output', 'vuln_red', style='dashed', color='#9C27B0')

dot.edge('vuln_sec', 'vuln_jury_output', style='dashed', color='#9C27B0')
dot.edge('vuln_arch', 'vuln_jury_output', style='dashed', color='#9C27B0')
dot.edge('vuln_biz', 'vuln_jury_output', style='dashed', color='#9C27B0')
dot.edge('vuln_ir', 'vuln_jury_output', style='dashed', color='#9C27B0')
dot.edge('vuln_red', 'vuln_jury_output', style='dashed', color='#9C27B0')

# Stage 5 connections
dot.edge('vuln_jury_output', 'stage5', label='ALL vulnerabilities')
dot.edge('stage5', 'attack_output', label='SCAMPER')

# Stage 6 connections
dot.edge('attack_output', 'attack_sec', style='dashed', color='#E91E63')
dot.edge('attack_output', 'attack_arch', style='dashed', color='#E91E63')
dot.edge('attack_output', 'attack_biz', style='dashed', color='#E91E63')
dot.edge('attack_output', 'attack_ir', style='dashed', color='#E91E63')
dot.edge('attack_output', 'attack_red', style='dashed', color='#E91E63')

dot.edge('attack_sec', 'attack_jury_output', style='dashed', color='#E91E63')
dot.edge('attack_arch', 'attack_jury_output', style='dashed', color='#E91E63')
dot.edge('attack_biz', 'attack_jury_output', style='dashed', color='#E91E63')
dot.edge('attack_ir', 'attack_jury_output', style='dashed', color='#E91E63')
dot.edge('attack_red', 'attack_jury_output', style='dashed', color='#E91E63')

# Stage 7 connections
dot.edge('vuln_jury_output', 'report_exec', label='vuln scores', style='dotted', color='#FF9800')
dot.edge('vuln_jury_output', 'report_tech', label='vuln scores', style='dotted', color='#FF9800')
dot.edge('attack_jury_output', 'report_exec', label='attack scores', style='dotted', color='#FF9800')
dot.edge('attack_jury_output', 'report_tech', label='attack scores', style='dotted', color='#FF9800')

dot.edge('report_exec', 'final_output', label='executive view')
dot.edge('report_tech', 'final_output', label='technical view')

# Add legend
with dot.subgraph(name='cluster_legend') as c:
    c.attr(label='Legend', style='filled', color='#E0E0E0', fontsize='10')
    c.node('leg1', '⭐ NEW = New component in refactored pipeline', shape='plaintext', fillcolor='white')
    c.node('leg2', 'Purple dashed = Vulnerability evaluation', shape='plaintext', fillcolor='white')
    c.node('leg3', 'Pink dashed = Attack evaluation', shape='plaintext', fillcolor='white')
    c.node('leg4', 'Orange dotted = Report synthesis', shape='plaintext', fillcolor='white')

# Render
output_path = 'artifacts/tmc-2027-pipeline-diagram'
dot.render(output_path, view=False, cleanup=True)
print(f"✅ Pipeline diagram saved to: {output_path}.png")
print(f"   Source file: {output_path}.dot")

# Also save the source
with open(f"{output_path}.dot", "w") as f:
    f.write(dot.source)

print("\n📊 Pipeline Overview:")
print("   Stage 1: VSG Generation (4 agents → 8 stories)")
print("   Stage 2: Deduplication (8 → ~6-7 stories)")
print("   Stage 3: Plausibility (filter by score ≥7.0)")
print("   Stage 4: Vulnerability Jury (5 judges × N vulnerabilities)")
print("   Stage 5: Attack Generation (SCAMPER framework)")
print("   Stage 6: Attack Jury (5 judges × M attack scenarios)")
print("   Stage 7: Report Generation (Executive + Technical)")
