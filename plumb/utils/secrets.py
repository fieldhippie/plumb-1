"""Simple secret redaction for transcripts before sending to LLM."""
from __future__ import annotations

import re

# Common patterns: API keys, tokens, private keys, etc.
_PATTERNS = [
    re.compile(r"sk-[a-zA-Z0-9]{20,}", re.I),          # OpenAI / Anthropic-style
    re.compile(r"sk-ant-[a-zA-Z0-9\-_]{20,}", re.I),   # Anthropic
    re.compile(r"ghp_[a-zA-Z0-9]{36}", re.I),          # GitHub PAT
    re.compile(r"github_pat_[a-zA-Z0-9_]{20,}", re.I),
    re.compile(r"xox[baprs]-[a-zA-Z0-9\-]+", re.I),    # Slack
    re.compile(r"AKIA[0-9A-Z]{16}", re.I),             # AWS
    re.compile(r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA |EC )?PRIVATE KEY-----", re.I),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[a-zA-Z0-9\-_\.]{8,}['\"]?"),
]

def redact_secrets(text: str) -> str:
    """Replace obvious secrets with [REDACTED]."""
    if not text:
        return text
    result = text
    for pat in _PATTERNS:
        result = pat.sub("[REDACTED]", result)
    return result
