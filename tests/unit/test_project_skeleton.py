def test_project_package_is_importable() -> None:
    import src.ledgerlens

    assert src.ledgerlens.__doc__ is not None
