def test_project_package_is_importable() -> None:
    import ledgerlens
    assert ledgerlens.__doc__ is not None
