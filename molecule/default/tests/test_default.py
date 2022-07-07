def test_default_files(host):
    f = host.file("/usr/local/bin/starship")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_default_cmd(host):
    cmd = "/usr/local/bin/starship --help"
    result = host.run(cmd)

    assert result.exit_status == 0
