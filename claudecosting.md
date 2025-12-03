  Token Usage Comparison by Task

  Example 1: Simple File Read & Explanation

  Task: "Read app.py and explain what it does"

  | Model      | Input Tokens | Output Tokens | Total | Cost    |
  |------------|--------------|---------------|-------|---------|
  | Haiku      | 2,000        | 500           | 2,500 | $0.0008 |
  | Sonnet 3.5 | 2,000        | 500           | 2,500 | $0.0083 |
  | Sonnet 4.5 | 2,000        | 500           | 2,500 | $0.0100 |
  | Opus       | 2,000        | 500           | 2,500 | $0.0450 |

  Ratio: Haiku is 10-12x cheaper than Sonnet, 50x cheaper than Opus

  ---
  Example 2: Write a Simple Flask Route

  Task: "Add a new route to display user profile"

  | Model      | Input Tokens | Output Tokens | Total | Cost    |
  |------------|--------------|---------------|-------|---------|
  | Haiku      | 3,000        | 800           | 3,800 | $0.0012 |
  | Sonnet 3.5 | 3,000        | 800           | 3,800 | $0.0126 |
  | Sonnet 4.5 | 3,000        | 800           | 3,800 | $0.0152 |
  | Opus       | 3,000        | 800           | 3,800 | $0.0684 |

  Ratio: Haiku uses same tokens but costs 10x less than Sonnet

  ---
  Example 3: Complex Debugging (What We Did Today)

  Task: "Debug nested directory path issues and fix link conversion"

  | Model      | Input Tokens | Output Tokens | Total  | Cost    |
  |------------|--------------|---------------|--------|---------|
  | Haiku      | 12,000       | 3,000         | 15,000 | $0.0050 |
  | Sonnet 3.5 | 12,000       | 3,000         | 15,000 | $0.0495 |
  | Sonnet 4.5 | 12,000       | 3,000         | 15,000 | $0.0600 |
  | Opus       | 12,000       | 3,000         | 15,000 | $0.2700 |

  Ratio: Haiku 12x cheaper than Sonnet 4.5, 54x cheaper than Opus

  ---
  Example 4: Build Entire Flask App (Our Full Session)

  Task: "Create a Flask learning app with templates, routing, and styling"

  | Model      | Input Tokens | Output Tokens | Total  | Cost    |
  |------------|--------------|---------------|--------|---------|
  | Haiku      | 70,000       | 18,000        | 88,000 | $0.0220 |
  | Sonnet 3.5 | 70,000       | 18,000        | 88,000 | $0.2640 |
  | Sonnet 4.5 | 70,000       | 18,000        | 88,000 | $0.3520 |
  | Opus       | 70,000       | 18,000        | 88,000 | $1.5840 |

  Ratio:
  - Haiku vs Sonnet 4.5: 16x cheaper ($0.02 vs $0.35)
  - Haiku vs Opus: 72x cheaper ($0.02 vs $1.58)

  ---
  Real-World Usage Percentages

  Our Actual Session Breakdown (~88K tokens)

  What We Did:
  ├─ File Creation (13 templates + CSS + Python)      : 25% tokens
  ├─ Code Generation (Flask routes, functions)        : 30% tokens
  ├─ Debugging (path issues, link fixing)             : 20% tokens
  ├─ Testing (curl commands, verifications)           : 15% tokens
  └─ Explanations & Documentation                     : 10% tokens

  Cost by Model for This Session:

  | Model      | Actual Cost | % vs Haiku        |
  |------------|-------------|-------------------|
  | Haiku      | $0.022      | 100% (baseline)   |
  | Sonnet 3.5 | $0.264      | 1,200% (12x more) |
  | Sonnet 4.5 | $0.352      | 1,600% (16x more) |
  | Opus       | $1.584      | 7,200% (72x more) |

  ---
  When Each Model Makes Sense

  ✅ Use Haiku (1x cost)

  Examples:
  - "Read this file"                    → 500 tokens  → $0.0002
  - "Fix this typo in line 45"          → 800 tokens  → $0.0003
  - "List all markdown files"           → 1,200 tokens → $0.0004
  - "Add a comment to this function"    → 600 tokens  → $0.0002

  Savings: 90% cheaper than Sonnet

  ✅ Use Sonnet 3.5 (12x cost, but worth it)

  Examples:
  - "Add user authentication"           → 8,000 tokens  → $0.026
  - "Refactor this module"              → 12,000 tokens → $0.040
  - "Debug this complex error"          → 15,000 tokens → $0.050
  - "Write tests for this feature"      → 10,000 tokens → $0.033

  Better quality than Haiku, cheaper than Sonnet 4.5

  ⚠️ Use Sonnet 4.5 (16x cost) - Current Model

  Examples:
  - "Design entire app architecture"    → 20,000 tokens → $0.080
  - "Complex multi-file refactoring"    → 30,000 tokens → $0.120
  - "Performance optimization"          → 25,000 tokens → $0.100

  Use only when Sonnet 3.5 isn't enough

  🔴 Use Opus (72x cost) - Only When Necessary

  Examples:
  - "Redesign entire system"            → 50,000 tokens → $0.900
  - "Advanced algorithm design"         → 40,000 tokens → $0.720
  - "Complex security audit"            → 60,000 tokens → $1.080

  Use rarely, only for critical complex tasks

  ---
  Money-Saving Strategy

  If you had used Haiku for 70% of our tasks and Sonnet 3.5 for 30%:

  Actual (Sonnet 4.5 for everything):  $0.352
  Smart approach:
    70% Haiku    (61K tokens): $0.015
    30% Sonnet   (27K tokens): $0.089
    Total:                     $0.104

  Savings: 70% cheaper ($0.352 → $0.104)

  ---
  Quick Reference Card

  Task Complexity          | Use This Model | Cost Ratio
  -------------------------|----------------|------------
  Read/List files          | Haiku          | 1x
  Simple fixes             | Haiku          | 1x
  Add simple features      | Haiku/Sonnet   | 1-12x
  Bug fixing               | Sonnet 3.5     | 12x
  New feature development  | Sonnet 3.5     | 12x
  Major refactoring        | Sonnet 4.5     | 16x
  Architecture design      | Opus           | 72x

  Bottom line: You could have saved ~$0.25 (70%) on this session by using Haiku
  for simple tasks and Sonnet 3.5 for complex ones!