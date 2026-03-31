# Application Tracker Schema

## Purpose

Use this reference to structure the application tracker used by the workflow.

The tracker should help the user avoid duplicated work, remember which resume version was used, understand what each JD exposed, and feed outcomes back into future applications.

Core principle:

The tracker is not just a status list. It is a decision log for the job-search process.

## Minimum Required Fields

Every tracker entry should ideally include:
- application date
- company
- role name
- role direction
- JD summary
- resume version
- fit judgment
- current status
- last update date
- next action

These fields are the minimum needed to make the tracker useful.

## Recommended Full Field Set

Recommended columns:
- application date
- company
- role name
- role direction
- city / work mode
- JD link
- JD summary
- resume version
- main keywords targeted
- emphasized projects
- weakened or omitted materials
- fit judgment
- status
- last update date
- latest progress
- next action
- deadline
- reply received
- interview result
- rejection reason
- feedback summary
- self-assessment
- exposed gaps
- top skill gap
- top material gap
- top metrics gap
- priority
- resume filename
- portfolio version exists
- referral exists
- source / contact

Not every field must be filled immediately, but the schema should stay stable.

## Field Definitions

### Identity and role fields
- application date: when the user actually applied or started tracking the role
- company: employer name
- role name: exact role title
- role direction: normalized category such as C-end product, AI product, growth, operations
- city / work mode: city, remote, hybrid, or onsite

### JD and strategy fields
- JD link: source link if available
- JD summary: one-line role summary
- resume version: label used in workflow
- main keywords targeted: keywords intentionally emphasized
- emphasized projects: projects or experiences foregrounded
- weakened or omitted materials: what was intentionally deprioritized
- fit judgment: high / medium / low or equivalent

### Process status fields
- status: where this application currently stands
- last update date: latest date of manual update
- latest progress: most recent meaningful event
- next action: specific next step
- deadline: application deadline if known
- reply received: yes / no / unknown

### Outcome and learning fields
- interview result: if interviews happened, record result
- rejection reason: if known
- feedback summary: employer or self feedback
- self-assessment: user's own judgment after applying or interviewing
- exposed gaps: what this role revealed as weak spots
- top skill gap: most important skill weakness
- top material gap: most important missing artifact or evidence
- top metrics gap: most important missing quantified proof

### Asset and sourcing fields
- priority: P1 / P2 / P3 or similar
- resume filename: the actual file used
- portfolio version exists: yes / no
- referral exists: yes / no
- source / contact: recruiter, friend, website, internal referral, etc.

## Status Suggestions

Keep statuses simple and mutually understandable.

Suggested values:
- to analyze
- analyzed
- resume drafted
- ready to apply
- applied
- replied
- written test
- interview scheduled
- interviewing
- offer
- rejected
- withdrawn
- archived

Choose a small set and use it consistently.

## Update Rules

Update the tracker when:
- a JD is analyzed
- a tailored resume is created
- the user applies
- the company replies
- an interview is scheduled or completed
- a rejection or offer arrives
- a new weakness or pattern is discovered

Do not wait until the end of the process to log the entry.

## Naming Rules

For resume-related fields:
- use stable version labels
- keep resume filenames consistent with actual stored files
- prefer company-role based filenames over vague version names once final

Example:
- resume version: 携程-C端产品实习生-v1
- resume filename: 携程-C端产品实习生-林雨涵.docx

## Interpretation Rules

The tracker should support these later questions:
- which JD types were strongest fits
- which projects keep getting used
- what gaps appear repeatedly
- which resume versions performed better
- where interviews were won or lost

Write entries so they can be analyzed later, not just viewed once.

## Common Mistakes

- tracking only applied roles and not analyzed roles
- using inconsistent status values
- failing to record which resume version was used
- omitting what was emphasized or omitted in tailoring
- storing no learning after rejection or interview
- letting filenames drift from actual files
- writing vague next actions like "follow up later"

## Exit Criteria

A tracker setup is good enough when:
- the columns are stable
- at least one real role can be logged end-to-end
- resume version and file naming are linked
- status and next action are clear
- gaps exposed by the JD can be captured

Once that is true, the tracker is ready for regular workflow use.
