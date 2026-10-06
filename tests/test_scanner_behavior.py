from contribradar.core import scan_repo


def test_missing_security_file_is_detected(tmp_path):
    (tmp_path / "README.md").write_text("test", encoding="utf-8")

    result = scan_repo(tmp_path)

    titles = {
        item["title"]
        for item in result["opportunities"]
    }

    assert "Add SECURITY.md" in titles


def test_todo_marker_is_detected(tmp_path):
    source = tmp_path / "example.py"

    source.write_text(
        "# TODO: improve this function\n"
        "print('hello')\n",
        encoding="utf-8",
    )

    result = scan_repo(tmp_path)

    titles = [
        item["title"]
        for item in result["opportunities"]
    ]

    assert any("TODO/FIXME" in title for title in titles)


def test_score_is_between_zero_and_hundred(tmp_path):
    result = scan_repo(tmp_path)

    assert 0 <= result["score"] <= 100


def test_result_contains_expected_fields(tmp_path):
    result = scan_repo(tmp_path)

    assert "score" in result
    assert "opportunities" in result
    assert "opportunity_count" in result

    for opportunity in result["opportunities"]:
        assert "title" in opportunity
        assert "priority" in opportunity
        assert "points" in opportunity
        assert "reason" in opportunity
