from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("paradise", 3) == "rap_esida"
    assert encrypt_message("paradise", 4) == "resid_arap"
    assert encrypt_message("paradise", 8) == "esidarap"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("paradise", "3")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(37452, 1)
