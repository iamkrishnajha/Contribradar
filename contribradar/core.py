from dataclasses import dataclass, asdict
from pathlib import Path
import re


@dataclass
class Opportunity:
    title: str
    priority: str
    points: int
    reason: str

    def to_dict(self):
        return asdict(self)


REQUIRED_FILES = {
    "README.md": (10, "Add clear project documentation."),
    "LICENSE": (8, "Add an explicit open-source license."),
    "CONTRIBUTING.md": (10, "Add contributor setup and workflow guidance."),
    "CODE_OF_CONDUCT.md": (5, "Add community participation guidelines."),
    "SECURITY.md": (7, "Add a vulnerability reporting policy."),
}


def _priority(points):
    if points >= 10:
        return "HIGH"
    if points >= 6:
        return "MEDIUM"
    return "LOW"


def scan_repo(path="."):
    root = Path(path).resolve()
    opportunities = []

    # Check important community and documentation files.
    for filename, (points, reason) in REQUIRED_FILES.items():
        if not (root / filename).exists():
            opportunities.append(
                Opportunity(
                    title=f"Add {filename}",
                    priority=_priority(points),
                    points=points,
                    reason=reason,
                )
            )

    # Check for GitHub Actions CI.
    workflows = root / ".github" / "workflows"
    workflow_files = []

    if workflows.exists():
        workflow_files = list(workflows.glob("*.yml"))
        workflow_files += list(workflows.glob("*.yaml"))

    if not workflow_files:
        opportunities.append(
            Opportunity(
                title="Add automated CI",
                priority="HIGH",
                points=10,
                reason="Run tests and checks automatically on pull requests.",
            )
        )

    # Check for a test suite.
    test_dirs = [root / "tests", root / "test"]

    if not any(directory.exists() for directory in test_dirs):
        opportunities.append(
            Opportunity(
                title="Add automated tests",
                priority="HIGH",
                points=12,
                reason="Create a repeatable test suite for contributors.",
            )
        )

    # Find TODO, FIXME and HACK markers.
    source_extensions = {
        ".py",
        ".js",
        ".ts",
        ".java",
        ".go",
        ".rs",
        ".rb",
        ".php",
        ".cpp",
        ".c",
        ".cs",
    }

    ignored_parts = {
        ".git",
        ".venv",
        "venv",
        "node_modules",
        "dist",
        "build",
    }

    todo_count = 0

    for file in root.rglob("*"):
        if not file.is_file():
            continue

        if file.suffix.lower() not in source_extensions:
            continue

        if any(part in ignored_parts for part in file.parts):
            continue

        try:
            text = file.read_text(
                encoding="utf-8",
                errors="ignore",
            )
        except OSError:
            continue

        todo_count += len(
            re.findall(
                r"\b(?:TODO|FIXME|HACK)\b",
                text,
                flags=re.IGNORECASE,
            )
        )

    if todo_count:
        points = min(12, 3 + todo_count)

        opportunities.append(
            Opportunity(
                title=f"Review {todo_count} TODO/FIXME item(s)",
                priority=_priority(points),
                points=points,
                reason=(
                    "Turn unresolved markers into documented issues, "
                    "tests, or completed work."
                ),
            )
        )

    # Check for common project metadata.
    project_files = [
        "pyproject.toml",
        "package.json",
        "Cargo.toml",
        "go.mod",
    ]

    if not any((root / filename).exists() for filename in project_files):
        opportunities.append(
            Opportunity(
                title="Document the project structure",
                priority="MEDIUM",
                points=6,
                reason=(
                    "Add clear setup, development, and release "
                    "instructions for contributors."
                ),
            )
        )

    opportunities.sort(
        key=lambda item: (-item.points, item.title.lower())
    )

    score = max(
        0,
        100 - sum(item.points for item in opportunities),
    )

    return {
        "score": score,
        "opportunities": [
            item.to_dict() for item in opportunities
        ],
        "opportunity_count": len(opportunities),
    }


def render_report(result):
    lines = [
        "ContribRadar — repository opportunity scan",
        "",
        f"Score: {result['score']}/100",
        "",
    ]

    if not result["opportunities"]:
        lines.append("No obvious opportunities detected.")
        return "\n".join(lines)

    for priority in ("HIGH", "MEDIUM", "LOW"):
        items = [
            item
            for item in result["opportunities"]
            if item["priority"] == priority
        ]

        if not items:
            continue

        lines.append(priority)

        for item in items:
            lines.append(
                f"  {item['title']} — {item['reason']}"
            )

        lines.append("")

    lines.append(
        f"Total opportunities: "
        f"{result['opportunity_count']}"
    )

    return "\n".join(lines)
