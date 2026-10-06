from contribradar.core import scan_repo


def test_empty_repo_has_opportunities(tmp_path):
    result = scan_repo(tmp_path)

    assert result["opportunity_count"] > 0

    titles = {
        item["title"]
        for item in result["opportunities"]
    }

    assert "Add README.md" in titles
    assert "Add automated tests" in titles
    assert "Add automated CI" in titles


def test_complete_basics_reduce_opportunities(tmp_path):
    required_files = [
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
    ]

    for filename in required_files:
        (tmp_path / filename).write_text(
            "placeholder",
            encoding="utf-8",
        )

    tests_dir = tmp_path / "tests"
    tests_dir.mkdir()

    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)

    (workflows / "ci.yml").write_text(
        "name: CI",
        encoding="utf-8",
    )

    (tmp_path / "pyproject.toml").write_text(
        "[project]\nname = 'example'",
        encoding="utf-8",
    )

    result = scan_repo(tmp_path)

    titles = {
        item["title"]
        for item in result["opportunities"]
    }

    assert "Add README.md" not in titles
    assert "Add automated tests" not in titles
    assert "Add automated CI" not in titles
