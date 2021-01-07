from wireviz_web.plantuml import plantuml_decode, plantuml_encode


def test_plantuml_decode_encode():

    original = "SyfFKj2rKt3CoKnELR1Io4ZDoSa700=="

    decoded = plantuml_decode(original)
    assert decoded == "Bob -> Alice : hello"

    reencoded = plantuml_encode(decoded)
    assert reencoded == original
