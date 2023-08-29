from main import random_numbers, user_input


def test_random(capsys):
    numbers = random_numbers()
    captured = capsys.readouterr()
    assert captured.out == f'{min(numbers)}\n{max(numbers)}\n'


def test_userinput_normal(capsys, monkeypatch):
    inputs = iter([31, -7, 258, 4, 0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    user_input()
    captured = capsys.readouterr()
    assert captured.out == f'-7\n258\n'


def test_userinput_special(capsys, monkeypatch):
    inputs = iter([42, 0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    user_input()
    captured = capsys.readouterr()
    assert captured.out == f'42\n42\n'
