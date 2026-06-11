from pathlib import Path

repo = Path(".")

domains = {
    "Domain-02-Java-Developer": 4,
    "Domain-03-Python-Full-Stack": 3,
    "Domain-06-Web-Designing": 4,
    "Domain-07-Java-Developer": 4,
    "Domain-09-SQL": 4,
    "Domain-12-Full-Stack": 4,
    "Domain-13-MERN-Stack": 4,
    "Domain-14-Python-Developer": 4,
    "Domain-15-Data-Analytics-Data-Science": 5,
    "Domain-16-Cyber-Security": 6,
    "Domain-17-VLSI": 3,
    "Domain-18-IOT": 6,
    "Domain-19-Ethical-Hacking": 4,
    "Domain-20-AI-ML": 6,
    "Domain-21": 3,
    "Domain-22": 3,
}

for domain, task_count in domains.items():
    domain_path = repo / domain
    domain_path.mkdir(parents=True, exist_ok=True)

    readme = domain_path / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# {domain}\n\n## Tasks\n\n"
            + "\n".join(
                [f"- [ ] Task-{i:02d}" for i in range(1, task_count + 1)]
            )
            + f"\n\n## Progress\n0/{task_count} Tasks Completed\n",
            encoding="utf-8",
        )

    for i in range(1, task_count + 1):
        task = domain_path / f"Task-{i:02d}"
        task.mkdir(exist_ok=True)

        task_readme = task / "README.md"
        if not task_readme.exists():
            task_readme.write_text(
                f"# Task {i}\n\nStatus: Not Started\n",
                encoding="utf-8",
            )

        for folder in ["src", "data", "outputs", "screenshots"]:
            sub = task / folder
            sub.mkdir(exist_ok=True)

            gitkeep = sub / ".gitkeep"
            gitkeep.touch(exist_ok=True)

print("Portfolio structure generated successfully!")