from project import caesar_cipher,decrypted_password,get_yes_no,save,get_length

def test_encryption():
    assert caesar_cipher("@Kagami2003") == "ᣕᣠ᣶᣼᣶ᤂ᣾ᣇᣅᣅᣈ"
    assert caesar_cipher("12345") == "ᣆᣇᣈᣉᣊ"


def test_decryption():
    assert decrypted_password("ᣕᣠ᣶᣼᣶ᤂ᣾ᣇᣅᣅᣈ") == "@Kagami2003"
    assert decrypted_password("ᣆᣇᣈᣉᣊ") == "12345"


def test_get_yes(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert get_yes_no() == True


def test_get_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert get_yes_no() == False


def test_save_file(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "Passwords")
    assert save("account","pass") == "Passwords.csv"

    monkeypatch.setattr("builtins.input", lambda _: "Passwords.csv")
    assert save("account", "pass") == "Passwordscsv.csv"


def test_length(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "30")
    assert get_length() == 30