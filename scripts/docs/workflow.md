# AI CTF Agent Workflow

## 1. Input Collection

The agent first collects all available information:

- Challenge title
- Description
- Target URL
- Attachment file names
- Source code
- Runtime logs
- Error messages
- Previous attempts

## 2. Information Summary

The agent summarizes:

- What is known
- What is unknown
- What has already been tested
- What should not be repeated

## 3. Solving Plan

The agent generates several possible solving paths instead of focusing on only one idea.

For example:

- Web: endpoint discovery, parameter testing, file access logic
- Crypto: weak randomness, reused nonce, small exponent, faulty CRT
- Reverse: strings, control flow, encryption logic, symbolic solving
- Misc: file carving, metadata, audio/image analysis

## 4. Script Generation

The agent generates Python scripts for testing and automation.

Scripts should be:

- Reproducible
- Easy to modify
- Clear in output
- Focused on verification

## 5. Runtime Feedback

The user runs the script and sends back the output.

The agent then analyzes:

- Status code
- Response length
- Error message
- Flag pattern
- Unexpected behavior

## 6. Iteration

The agent updates the plan based on the runtime result.

This avoids repeating failed paths and helps move toward the final solution.

## 7. Writeup

After solving or making progress, the agent generates a final writeup including:

- Challenge summary
- Key vulnerability or idea
- Exploit process
- Final script
- Lessons learned
