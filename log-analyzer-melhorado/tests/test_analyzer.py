from app.analyzer import LogAnalyzer


def test_parse_valid_line():
    line = "2024-05-03 10:30:45 ERROR IP=192.168.1.1 Erro crítico"
    parsed = LogAnalyzer.parse_line(line)

    assert parsed is not None
    assert parsed.log_level == "ERROR"
    assert parsed.ip_address == "192.168.1.1"
    assert "Erro crítico" in parsed.message


def test_parse_invalid_line():
    assert LogAnalyzer.parse_line("linha sem formato") is None
